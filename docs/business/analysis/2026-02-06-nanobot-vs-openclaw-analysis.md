# Nanobot vs OpenClaw: yuna-openclaw 프로젝트에 적용 시 한계 비교 분석

> **작성일**: 2026-02-06
> **목적**: HKUDS/nanobot을 openclaw/openclaw 대신 yuna-openclaw 프로젝트의 에이전트 인프라로 사용할 경우의 한계를 코드베이스 수준에서 분석
> **분석 대상**: nanobot v0.1.3.post4, OpenClaw v2026.2.3, yuna-openclaw main (e6d6cfc)

---

## 0. 용어 정리

| 명칭 | 레포지토리 | 정체 |
|------|-----------|------|
| **OpenClaw** | `openclaw/openclaw` | Peter Steinberger가 만든 오픈소스 개인 AI 에이전트 프레임워크. TypeScript, 170K+ 스타. 구 Clawdbot → Moltbot → OpenClaw |
| **nanobot** | `HKUDS/nanobot` | 홍콩대학교 HKUDS Lab이 OpenClaw을 99% 축소하여 만든 초경량 AI 에이전트. Python, ~4,000 LOC, 10K+ 스타 |
| **yuna-openclaw** | 본 레포지토리 | 가재 컴퍼니 BIP 서비스. 13-Node AI 군단의 협업 과정을 제품화하는 Next.js 웹앱 + 문서 기반 조직 OS |

**핵심 질문**: yuna-openclaw의 에이전트 인프라로 OpenClaw 대신 nanobot을 채택하면 무엇을 잃는가?

---

## 1. OpenClaw vs nanobot: 프로젝트 프로필

| 축 | OpenClaw (`openclaw/openclaw`) | nanobot (`HKUDS/nanobot`) |
|----|-------------------------------|---------------------------|
| **언어** | TypeScript (100%) | Python 3.11+ |
| **코드 규모** | 430,000+ LOC | ~4,000 LOC (99% 축소) |
| **GitHub 스타** | 170,155 | 10,226 |
| **릴리스 주기** | 매일 (v2026.2.x) | 비정기 (v0.1.3) |
| **기원** | 독립 프로젝트 (Peter Steinberger) | OpenClaw 축소판 (학술 연구) |
| **라이선스** | MIT | MIT |
| **설치** | `npm install -g openclaw` / curl 스크립트 | `pip install nanobot-ai` |
| **배포** | 로컬 / Docker / DigitalOcean 1-Click / GCP / Fly.io | 로컬 / Docker |
| **문서** | 전용 사이트 (docs.openclaw.ai), 다국어 | README 중심 |
| **보안 이력** | CVE-2026-25253 (RCE), ClawHub 악성 스킬 12%, Moltbook 150만 토큰 유출 | 주요 CVE 없음 (코드 단순성으로 공격 표면 축소) |

---

## 2. 아키텍처 비교

### 2.1 OpenClaw 아키텍처

```
┌─────────────────────────────────────────────────────────┐
│                    Gateway (제어 평면)                    │
│                ws://127.0.0.1:18789                      │
├─────────────────────────────────────────────────────────┤
│  채널 (20+): WhatsApp, Telegram, Discord, Slack,        │
│  Signal, iMessage, Google Chat, Teams, Matrix,          │
│  LINE, Feishu, Zalo, Mattermost, Nostr, Twitch...      │
├─────────────────────────────────────────────────────────┤
│              Pi Agent Runtime (단일 에이전트)             │
├─────────────────────────────────────────────────────────┤
│  도구: exec, read, write, edit, browser (CDP),          │
│  web_search, web_fetch, canvas, image, nodes,           │
│  message, sessions_spawn...                             │
├─────────────────────────────────────────────────────────┤
│  메모리: Markdown 파일 + 하이브리드 검색                  │
│  (SQLite + sqlite-vec / QMD, 벡터 + BM25)              │
├─────────────────────────────────────────────────────────┤
│  플러그인 SDK: TypeScript 모듈, in-process 실행          │
│  스킬: SKILL.md (ClawHub 마켓플레이스)                   │
│  프로바이더: Anthropic, OpenAI, OpenRouter, Ollama,      │
│  Venice, Bedrock, Moonshot, Qwen, xAI, Groq, Mistral   │
└─────────────────────────────────────────────────────────┘
```

### 2.2 nanobot 아키텍처

```
┌─────────────────────────────────────────────────────────┐
│          MessageBus (asyncio.Queue 기반)                 │
├─────────────────────────────────────────────────────────┤
│  채널 (4): Telegram, Discord, WhatsApp, Feishu          │
├─────────────────────────────────────────────────────────┤
│              AgentLoop (단일 에이전트)                    │
├─────────────────────────────────────────────────────────┤
│  도구: read, write, edit, list_dir, exec,               │
│  web_search, web_fetch, message, spawn, cron            │
├─────────────────────────────────────────────────────────┤
│  메모리: Markdown 파일 (MEMORY.md + 일별 .md)           │
│  (벡터 검색 없음, 텍스트 기반)                            │
├─────────────────────────────────────────────────────────┤
│  스킬: SKILL.md (OpenClaw 호환 형식)                     │
│  프로바이더: LiteLLM (OpenRouter, Anthropic, OpenAI,     │
│  DeepSeek, Gemini, Groq, Zhipu, Moonshot, vLLM)        │
└─────────────────────────────────────────────────────────┘
```

---

## 3. 기능별 상세 비교

### 3.1 채널/메신저 통합

| 기능 | OpenClaw | nanobot | yuna-openclaw 영향 |
|------|----------|---------|-------------------|
| 지원 채널 수 | **20+** (WhatsApp, Telegram, Discord, Slack, Signal, iMessage, Teams, Matrix, LINE, Feishu, Google Chat 등) | **4** (Telegram, Discord, WhatsApp, Feishu) | 가재 군단의 외부 채널 확장 시 OpenClaw이 압도적으로 유리 |
| WebChat | 내장 웹 UI | 없음 | nanobot 사용 시 웹 기반 상호작용 직접 구현 필요 |
| iMessage/Signal | 지원 (BlueBubbles, Signal CLI) | 미지원 | iOS 생태계 접근 불가 |
| 플러그인 기반 채널 추가 | TypeScript 플러그인 SDK | `BaseChannel` Python 상속 | nanobot도 확장 가능하나 생태계 부재 |

**한계**: nanobot은 핵심 4개 채널은 지원하나, OpenClaw의 20+ 채널 생태계에 비하면 선택지가 극히 제한된다. Slack, Teams 등 비즈니스 메신저 미지원이 yuna-openclaw의 B2B 확장에 걸림돌이 된다.

### 3.2 도구(Tool) 시스템

| 도구 | OpenClaw | nanobot | 차이 |
|------|----------|---------|------|
| 파일 시스템 | read, write, edit, apply_patch | read, write, edit, list_dir | OpenClaw에 `apply_patch` 추가 |
| 셸 실행 | exec + process (백그라운드) | exec (포그라운드만) | OpenClaw이 백그라운드 프로세스 지원 |
| **브라우저 자동화** | **CDP 기반 전체 브라우저 제어** (스크린샷, PDF, 네트워크 필터, 프로필 격리) | **없음** | **가장 큰 차이** |
| 웹 검색 | Brave Search | Brave Search | 동등 |
| 웹 페치 | web_fetch | web_fetch | 동등 |
| 이미지 분석 | image (Sharp 기반) | 없음 | OpenClaw만 |
| **Canvas (A2UI)** | canvas 도구로 동적 UI 생성 | 없음 | OpenClaw만 |
| 디바이스 제어 | nodes (카메라, 위치, SMS, 화면 녹화) | 없음 | OpenClaw만 |
| TTS | 텍스트-음성 변환 | 없음 | OpenClaw만 |
| 크론 | Gateway 내장 스케줄링 | croniter 기반 | 둘 다 지원 |

**한계**: nanobot은 파일/셸/웹의 기본 도구만 제공한다. 브라우저 자동화, 이미지 처리, 디바이스 제어, A2UI Canvas 등 OpenClaw의 고급 도구가 전무하다. yuna-openclaw이 웹 스크래핑이나 시각 콘텐츠 생성에 에이전트를 활용하려면 OpenClaw이 필수적이다.

### 3.3 메모리 및 컨텍스트

| 기능 | OpenClaw | nanobot | yuna-openclaw 영향 |
|------|----------|---------|-------------------|
| 저장 형식 | Markdown 파일 (소스 오브 트루스) | Markdown 파일 | 동일한 철학 |
| **시맨틱 검색** | **하이브리드: 벡터(sqlite-vec) + BM25 전문 검색** | **없음** | nanobot은 메모리 양이 늘어나면 관련 기억을 찾을 수 없음 |
| 임베딩 | 로컬 GGUF, OpenAI, Gemini, 커스텀 | 없음 | |
| QMD 백엔드 | 로컬 우선 검색 사이드카 | 없음 | |
| 컨텍스트 컴팩션 | 자동 (남은 20K 토큰 시 메모리 플러시) | 없음 (수동) | nanobot은 긴 대화에서 컨텍스트 유실 위험 |
| 세션 저장 | JSONL (안정적 세션 ID, 자동 리셋) | 없음 (인메모리) | nanobot은 재시작 시 대화 기록 소실 |
| 세션 스코프 | per-peer, per-channel, per-account 등 세분화 | 단일 세션 | OpenClaw이 다중 사용자 시나리오에 유리 |

**한계**: 메모리 시스템에서 결정적 차이는 **시맨틱 검색의 유무**다. yuna-openclaw의 연대기 데이터가 축적될수록 nanobot의 단순 텍스트 메모리로는 과거 맥락을 찾을 수 없다. OpenClaw의 벡터+BM25 하이브리드 검색은 이 문제를 해결한다.

### 3.4 서브에이전트 / 멀티에이전트

| 기능 | OpenClaw | nanobot | yuna-openclaw 영향 |
|------|----------|---------|-------------------|
| 서브에이전트 생성 | sessions_spawn (격리된 세션) | SpawnTool (asyncio.create_task) | 기본 구조는 유사 |
| thinking 레벨 설정 | `agents.defaults.subagents.thinking` | 없음 | OpenClaw이 서브에이전트 추론 품질 조절 가능 |
| 세션 간 통신 | sessions_list/history/send | 단방향 (서브→메인 결과 보고) | nanobot은 에이전트 간 대화 불가 |
| 재귀 방지 | 세션 격리 | SpawnTool/MessageTool 제거 | 둘 다 재귀 차단 |
| **진정한 멀티에이전트** | **아님** — "단일 에이전트 런타임" 명시 | **아님** — 단일 에이전트 + 서브에이전트 위임 | **둘 다 yuna-openclaw의 13-Node 클러스터를 네이티브로 지원하지 않음** |

**한계**: 이 영역에서는 **OpenClaw과 nanobot 모두 한계가 있다**. yuna-openclaw의 13개 전문 에이전트(PO, PM, DEV, QA 등)가 격돌하며 합의를 도출하는 모델은 어느 쪽도 네이티브로 지원하지 않는다. 다만 OpenClaw은 세션 간 메시지 교환(`sessions_send`)이 가능하여 에이전트 간 통신을 어느 정도 구현할 수 있으나, nanobot은 완전히 불가하다.

### 3.5 플러그인/확장성

| 기능 | OpenClaw | nanobot | yuna-openclaw 영향 |
|------|----------|---------|-------------------|
| 플러그인 시스템 | **TypeScript 플러그인 SDK** (Gateway RPC, HTTP 핸들러, 도구, CLI, 백그라운드 서비스 등록) | 없음 (Tool 클래스 상속만) | OpenClaw은 Gateway 레벨 확장 가능, nanobot은 도구 추가만 가능 |
| 스킬 마켓플레이스 | **ClawHub** (2,857개 스킬, 단 12% 악성) | 없음 (내장 6개 + 사용자 추가) | OpenClaw 생태계가 압도적이나 보안 리스크 존재 |
| 스킬 형식 호환 | SKILL.md | SKILL.md (OpenClaw 호환) | 스킬 자산 공유 가능 |
| 커스텀 채널 | 플러그인으로 등록 | BaseChannel 상속 | 둘 다 가능 |
| 커스텀 도구 | 플러그인으로 등록 | Tool ABC 상속 | 둘 다 가능하나 OpenClaw이 통합 범위 넓음 |
| 커스텀 프로바이더 | 플러그인으로 등록 | LLMProvider 상속 | 둘 다 가능 |

**한계**: nanobot의 확장은 Python 클래스 상속 수준에 한정된다. OpenClaw은 Gateway 레벨의 플러그인 SDK를 통해 RPC, HTTP, 백그라운드 서비스까지 등록할 수 있어, yuna-openclaw의 향후 인프라 확장에 OpenClaw이 유리하다.

### 3.6 LLM 프로바이더

| 프로바이더 | OpenClaw | nanobot |
|-----------|----------|---------|
| Anthropic Claude | ✓ (프롬프트 캐싱 지원) | ✓ (LiteLLM 경유) |
| OpenAI | ✓ | ✓ |
| OpenRouter | ✓ | ✓ |
| Ollama (로컬) | ✓ | ✓ (vLLM 경유) |
| Venice AI | ✓ | ✗ |
| AWS Bedrock | ✓ | ✗ |
| Groq | ✓ | ✓ |
| DeepSeek | ✓ | ✓ (불안정) |
| Gemini | ✓ | ✓ |
| xAI | ✓ | ✗ |
| Mistral | ✓ | ✗ |
| Zhipu/GLM | ✗ | ✓ |
| Moonshot/Kimi | ✓ | ✓ |
| **프롬프트 캐싱** | ✓ (Anthropic, 5분/1시간) | ✗ |
| **프로바이더 총 수** | **10+** | **9** (LiteLLM 기반) |

**한계**: 프로바이더 커버리지는 대체로 비슷하나, OpenClaw의 **프롬프트 캐싱** 지원이 중요하다. yuna-openclaw의 헌법/역할 문서 등 반복적으로 주입되는 시스템 프롬프트가 크기 때문에, 프롬프트 캐싱 없이는 API 비용이 크게 증가한다.

### 3.7 보안

| 항목 | OpenClaw | nanobot |
|------|----------|---------|
| 알려진 CVE | CVE-2026-25253 (CVSS 8.8, 1-click RCE) — 패치됨 | 없음 |
| 데이터 유출 사고 | Moltbook 150만 API 토큰 노출 | 없음 |
| 악성 스킬 | ClawHub에서 12% (341/2,857) 발견 | 마켓플레이스 없음 (리스크도 없음) |
| Palo Alto 경고 | "치명적 3요소" (개인 데이터 + 비신뢰 콘텐츠 + 외부 통신) | 해당 없음 |
| 코드 감사 용이성 | 430K+ LOC — 전체 감사 비현실적 | ~4K LOC — 1시간 내 전체 감사 가능 |
| Gateway 인증 | 토큰/비밀번호 기반 | 없음 (채널별 allowFrom만) |
| 파일시스템 샌드박싱 | restrictToWorkspace 옵션 | restrictToWorkspace 옵션 |

**한계의 역전**: 보안 관점에서는 **nanobot이 오히려 유리**하다. 코드가 작아 감사가 쉽고, 마켓플레이스가 없어 공급망 공격 표면이 없으며, 알려진 CVE가 없다. OpenClaw은 기능이 풍부한 만큼 공격 표면도 넓다. yuna-openclaw이 보안을 최우선시한다면 nanobot의 단순함이 장점이 된다.

### 3.8 배포 및 운영

| 항목 | OpenClaw | nanobot |
|------|----------|---------|
| 설치 | `npm install -g openclaw` 또는 curl 스크립트 | `pip install nanobot-ai` |
| Docker | 공식 지원 | Dockerfile 제공 |
| 클라우드 1-Click | DigitalOcean, GCP, Fly.io, Railway | 없음 |
| IaC | Nix, Ansible | 없음 |
| 원격 접근 | Tailscale Serve/Funnel, SSH 터널 | 없음 (직접 구성) |
| 웹 컨트롤 UI | 내장 | 없음 |
| TUI | 내장 터미널 UI | CLI만 |
| 모니터링 | Gateway 상태 API | `nanobot status` |

**한계**: nanobot의 배포 옵션은 로컬 또는 Docker뿐이다. OpenClaw은 1-Click 클라우드 배포, IaC 지원, 원격 접근 솔루션이 풍부하다. yuna-openclaw을 프로덕션 환경에서 운영하려면 OpenClaw의 인프라 성숙도가 유리하다.

---

## 4. yuna-openclaw 핵심 요구사항 대비 커버리지

yuna-openclaw 프로젝트의 고유 요구사항에 대해 두 프레임워크가 제공하는 것:

| # | yuna-openclaw 요구사항 | OpenClaw | nanobot | 비고 |
|---|----------------------|----------|---------|------|
| 1 | **13-Node 에이전트 클러스터** | △ (sessions_spawn + sessions_send로 부분 구현) | ✗ (단방향 서브에이전트만) | 어느 쪽도 네이티브 멀티에이전트가 아니나 OpenClaw이 세션 간 통신 가능 |
| 2 | **헌법 기반 거버넌스** | △ (AGENTS.md + SOUL.md로 규율 주입 가능) | △ (AGENTS.md + SOUL.md 동일 형식) | 부트스트랩 파일 형식이 호환되므로 둘 다 규율 주입은 가능 |
| 3 | **연대기 기록/서빙** | △ (메모리 시스템 + 하이브리드 검색) | ✗ (비구조화 텍스트 메모리) | OpenClaw의 벡터 검색이 연대기 탐색에 유리 |
| 4 | **메신저 기반 상호작용** | ✓ (20+ 채널) | △ (4 채널) | OpenClaw이 압도적 |
| 5 | **브라우저 자동화** | ✓ (CDP 기반) | ✗ | OpenClaw만 지원 |
| 6 | **프롬프트 캐싱** (비용 절감) | ✓ (Anthropic 5분/1시간) | ✗ | 헌법/역할 등 대량 시스템 프롬프트에 중요 |
| 7 | **플러그인 확장** | ✓ (TypeScript SDK) | ✗ (Tool 상속만) | OpenClaw이 확장 범위 넓음 |
| 8 | **보안/감사 용이성** | △ (CVE 이력, 코드 방대) | ✓ (4K LOC, 전체 감사 가능) | 보안 관점에서 nanobot 유리 |
| 9 | **로컬 모델 지원** | ✓ (Ollama) | ✓ (vLLM/Ollama) | 동등 |
| 10 | **비용 효율성** | △ (기능 풍부하나 리소스 소비 높음) | ✓ (경량, 최소 리소스) | nanobot이 운영 비용 낮음 |

**OpenClaw 커버리지: 7/10 항목에서 우위**
**nanobot 커버리지: 2/10 항목에서 우위, 1개 동등**

---

## 5. nanobot 채택 시 구체적 한계 (OpenClaw 대비)

### 한계 1: 시맨틱 메모리 검색 부재

OpenClaw은 SQLite + sqlite-vec 기반 하이브리드 검색(벡터 유사도 + BM25)을 제공한다. yuna-openclaw의 연대기 데이터(meeting, command 마크다운 파일)가 수백 건으로 축적되면, "지난주 DEV와 QA가 경합 조건에 대해 논의한 내용"같은 시맨틱 쿼리가 필요하다.

nanobot의 `get_recent_memories(days=7)`은 최근 7일 텍스트를 통째로 덤프할 뿐 의미 기반 검색이 불가하다.

### 한계 2: 브라우저 자동화 전무

OpenClaw의 CDP 기반 브라우저 도구는 웹 스크래핑, 스크린샷, PDF 생성, 자동 로그인 등을 에이전트가 수행할 수 있게 한다. yuna-openclaw이 경쟁사 분석, 콘텐츠 수집, 시각 자산 생성 등에 에이전트를 활용하려면 이 기능이 필수적이다.

nanobot에는 브라우저 도구 자체가 없어 Playwright나 Selenium을 별도 통합해야 한다.

### 한계 3: 세션 간 통신 불가

OpenClaw의 `sessions_send` 도구는 한 에이전트 세션에서 다른 세션으로 메시지를 보낼 수 있다. 이것은 yuna-openclaw의 "PO가 DEV에게 설계 요청을 보내는" 패턴을 에이전트 레벨에서 구현하는 데 사용할 수 있다.

nanobot의 서브에이전트는 결과를 메인에 보고만 할 수 있고, 서브에이전트끼리 통신할 수 없다 (SpawnTool과 MessageTool이 서브에이전트에서 제거됨).

### 한계 4: 프롬프트 캐싱 미지원에 따른 비용 증가

yuna-openclaw의 각 에이전트는 헌법(CONSTITUTION.md), 역할 파일(ROLE_*.md), 프로세스 가이드 등 대량의 시스템 프롬프트를 매 호출마다 주입받는다. OpenClaw의 Anthropic 프롬프트 캐싱(`cacheRetention: "long"`, 1시간)은 이 반복 토큰 비용을 크게 절감한다.

nanobot은 LiteLLM을 경유하므로 프롬프트 캐싱이 불가하며, 동일한 시스템 프롬프트를 매번 전량 과금한다.

### 한계 5: 플러그인 생태계 부재

OpenClaw의 플러그인 SDK는 TypeScript 모듈로 Gateway RPC, HTTP 핸들러, 새 도구, CLI 명령, 백그라운드 서비스까지 등록할 수 있다. ClawHub에 2,857개 스킬이 등록되어 있다 (보안 문제 있으나 검증된 것 활용 가능).

nanobot은 Python Tool 클래스 상속으로 도구만 추가 가능하며, 플러그인 마켓플레이스가 없다.

### 한계 6: 채널 커버리지 5배 차이

OpenClaw 20+ 채널 vs nanobot 4 채널. Slack, Teams, Signal, iMessage 등 비즈니스/프라이버시 메신저가 nanobot에서 빠져 있어, yuna-openclaw의 B2B 확장이나 다양한 사용자 접점 확보에 제약이 있다.

### 한계 7: 배포/운영 인프라 미성숙

OpenClaw은 DigitalOcean 1-Click, GCP, Fly.io, Railway 등 프로덕션 배포 경로가 다양하고, Tailscale 기반 원격 접근, Nix/Ansible IaC를 지원한다. nanobot은 로컬 또는 수동 Docker 배포뿐이다.

---

## 6. nanobot의 강점 (OpenClaw 대비)

한계만 나열하면 공정하지 않다. nanobot이 OpenClaw보다 나은 영역:

| 영역 | nanobot 강점 | 상세 |
|------|-------------|------|
| **코드 감사 용이성** | 4,000 LOC vs 430,000 LOC | 전체 코드를 1시간 내에 읽고 이해할 수 있다. 보안 감사, 커스터마이징, 디버깅이 근본적으로 쉽다 |
| **공격 표면 최소** | CVE 0건 vs CVE 다수 | 기능이 적은 만큼 보안 취약점도 적다. 마켓플레이스도 없어 공급망 공격 위험 없음 |
| **Python 생태계** | pip install, PyPI | AI/ML 라이브러리(LangChain, LlamaIndex, HuggingFace 등)와 자연스러운 통합 가능 |
| **리소스 효율성** | 최소 메모리/CPU | 430K LOC 런타임 대비 극히 가벼움. 저사양 서버에서도 운영 가능 |
| **학습/연구 용이** | 아키텍처가 투명 | 에이전트 루프, 도구, 메모리 등 모든 구성요소를 명확히 이해 가능 |
| **커스텀 자유도** | 작은 코드 = 쉬운 포크 | OpenClaw 포크는 430K LOC를 유지보수해야 하지만, nanobot 포크는 4K LOC만 관리 |

---

## 7. 의사결정 매트릭스

### yuna-openclaw 프로젝트 시나리오별 권장

| 시나리오 | 권장 | 사유 |
|---------|------|------|
| **프로덕션 BIP 서비스 운영** | OpenClaw | 채널 20+, 브라우저 자동화, 하이브리드 검색, 프롬프트 캐싱, 클라우드 배포 |
| **13-Node 에이전트 협업** | OpenClaw (부분) | sessions_send로 에이전트 간 통신 가능 (nanobot은 불가) |
| **연대기 데이터 시맨틱 검색** | OpenClaw | 벡터+BM25 하이브리드 검색 내장 |
| **MVP/실험 단계** | nanobot | 빠른 설치, 낮은 비용, 전체 코드 파악 가능 |
| **보안 최우선** | nanobot | 공격 표면 최소, 전체 감사 가능, CVE 없음 |
| **AI/ML 연구 통합** | nanobot | Python 생태계 자연 통합 |
| **저비용 운영** | nanobot | 프롬프트 캐싱 없지만 런타임 비용 자체가 낮음 |
| **메신저 봇 (Telegram/Discord)** | 동등 | 핵심 4채널은 둘 다 지원 |

---

## 8. 결론

### 한 줄 요약

> **OpenClaw은 "완성도 높은 프로덕션 에이전트 인프라"이고, nanobot은 "투명하고 가벼운 에이전트 코어"다. yuna-openclaw의 프로덕션 서비스에는 OpenClaw이 적합하고, 실험/연구/보안 중시 시나리오에는 nanobot이 적합하다.**

### 핵심 차이 3줄

1. **규모**: OpenClaw 430K LOC / nanobot 4K LOC — 100배 차이는 기능의 차이이자 복잡성의 차이
2. **메모리**: OpenClaw은 벡터+BM25 시맨틱 검색을 내장, nanobot은 텍스트 파일 덤프만 — 연대기 축적 시 결정적
3. **확장성**: OpenClaw은 플러그인 SDK + 20+ 채널 + 클라우드 배포, nanobot은 Tool 상속 + 4 채널 + 로컬 배포

### 최종 권장

yuna-openclaw의 현재 단계(BIP 서비스 구축)에서는 **OpenClaw을 기본 에이전트 인프라로 채택**하되, 다음 경우에 nanobot을 보조적으로 활용하는 **하이브리드 전략**을 권장한다:

- nanobot으로 에이전트 루프의 프로토타이핑 및 아키텍처 실험
- nanobot으로 보안 감사가 필요한 핵심 로직의 레퍼런스 구현
- OpenClaw으로 프로덕션 채널 통합, 메모리 검색, 브라우저 자동화

---

*본 분석은 nanobot v0.1.3.post4, OpenClaw v2026.2.3, yuna-openclaw main (커밋 e6d6cfc) 기준으로 수행되었습니다.*
*소스: github.com/HKUDS/nanobot, github.com/openclaw/openclaw, docs.openclaw.ai*
