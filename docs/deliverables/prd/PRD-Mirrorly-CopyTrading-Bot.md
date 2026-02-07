# PRD: Mirrorly Copy Trading Bot

> **문서 버전**: 1.0  
> **작성일**: 2026-02-07  
> **작성자**: PO Agent  
> **상태**: Draft → CEO 리뷰 대기  

---

## 1. 제품 개요

### 1.1 배경
[Mirrorly Live](https://t.me/MirrorlyLive)는 Hyperliquid, Binance 등 탑 거래소의 고래 트레이더 포지션을 실시간으로 알려주는 Telegram 채널이다. Mirrorly 자체는 "Self-Custody Copy Trading Platform"을 표방하지만, 텔레그램 채널의 시그널을 자동으로 수신·파싱·실행하는 독립 봇은 아직 존재하지 않는다.

### 1.2 제품 비전
**"고래가 움직이면 나도 움직인다 — 지연 없이, 감정 없이."**

Mirrorly Live 채널의 시그널을 실시간 수신하여, 사전 설정된 규칙에 따라 Hyperliquid/Binance에서 자동 카피 트레이딩을 실행하는 봇을 구축한다.

### 1.3 목표 사용자
| 구분 | 설명 |
|------|------|
| **1차 사용자** | 프로젝트 오너(CEO) — 개인 트레이딩 자동화 |
| **2차 사용자** | (서비스화 시) 소규모 크립토 트레이더, 시그널 팔로워 |

---

## 2. 실제 시그널 분석

### 2.1 채널 메시지 포맷 (실데이터 기반)

텔레그램 채널 스크래핑 결과, 시그널은 크게 **3가지 유형**으로 분류된다:

#### 유형 A: 신규 포지션 진입
```
larger than normal position from [트레이더명](리더보드URL). 
$금액 long/short on 코인 at $가격 (거래소).
```
**실제 예시:**
- `larger than normal position from Icy9999. $1,040,280 short on BTC at $69,309.039 (Hyperliquid).`
- `larger than normal position from Icy9999. $1,394,454 long on BTC at $70,840.218 (Hyperliquid).`

#### 유형 B: 포지션 종료 (수익)
```
[트레이더명] closed +$수익금 on 코인 (거래소). [코멘트]
+$수익금 on 코인 (거래소) for [트레이더명]. [코멘트]
[트레이더명] cooked +$수익금 on 코인 (거래소). [코멘트]
[트레이더명] did the job. (별도 문맥)
```
**실제 예시:**
- `Cyborg0578 closed +$31,436 on ZRO (BinanceSM). Good one.`
- `+$807,676 on BTC (Hyperliquid) for Mega Wombat. Easy green.`
- `Steel Mole just dropped +$13,573 on ZEC (Hyperliquid). Good clip.`
- `GDVLD cooked +$34,185 on BERA (Hyperliquid). Strong hit.`
- `Sifu closed +$187,110 on BTC (Hyperliquid). Nice print.`

#### 유형 C: 포지션 종료 (손실)
```
[트레이더명] closed -$손실금 on 코인 (거래소). [코멘트]
-$손실금 on 코인 (거래소) for [트레이더명]. [코멘트]
```
**실제 예시:**
- `TheCryptoNexus closed for -$859,383 on BTC (Hyperliquid). Took the hit.`
- `-$441,930 on BTC (Hyperliquid) for Wild Tamarin. reverse print.`
- `Ghost Duck closed -$36,410 on BTC (Hyperliquid). Rough.`

### 2.2 핵심 데이터 필드
| 필드 | 유형 A (진입) | 유형 B/C (종료) | 비고 |
|------|:---:|:---:|------|
| 트레이더명 | ✅ | ✅ | 하이퍼링크에 리더보드 URL 포함 |
| 지갑주소/UID | ✅ (URL 내) | ✅ (URL 내) | Hyperliquid: 0x 주소, Binance: 숫자 UID |
| 포지션 사이즈 ($) | ✅ | ❌ | 진입 시에만 |
| 방향 (long/short) | ✅ | ❌ | 진입 시에만 |
| 코인 | ✅ | ✅ | BTC, ETH, ZEC, ZRO, BERA 등 |
| 진입가 | ✅ | ❌ | 진입 시에만 |
| 거래소 | ✅ | ✅ | Hyperliquid, BinanceSM |
| 손익 ($) | ❌ | ✅ | +/- 부호로 수익/손실 구분 |
| 코멘트 | △ | ✅ | "Good clip", "Rough" 등 (파싱 불필요) |
| 크기 플래그 | ✅ | ❌ | "larger than normal position" 등 |

### 2.3 거래소 매핑
| 채널 표기 | 실제 거래소 | API |
|-----------|-----------|-----|
| Hyperliquid | Hyperliquid DEX | Hyperliquid Python SDK |
| BinanceSM | Binance 선물 (Strategy Manager) | Binance Futures API / ccxt |

---

## 3. 유저 스토리

### 3.1 핵심 유저 스토리 (Must-Have)

| ID | 유저 스토리 | 우선순위 | 단계 |
|----|-----------|---------|------|
| US-01 | 사용자로서, Mirrorly Live 채널의 시그널을 실시간으로 수신하고 싶다 | P0 | MVP 1단계 |
| US-02 | 사용자로서, 수신된 시그널에서 트레이더명, 방향, 코인, 사이즈, 진입가, 거래소를 자동 추출하고 싶다 | P0 | MVP 1단계 |
| US-03 | 사용자로서, 특정 트레이더만 필터링하여 팔로우하고 싶다 (화이트리스트) | P0 | MVP 1단계 |
| US-04 | 사용자로서, 파싱된 시그널을 로그로 저장하고 대시보드에서 확인하고 싶다 | P0 | MVP 1단계 |
| US-05 | 사용자로서, 시그널 진입 시 자동으로 Hyperliquid에 주문을 실행하고 싶다 | P0 | MVP 2단계 |
| US-06 | 사용자로서, 포지션 사이즈를 내 자본 대비 비율로 자동 조절하고 싶다 | P0 | MVP 2단계 |
| US-07 | 사용자로서, 시그널의 포지션 종료 알림 시 자동으로 포지션을 청산하고 싶다 | P0 | MVP 2단계 |

### 3.2 중요 유저 스토리 (Should-Have)

| ID | 유저 스토리 | 우선순위 | 단계 |
|----|-----------|---------|------|
| US-08 | 사용자로서, Binance 선물에서도 자동 주문을 실행하고 싶다 | P1 | 2단계+ |
| US-09 | 사용자로서, 최대 동시 포지션 수와 최대 손실 한도를 설정하고 싶다 | P1 | 2단계 |
| US-10 | 사용자로서, 각 트레이더별 과거 성과(승률, 수익률)를 자동 집계하고 싶다 | P1 | 1단계+ |
| US-11 | 사용자로서, 봇 상태와 포지션 현황을 Telegram 개인 채널로 알림받고 싶다 | P1 | 2단계 |
| US-12 | 사용자로서, 특정 코인만 트레이딩하거나 제외하고 싶다 (코인 필터) | P1 | 1단계 |

### 3.3 추후 유저 스토리 (Nice-to-Have)

| ID | 유저 스토리 | 우선순위 | 단계 |
|----|-----------|---------|------|
| US-13 | 사용자로서, 시그널 기반 백테스팅을 실행하고 싶다 | P2 | 3단계 |
| US-14 | 사용자로서, 여러 시그널 소스(다른 Telegram 채널)를 추가하고 싶다 | P2 | 3단계 |
| US-15 | 사용자로서, 웹 대시보드에서 전체 성과를 모니터링하고 싶다 | P2 | 3단계 |
| US-16 | 사용자로서, "larger than normal" 같은 크기 플래그에 따라 배팅 비율을 다르게 설정하고 싶다 | P2 | 2단계+ |

---

## 4. MVP 범위 정의

### 4.1 MVP 1단계: 시그널 수집 + 파싱 (2~3주)

#### 범위 포함 (In Scope)
- Telethon 기반 Mirrorly Live 채널 실시간 리스너
- 정규식 + 패턴 매칭 기반 시그널 파서 (유형 A/B/C)
- 트레이더 화이트리스트/블랙리스트 필터
- 코인 필터 (허용/제외 목록)
- 파싱 결과 JSON/DB 저장 (SQLite 또는 PostgreSQL)
- 파싱 실패 시 원본 메시지 로깅 + 알림
- 기본 CLI 대시보드 (최근 시그널, 트레이더 통계)
- Docker 컨테이너화

#### 범위 제외 (Out of Scope)
- 실제 주문 실행
- 웹 UI
- 멀티 채널 지원

#### 핵심 산출물
```
mirrorly-bot/
├── src/
│   ├── collector/          # Telethon 채널 리스너
│   ├── parser/             # 시그널 파서 (3가지 유형)
│   ├── filter/             # 트레이더/코인 필터
│   ├── storage/            # DB 저장 레이어
│   └── notifier/           # 상태 알림 (Telegram DM)
├── config.yaml             # 설정 파일
├── tests/                  # 파서 유닛 테스트
└── docker-compose.yml
```

### 4.2 MVP 2단계: 자동 주문 실행 (3~4주)

#### 범위 포함 (In Scope)
- Hyperliquid Python SDK 연동 (시장가/지정가 주문)
- 포지션 사이즈 자동 조절 (자본 대비 비율 방식)
- 시그널 종료 알림 기반 자동 청산
- 리스크 관리 모듈:
  - 최대 동시 포지션 수 제한
  - 단일 포지션 최대 사이즈 제한
  - 일일/주간 최대 손실 한도 (킬스위치)
  - 긴급 전체 청산 명령
- Telegram DM으로 주문 실행/결과 알림
- 시뮬레이션 모드 (Paper Trading)

#### 범위 제외 (Out of Scope)
- Binance 연동 (P1, 2단계 이후 확장)
- 웹 대시보드
- 서비스화 / 멀티 유저

---

## 5. 시그널 파싱 명세

### 5.1 파싱 패턴 정의

#### 패턴 A: 신규 포지션 진입
```python
# 패턴 A-1: "larger than normal position from [name]. $amount direction on COIN at $price (exchange)."
r'(?:larger than normal position from|new position from)\s+\[?(\w[\w\s]*?)\]?\s*[\.\!]?\s*\$([0-9,.]+)\s+(long|short)\s+on\s+(\w+)\s+at\s+\$([0-9,.]+)\s+\((\w+)\)'

# 패턴 A-2: "[name] going bigger than usual. $amount direction on COIN at $price (exchange)."
r'\[?(\w[\w\s]*?)\]?\s+going\s+bigger.*?\$([0-9,.]+)\s+(long|short)\s+on\s+(\w+)\s+at\s+\$([0-9,.]+)\s+\((\w+)\)'
```

#### 패턴 B: 포지션 종료 (수익/손실)
```python
# 패턴 B-1: "[name] closed +/-$amount on COIN (exchange)."
r'\[?(\w[\w\s]*?)\]?\s+(?:closed|closed for|just dropped|cooked)\s+([+-]?\$[0-9,.]+)\s+on\s+(\w+)\s+\((\w+)\)'

# 패턴 B-2: "+/-$amount on COIN (exchange) for [name]."
r'([+-]?\$[0-9,.]+)\s+on\s+(\w+)\s+\((\w+)\)\s+for\s+\[?(\w[\w\s]*?)\]?'
```

### 5.2 파싱 출력 스키마
```json
{
  "signal_id": "uuid",
  "timestamp": "2026-02-07T01:05:00Z",
  "raw_message": "원본 메시지 전문",
  "type": "entry | exit",
  "trader": {
    "name": "Icy9999",
    "address": "0x8434b7844Fd17fAD52f0aCEae50a834Cd4896577",
    "profile_url": "https://portal.mirrorly.xyz/leaderboard/..."
  },
  "exchange": "Hyperliquid",
  "coin": "BTC",
  "direction": "long | short | null",
  "entry_price": 70840.218,
  "position_size_usd": 1394454,
  "pnl_usd": null,
  "size_flag": "larger_than_normal | bigger_than_usual | normal",
  "parsed_successfully": true
}
```

---

## 6. 피쳐 우선순위 매트릭스

| 순위 | 피쳐 | 영향도 | 구현 난이도 | MVP 단계 | 비고 |
|:----:|------|:------:|:---------:|:--------:|------|
| 1 | Telegram 채널 실시간 리스너 | 🔴 Critical | 낮음 | 1단계 | Telethon 성숙 라이브러리 |
| 2 | 시그널 파서 (3유형) | 🔴 Critical | 중간 | 1단계 | 정규식 + 폴백 필요 |
| 3 | 트레이더 화이트리스트 | 🔴 Critical | 낮음 | 1단계 | config 기반 |
| 4 | 파싱 결과 DB 저장 | 🟡 High | 낮음 | 1단계 | SQLite로 시작 |
| 5 | 트레이더 성과 통계 | 🟡 High | 낮음 | 1단계 | 저장 데이터 기반 집계 |
| 6 | 시뮬레이션 모드 (Paper) | 🔴 Critical | 중간 | 2단계 | 실제 실행 전 검증 필수 |
| 7 | Hyperliquid 주문 실행 | 🔴 Critical | 높음 | 2단계 | SDK 연동 + 에러 핸들링 |
| 8 | 포지션 사이즈 자동 조절 | 🔴 Critical | 중간 | 2단계 | 고래 사이즈 → 내 자본 비율 변환 |
| 9 | 시그널 기반 자동 청산 | 🟡 High | 중간 | 2단계 | 종료 시그널 매칭 로직 |
| 10 | 리스크 관리 (킬스위치) | 🔴 Critical | 중간 | 2단계 | 손실 한도 초과 시 전체 청산 |
| 11 | Telegram 알림 (봇 → 나) | 🟡 High | 낮음 | 2단계 | Bot API 사용 |
| 12 | 코인 필터 | 🟢 Medium | 낮음 | 1단계 | config 기반 |
| 13 | 크기 플래그별 배팅 조절 | 🟢 Medium | 낮음 | 2단계+ | "larger than normal" → 1.5x 등 |
| 14 | Binance 선물 연동 | 🟡 High | 높음 | 3단계 | ccxt 기반 |
| 15 | 백테스팅 엔진 | 🟢 Medium | 높음 | 3단계 | 축적 데이터 필요 |
| 16 | 웹 대시보드 | 🟢 Medium | 높음 | 3단계 | 개인용이면 CLI 충분 |

---

## 7. 성공 지표 (KPI)

### 7.1 MVP 1단계 KPI

| 지표 | 목표값 | 측정 방법 |
|------|--------|----------|
| **시그널 수신율** | ≥ 99.5% | 수신 메시지 수 / 채널 실제 메시지 수 |
| **파싱 성공률** | ≥ 95% | 정상 파싱 수 / 전체 수신 메시지 수 |
| **수신 지연시간** | < 2초 | 채널 게시 → 봇 수신 타임스탬프 차이 |
| **파싱 지연시간** | < 100ms | 수신 → 파싱 완료 시간 |
| **봇 가동률** | ≥ 99% | 월간 업타임 |
| **트레이더 통계 정확도** | ≥ 98% | 수동 검증 대비 일치율 |

### 7.2 MVP 2단계 KPI

| 지표 | 목표값 | 측정 방법 |
|------|--------|----------|
| **주문 실행 지연시간** | < 5초 | 시그널 수신 → 주문 체결 시간 |
| **주문 실행 성공률** | ≥ 98% | 성공 주문 / 시도 주문 |
| **슬리피지** | < 0.3% | 시그널 가격 vs 실제 체결 가격 차이 |
| **시뮬레이션 추적 오차** | < 1% | Paper 결과 vs 실제 시장 결과 |
| **킬스위치 반응시간** | < 1초 | 한도 초과 감지 → 전체 청산 실행 |
| **수익 추적률** | 100% | 모든 트레이드 PnL 기록 여부 |

### 7.3 비즈니스 KPI (장기)

| 지표 | 목표값 | 비고 |
|------|--------|------|
| **월간 순수익률** | > 0% (수익) | 수수료 차감 후 |
| **최대 낙폭 (MDD)** | < 20% | 리스크 관리 효과성 |
| **샤프 비율** | > 1.0 | 리스크 대비 수익 |
| **시그널 팔로우 수익 vs 직접 트레이딩** | 양의 알파 | A/B 비교 |

---

## 8. 리스크 분석

### 8.1 기술적 리스크

| 리스크 | 심각도 | 발생확률 | 완화 방안 |
|--------|:------:|:--------:|----------|
| **Telegram MTProto 차단/제한** | 🔴 높음 | 중간 | 유저 API 사용 시 레이트 리밋 준수, 세션 관리, 자동 재연결 로직 |
| **시그널 포맷 변경** | 🟡 중간 | 높음 | 파싱 실패 알림 + 원본 저장, 정규식 모듈화로 빠른 업데이트 |
| **Hyperliquid API 장애** | 🟡 중간 | 중간 | 재시도 로직, 주문 상태 폴링, 수동 개입 알림 |
| **네트워크 지연으로 슬리피지 증가** | 🟡 중간 | 중간 | 서버 위치 최적화 (Hyperliquid 노드 근접), 시장가 주문 시 슬리피지 한도 설정 |
| **동시 시그널 폭주** | 🟢 낮음 | 낮음 | 큐 기반 처리, 동시 포지션 수 제한 |
| **봇 프로세스 다운** | 🔴 높음 | 낮음 | systemd/Docker 자동 재시작, 상태 영속화, 헬스체크 |

### 8.2 재무적 리스크

| 리스크 | 심각도 | 발생확률 | 완화 방안 |
|--------|:------:|:--------:|----------|
| **고래 시그널이 악의적/조작** | 🔴 높음 | 낮음 | 트레이더별 성과 추적, 승률 낮은 트레이더 자동 제외 |
| **연쇄 손실 (마진콜)** | 🔴 높음 | 중간 | 일일 최대 손실 킬스위치, 계좌 잔고 비율 제한 (예: 최대 30%) |
| **슬리피지/수수료 누적** | 🟡 중간 | 높음 | 최소 포지션 사이즈 설정, 수수료 시뮬레이션 사전 계산 |
| **API 키 유출** | 🔴 높음 | 낮음 | 환경변수 관리, 서브계정 사용, 출금 권한 제외, IP 화이트리스트 |
| **시그널 수신 지연으로 진입가 불리** | 🟡 중간 | 중간 | 최대 슬리피지 허용치 설정, 초과 시 주문 스킵 |

### 8.3 법적 리스크

| 리스크 | 심각도 | 발생확률 | 완화 방안 |
|--------|:------:|:--------:|----------|
| **Telegram 채널 스크래핑 ToS 위반** | 🟡 중간 | 중간 | 유저 API(MTProto)는 공식 지원, 과도한 자동화 지양 |
| **Mirrorly 서비스 약관 위반** | 🟡 중간 | 불명 | Mirrorly 약관 확인 필요, 공개 채널 데이터 활용 |
| **금융규제 (투자자문업)** | 🔴 높음 | 낮음 (개인용) | 개인 사용 한정, 서비스화 시 법률 검토 필수 |
| **거래소 API 이용 약관** | 🟡 중간 | 낮음 | 자동매매는 일반적으로 허용, 각 거래소 약관 확인 |

### 8.4 운영 리스크

| 리스크 | 심각도 | 발생확률 | 완화 방안 |
|--------|:------:|:--------:|----------|
| **Mirrorly Live 채널 폐쇄/이전** | 🔴 높음 | 낮음 | 멀티 소스 아키텍처 설계, 채널 ID 외부 설정 |
| **Telegram 계정 밴** | 🟡 중간 | 낮음 | 전용 계정 사용, 읽기 전용 동작, 메시지 전송 없음 |

---

## 9. 기술 아키텍처 (High-Level)

```
┌─────────────────┐     ┌──────────────┐     ┌──────────────┐
│  Telegram        │     │   Signal     │     │   Order      │
│  Mirrorly Live   │────▶│   Parser     │────▶│   Executor   │
│  (MTProto)       │     │              │     │              │
└─────────────────┘     └──────┬───────┘     └──────┬───────┘
                               │                     │
                        ┌──────▼───────┐     ┌──────▼───────┐
                        │   Filter     │     │  Hyperliquid │
                        │  (Trader/    │     │    SDK       │
                        │   Coin)      │     │  Binance API │
                        └──────┬───────┘     └──────┬───────┘
                               │                     │
                        ┌──────▼───────┐     ┌──────▼───────┐
                        │   Storage    │     │    Risk      │
                        │  (SQLite/    │     │   Manager    │
                        │   Postgres)  │     │  (Kill Switch│
                        └──────┬───────┘     │   Limits)    │
                               │             └──────────────┘
                        ┌──────▼───────┐
                        │   Notifier   │
                        │  (Telegram   │
                        │   Bot DM)    │
                        └──────────────┘
```

### 9.1 기술 스택 (권장)
| 레이어 | 기술 | 이유 |
|--------|------|------|
| 언어 | Python 3.11+ | Telethon, Hyperliquid SDK 모두 Python |
| Telegram 수신 | Telethon (MTProto User API) | 채널 읽기에 Bot API 불가, User API 필수 |
| 시그널 파싱 | 정규식 + 구조화 파서 | 비정형 텍스트, LLM 파싱은 지연 과다 |
| DB | SQLite (MVP) → PostgreSQL | 단일 유저 MVP는 SQLite 충분 |
| 주문 실행 | hyperliquid-python-sdk, ccxt | 공식 SDK 우선, ccxt는 Binance 용 |
| 배포 | Docker + docker-compose | 재현성, 이식성 |
| 모니터링 | Telegram Bot 알림 + 로그 | 별도 모니터링 인프라 불필요 (MVP) |

---

## 10. 수익 모델 검토

### 10.1 개인 사용 (1차 목표)

| 항목 | 내용 |
|------|------|
| **목적** | CEO 개인 트레이딩 자동화 |
| **수익** | 카피 트레이딩 수익 자체 |
| **비용** | 서버 비용 (~$10-30/월), 거래 수수료, 개발 인건비 |
| **손익분기** | 월 $50+ 순수익 시 서버 비용 커버 |
| **장점** | 법적 리스크 최소, 빠른 MVP, 규제 무관 |

### 10.2 서비스화 (2차 검토)

| 모델 | 설명 | 수익 구조 | 리스크 |
|------|------|----------|--------|
| **A. 시그널 리셀** | 파싱된 시그널을 구조화하여 유료 채널 운영 | 구독료 $29-99/월 | Mirrorly 저작권, 금융규제 |
| **B. 봇 SaaS** | 봇 자체를 클라우드 서비스로 제공, 유저가 자기 API 키 연결 | 구독료 $49-199/월 | 개발·운영 비용 높음, 책임 이슈 |
| **C. 수익 배분** | 유저 수익의 10-20% 수수료 | 성과 기반 수수료 | 정산 복잡, 신뢰 필요 |
| **D. 오픈소스 + 프리미엄** | 코어는 무료, 고급 필터/분석은 유료 | 프리미엄 $19-49/월 | 커뮤니티 관리 필요 |

### 10.3 수익 모델 권고
> **1단계에서는 개인 사용에 집중**하되, 아키텍처를 멀티 유저 확장 가능하게 설계한다. 서비스화는 3개월간 실전 성과 데이터 축적 후, 수익률/안정성이 검증되면 **모델 B (봇 SaaS)** 를 우선 검토한다.

---

## 11. 프로젝트 타임라인

```
Phase 1 (MVP 1단계): 시그널 수집 + 파싱
├── Week 1: Telethon 연동 + 기본 파서 개발
├── Week 2: 필터 + DB 저장 + 테스트
└── Week 3: 안정화 + 파싱 커버리지 검증 + 트레이더 통계

Phase 2 (MVP 2단계): 자동 주문 실행
├── Week 4: Hyperliquid SDK 연동 + 시뮬레이션 모드
├── Week 5: 포지션 사이징 + 리스크 관리
├── Week 6: 시그널→주문 자동 파이프라인 + 알림
└── Week 7: 실전 투입 (소액) + 모니터링 + 안정화

Phase 3 (확장): 
├── Week 8-10: Binance 연동 + 크기 플래그 배팅 조절
├── Week 11-12: 백테스팅 엔진 + 성과 분석
└── Week 13+: 서비스화 검토 (성과 데이터 기반)
```

---

## 12. 설정 파일 구조 (Config Spec)

```yaml
# config.yaml
telegram:
  api_id: "YOUR_API_ID"
  api_hash: "YOUR_API_HASH"
  phone: "+82XXXXXXXXXX"
  channel: "MirrorlyLive"            # 채널 username
  channel_id: -1003757236448          # 채널 numeric ID (실데이터 확인)

trading:
  mode: "paper"                       # paper | live
  exchange: "hyperliquid"             # hyperliquid | binance
  
  position_sizing:
    method: "fixed_ratio"             # fixed_ratio | fixed_amount
    ratio: 0.02                       # 자본의 2% per trade
    max_amount_usd: 1000              # 단일 최대 $1,000
  
  risk_management:
    max_concurrent_positions: 5
    max_daily_loss_usd: 500
    max_weekly_loss_usd: 2000
    max_slippage_pct: 0.5             # 0.5% 초과 시 주문 스킵
    kill_switch_loss_pct: 10          # 계좌 10% 손실 시 전체 청산

filters:
  trader_whitelist:                   # 빈 목록 = 전체 허용
    - "Icy9999"
    - "Sifu"
    - "Mega Wombat"
  trader_blacklist: []
  coin_whitelist: []                  # 빈 목록 = 전체 허용
  coin_blacklist:
    - "SHIB"
    - "DOGE"
  min_position_size_usd: 100000      # 최소 포지션 사이즈 (작은 포지션 무시)
  size_flag_multiplier:
    larger_than_normal: 1.5
    bigger_than_usual: 1.5
    normal: 1.0

notifications:
  telegram_bot_token: "YOUR_BOT_TOKEN"
  chat_id: "YOUR_CHAT_ID"
  notify_on:
    - signal_received
    - order_executed
    - order_failed
    - daily_summary
    - kill_switch_triggered

hyperliquid:
  wallet_address: "0xYOUR_ADDRESS"
  private_key_env: "HL_PRIVATE_KEY"   # 환경변수 참조 (파일에 직접 저장 금지)

binance:
  api_key_env: "BINANCE_API_KEY"
  api_secret_env: "BINANCE_API_SECRET"
```

---

## 13. 의존성 및 전제 조건

| # | 전제 조건 | 담당 | 상태 |
|---|----------|------|------|
| 1 | Telegram 계정 + API ID/Hash 확보 | CEO | ⬜ 미완 |
| 2 | Hyperliquid 지갑 + 트레이딩 서브계정 생성 | CEO | ⬜ 미완 |
| 3 | 서버/VPS 환경 확보 (Python 3.11+, Docker) | DevOps | ⬜ 미완 |
| 4 | Mirrorly Live 채널 조인 (Telegram 계정으로) | CEO | ⬜ 미완 |
| 5 | 초기 운용 자본 확보 (2단계용) | CEO | ⬜ 미완 |
| 6 | Binance 선물 계정 + API 키 (3단계용) | CEO | ⬜ 미완 |

---

## 14. 오픈 이슈 & 결정 필요 항목

| # | 이슈 | 의사결정자 | 기한 |
|---|------|----------|------|
| 1 | Mirrorly 약관에서 시그널 스크래핑 제한 여부 확인 | CEO/법무 | Phase 1 시작 전 |
| 2 | 초기 운용 자본 규모 결정 ($500? $1,000? $5,000?) | CEO | Phase 2 시작 전 |
| 3 | 시뮬레이션 최소 기간 결정 (1주? 2주?) | CEO/PO | Phase 2 시작 전 |
| 4 | 트레이더 화이트리스트 초기 선정 (채널 데이터 기반 성과 분석 후) | CEO/PO | Phase 1 완료 후 |
| 5 | 서비스화 검토 시점 및 기준 | CEO | Phase 2 완료 후 |

---

## 부록 A: 참고 트레이더 목록 (채널 실데이터 기반)

| 트레이더명 | 거래소 | 관찰된 코인 | 관찰된 규모 | 비고 |
|-----------|--------|-----------|-----------|------|
| Icy9999 | Hyperliquid | BTC | $1M~1.4M | 대형 포지션, 빈번 |
| Sifu | Hyperliquid | BTC, ETH | $185K~187K | 다중 코인 |
| Mega Wombat | Hyperliquid | BTC | $807K | 대형 |
| TheCryptoNexus | Hyperliquid | BTC | $859K (손실) | 고위험 |
| Steel Mole | Hyperliquid | ZEC | $13K | 소형 |
| Cyborg0578 | BinanceSM | ZRO | $31K | Binance 유일 관찰 |
| GDVLD | Hyperliquid | BERA | $34K | 알트코인 |
| Wild Tamarin | Hyperliquid | BTC | $441K (손실) | 고위험 |
| Phantom Yak | Hyperliquid | BTC | $500K | 대형 |
| Ghost Duck | Hyperliquid | BTC | $36K (손실) | - |

---

## 부록 B: 경쟁/유사 서비스

| 서비스 | 특징 | 차이점 |
|--------|------|--------|
| Mirrorly Portal | 자체 카피 트레이딩 플랫폼 | 자체 UI, 우리는 텔레그램 시그널 기반 |
| Copin.io | 온체인 카피 트레이딩 | Hyperliquid 특화, 유료 |
| 3Commas | 시그널 기반 봇 | 범용, 커스텀 시그널 소스 미지원 |
| Cornix | Telegram 시그널 봇 | 특정 포맷만 지원, Mirrorly 비호환 |

---

*끝. 이 PRD는 CEO 리뷰 후 개발팀에 전달됩니다.*
