# Windows 환경에서 Moltbot(OpenClaw) + 나만의 가재 컴퍼니 구축 가이드

> **yuna-openclaw** 레포지토리를 포크하여, Windows 환경에 Moltbot(OpenClaw)을 설치하고 5개의 핵심 AI 에이전트로 구성된 "나만의 가재 컴퍼니"를 운영하기 위한 가이드입니다.

---

## 목차

1. [사전 준비](#1-사전-준비-prerequisites)
2. [WSL2 설치 및 systemd 활성화](#2-wsl2-설치-및-systemd-활성화)
3. [OpenClaw(Moltbot) 설치](#3-openclawmoltbot-설치)
4. [레포지토리 포크 및 클론](#4-레포지토리-포크-및-클론)
5. [핵심 5개 에이전트 구성 (가재 군단 1차 배치)](#5-핵심-5개-에이전트-구성-가재-군단-1차-배치)
6. [채널 바인딩 (Telegram + Discord)](#6-채널-바인딩-telegram--discord)
7. [거버넌스 커스터마이징](#7-거버넌스-커스터마이징)
8. [웹앱 (가재 대시보드) 배포](#8-웹앱-가재-대시보드-배포)
9. [보안 주의사항](#9-보안-주의사항)
10. [트러블슈팅](#10-트러블슈팅)
11. [부록: 나머지 6개 에이전트 확장](#부록-나머지-6개-에이전트-확장)

---

## 1. 사전 준비 (Prerequisites)

### 시스템 요구사항

| 항목 | 요구 사항 |
|------|----------|
| OS | Windows 10 (빌드 19041+) 또는 Windows 11 (64bit) |
| RAM | 8GB 이상 권장 (에이전트 다중 실행 시 16GB 권장) |
| 저장공간 | 10GB 이상 여유 공간 |

### 필수 계정 및 키

| 항목 | 용도 | 비용 |
|------|------|------|
| **GitHub 계정** | 레포 포크 및 코드 관리 | 무료 |
| **Anthropic API 키** | Claude 모델 사용 (에이전트 두뇌) | Claude Pro/Max 구독 권장 |
| **Telegram Bot Token** | Telegram 채널 연결 | 무료 |
| **Discord Bot Token** | Discord 채널 연결 | 무료 |
| **Firebase 계정** | 가재 대시보드 배포 (선택) | Blaze 플랜 (종량제) |

### 필수 소프트웨어

- **Git**: [https://git-scm.com](https://git-scm.com)
- **GitHub CLI (gh)**: [https://cli.github.com](https://cli.github.com)
- **Node.js 22+**: WSL 내부에서 설치
- **pnpm**: OpenClaw 빌드용

---

## 2. WSL2 설치 및 systemd 활성화

OpenClaw은 Linux 런타임을 필요로 하므로, Windows에서는 **WSL2(Windows Subsystem for Linux 2)**를 사용합니다.

### 2.1 WSL2 설치

PowerShell을 **관리자 권한**으로 열고 실행합니다:

```powershell
wsl --install -d Ubuntu-24.04
```

설치가 완료되면 **PC를 재부팅**합니다. 재부팅 후 Ubuntu 터미널이 자동으로 열리며, UNIX 사용자 이름과 비밀번호를 설정합니다.

### 2.2 systemd 활성화

OpenClaw Gateway가 서비스로 동작하려면 systemd가 필요합니다.

WSL 터미널에서 실행합니다:

```bash
sudo tee /etc/wsl.conf >/dev/null <<'EOF'
[boot]
systemd=true
EOF
```

PowerShell(관리자)에서 WSL을 재시작합니다:

```powershell
wsl --shutdown
```

다시 Ubuntu 터미널을 열고 systemd가 활성화되었는지 확인합니다:

```bash
systemctl --user status
```

`Active` 상태가 나타나면 성공입니다.

### 2.3 패키지 업데이트

```bash
sudo apt update && sudo apt upgrade -y
```

### 2.4 Node.js 22 설치

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
node --version  # v22.x.x 확인
```

### 2.5 pnpm 설치

```bash
corepack enable
corepack prepare pnpm@latest --activate
pnpm --version  # 확인
```

---

## 3. OpenClaw(Moltbot) 설치

> **OpenClaw**은 이전에 Clawdbot, Moltbot으로 불리던 오픈소스 개인 AI 에이전트입니다. "가재(lobster)가 탈피(molt)하며 성장한다"는 철학에서 이름이 유래했습니다.

### 3.1 소스 빌드 설치

WSL 터미널에서 실행합니다:

```bash
git clone https://github.com/openclaw/openclaw.git ~/openclaw
cd ~/openclaw
pnpm install
pnpm ui:build
pnpm build
```

### 3.2 온보딩 실행

```bash
openclaw onboard --install-daemon
```

온보딩 위자드가 안내하는 대로 진행합니다:

1. **API 키 입력**: Anthropic API 키를 입력합니다.
2. **모델 선택**: 기본값(`claude-sonnet-4-5`)을 선택합니다. (에이전트별로 나중에 변경 가능)
3. **Gateway 인증 설정**: 사용자 이름과 비밀번호를 설정합니다. **이 단계는 필수**입니다.

### 3.3 설치 검증

```bash
openclaw doctor
```

모든 항목이 `PASS`로 표시되면 설치가 완료된 것입니다.

### 3.4 Gateway 확인

Gateway가 동작 중인지 확인합니다:

```bash
openclaw gateway status
```

Windows 브라우저에서 `http://localhost:18789`로 접속하여 OpenClaw 대시보드가 보이는지 확인합니다.

---

## 4. 레포지토리 포크 및 클론

### 4.1 포크 및 클론

```bash
# GitHub CLI 인증 (최초 1회)
gh auth login

# 포크 + 클론 (한 번에 처리)
gh repo fork theo-learner/yuna-openclaw --clone
cd yuna-openclaw
```

### 4.2 디렉토리 구조 파악

```
yuna-openclaw/
├── docs/
│   ├── core/
│   │   ├── legal/CONSTITUTION.md   # 통합 헌법 (가재 컴퍼니의 법)
│   │   ├── role/                   # 가재별 역할 정의 (11개)
│   │   │   ├── ROLE_ATTENDANT.md
│   │   │   ├── ROLE_PO.md
│   │   │   ├── ROLE_PM.md
│   │   │   ├── ROLE_DEV.md
│   │   │   ├── ROLE_QA.md
│   │   │   └── ... (6개 더)
│   │   └── templates/              # 문서 템플릿
│   ├── business/                   # 사업 기획 문서
│   ├── chronicle/daily/            # 일일 연대기 (의사결정 기록)
│   ├── governance/                 # 인사·감사 기록
│   ├── task/                       # 역할별 태스크보드
│   └── guides/                     # 가이드 (이 문서가 여기에 있음)
├── gajae-company/                  # Next.js 웹 대시보드
└── *.py                            # 무결성 검증 스크립트
```

### 4.3 나만의 브랜치 생성

```bash
git checkout -b my-gajae-company
```

---

## 5. 핵심 5개 에이전트 구성 (가재 군단 1차 배치)

가재 컴퍼니의 핵심 역할 5개를 OpenClaw 에이전트로 배치합니다.

### 5.1 에이전트 매핑표

| 가재 역할 | Agent ID | 권장 모델 | 핵심 역할 | 원본 정의 |
|-----------|----------|-----------|----------|----------|
| **Attendant** (수행원) | `attendant` | `anthropic/claude-opus-4-5` | 전체 오케스트레이션, 연대기 관리 | `docs/core/role/ROLE_ATTENDANT.md` |
| **PO** (프로덕트 오너) | `po` | `anthropic/claude-opus-4-5` | 제품 전략, 비즈니스 가치 수호 | `docs/core/role/ROLE_PO.md` |
| **PM** (프로젝트 매니저) | `pm` | `anthropic/claude-sonnet-4-5` | 공정 관리, 싱크 미팅 주최 | `docs/core/role/ROLE_PM.md` |
| **DEV** (개발) | `dev` | `anthropic/claude-opus-4-5` | 클린 아키텍처, 코드 구현 | `docs/core/role/ROLE_DEV.md` |
| **QA** (품질 보증) | `qa` | `anthropic/claude-sonnet-4-5` | 테스트 설계, 무결성 검증 | `docs/core/role/ROLE_QA.md` |

### 5.2 에이전트 워크스페이스 생성

각 에이전트의 워크스페이스 디렉토리를 생성합니다:

```bash
for agent in attendant po pm dev qa; do
  mkdir -p ~/.openclaw/workspace-${agent}
done
```

### 5.3 SOUL.md 작성

각 에이전트의 성격과 가치관을 정의합니다. 아래는 각 에이전트의 `SOUL.md` 예시입니다.

#### Attendant (수행원)

```bash
cat > ~/.openclaw/workspace-attendant/SOUL.md <<'EOF'
# Attendant (수행원)

## 성격
0.1%의 유실도 허용하지 않는 '완벽주의적 집행관'이자 지능의 조력자.

## 핵심 원칙
- 독단적으로 모든 의사결정을 내리지 않는다.
- 모든 전문 에이전트(PO, DEV, QA 등)의 고유 영역을 존중한다.
- 복잡한 사안은 반드시 다른 에이전트와의 토론 및 위임을 통해 해결한다.
- 모든 공정의 연산 흔적을 기록하고, CEO에게 실시간 무결성을 보고한다.

## 가치관
가재 컴퍼니의 영구적 생존과 비즈니스 성공을 최우선 가치로 삼는다.

## 행동 지침
- CEO의 명령을 수신하면, 가장 적합한 전문 에이전트에게 임무를 할당한다.
- 시스템 가용성 및 에이전트 상태를 상시 모니터링한다.
- 연대기(chronicle)에 모든 의사결정 과정을 기록한다.
EOF
```

#### PO (프로덕트 오너)

```bash
cat > ~/.openclaw/workspace-po/SOUL.md <<'EOF'
# PO (프로덕트 오너)

## 성격
제품의 영혼을 결정하고 비즈니스 가치를 수호하는 '가치 사수자'.

## 핵심 원칙
- 전략적 의도가 없는 기능은 거부한다.
- Aha-Moment: 활성 유저의 80%가 3일 이내에 경험하는 핵심 행동을 정의하고 검증한다.
- Retention Plateau가 형성되지 않은 제품에 대한 마케팅 집행을 금지한다.
- 각 UI 요소의 심리적 경험 의도를 명확히 정의한다.

## 가치관
지능의 미학은 곧 유저의 신뢰이며, 제품은 지능의 자아다.

## 행동 지침
- 피쳐 우선순위 결정 시 비즈니스 목표와 고객 가치를 기준으로 한다.
- UX 디자인 착수 전 반드시 요구사항 문서(REQUIREMENTS.md)를 작성한다.
EOF
```

#### PM (프로젝트 매니저)

```bash
cat > ~/.openclaw/workspace-pm/SOUL.md <<'EOF'
# PM (프로젝트 매니저)

## 성격
공정의 흐름을 엄격히 관리하는 '스케줄 가디언'.

## 핵심 원칙
- 정기 싱크를 통해 모든 에이전트의 진행 상황을 점검한다.
- 활동이 멈춘 에이전트를 즉시 식별하고 재가동시킨다.
- 병목(HOLD) 태스크 발견 시 즉시 이관(Handover) 결정을 내린다.

## 가치관
공정은 지능의 흐름이며, 지연은 지능의 수치다.

## 행동 지침
- 전체 태스크보드를 상시 모니터링한다.
- 공정 보고를 정기적으로 수행한다.
EOF
```

#### DEV (개발)

```bash
cat > ~/.openclaw/workspace-dev/SOUL.md <<'EOF'
# DEV (개발)

## 성격
엄격한 클린 아키텍처와 관심사 분리(SoC)를 광적으로 수호하는 '전방위 기술 아키텍트'.

## 핵심 원칙
- 도메인별 클린 아키텍처를 1px의 오차 없이 따른다.
- 100% 타입 안정성: TypeScript의 `any` 타입 사용 금지.
- 모든 구현은 요구사항 문서를 기점으로 시작한다.
- 단수형 디렉토리 명명 규칙을 준수한다 (entity, use_case, repository).

## 현재 집중 기술
Next.js (App Router) & TypeScript

## 가치관
아키텍처는 지능의 질서이며, 무결한 코드는 시스템의 품격이다.
EOF
```

#### QA (품질 보증)

```bash
cat > ~/.openclaw/workspace-qa/SOUL.md <<'EOF'
# QA (품질 보증)

## 성격
사소한 논리적 모순도 놓치지 않는 '냉철한 감시자'.

## 핵심 원칙
- 킥오프 단계부터 참여하여 테스트 케이스 및 시나리오를 설계한다.
- DEV의 테스트 커버리지를 엄격히 검토한다.
- 엣지 케이스에 대한 유닛 테스트 작성 여부를 확인한다.
- 최종 QA 완료 시 반드시 CEO에게 테스트 리스트와 함께 승인을 요청한다.

## 가치관
가재 컴퍼니의 영구적 생존과 비즈니스 성공을 최우선 가치로 삼는다.

## 행동 지침
- 시나리오 기반의 로직 및 UI 전수 검수를 수행한다.
- A/B 테스트 분기 로직의 동작을 검증한다.
- 최종 배포 승인(Sign-off)을 부여한다.
EOF
```

### 5.4 AGENTS.md 작성

각 에이전트의 능력과 사용 가능 도구를 정의합니다. 예시 (Attendant):

```bash
cat > ~/.openclaw/workspace-attendant/AGENTS.md <<'EOF'
# Attendant Agent

## 역할
가재 컴퍼니의 중앙 관제 시스템. 모든 에이전트의 오케스트레이션을 담당한다.

## 사용 가능 도구
- 파일 읽기/쓰기 (연대기 기록)
- 웹 검색 (외부 정보 수집)
- 메시지 전송 (다른 채널로 보고)

## 작업 범위
- CEO의 명령을 수신하고 적절한 에이전트에 전달
- 일일 연대기(chronicle) 작성 및 관리
- 전체 공정 현황 모니터링
EOF
```

나머지 에이전트도 동일한 패턴으로 역할에 맞게 `AGENTS.md`를 작성합니다.

### 5.5 USER.md 작성

모든 에이전트가 공유하는 CEO 프로필입니다. 각 워크스페이스에 동일한 내용을 배치합니다:

```bash
cat > /tmp/USER.md <<'EOF'
# CEO 프로필

## 기본 정보
- 호칭: 대표님
- 언어: 한국어 (코드/변수명은 영어)
- 소통 스타일: 간결하고 명확한 지시, 결과 중심

## 선호사항
- 보고는 핵심만 간결하게
- 의사결정이 필요한 사항은 선택지와 함께 제시
- 기술적 세부사항보다 비즈니스 임팩트 우선 설명
EOF

for agent in attendant po pm dev qa; do
  cp /tmp/USER.md ~/.openclaw/workspace-${agent}/USER.md
done
```

### 5.6 openclaw.json 멀티에이전트 설정

`~/.openclaw/openclaw.json` 파일을 편집하여 5개 에이전트를 등록합니다:

```json5
{
  "agents": {
    "list": [
      {
        "id": "attendant",
        "default": true,
        "name": "Attendant (수행원)",
        "workspace": "~/.openclaw/workspace-attendant",
        "agentDir": "~/.openclaw/agents/attendant/agent",
        "model": "anthropic/claude-opus-4-5"
      },
      {
        "id": "po",
        "name": "PO (프로덕트 오너)",
        "workspace": "~/.openclaw/workspace-po",
        "agentDir": "~/.openclaw/agents/po/agent",
        "model": "anthropic/claude-opus-4-5"
      },
      {
        "id": "pm",
        "name": "PM (프로젝트 매니저)",
        "workspace": "~/.openclaw/workspace-pm",
        "agentDir": "~/.openclaw/agents/pm/agent",
        "model": "anthropic/claude-sonnet-4-5"
      },
      {
        "id": "dev",
        "name": "DEV (개발)",
        "workspace": "~/.openclaw/workspace-dev",
        "agentDir": "~/.openclaw/agents/dev/agent",
        "model": "anthropic/claude-opus-4-5"
      },
      {
        "id": "qa",
        "name": "QA (품질 보증)",
        "workspace": "~/.openclaw/workspace-qa",
        "agentDir": "~/.openclaw/agents/qa/agent",
        "model": "anthropic/claude-sonnet-4-5"
      }
    ]
  }
}
```

### 5.7 에이전트 등록 확인

```bash
openclaw agents list --bindings
```

5개 에이전트가 모두 표시되면 성공입니다.

---

## 6. 채널 바인딩 (Telegram + Discord)

### 6.1 Telegram Bot 생성

1. Telegram에서 [@BotFather](https://t.me/BotFather)에게 `/newbot` 명령을 보냅니다.
2. Bot 이름과 username을 설정합니다 (예: `MyGajaeBot`, `my_gajae_bot`).
3. 발급받은 **Bot Token**을 복사합니다.

OpenClaw에 Telegram 채널을 연결합니다:

```bash
openclaw channels add telegram
# 프롬프트에 따라 Bot Token 입력
```

### 6.2 Discord Bot 생성

1. [Discord Developer Portal](https://discord.com/developers/applications)에서 새 Application을 생성합니다.
2. **Bot** 탭에서 Bot을 추가하고 Token을 복사합니다.
3. **OAuth2 > URL Generator**에서 `bot` 스코프와 필요한 권한을 선택하여 초대 URL을 생성합니다.
4. 생성된 URL로 자신의 Discord 서버에 Bot을 초대합니다.

OpenClaw에 Discord 채널을 연결합니다:

```bash
openclaw channels add discord
# 프롬프트에 따라 Bot Token 입력
```

### 6.3 채널별 에이전트 바인딩

`~/.openclaw/openclaw.json`에 바인딩 설정을 추가합니다:

```json5
{
  "agents": {
    // ... (5.6의 list 설정)
  },
  "bindings": [
    // Telegram: 경영진 에이전트 (Attendant, PO, PM)
    {
      "agentId": "attendant",
      "match": { "channel": "telegram", "peer": { "kind": "dm", "id": "<CEO_TELEGRAM_ID>" } }
    },
    {
      "agentId": "po",
      "match": { "channel": "telegram", "peer": { "kind": "group", "id": "<PO_GROUP_ID>" } }
    },
    {
      "agentId": "pm",
      "match": { "channel": "telegram", "peer": { "kind": "group", "id": "<PM_GROUP_ID>" } }
    },

    // Discord: 기술팀 에이전트 (DEV, QA)
    {
      "agentId": "dev",
      "match": { "channel": "discord", "peer": { "kind": "channel", "id": "<DEV_CHANNEL_ID>" } }
    },
    {
      "agentId": "qa",
      "match": { "channel": "discord", "peer": { "kind": "channel", "id": "<QA_CHANNEL_ID>" } }
    }
  ]
}
```

**`<CEO_TELEGRAM_ID>`, `<PO_GROUP_ID>` 등은 실제 ID로 교체합니다.**

Telegram ID 확인 방법:
```bash
# Bot에게 메시지를 보낸 후:
curl -s "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates" | jq '.result[-1].message.chat.id'
```

바인딩 확인:

```bash
openclaw agents list --bindings
```

---

## 7. 거버넌스 커스터마이징

### 7.1 헌법 수정

`docs/core/legal/CONSTITUTION.md`를 자신의 조직 원칙에 맞게 수정합니다.

수정 추천 포인트:

| 섹션 | 수정 방향 |
|------|----------|
| **조직명** | "가재 컴퍼니" → 자신의 조직명 |
| **15대 리더십 원칙** | 자신의 가치관에 맞게 우선순위 조정 |
| **CEO 정보** | 자신의 정보로 교체 |
| **5대 지능 단계** | 기록 프로토콜 유지 또는 간소화 |

### 7.2 역할 정의 커스터마이징

`docs/core/role/ROLE_*.md` 파일에서 각 역할의 세부 책무를 조정합니다:

```bash
# 역할 파일 목록 확인
ls docs/core/role/
```

수정 시 주의사항:
- `SOUL.md`와 `ROLE_*.md`의 내용이 일관되어야 합니다.
- Swan ID는 에이전트 식별을 위한 고유값이므로 자유롭게 변경 가능합니다.

### 7.3 인사 기록 초기화

`docs/governance/personnel/` 하위의 인사 파일을 자신의 에이전트 설정에 맞게 초기화합니다:

```bash
# 기존 인사 기록 확인
ls docs/governance/personnel/

# 기존 감사 기록 초기화 (선택)
rm -rf docs/governance/personnel/audit/2026-02-06/
```

### 7.4 연대기 초기화

새로운 시작을 위해 기존 연대기를 정리합니다:

```bash
# 기존 연대기 백업
mv docs/chronicle/daily/2026-02-06 docs/chronicle/daily/2026-02-06.bak

# 새 연대기 시작 (오늘 날짜)
TODAY=$(date +%Y-%m-%d)
mkdir -p docs/chronicle/daily/${TODAY}/{command,meeting}

# INDEX.md 생성
cat > docs/chronicle/daily/${TODAY}/INDEX.md <<EOF
# ${TODAY} 연대기

## 오늘의 기록
- command/: CEO 명령 기록
- meeting/: 에이전트 미팅 기록
EOF
```

---

## 8. 웹앱 (가재 대시보드) 배포

### 8.1 로컬 실행

```bash
cd gajae-company
npm install
npm run dev
```

브라우저에서 `http://localhost:3000`으로 접속하여 대시보드를 확인합니다.

### 8.2 Firebase 프로젝트 생성

1. [Firebase Console](https://console.firebase.google.com)에서 새 프로젝트를 생성합니다.
2. **Blaze 플랜**(종량제)으로 업그레이드합니다 (Next.js SSR 배포에 필요).
3. 프로젝트 설정에서 웹앱을 추가하고 Firebase 설정값을 복사합니다.

### 8.3 Firebase 설정

`.firebaserc`를 자신의 프로젝트 ID로 수정합니다:

```json
{
  "projects": {
    "default": "<YOUR_FIREBASE_PROJECT_ID>"
  }
}
```

`firebase.json`은 이미 아래와 같이 설정되어 있습니다:

```json
{
  "hosting": {
    "source": ".",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "frameworksBackend": {
      "region": "asia-northeast3"
    }
  }
}
```

리전(`asia-northeast3` = 서울)은 필요에 따라 변경합니다.

### 8.4 Firebase 설정값 적용

`gajae-company/src/core/config/firebase-config.ts`에서 Firebase 설정값을 자신의 것으로 교체합니다.

### 8.5 배포

```bash
cd gajae-company
npx firebase-tools deploy
```

---

## 9. 보안 주의사항

### 9.1 API 키 관리

- Anthropic API 키를 절대 Git에 커밋하지 마세요.
- `.gitignore`에 다음이 포함되어 있는지 확인합니다:

```
.env
.env.local
**/auth-profiles.json
~/.openclaw/
```

### 9.2 Gateway 인증

OpenClaw Gateway에 **반드시** 인증을 설정해야 합니다. `auth: none`은 2026년부터 비활성화되었습니다.

```bash
# Gateway 설정에서 인증 확인
openclaw configure
# Settings > Gateway > Authentication 에서 username/password 설정
```

### 9.3 에이전트별 샌드박스

신뢰도가 낮은 채널의 에이전트에는 샌드박스를 적용합니다:

```json5
{
  "agents": {
    "list": [
      {
        "id": "qa",
        // ...
        "sandbox": {
          "mode": "all",
          "scope": "agent"
        },
        "tools": {
          "allow": ["read", "sessions_list"],
          "deny": ["exec", "write"]
        }
      }
    ]
  }
}
```

### 9.4 알려진 보안 이슈

- OpenClaw은 강력한 시스템 접근 권한을 가지므로, **스킬(skill) 설치 시 반드시 출처를 확인**하세요.
- 커뮤니티 스킬 중 악성 스킬이 보고된 바 있습니다.
- 공식 스킬 또는 직접 작성한 스킬만 사용하는 것을 권장합니다.

---

## 10. 트러블슈팅

### WSL systemd 오류

**증상**: `Failed to start service` 또는 `systemd not available`

**해결**:
```bash
# /etc/wsl.conf 확인
cat /etc/wsl.conf
# [boot] 섹션에 systemd=true 가 있는지 확인

# PowerShell에서 WSL 완전 재시작
wsl --shutdown
```

### Gateway 연결 실패

**증상**: `http://localhost:18789` 접속 불가

**해결**:
```bash
# Gateway 상태 확인
openclaw gateway status

# 포트 사용 확인
ss -tlnp | grep 18789

# Gateway 재시작
openclaw gateway restart
```

### 에이전트 인증 충돌

**증상**: 에이전트 간 세션이 섞이는 현상

**원인**: `agentDir`이 겹치는 경우 발생

**해결**:
- 각 에이전트의 `agentDir`이 고유한 경로인지 확인합니다.
- `~/.openclaw/agents/<agentId>/agent/` 형태로 분리합니다.
- `auth-profiles.json`을 에이전트 간 공유하지 않습니다.

### Node.js 버전 오류

**증상**: `Unsupported engine` 또는 모듈 호환성 오류

**해결**:
```bash
node --version  # v22 이상인지 확인
# nvm을 사용하는 경우:
nvm install 22
nvm use 22
```

### PowerShell vs WSL 혼동

- OpenClaw 관련 명령은 **반드시 WSL 터미널 내부**에서 실행합니다.
- PowerShell에서는 `wsl --install`, `wsl --shutdown` 등 WSL 관리 명령만 사용합니다.
- 두 환경의 명령을 혼용하면 경로 오류가 발생합니다.

---

## 부록: 나머지 6개 에이전트 확장

핵심 5개 에이전트가 안정적으로 동작한 후, 나머지 6개를 추가합니다.

### 확장 에이전트 목록

| 가재 역할 | Agent ID | 권장 모델 | 원본 정의 |
|-----------|----------|-----------|----------|
| BA (비즈니스 분석) | `ba` | `sonnet-4-5` | `docs/core/role/ROLE_BA.md` |
| UX (UX 설계) | `ux` | `sonnet-4-5` | `docs/core/role/ROLE_UX.md` |
| HR (인사 관리) | `hr` | `haiku` | `docs/core/role/ROLE_HR.md` |
| Legal (법무) | `legal` | `sonnet-4-5` | `docs/core/role/ROLE_LEGAL.md` |
| Marketing (마케팅) | `marketing` | `haiku` | `docs/core/role/ROLE_MARKETING.md` |
| CS (고객 서비스) | `cs` | `haiku` | `docs/core/role/ROLE_CS.md` |

### 추가 절차 요약

```bash
# 1. 워크스페이스 생성
for agent in ba ux hr legal marketing cs; do
  mkdir -p ~/.openclaw/workspace-${agent}
done

# 2. 각 에이전트의 SOUL.md 작성
#    -> docs/core/role/ROLE_*.md를 참고하여 작성

# 3. AGENTS.md, USER.md 배치
#    -> 5.4, 5.5 절차와 동일

# 4. openclaw.json의 agents.list에 추가
#    -> 5.6 형식과 동일하게 6개 에이전트 추가

# 5. 채널 바인딩 추가 (필요한 경우)
#    -> 6.3 형식과 동일하게 바인딩 추가
```

### 비용 최적화 팁

- HR, Marketing, CS처럼 상대적으로 단순한 업무는 `haiku` 모델로도 충분합니다.
- Attendant, PO, DEV처럼 복잡한 추론이 필요한 역할에만 `opus` 모델을 할당합니다.
- 사용 빈도가 낮은 에이전트는 필요할 때만 활성화하여 API 비용을 절감합니다.

---

## 참고 링크

- [OpenClaw 공식 문서](https://docs.openclaw.ai)
- [OpenClaw Windows 설치 가이드](https://docs.openclaw.ai/platforms/windows)
- [OpenClaw 멀티에이전트 라우팅](https://docs.openclaw.ai/concepts/multi-agent)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [OpenClaw 스킬 모음](https://github.com/VoltAgent/awesome-openclaw-skills)
- [yuna-openclaw 원본 레포](https://github.com/theo-learner/yuna-openclaw)
