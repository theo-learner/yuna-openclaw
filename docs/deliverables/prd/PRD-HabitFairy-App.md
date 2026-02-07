# 습관요정 (HabitFairy) — Product Requirements Document

> **문서 버전:** v1.0  
> **작성일:** 2026-02-07  
> **작성자:** PO Agent  
> **상태:** CEO 승인 대기  
> **대상 독자:** DEV, Design, Marketing, 경영진

---

## 목차

1. [프로덕트 정의](#1-프로덕트-정의)
2. [MVP 기능 (Week 1~3)](#2-mvp-기능-week-13)
3. [기술 스택 및 아키텍처](#3-기술-스택-및-아키텍처)
4. [수익 모델](#4-수익-모델)
5. [Day 1~21 실행 일정](#5-day-121-실행-일정)
6. [비용 산출 + BEP](#6-비용-산출--bep)
7. [KPI](#7-kpi)
8. [리스크 + 법률 체크리스트](#8-리스크--법률-체크리스트)
9. [DEV 구현 기술 스펙](#9-dev-구현-기술-스펙)

---

## 1. 프로덕트 정의

### 1.1 서비스 개요

| 항목 | 내용 |
|------|------|
| **서비스명** | 습관요정 (HabitFairy) |
| **한줄 설명** | AI 요정이 4~6세 아이의 생활습관을 게임처럼 만들어주는 앱 |
| **타겟 시장** | 대한민국, 4~6세 아이 + 부모 |
| **플랫폼** | Next.js PWA (Web-first, 추후 앱스토어 래핑) |
| **TAM** | 한국 4~6세 아동 약 120만명 × 가구당 1 구독 |

### 1.2 핵심 기능

1. **AI 요정 캐릭터** — 미션 부여, 응원, 완료 축하 (음성 + 애니메이션)
2. **기본 미션 10개 프리셋** — 양치, 정리, 인사, 옷 입기, 신발 신기, 손 씻기, 식사, 책 읽기, 장난감 정리, 인사하기
3. **타이머 + 음악** — 미션별 타이머 (양치 3분 등) + 동기부여 BGM
4. **별 보상 시스템** — 미션 완료 → 별 획득 → 캐릭터 꾸미기 아이템 교환
5. **부모 대시보드** — 달성률, 주간 리포트, 커스텀 미션 추가
6. **부모 커스텀 미션** — 부모가 직접 미션 생성 (이름, 설명, 타이머, 보상)

### 1.3 유저 페르소나

#### 페르소나 A: 아이 (주 사용자)
- **이름:** 하은 (5세, 여)
- **상황:** 매일 아침 양치를 싫어하고, 옷 입기를 거부함
- **니즈:** 재미있는 동기부여, 캐릭터와의 교감, 즉각적 보상
- **행동:** 태블릿/스마트폰 조작 가능, 그림/캐릭터에 반응
- **Pain:** 반복적 잔소리에 의한 저항감

#### 페르소나 B: 부모 (구매 결정자)
- **이름:** 민지맘 (34세, 직장인)
- **상황:** 맞벌이, 아침마다 아이와 전쟁
- **니즈:** 아이 자발적 습관 형성, 진행 상황 확인, 교육적 콘텐츠
- **행동:** 앱스토어 리뷰 확인, 엄마 카페 추천 신뢰
- **Pain:** 매일 반복되는 습관 지도 피로

### 1.4 경쟁사 분석

| 앱 | 타겟 연령 | 핵심 기능 | 한국 지원 | 약점 |
|----|----------|----------|----------|------|
| **Joon** | 6~12세 | 가상 펫 육성 + 과제 관리 | ❌ 영어만 | 나이 타겟 높음, 한국어 미지원 |
| **Habitica** | 성인/청소년 | RPG 게이미피케이션 | 부분 | 어린이 부적합, 복잡한 UI |
| **ChoreMonster** | 6~12세 | 보상 기반 할일 관리 | ❌ | 서비스 중단됨 |
| **뽀로로 습관놀이** | 3~6세 | 캐릭터 기반 습관 | ✅ | AI 미적용, 커스텀 불가 |

### 1.5 차별화 포인트 (Moat)

1. **AI 개인화** — 아이 이름 호출, 달성률 기반 응원 메시지 동적 생성
2. **한국 타겟 최적화** — 한국어 음성, 한국 문화 미션 (인사/신발 정리 등)
3. **4~6세 전문** — 경쟁사 대비 더 낮은 연령대에 최적화된 UX
4. **부모 커스텀** — 부모가 자유롭게 미션 추가/수정 가능
5. **PWA + 웹 결제** — 앱스토어 수수료 30% 회피, 빠른 배포

---

## 2. MVP 기능 (Week 1~3)

### 2.1 P0 — 필수 (MVP, Week 1~3)

#### F-001: 기본 미션 10개 프리셋
| 항목 | 상세 |
|------|------|
| **미션 목록** | ① 양치하기 ② 세수하기 ③ 손 씻기 ④ 옷 입기 ⑤ 신발 신기 ⑥ 인사하기 ⑦ 밥 먹기 ⑧ 장난감 정리 ⑨ 책 읽기 ⑩ 잠자리 준비 |
| **미션 속성** | `id`, `name`, `description`, `icon`, `timer_seconds`, `bgm_url`, `star_reward`, `category` (아침/점심/저녁), `fairy_message_start`, `fairy_message_complete` |
| **카테고리** | 아침 루틴 (①②④⑤⑥), 일과 (③⑦⑧⑨), 저녁 루틴 (⑩) |

#### F-002: AI 요정 캐릭터
| 항목 | 상세 |
|------|------|
| **캐릭터** | "별이" — 반짝이는 요정 (Lottie 애니메이션) |
| **인터랙션** | 미션 시작 시 응원 → 진행 중 힌트 → 완료 시 축하 |
| **AI 대화** | Claude API 사용, 아이 이름 포함, 5세 수준 쉬운 말투 |
| **음성** | TTS (네이버 클로바 or Google Cloud TTS 한국어) |
| **프롬프트** | `너는 5세 아이의 생활습관 요정 '별이'야. 항상 밝고 귀엽게 말하고, 아이 이름을 불러줘. 미션을 재미있게 설명하고, 완료하면 신나게 축하해줘. 3문장 이내로 말해.` |

#### F-003: 타이머 + 음악
| 항목 | 상세 |
|------|------|
| **타이머** | 미션별 커스텀 시간 (양치 180초, 손씻기 30초 등) |
| **UI** | 원형 프로그레스 바 + 숫자 카운트다운 + 캐릭터 애니메이션 |
| **음악** | 미션별 BGM (로열티 프리), 완료 시 팡파레 효과음 |
| **구현** | `setInterval` 기반, 백그라운드 전환 시 `visibilitychange` 처리 |

#### F-004: 별 보상 시스템 + 캐릭터 꾸미기
| 항목 | 상세 |
|------|------|
| **보상** | 미션 1개 완료 = 1~3별 (난이도별 차등) |
| **꾸미기 아이템** | 모자, 옷, 날개, 배경 등 총 30개 (MVP) |
| **아이템 해금** | 별 5/10/20/50개 단위 |
| **저장** | Supabase DB (`user_stars`, `user_items`, `user_avatar`) |

#### F-005: 부모 대시보드
| 항목 | 상세 |
|------|------|
| **달성률** | 일별/주별 미션 완료율 차트 (Recharts) |
| **주간 리포트** | 매주 일요일 자동 생성, 이메일 발송 (선택) |
| **미션 관리** | 미션 on/off, 순서 변경, 시간대 설정 |
| **인증** | 부모 전용 PIN (4자리) 또는 패턴 잠금 |

#### F-006: 부모 커스텀 미션 추가
| 항목 | 상세 |
|------|------|
| **입력 필드** | 미션 이름, 설명 (선택), 타이머 시간 (선택), 별 보상 수, 카테고리, 반복 주기 |
| **AI 보조** | 미션 이름 입력 시 AI가 아이 친화적 설명 자동 생성 |
| **제한** | 무료 플랜: 커스텀 미션 2개, 베이직: 무제한 |

### 2.2 P1 — Phase 2 (Week 4~6)

#### F-007: AI 난이도 자동 조절
- 최근 7일 달성률 분석 → 80% 이상이면 미션 추가/난이도 업 → 50% 이하면 미션 축소/격려 강화
- Claude API로 개인화된 난이도 조절 로직

#### F-008: 스토리 해금
- 별 50개 → 동화 에피소드 1편 해금 (총 12편, 시즌 1)
- "별이의 모험" 시리즈 — 습관과 연결된 교훈 동화
- 일러스트 + TTS 나레이션

#### F-009: 알림/리마인더
- 부모 설정 시간에 Push 알림 (아침 7시 "아침 루틴 시작!", 저녁 8시 "잠자리 준비!")
- PWA Web Push (Service Worker)
- FCM (Firebase Cloud Messaging) 연동

---

## 3. 기술 스택 및 아키텍처

### 3.1 기술 스택 결정

| 레이어 | 선택 | 근거 |
|--------|------|------|
| **Frontend** | Next.js 14 (App Router) + PWA | 앱스토어 심사 회피, 즉시 배포, 토스 미니앱 연동 가능, SEO |
| **UI Framework** | Tailwind CSS + Framer Motion | 빠른 개발, 부드러운 애니메이션 |
| **상태 관리** | Zustand | 경량, 간단한 API |
| **Backend** | Supabase (PostgreSQL + Auth + Storage + Edge Functions) | BaaS로 개발 속도 극대화 |
| **AI** | Claude API (Anthropic) | 한국어 성능 우수, 아동 안전 필터 내장 |
| **TTS** | Google Cloud TTS (한국어, WaveNet) | 자연스러운 음성, 아이 친화적 톤 가능 |
| **결제** | 토스페이먼츠 (빌링키 방식 정기결제) | 한국 결제 최적화, PG 수수료 ~3.3% |
| **호스팅** | Vercel | Next.js 최적 호스팅, Edge Network |
| **애니메이션** | Lottie (lottie-react) | 경량 벡터 애니메이션, 캐릭터 표현 |
| **차트** | Recharts | React 네이티브 차트 라이브러리 |
| **모니터링** | Sentry + Vercel Analytics | 에러 추적 + 성능 모니터링 |

### 3.2 아키텍처 다이어그램

```
┌─────────────────────────────────────────────────────┐
│                    Client (PWA)                      │
│  ┌──────────┐  ┌──────────┐  ┌───────────────────┐  │
│  │ 아이 모드 │  │ 부모 모드 │  │ Service Worker    │  │
│  │(미션/보상)│  │(대시보드) │  │(오프라인/Push)    │  │
│  └────┬─────┘  └────┬─────┘  └───────────────────┘  │
│       │              │                                │
│  ┌────┴──────────────┴─────┐                         │
│  │    Next.js App Router    │                         │
│  │  + Zustand State Mgmt    │                         │
│  └────────────┬─────────────┘                         │
└───────────────┼─────────────────────────────────────┘
                │ HTTPS
    ┌───────────┼───────────────────────────┐
    │           ▼                           │
    │  ┌─────────────────┐                  │
    │  │   Supabase       │                  │
    │  │  ┌─────────────┐ │  ┌────────────┐ │
    │  │  │ PostgreSQL   │ │  │ Edge Funcs  │ │
    │  │  │ (데이터)     │ │  │ (AI 프록시) │ │
    │  │  ├─────────────┤ │  └──────┬─────┘ │
    │  │  │ Auth         │ │        │        │
    │  │  │ (소셜로그인) │ │        ▼        │
    │  │  ├─────────────┤ │  ┌────────────┐ │
    │  │  │ Storage      │ │  │ Claude API │ │
    │  │  │ (에셋)       │ │  │ (AI 요정)  │ │
    │  │  └─────────────┘ │  └────────────┘ │
    │  └─────────────────┘                  │
    │                                       │
    │  ┌─────────────┐  ┌───────────────┐   │
    │  │ Google TTS   │  │ 토스페이먼츠   │   │
    │  │ (음성 생성)  │  │ (정기 결제)   │   │
    │  └─────────────┘  └───────────────┘   │
    └───────────────────────────────────────┘
```

### 3.3 데이터 모델 (Supabase PostgreSQL)

```sql
-- =============================================
-- 습관요정 Database Schema
-- =============================================

-- 사용자 프로필 (부모 계정)
CREATE TABLE profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id),
  email TEXT NOT NULL,
  name TEXT,
  phone TEXT,
  plan TEXT DEFAULT 'free' CHECK (plan IN ('free', 'basic', 'premium')),
  plan_expires_at TIMESTAMPTZ,
  parent_pin TEXT, -- 4자리 PIN (해시 저장)
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 아이 프로필 (부모 1명 → 아이 N명)
CREATE TABLE children (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  parent_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  birth_date DATE,
  avatar_config JSONB DEFAULT '{}', -- 꾸미기 설정
  total_stars INTEGER DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 미션 정의 (프리셋 + 커스텀)
CREATE TABLE missions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  parent_id UUID REFERENCES profiles(id) ON DELETE CASCADE, -- NULL = 프리셋
  name TEXT NOT NULL,
  description TEXT,
  icon TEXT NOT NULL DEFAULT '⭐',
  category TEXT CHECK (category IN ('morning', 'daytime', 'evening')),
  timer_seconds INTEGER DEFAULT 0,
  bgm_url TEXT,
  star_reward INTEGER DEFAULT 1 CHECK (star_reward BETWEEN 1 AND 5),
  fairy_message_start TEXT,
  fairy_message_complete TEXT,
  is_preset BOOLEAN DEFAULT FALSE,
  is_active BOOLEAN DEFAULT TRUE,
  sort_order INTEGER DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 미션 완료 기록
CREATE TABLE mission_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  child_id UUID NOT NULL REFERENCES children(id) ON DELETE CASCADE,
  mission_id UUID NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  completed_at TIMESTAMPTZ DEFAULT NOW(),
  stars_earned INTEGER NOT NULL,
  timer_used BOOLEAN DEFAULT FALSE,
  duration_seconds INTEGER, -- 실제 소요 시간
  fairy_response TEXT -- AI 요정 축하 메시지
);

-- 꾸미기 아이템 카탈로그
CREATE TABLE avatar_items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  category TEXT CHECK (category IN ('hat', 'clothes', 'wings', 'background', 'accessory')),
  image_url TEXT NOT NULL,
  star_cost INTEGER NOT NULL,
  is_premium BOOLEAN DEFAULT FALSE,
  sort_order INTEGER DEFAULT 0
);

-- 아이가 보유한 아이템
CREATE TABLE child_items (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  child_id UUID NOT NULL REFERENCES children(id) ON DELETE CASCADE,
  item_id UUID NOT NULL REFERENCES avatar_items(id) ON DELETE CASCADE,
  acquired_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(child_id, item_id)
);

-- 아이별 미션 할당 (어떤 미션을 보여줄지)
CREATE TABLE child_missions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  child_id UUID NOT NULL REFERENCES children(id) ON DELETE CASCADE,
  mission_id UUID NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
  is_active BOOLEAN DEFAULT TRUE,
  sort_order INTEGER DEFAULT 0,
  UNIQUE(child_id, mission_id)
);

-- 구독 결제 내역
CREATE TABLE subscriptions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  parent_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  plan TEXT NOT NULL CHECK (plan IN ('basic', 'premium')),
  billing_key TEXT, -- 토스페이먼츠 빌링키
  amount INTEGER NOT NULL,
  status TEXT DEFAULT 'active' CHECK (status IN ('active', 'cancelled', 'expired')),
  current_period_start TIMESTAMPTZ,
  current_period_end TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 스토리 콘텐츠 (P1)
CREATE TABLE stories (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title TEXT NOT NULL,
  episode_number INTEGER NOT NULL,
  content_url TEXT, -- 일러스트 + 텍스트 JSON
  narration_url TEXT, -- TTS 오디오 URL
  star_cost INTEGER NOT NULL DEFAULT 50,
  is_premium BOOLEAN DEFAULT FALSE,
  sort_order INTEGER DEFAULT 0
);

-- 아이가 해금한 스토리
CREATE TABLE child_stories (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  child_id UUID NOT NULL REFERENCES children(id) ON DELETE CASCADE,
  story_id UUID NOT NULL REFERENCES stories(id) ON DELETE CASCADE,
  unlocked_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(child_id, story_id)
);

-- 인덱스
CREATE INDEX idx_mission_logs_child ON mission_logs(child_id, completed_at DESC);
CREATE INDEX idx_mission_logs_date ON mission_logs(completed_at);
CREATE INDEX idx_children_parent ON children(parent_id);
CREATE INDEX idx_child_missions_child ON child_missions(child_id);

-- RLS (Row Level Security) 정책
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE children ENABLE ROW LEVEL SECURITY;
ALTER TABLE missions ENABLE ROW LEVEL SECURITY;
ALTER TABLE mission_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE child_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE subscriptions ENABLE ROW LEVEL SECURITY;

-- 부모는 자신의 데이터만 접근
CREATE POLICY "Users can view own profile"
  ON profiles FOR ALL USING (auth.uid() = id);

CREATE POLICY "Parents can manage own children"
  ON children FOR ALL USING (parent_id = auth.uid());

CREATE POLICY "Parents can view preset and own missions"
  ON missions FOR SELECT USING (is_preset = TRUE OR parent_id = auth.uid());

CREATE POLICY "Parents can manage own custom missions"
  ON missions FOR INSERT WITH CHECK (parent_id = auth.uid());

CREATE POLICY "Parents can view own children logs"
  ON mission_logs FOR ALL
  USING (child_id IN (SELECT id FROM children WHERE parent_id = auth.uid()));
```

### 3.4 API 설계

#### Supabase Edge Functions

```
/functions/
├── ai-fairy-message/     # AI 요정 메시지 생성
│   └── index.ts
├── generate-report/      # 주간 리포트 생성
│   └── index.ts
├── toss-webhook/         # 토스페이먼츠 웹훅
│   └── index.ts
├── toss-billing/         # 빌링키 발급 + 결제
│   └── index.ts
└── adjust-difficulty/    # AI 난이도 조절 (P1)
    └── index.ts
```

#### 주요 API 엔드포인트

| Method | Endpoint | 설명 | Auth |
|--------|----------|------|------|
| `POST` | `/functions/v1/ai-fairy-message` | AI 요정 메시지 생성 | ✅ |
| `POST` | `/functions/v1/generate-report` | 주간 리포트 생성 | ✅ |
| `POST` | `/functions/v1/toss-billing` | 정기결제 빌링키 발급 | ✅ |
| `POST` | `/functions/v1/toss-webhook` | 결제 웹훅 수신 | API Key |
| Supabase Client | `missions` table | 미션 CRUD | RLS |
| Supabase Client | `mission_logs` table | 미션 완료 기록 | RLS |
| Supabase Client | `children` table | 아이 프로필 CRUD | RLS |
| Supabase Client | `child_items` table | 아이템 관리 | RLS |

#### AI 요정 메시지 API 상세

```typescript
// POST /functions/v1/ai-fairy-message
// Request
{
  "child_name": "하은",
  "mission_name": "양치하기",
  "message_type": "start" | "encourage" | "complete",
  "context": {
    "streak_days": 3,        // 연속 달성일
    "total_stars": 45,       // 총 별 개수
    "completion_rate": 0.75  // 최근 7일 달성률
  }
}

// Response
{
  "message": "하은아~ 별이가 왔어! 오늘도 치카치카 할 시간이야! 반짝반짝 이를 닦으면 별이가 선물 줄게! ⭐",
  "emotion": "excited",     // 캐릭터 표정 결정용
  "tts_url": "https://..."  // 생성된 TTS 오디오 URL (캐싱)
}
```

### 3.5 프로젝트 구조 (Next.js)

```
habit-fairy/
├── app/
│   ├── layout.tsx                 # 루트 레이아웃 + PWA 메타
│   ├── page.tsx                   # 랜딩 페이지
│   ├── (auth)/
│   │   ├── login/page.tsx         # 로그인 (카카오/네이버/이메일)
│   │   └── signup/page.tsx        # 회원가입
│   ├── (child)/                   # 아이 모드 (큰 버튼, 밝은 색상)
│   │   ├── layout.tsx             # 아이 모드 레이아웃
│   │   ├── missions/page.tsx      # 오늘의 미션 목록
│   │   ├── mission/[id]/page.tsx  # 미션 수행 (타이머 + 요정)
│   │   ├── avatar/page.tsx        # 캐릭터 꾸미기
│   │   └── stars/page.tsx         # 별 모아보기
│   ├── (parent)/                  # 부모 모드 (PIN 잠금)
│   │   ├── layout.tsx             # 부모 모드 레이아웃 + PIN 가드
│   │   ├── dashboard/page.tsx     # 대시보드 (달성률 차트)
│   │   ├── missions/page.tsx      # 미션 관리 + 커스텀 추가
│   │   ├── children/page.tsx      # 아이 프로필 관리
│   │   ├── report/page.tsx        # 주간 리포트
│   │   └── settings/page.tsx      # 설정 (알림, 결제, 계정)
│   └── api/                       # Next.js API Routes (프록시)
│       └── tts/route.ts           # TTS 프록시 (CORS 해결)
├── components/
│   ├── fairy/
│   │   ├── FairyCharacter.tsx     # Lottie 요정 캐릭터
│   │   ├── FairyMessage.tsx       # 말풍선 + TTS 재생
│   │   └── FairyAnimation.tsx     # 상태별 애니메이션
│   ├── mission/
│   │   ├── MissionCard.tsx        # 미션 카드 UI
│   │   ├── MissionTimer.tsx       # 원형 타이머
│   │   ├── MissionComplete.tsx    # 완료 축하 (컨페티)
│   │   └── MissionList.tsx        # 미션 목록
│   ├── avatar/
│   │   ├── AvatarDisplay.tsx      # 캐릭터 렌더링
│   │   ├── ItemShop.tsx           # 아이템 교환소
│   │   └── AvatarEditor.tsx       # 꾸미기 에디터
│   ├── parent/
│   │   ├── PinGuard.tsx           # PIN 잠금 컴포넌트
│   │   ├── StatsChart.tsx         # 달성률 차트
│   │   ├── WeeklyReport.tsx       # 주간 리포트
│   │   └── MissionEditor.tsx      # 커스텀 미션 편집
│   └── ui/                        # 공통 UI 컴포넌트
│       ├── Button.tsx
│       ├── Card.tsx
│       ├── Modal.tsx
│       └── StarCounter.tsx
├── lib/
│   ├── supabase/
│   │   ├── client.ts              # Supabase 클라이언트
│   │   ├── server.ts              # 서버 사이드 클라이언트
│   │   └── types.ts               # DB 타입 (generated)
│   ├── ai/
│   │   └── fairy.ts               # AI 요정 메시지 호출
│   ├── tts/
│   │   └── speak.ts               # TTS 재생 유틸
│   ├── payment/
│   │   └── toss.ts                # 토스페이먼츠 SDK
│   └── utils/
│       ├── timer.ts               # 타이머 로직
│       ├── confetti.ts            # 축하 파티클
│       └── sound.ts               # 효과음 재생
├── stores/
│   ├── useChildStore.ts           # 아이 상태 관리
│   ├── useMissionStore.ts         # 미션 상태 관리
│   └── useAudioStore.ts           # 오디오 상태 관리
├── public/
│   ├── manifest.json              # PWA 매니페스트
│   ├── sw.js                      # Service Worker
│   ├── animations/                # Lottie JSON 파일
│   ├── sounds/                    # BGM + 효과음
│   └── icons/                     # 앱 아이콘
├── supabase/
│   ├── migrations/                # DB 마이그레이션
│   └── functions/                 # Edge Functions
├── next.config.js
├── tailwind.config.ts
├── tsconfig.json
└── package.json
```

---

## 4. 수익 모델

### 4.1 구독 플랜

| 플랜 | 가격 | 기능 |
|------|------|------|
| **무료** | ₩0 | 기본 미션 5개, 일일 미션 3회, 별 보상, 기본 아바타 아이템 5개 |
| **베이직** | ₩4,900/월 | 전체 미션 10개 + 커스텀 무제한, 전체 아바타 아이템, 주간 리포트, 이메일 리포트 |
| **프리미엄** | ₩9,900/월 | 베이직 전체 + AI 난이도 조절, 스토리 해금, 교구 추천, 가족 공유 (아이 3명) |

### 4.2 연간 구독 할인

| 플랜 | 월간 | 연간 (월 환산) | 할인율 |
|------|------|--------------|--------|
| 베이직 | ₩4,900 | ₩3,900 (₩46,800/년) | 20% |
| 프리미엄 | ₩9,900 | ₩7,900 (₩94,800/년) | 20% |

### 4.3 결제 플로우 (토스페이먼츠 빌링)

```
1. 부모 → 플랜 선택 → 토스페이먼츠 SDK 호출
2. 카드 정보 입력 → 빌링키 발급 (customerKey 기반)
3. 빌링키로 첫 결제 실행
4. 성공 시 → Supabase profiles.plan 업데이트
5. 매월 갱신일 → Edge Function에서 빌링키로 자동결제
6. 실패 시 → 3회 재시도 → 이메일 알림 → 다운그레이드
```

---

## 5. Day 1~21 실행 일정

### Phase 0: 사전 준비 (Day 0)
- [ ] Supabase 프로젝트 생성 + DB 스키마 적용
- [ ] Next.js 프로젝트 초기화 + Vercel 연동
- [ ] 디자인 시스템 확정 (색상, 폰트, 컴포넌트)
- [ ] Lottie 요정 캐릭터 시안 (외주 or 에셋 구매)
- [ ] Claude API 키 발급 + 프롬프트 초안

### Week 1 (Day 1~7): 코어 기능

| Day | DEV 작업 | 산출물 |
|-----|---------|--------|
| **D1** | 프로젝트 셋업, Supabase 연동, Auth (카카오 로그인) | 로그인 가능한 앱 셸 |
| **D2** | 아이 프로필 CRUD, 아이/부모 모드 전환 | 프로필 생성 플로우 |
| **D3** | 미션 목록 UI + 프리셋 10개 시드 데이터 | 미션 목록 화면 |
| **D4** | 미션 수행 화면 + 타이머 구현 | 타이머 동작 확인 |
| **D5** | AI 요정 메시지 (Claude API + Edge Function) | 요정 대화 동작 |
| **D6** | 별 보상 시스템 + 미션 완료 플로우 | 미션→별 적립 완성 |
| **D7** | 버그 수정 + 아이 모드 UX 점검 | Week 1 빌드 |

### Week 2 (Day 8~14): 부모 기능 + 꾸미기

| Day | DEV 작업 | 산출물 |
|-----|---------|--------|
| **D8** | 부모 대시보드 UI (달성률 차트) | 대시보드 화면 |
| **D9** | 주간 리포트 생성 로직 | 리포트 뷰 |
| **D10** | 부모 커스텀 미션 추가/편집 | 미션 편집 화면 |
| **D11** | 아바타 꾸미기 (아이템 교환소 + 에디터) | 꾸미기 화면 |
| **D12** | TTS 연동 (Google Cloud TTS) + 효과음 | 음성 재생 |
| **D13** | PIN 잠금 + 부모/아이 모드 전환 UX | 모드 전환 |
| **D14** | 통합 테스트 + 버그 수정 | Week 2 빌드 |

### Week 3 (Day 15~21): 결제 + PWA + 런칭

| Day | DEV 작업 | 산출물 |
|-----|---------|--------|
| **D15** | 토스페이먼츠 빌링 연동 (빌링키 발급) | 결제 플로우 |
| **D16** | 구독 관리 (플랜 변경, 해지) | 구독 화면 |
| **D17** | PWA 설정 (manifest, SW, 오프라인) | 홈화면 추가 가능 |
| **D18** | 랜딩 페이지 + 온보딩 플로우 | 첫 방문 경험 |
| **D19** | Sentry 에러 모니터링 + Analytics 설치 | 모니터링 |
| **D20** | QA (5세 아이 실제 테스트 1~2명) + 수정 | 사용성 검증 |
| **D21** | 🚀 **소프트 런칭** (베타, 지인 50명) | MVP 배포 |

---

## 6. 비용 산출 + BEP

### 6.1 월간 고정 비용 (MVP 운영)

| 항목 | 비용/월 | 비고 |
|------|---------|------|
| Supabase Pro | $25 (~₩34,000) | 500MB DB, 250MB Storage, 100K Auth |
| Vercel Pro | $20 (~₩27,000) | 100GB Bandwidth, Analytics |
| Claude API | ~₩100,000 | Sonnet 3.5, 예상 10K req/월 × $0.01 |
| Google Cloud TTS | ~₩50,000 | WaveNet, 예상 50K chars/월 |
| 도메인 + SSL | ₩2,000 | habitfairy.kr |
| Sentry | $0 (Free) | 5K errors/월 |
| **합계** | **~₩213,000/월** | |

### 6.2 초기 1회성 비용

| 항목 | 비용 | 비고 |
|------|------|------|
| Lottie 요정 캐릭터 제작 | ₩500,000 | 외주 or 에셋 구매 |
| BGM/효과음 라이센스 | ₩100,000 | 로열티프리 패키지 |
| 아바타 아이템 일러스트 | ₩300,000 | 30개 아이템 |
| 토스페이먼츠 심사 | ₩0 | 무료 |
| **합계** | **~₩900,000** | |

### 6.3 총 3개월 비용 (런칭까지)

```
초기 비용:     ₩900,000
운영 3개월:    ₩213,000 × 3 = ₩639,000
인건비 제외
──────────────────────
총 비용:       ₩1,539,000 (~₩150만)
```

### 6.4 BEP (손익분기점) 분석

**가정:**
- ARPU (월 평균 매출/유저): ₩3,500 (무료 70% + 베이직 20% + 프리미엄 10%)
- 월 고정비: ₩213,000
- 변동비 (AI/TTS per user): ~₩200/월

```
BEP 유저 수 = 고정비 / (ARPU - 변동비)
            = ₩213,000 / (₩3,500 - ₩200)
            = 65명 유료 구독자

전환율 10% 가정 시 → MAU 650명에서 BEP 달성
```

**월별 목표:**
| 월 | MAU | 유료 전환 | MRR | 순이익 |
|----|-----|----------|-----|--------|
| M1 (베타) | 50 | 5 | ₩24,500 | -₩188,500 |
| M2 | 200 | 20 | ₩98,000 | -₩115,000 |
| M3 | 500 | 50 | ₩245,000 | +₩32,000 |
| M6 | 2,000 | 200 | ₩980,000 | +₩767,000 |
| M12 | 10,000 | 1,000 | ₩4,900,000 | +₩4,687,000 |

---

## 7. KPI

### 7.1 North Star Metric
> **주간 미션 완료 횟수 (Weekly Active Missions Completed)**

### 7.2 핵심 지표

| 카테고리 | KPI | 목표 (M3) | 목표 (M6) |
|----------|-----|----------|----------|
| **획득** | MAU (Monthly Active Users) | 500 | 2,000 |
| **활성화** | 회원가입 → 첫 미션 완료율 | 60% | 70% |
| **유지** | D7 리텐션 | 40% | 50% |
| **유지** | D30 리텐션 | 20% | 30% |
| **수익** | 무료→유료 전환율 | 8% | 12% |
| **수익** | MRR (Monthly Recurring Revenue) | ₩245K | ₩980K |
| **수익** | Churn Rate (월간 이탈률) | <10% | <8% |
| **인게이지먼트** | 일평균 미션 완료 수/아이 | 2.5 | 3.5 |
| **인게이지먼트** | 주간 활성일 수/아이 | 4일 | 5일 |
| **NPS** | Net Promoter Score | 30+ | 50+ |

### 7.3 추적 도구
- **Vercel Analytics** — 페이지뷰, 성능
- **Supabase** — DB 쿼리 기반 커스텀 대시보드
- **Sentry** — 에러율, 성능 병목
- **자체 대시보드** — Supabase 뷰 + Recharts 내부 어드민

---

## 8. 리스크 + 법률 체크리스트

### 8.1 리스크 매트릭스

| # | 리스크 | 확률 | 영향 | 대응 |
|---|--------|------|------|------|
| R1 | 아이가 1~2주 후 흥미 잃음 | 높음 | 높음 | AI 기반 변화 주기 (새 미션, 랜덤 보상), 스토리 해금으로 장기 동기부여 |
| R2 | 부모가 설정/관리 번거로워 이탈 | 중간 | 높음 | 온보딩 최소화 (3탭 완료), 기본 미션 자동 활성화 |
| R3 | AI 요정이 부적절한 발언 | 낮음 | 매우 높음 | Claude system prompt 엄격 제한 + 출력 필터링 + 사전 검열 로직 |
| R4 | 아이 개인정보 유출 | 낮음 | 매우 높음 | 최소 수집 원칙, 아이 이름만 저장, 이미지/음성 비저장 |
| R5 | 앱스토어 정책 변경 (PWA 제한) | 낮음 | 중간 | React Native 래핑 백업 플랜 보유 |
| R6 | 경쟁사 (대기업) 유사 서비스 출시 | 중간 | 중간 | AI 개인화 + 커뮤니티 락인으로 차별화 |
| R7 | TTS/AI API 비용 급증 | 중간 | 중간 | 메시지 캐싱, 프리셋 응답 비율 80% 유지 |

### 8.2 법률 체크리스트 (아동 서비스 필수)

#### ✅ 개인정보보호법 (한국)
- [ ] **만 14세 미만 아동** → 법정대리인(부모) 동의 필수 (제22조)
- [ ] 법정대리인 동의 확인 방법 구현 (공동인증서, 아이핀, 휴대폰 본인확인 중 택1)
- [ ] 개인정보 처리방침 작성 및 공개
- [ ] 수집 항목 최소화: 부모 이메일/전화, 아이 이름/생년월일만 수집
- [ ] 아이 프로필 사진/음성 데이터 수집 금지

#### ✅ 아동·청소년 개인정보보호 가이드라인 (개인정보보호위원회)
- [ ] 아동 대상 서비스임을 명시
- [ ] 부모 동의 없이 아동 정보 제3자 제공 금지
- [ ] 행태정보 기반 광고 금지
- [ ] 아동 정보 파기 요청 시 즉시 처리

#### ✅ 전자상거래법
- [ ] 구독 결제 시 청약철회 14일 보장
- [ ] 자동갱신 전 사전 고지 (결제 3일 전 이메일/푸시)
- [ ] 해지 절차를 가입 절차보다 어렵게 하지 않을 것

#### ✅ 통신판매업 신고
- [ ] 유료 구독 서비스 → 통신판매업 신고 필수
- [ ] 사업자등록 + 통신판매업 신고번호 표기

#### ✅ AI 관련
- [ ] AI 생성 콘텐츠임을 부모에게 고지
- [ ] AI 대화 로그 30일 보관 후 자동 삭제
- [ ] AI 프롬프트에 아동 안전 가드레일 포함
- [ ] 아이에게 AI와 채팅 자유입력 금지 (선택지 기반 인터랙션만)

#### ✅ 앱 심사 관련 (추후 앱스토어 래핑 시)
- [ ] Apple COPPA 규정 준수
- [ ] Google Family Policy 준수
- [ ] Kids Category 등록 시 제3자 추적 SDK 금지

### 8.3 보험/인증 (Phase 2)

- [ ] 정보보호관리체계(ISMS) 인증 검토 (MAU 10만 초과 시)
- [ ] 개인정보 영향평가 실시 (5만건 이상 개인정보 처리 시)

---

## 9. DEV 구현 기술 스펙

> 이 섹션은 DEV가 즉시 구현에 착수할 수 있도록 상세 기술 명세를 포함합니다.

### 9.1 환경 설정

#### package.json 핵심 의존성

```json
{
  "dependencies": {
    "next": "^14.2.0",
    "@supabase/supabase-js": "^2.45.0",
    "@supabase/ssr": "^0.5.0",
    "zustand": "^4.5.0",
    "framer-motion": "^11.0.0",
    "lottie-react": "^2.4.0",
    "recharts": "^2.12.0",
    "canvas-confetti": "^1.9.0",
    "@tosspayments/payment-sdk": "^2.3.0",
    "howler": "^2.2.4",
    "date-fns": "^3.6.0",
    "next-pwa": "^5.6.0"
  },
  "devDependencies": {
    "typescript": "^5.4.0",
    "tailwindcss": "^3.4.0",
    "@types/canvas-confetti": "^1.6.0",
    "supabase": "^1.200.0"
  }
}
```

#### 환경 변수 (.env.local)

```env
# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
SUPABASE_SERVICE_ROLE_KEY=eyJ...

# AI
ANTHROPIC_API_KEY=sk-ant-...

# TTS
GOOGLE_CLOUD_TTS_API_KEY=AIza...

# Payment
TOSS_CLIENT_KEY=test_ck_...
TOSS_SECRET_KEY=test_sk_...

# App
NEXT_PUBLIC_APP_URL=https://habitfairy.kr
```

### 9.2 핵심 컴포넌트 구현 가이드

#### AI 요정 메시지 Edge Function

```typescript
// supabase/functions/ai-fairy-message/index.ts
import { serve } from 'https://deno.land/std@0.177.0/http/server.ts'
import Anthropic from '@anthropic-ai/sdk'

const anthropic = new Anthropic({
  apiKey: Deno.env.get('ANTHROPIC_API_KEY')!,
})

const FAIRY_SYSTEM_PROMPT = `너는 '별이'라는 이름의 아이 생활습관 요정이야.

규칙:
1. 항상 밝고 귀엽고 다정하게 말해
2. 아이 이름을 꼭 불러줘
3. 3문장 이내로 짧게 말해
4. 절대로 무섭거나 슬프거나 폭력적인 말 하지 마
5. 구체적으로 칭찬해줘 (예: "이를 정말 깨끗하게 닦았구나!")
6. 이모지를 1~2개 사용해
7. 절대로 개인정보를 물어보지 마
8. 교육적이지만 설교하지 마`

serve(async (req) => {
  const { child_name, mission_name, message_type, context } = await req.json()

  const userPrompt = buildPrompt(child_name, mission_name, message_type, context)

  const response = await anthropic.messages.create({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 150,
    system: FAIRY_SYSTEM_PROMPT,
    messages: [{ role: 'user', content: userPrompt }],
  })

  const message = response.content[0].type === 'text'
    ? response.content[0].text
    : ''

  // 안전 필터링
  const sanitized = sanitizeForChild(message)

  return new Response(JSON.stringify({
    message: sanitized,
    emotion: detectEmotion(message_type),
  }), {
    headers: { 'Content-Type': 'application/json' },
  })
})

function buildPrompt(name: string, mission: string, type: string, ctx: any): string {
  switch (type) {
    case 'start':
      return `${name}(이/가) "${mission}" 미션을 시작하려고 해. 신나게 응원해줘!`
    case 'encourage':
      return `${name}(이/가) "${mission}" 미션을 하는 중이야. 힘내라고 격려해줘!`
    case 'complete':
      return `${name}(이/가) "${mission}" 미션을 완료했어! ${ctx.streak_days}일 연속 성공이야. 축하해줘!`
    default:
      return `${name}에게 인사해줘.`
  }
}

function sanitizeForChild(text: string): string {
  const forbidden = ['죽', '피', '무서', '바보', '싫어', '못생']
  let safe = text
  for (const word of forbidden) {
    if (safe.includes(word)) {
      safe = safe.replace(new RegExp(word, 'g'), '***')
    }
  }
  return safe
}

function detectEmotion(type: string): string {
  switch (type) {
    case 'start': return 'excited'
    case 'encourage': return 'cheering'
    case 'complete': return 'celebrating'
    default: return 'happy'
  }
}
```

#### 미션 타이머 컴포넌트

```typescript
// components/mission/MissionTimer.tsx
'use client'

import { useState, useEffect, useCallback, useRef } from 'react'
import { motion } from 'framer-motion'

interface MissionTimerProps {
  totalSeconds: number
  onComplete: () => void
  onTick?: (remaining: number) => void
}

export function MissionTimer({ totalSeconds, onComplete, onTick }: MissionTimerProps) {
  const [remaining, setRemaining] = useState(totalSeconds)
  const [isRunning, setIsRunning] = useState(false)
  const startTimeRef = useRef<number>(0)
  const expectedEndRef = useRef<number>(0)

  useEffect(() => {
    if (!isRunning) return

    const interval = setInterval(() => {
      const now = Date.now()
      const elapsed = Math.floor((now - startTimeRef.current) / 1000)
      const newRemaining = Math.max(0, totalSeconds - elapsed)

      setRemaining(newRemaining)
      onTick?.(newRemaining)

      if (newRemaining <= 0) {
        clearInterval(interval)
        setIsRunning(false)
        onComplete()
      }
    }, 100) // 100ms 간격으로 정확도 높임

    // 백그라운드 전환 대응
    const handleVisibility = () => {
      if (document.visibilityState === 'visible') {
        const now = Date.now()
        const elapsed = Math.floor((now - startTimeRef.current) / 1000)
        setRemaining(Math.max(0, totalSeconds - elapsed))
      }
    }
    document.addEventListener('visibilitychange', handleVisibility)

    return () => {
      clearInterval(interval)
      document.removeEventListener('visibilitychange', handleVisibility)
    }
  }, [isRunning, totalSeconds, onComplete, onTick])

  const start = useCallback(() => {
    startTimeRef.current = Date.now()
    expectedEndRef.current = Date.now() + totalSeconds * 1000
    setIsRunning(true)
  }, [totalSeconds])

  const progress = (totalSeconds - remaining) / totalSeconds
  const minutes = Math.floor(remaining / 60)
  const seconds = remaining % 60

  const circumference = 2 * Math.PI * 45 // r=45

  return (
    <div className="flex flex-col items-center gap-4">
      <div className="relative w-40 h-40">
        <svg className="w-full h-full -rotate-90" viewBox="0 0 100 100">
          {/* 배경 원 */}
          <circle cx="50" cy="50" r="45" fill="none"
            stroke="#E5E7EB" strokeWidth="8" />
          {/* 프로그레스 */}
          <motion.circle cx="50" cy="50" r="45" fill="none"
            stroke="#FBBF24" strokeWidth="8" strokeLinecap="round"
            strokeDasharray={circumference}
            strokeDashoffset={circumference * (1 - progress)}
            transition={{ duration: 0.1 }} />
        </svg>
        {/* 시간 표시 */}
        <div className="absolute inset-0 flex items-center justify-center">
          <span className="text-3xl font-bold text-gray-800">
            {minutes}:{seconds.toString().padStart(2, '0')}
          </span>
        </div>
      </div>

      {!isRunning ? (
        <button onClick={start}
          className="px-8 py-4 bg-yellow-400 rounded-full text-xl font-bold
                     text-white shadow-lg active:scale-95 transition">
          시작! 🌟
        </button>
      ) : (
        <p className="text-lg text-gray-500 animate-pulse">
          잘하고 있어! 조금만 더~
        </p>
      )}
    </div>
  )
}
```

#### Zustand 스토어 (아이 상태)

```typescript
// stores/useChildStore.ts
import { create } from 'zustand'
import { createClient } from '@/lib/supabase/client'

interface Child {
  id: string
  name: string
  birth_date: string | null
  avatar_config: Record<string, string>
  total_stars: number
}

interface ChildState {
  currentChild: Child | null
  children: Child[]
  isLoading: boolean

  // Actions
  fetchChildren: (parentId: string) => Promise<void>
  setCurrentChild: (child: Child) => void
  addStars: (childId: string, stars: number) => Promise<void>
  updateAvatar: (childId: string, config: Record<string, string>) => Promise<void>
}

export const useChildStore = create<ChildState>((set, get) => ({
  currentChild: null,
  children: [],
  isLoading: false,

  fetchChildren: async (parentId) => {
    set({ isLoading: true })
    const supabase = createClient()
    const { data, error } = await supabase
      .from('children')
      .select('*')
      .eq('parent_id', parentId)
      .order('created_at')

    if (!error && data) {
      set({ children: data, currentChild: data[0] || null })
    }
    set({ isLoading: false })
  },

  setCurrentChild: (child) => set({ currentChild: child }),

  addStars: async (childId, stars) => {
    const supabase = createClient()
    const { data } = await supabase.rpc('add_stars', {
      p_child_id: childId,
      p_stars: stars,
    })

    // 로컬 상태 업데이트
    const current = get().currentChild
    if (current?.id === childId) {
      set({ currentChild: { ...current, total_stars: current.total_stars + stars } })
    }
  },

  updateAvatar: async (childId, config) => {
    const supabase = createClient()
    await supabase
      .from('children')
      .update({ avatar_config: config })
      .eq('id', childId)

    const current = get().currentChild
    if (current?.id === childId) {
      set({ currentChild: { ...current, avatar_config: config } })
    }
  },
}))
```

#### 토스페이먼츠 결제 연동

```typescript
// lib/payment/toss.ts
import { loadPaymentWidget, ANONYMOUS } from '@tosspayments/payment-widget-sdk'

const CLIENT_KEY = process.env.NEXT_PUBLIC_TOSS_CLIENT_KEY!

export async function initPaymentWidget(customerKey: string) {
  const paymentWidget = await loadPaymentWidget(CLIENT_KEY, customerKey)
  return paymentWidget
}

export async function requestBillingAuth(
  paymentWidget: any,
  plan: 'basic' | 'premium'
) {
  const amount = plan === 'basic' ? 4900 : 9900
  const orderName = plan === 'basic' ? '습관요정 베이직' : '습관요정 프리미엄'

  await paymentWidget.requestPayment({
    orderId: `habit-fairy-${plan}-${Date.now()}`,
    orderName,
    amount,
    successUrl: `${window.location.origin}/payment/success`,
    failUrl: `${window.location.origin}/payment/fail`,
  })
}
```

```typescript
// supabase/functions/toss-billing/index.ts
// 빌링키 발급 + 자동결제 처리
import { serve } from 'https://deno.land/std@0.177.0/http/server.ts'
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

const TOSS_SECRET_KEY = Deno.env.get('TOSS_SECRET_KEY')!
const TOSS_API_URL = 'https://api.tosspayments.com/v1/billing'

serve(async (req) => {
  const { authKey, customerKey, parentId, plan } = await req.json()

  // 1. 빌링키 발급
  const billingRes = await fetch(`${TOSS_API_URL}/authorizations/issue`, {
    method: 'POST',
    headers: {
      Authorization: `Basic ${btoa(`${TOSS_SECRET_KEY}:`)}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ authKey, customerKey }),
  })
  const billing = await billingRes.json()

  if (!billingRes.ok) {
    return new Response(JSON.stringify({ error: billing }), { status: 400 })
  }

  // 2. 첫 결제 실행
  const amount = plan === 'basic' ? 4900 : 9900
  const paymentRes = await fetch(TOSS_API_URL, {
    method: 'POST',
    headers: {
      Authorization: `Basic ${btoa(`${TOSS_SECRET_KEY}:`)}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      billingKey: billing.billingKey,
      customerKey,
      amount,
      orderId: `habit-fairy-${plan}-${Date.now()}`,
      orderName: plan === 'basic' ? '습관요정 베이직' : '습관요정 프리미엄',
    }),
  })

  if (paymentRes.ok) {
    // 3. DB 업데이트
    const supabase = createClient(
      Deno.env.get('SUPABASE_URL')!,
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
    )

    const now = new Date()
    const nextMonth = new Date(now)
    nextMonth.setMonth(nextMonth.getMonth() + 1)

    await supabase.from('subscriptions').upsert({
      parent_id: parentId,
      plan,
      billing_key: billing.billingKey,
      amount,
      status: 'active',
      current_period_start: now.toISOString(),
      current_period_end: nextMonth.toISOString(),
    })

    await supabase.from('profiles').update({
      plan,
      plan_expires_at: nextMonth.toISOString(),
    }).eq('id', parentId)
  }

  return new Response(JSON.stringify({ success: true }), {
    headers: { 'Content-Type': 'application/json' },
  })
})
```

### 9.3 PWA 설정

```json
// public/manifest.json
{
  "name": "습관요정 - HabitFairy",
  "short_name": "습관요정",
  "description": "AI 요정과 함께하는 아이 생활습관 게임",
  "start_url": "/",
  "display": "standalone",
  "orientation": "portrait",
  "background_color": "#FFF7ED",
  "theme_color": "#F59E0B",
  "icons": [
    { "src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "/icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable" }
  ],
  "categories": ["education", "kids"],
  "lang": "ko",
  "dir": "ltr"
}
```

### 9.4 디자인 시스템

```typescript
// tailwind.config.ts (핵심 값)
const config = {
  theme: {
    extend: {
      colors: {
        fairy: {
          50: '#FFFBEB',   // 배경
          100: '#FEF3C7',  // 카드 배경
          200: '#FDE68A',  // 액센트 라이트
          400: '#FBBF24',  // 별/보상 (Primary)
          500: '#F59E0B',  // CTA 버튼
          600: '#D97706',  // CTA hover
          700: '#B45309',  // 텍스트 강조
        },
        child: {
          blue: '#60A5FA',   // 아이 모드 포인트
          pink: '#F472B6',   // 여아 테마
          green: '#34D399',  // 완료/성공
          purple: '#A78BFA', // 요정 색상
        },
      },
      fontFamily: {
        heading: ['Pretendard', 'sans-serif'],
        body: ['Pretendard', 'sans-serif'],
      },
      borderRadius: {
        'child': '1.5rem', // 아이 모드: 큰 라운드
      },
    },
  },
}
```

### 9.5 테스트 전략

| 구분 | 도구 | 범위 |
|------|------|------|
| Unit | Vitest | Zustand 스토어, 유틸 함수, 타이머 로직 |
| Component | React Testing Library | 미션 카드, 타이머, 요정 메시지 |
| E2E | Playwright | 미션 완료 플로우, 결제 플로우 |
| AI 안전성 | 수동 테스트 | 100개 시나리오 프롬프트 테스트 |
| 사용성 | 실제 아이 테스트 | 5세 아이 2~3명, 부모 관찰 기록 |

### 9.6 배포 파이프라인

```
main branch → Vercel Auto Deploy (Production)
develop branch → Vercel Preview Deploy (Staging)

GitHub Actions:
  - PR → Lint + Type Check + Unit Test
  - Merge to develop → Staging 배포 + E2E 테스트
  - Merge to main → Production 배포
```

---

## 부록: 미션 프리셋 시드 데이터

```json
[
  {
    "name": "양치하기",
    "description": "치카치카! 위아래 골고루 닦아요",
    "icon": "🪥",
    "category": "morning",
    "timer_seconds": 180,
    "star_reward": 2,
    "fairy_message_start": "이를 반짝반짝 닦을 시간이야!",
    "fairy_message_complete": "와~ 이가 정말 깨끗해졌다!"
  },
  {
    "name": "세수하기",
    "description": "물로 세수하고 깨끗한 얼굴!",
    "icon": "🧼",
    "category": "morning",
    "timer_seconds": 60,
    "star_reward": 1,
    "fairy_message_start": "얼굴을 깨끗하게 씻어볼까?",
    "fairy_message_complete": "깨끗한 얼굴! 정말 예쁘다!"
  },
  {
    "name": "손 씻기",
    "description": "비누로 거품 내서 깨끗하게!",
    "icon": "🫧",
    "category": "daytime",
    "timer_seconds": 30,
    "star_reward": 1,
    "fairy_message_start": "손에 있는 세균을 물리치자!",
    "fairy_message_complete": "세균이 모두 도망갔어!"
  },
  {
    "name": "옷 입기",
    "description": "오늘의 옷을 스스로 입어요",
    "icon": "👕",
    "category": "morning",
    "timer_seconds": 300,
    "star_reward": 2,
    "fairy_message_start": "멋진 옷을 스스로 입어볼까?",
    "fairy_message_complete": "혼자 옷을 입다니 정말 대단해!"
  },
  {
    "name": "신발 신기",
    "description": "왼쪽 오른쪽 잘 맞춰서!",
    "icon": "👟",
    "category": "morning",
    "timer_seconds": 120,
    "star_reward": 1,
    "fairy_message_start": "신발을 척척 신어볼까?",
    "fairy_message_complete": "왼쪽 오른쪽 완벽하게 신었네!"
  },
  {
    "name": "인사하기",
    "description": "안녕하세요! 밝게 인사해요",
    "icon": "👋",
    "category": "morning",
    "timer_seconds": 0,
    "star_reward": 1,
    "fairy_message_start": "오늘 만나는 사람에게 인사해볼까?",
    "fairy_message_complete": "밝은 인사 너무 멋져!"
  },
  {
    "name": "밥 먹기",
    "description": "골고루 냠냠 맛있게 먹어요",
    "icon": "🍚",
    "category": "daytime",
    "timer_seconds": 0,
    "star_reward": 3,
    "fairy_message_start": "맛있는 밥을 골고루 먹어볼까?",
    "fairy_message_complete": "골고루 다 먹었구나! 정말 잘했어!"
  },
  {
    "name": "장난감 정리",
    "description": "놀고 난 장난감을 제자리에!",
    "icon": "🧸",
    "category": "daytime",
    "timer_seconds": 300,
    "star_reward": 2,
    "fairy_message_start": "장난감들이 집에 가고 싶대!",
    "fairy_message_complete": "와~ 방이 정말 깨끗해졌다!"
  },
  {
    "name": "책 읽기",
    "description": "그림책 한 권을 읽어요",
    "icon": "📚",
    "category": "daytime",
    "timer_seconds": 600,
    "star_reward": 3,
    "fairy_message_start": "오늘은 어떤 이야기를 읽어볼까?",
    "fairy_message_complete": "책 한 권을 다 읽다니 대단해!"
  },
  {
    "name": "잠자리 준비",
    "description": "이 닦고 파자마 입고 잘 준비!",
    "icon": "🌙",
    "category": "evening",
    "timer_seconds": 0,
    "star_reward": 2,
    "fairy_message_start": "오늘 하루 수고했어! 잘 준비해볼까?",
    "fairy_message_complete": "내일도 별이가 기다리고 있을게. 잘 자!"
  }
]
```

---

## 변경 이력

| 버전 | 날짜 | 작성자 | 내용 |
|------|------|--------|------|
| v1.0 | 2026-02-07 | PO Agent | 초안 작성 |

---

> **다음 단계:** CEO 승인 후 DEV에게 전달 → Day 1 착수
