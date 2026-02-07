# PRD: AI 성장 트래커 (AI Growth Tracker)

> **문서 버전:** v1.0  
> **작성일:** 2026-02-07  
> **작성자:** PO Agent  
> **상태:** Draft → CEO 리뷰 대기  
> **코드네임:** `GrowthLens`

---

## 목차
1. [프로덕트 정의](#1-프로덕트-정의)
2. [MVP 기능 정의 (P0/P1/P2)](#2-mvp-기능-정의)
3. [인풋/아웃풋 상세 설계](#3-인풋아웃풋-상세-설계)
4. [기술 스택](#4-기술-스택)
5. [데이터 모델](#5-데이터-모델)
6. [AI 엔진 설계](#6-ai-엔진-설계)
7. [수익 모델 상세](#7-수익-모델-상세)
8. [Day 1~30 실행 일정](#8-day-130-실행-일정)
9. [비용 산출 + BEP](#9-비용-산출--bep)
10. [KPI](#10-kpi)
11. [리스크 + 법률](#11-리스크--법률)
12. [확장 로드맵](#12-확장-로드맵)

---

## 1. 프로덕트 정의

### 1.1 비전

> **"매일 2분의 기록으로, 우리 아이 발달의 큰 그림을 그리다."**

부모의 일상 관찰 데이터를 AI가 수집·분석하여, 전문 검사(K-WISC-V) 수준의 인지 발달 인사이트를 제공하는 **세계 최초의 일상 기반 아동 발달 추적 플랫폼**.

### 1.2 핵심 가치 제안

| 기존 방식 | GrowthLens |
|---|---|
| K-WISC 검사 1회 30~50만원 | 월 ₩9,900~₩19,900 상시 추적 |
| 검사 결과 스냅샷 (한 시점) | 연속 데이터 기반 트렌드 분석 |
| 전문 용어 해석 필요 | 엄마 언어로 인사이트 전달 |
| ChatGPT에 수동 기록 (1년간) | 자동 구조화 + 분석 + 추천 |
| 부모 주관 편향 | AI 객관적 데이터 교차 검증 |

### 1.3 타겟 페르소나

#### 1차 타겟: "동탄 은지맘" (주양육자)

| 항목 | 상세 |
|---|---|
| **인구통계** | 32~38세 여성, 수도권/신도시 거주 |
| **자녀** | 4~6세 1~2명 |
| **소득** | 가구 연소득 6,000만~1억원 |
| **행동** | 맘카페 활동, 교구 구매에 월 10~30만원 지출 |
| **Pain** | "우리 아이 잘 크고 있는지 불안", 전문가 상담 접근성 낮음 |
| **Gain** | 객관적 데이터로 불안 해소, 맞춤 활동 추천으로 시간 절약 |
| **디지털** | 카카오톡/네이버/인스타 헤비유저, 토스 일상 결제 |

#### 2차 타겟: "영재 관심 아빠"
- 아이 발달에 적극적 관심, WISC 검사 경험 있음
- 데이터/수치에 민감, 상세 리포트 선호

### 1.4 시장 규모 (TAM/SAM/SOM)

```
TAM: 대한민국 0~6세 아동 가구 ≈ 180만 가구 (2024 출생아 23.8만명 × 7년치)
     × 육아앱 지출 의향 가구 60% = 108만 가구
     × 연 ₩120,000(베이직 기준) = ₩1,296억/년

SAM: 4~6세 집중 (3개년) ≈ 77만 가구
     × 관심 가구 40% = 30.8만 가구
     × 연 ₩120,000 = ₩370억/년

SOM (Year 1): 동탄/수도권 집중, 1% 침투
     = 3,080 유료 가구 × ₩120,000 = ₩3.7억/년
```

### 1.5 경쟁사 분석

| 서비스 | 카테고리 | 강점 | 약점 | 우리 차별화 |
|---|---|---|---|---|
| **Kinedu** (글로벌) | 발달 마일스톤 추적 | 전문가 기반 활동 추천, 1M+ 다운로드 | 한국 미진출, 영미권 기준, AI 분석 없음 | 한국 발달 기준 + AI 예측 |
| **챗GPT 수동기록** (현재 CEO 방식) | 범용 AI | 유연한 질의응답 | 구조화 안 됨, 연속 분석 불가 | 구조화 + 자동 트렌드 |
| **아이의 발견** (국내) | 놀이 추천 | 연령별 놀이 컨텐츠 | 기록·추적 없음 | 데이터 기반 개인화 |
| **GrowCoach/습관요정** (자사) | 습관/성장 | 기존 사용자 base | 인지발달 특화 아님 | 상위 플랫폼으로 통합 |
| **소아과 발달검사** | 오프라인 | 전문가 신뢰도 | 비용(30~50만), 1회성 | 상시 추적 + 저비용 |

### 1.6 핵심 차별화 = 해자(Moat)

1. **데이터 네트워크 효과**: 기록이 쌓일수록 분석 정확도 ↑ → 이탈 비용 ↑
2. **한국형 발달 기준**: K-WISC-V 5개 기본지표 매핑 (언어이해/시공간/유동추론/작업기억/처리속도)
3. **엄마 언어 UX**: 전문 용어 → 직관적 표현 자동 변환
4. **커머스 통합**: 분석 → 교구 추천 → 즉시 구매 (쿠팡/네이버)

---

## 2. MVP 기능 정의

### 2.1 우선순위 매트릭스

#### P0 — MVP Day 1 (필수 출시)

| ID | 기능 | 설명 | 사용자 가치 |
|---|---|---|---|
| F-001 | **초기 프로필 설정** | 아이 나이/성별 + 기질 질문 5개 + 관심 영역 | 베이스라인 추정 |
| F-002 | **일일 활동 기록** | 텍스트 + 사진 기반 활동 로그 (퍼즐/독서/놀이/질문) | 핵심 인풋 |
| F-003 | **일간 인사이트** | 당일 기록 기반 한줄 피드백 | 즉각 가치 전달 |
| F-004 | **주간 리포트** | 5개 영역 레이더 차트 + 변화 추이 | 핵심 아웃풋 |
| F-005 | **회원가입/인증** | 카카오 소셜 로그인 + 법정대리인 동의 | 진입 |
| F-006 | **아이 프로필 관리** | 다자녀 지원, 닉네임 사용 | 기본 |
| F-007 | **구독 결제** | 무료/베이직/프리미엄 3단계 | 수익화 |

#### P1 — MVP+2주 (빠른 후속)

| ID | 기능 | 설명 |
|---|---|---|
| F-101 | **사진 AI 분석** | 퍼즐/그림/글씨 사진 → 난이도·완성도 자동 인식 |
| F-102 | **발달 밴드 예측** | "상위 20~30% 구간" 표시 (IQ 점수 ❌) |
| F-103 | **교구 추천** | AI 분석 → 맞춤 교구 추천 + 구매 링크 |
| F-104 | **알림/리마인더** | 매일 기록 유도 푸시 (19~21시) |
| F-105 | **독서 기록 특화** | 책 제목 자동완성 + 읽기 수준 추적 |

#### P2 — Month 2~3 (확장)

| ID | 기능 | 설명 |
|---|---|---|
| F-201 | **영상 분석** | 놀이 영상 → 대근육/소근육/사회성 분석 |
| F-202 | **양육 피드백** | 감정/훈육 메모 기반 양육 조언 |
| F-203 | **월간 심화 리포트** | 월별 종합 분석 + AI 추가 질문 |
| F-204 | **WISC 결과 업로드** | 기존 검사 결과 연동 → 예측 보정 |
| F-205 | **커뮤니티 벤치마크** | 익명화된 동연령 비교 (선택적) |
| F-206 | **토스 미니앱 버전** | 앱인토스 생태계 입점 |

### 2.2 MVP 유저 플로우

```
[카카오 로그인] → [아이 프로필 생성 (5분)]
    ↓
[홈 대시보드] → [오늘 기록하기] → [활동 선택] → [상세 입력] → [일간 인사이트]
    ↓                                                              ↓
[주간 리포트 열람] ← ← ← ← ← ← ← ← ← ← ← ← [7일 데이터 축적]
    ↓
[교구 추천 확인] → [구매 링크 클릭]
```

---

## 3. 인풋/아웃풋 상세 설계

### 3.1 인풋 상세

#### Stage 1: 초기 프로필 (가입 시 5분)

```yaml
onboarding_profile:
  child_info:
    birth_year_month: "2021-03"        # 만 나이 자동 계산
    gender: "male" | "female"
    nickname: "별이"                     # 실명 대신 닉네임

  temperament_questions:                 # 전문 용어 ❌, 엄마 말로
    Q1_new_environment:
      question: "새로운 환경에서 우리 아이는?"
      options:
        - { label: "쭈뼛거려요", value: "inhibited", tag: "기질-억제" }
        - { label: "금세 적응해요", value: "adaptive", tag: "기질-적응" }
        - { label: "바로 뛰어들어요", value: "bold", tag: "기질-대담" }

    Q2_faster_than_peers:
      question: "또래보다 빠르다고 느끼는 건?"
      options:                           # 복수 선택 가능
        - { label: "말하기", value: "verbal", maps_to: "언어이해" }
        - { label: "모양 구분", value: "visual_spatial", maps_to: "시공간" }
        - { label: "몸 움직임", value: "motor", maps_to: "처리속도" }
        - { label: "기억력", value: "memory", maps_to: "작업기억" }
        - { label: "모방/흉내", value: "imitation", maps_to: "유동추론" }

    Q3_slower_than_peers:
      question: "또래보다 느리다고 느끼는 건?"
      options: # Q2와 동일 선택지

    Q4_current_obsession:
      question: "요즘 아이가 빠져있는 건?"
      options:
        - { label: "퍼즐", value: "puzzle", maps_to: ["시공간", "유동추론"] }
        - { label: "블록", value: "blocks", maps_to: ["시공간", "처리속도"] }
        - { label: "그림", value: "drawing", maps_to: ["시공간", "소근육"] }
        - { label: "책", value: "books", maps_to: ["언어이해"] }
        - { label: "역할놀이", value: "roleplay", maps_to: ["언어이해", "사회성"] }
        - { label: "신체활동", value: "physical", maps_to: ["처리속도", "대근육"] }

  existing_assessment:
    has_wisc: boolean
    wisc_upload: File | null             # P2에서 구현
    wisc_summary: string | null          # "전체 IQ 120, 처리속도 낮음" 등 자유 기술
```

#### Stage 2: 일상 기록 (매일 2~3분)

```yaml
daily_log:
  date: "2026-02-07"
  child_id: "child_uuid"

  activities:                            # 1개 이상, 최대 10개/일
    - type: "puzzle"
      detail:
        piece_count: 72                  # 선택지: 24/48/72/100/200+
        completion_time_min: 48
        helped: false                    # 혼자 완성 여부
        photo: File | null               # 완성 사진 (선택)
      → AI 매핑: 처리속도(시간), 시공간(조각수), 작업기억(복잡도), 집중력(시간)

    - type: "reading"
      detail:
        book_title: "구름빵"             # 자동완성 제공
        read_alone: false                # 혼자 읽음 / 같이 읽음
        duration_min: 20
        comprehension_note: "왜 구름으로 빵을 만들었는지 물어봄"
      → AI 매핑: 언어이해(이해도), 읽기수준(독립성)

    - type: "question"
      detail:
        quote: "엄마 왜 달은 낮에도 있어?"
        context: "산책 중에 갑자기"
      → AI 매핑: 언어발달(문장구조), 호기심(주제), 유동추론(논리성)

    - type: "activity"
      detail:
        category: "art" | "english" | "brain_plus" | "physical" | "music" | "coding"
        duration_min: 40
        note: "색연필로 가족 그림 그림"
      → AI 매핑: 다중지능 노출량 트래킹

    - type: "writing"
      detail:
        content: "ㄱㄴㄷ 따라쓰기"
        photo: File | null               # 글씨 사진
      → AI 매핑: 소근육, 언어이해

  emotion_memo:                          # 선택 입력
    mood: "good" | "normal" | "fussy" | "upset"
    discipline_note: "오늘 많이 혼냈음"  # 자유 기술
    parent_mood: "tired" | "ok" | "good" # 부모 컨디션 (양육 피드백용)
```

#### Stage 3: 월간 심화 (월 1회, P2)

```yaml
monthly_deep_dive:
  month: "2026-01"
  child_id: "child_uuid"

  media_upload:
    photos: File[]                       # 이번 달 하이라이트 사진
    videos: File[]                       # 놀이 영상 (최대 3분 × 3개)

  parent_narrative: string               # "이번 달 변화" 자유 서술

  ai_follow_up_questions:                # AI가 부족 영역 탐색용 질문 생성
    - question: "요즘 숫자 세기에 관심이 있나요?"
      answer: string
```

### 3.2 아웃풋 상세

#### 일간 인사이트 (P0)

```json
{
  "date": "2026-02-07",
  "insights": [
    {
      "type": "progress",
      "icon": "📈",
      "message": "퍼즐 완성 시간이 지난주보다 4분 빨라졌어요. 처리 속도가 꾸준히 좋아지고 있어요!",
      "domain": "처리속도",
      "confidence": 0.72
    },
    {
      "type": "observation",
      "icon": "💡",
      "message": "\"달은 왜 낮에도 있어?\" — 과학적 사고의 시작이에요! 이런 질문을 많이 하면 논리력이 쑥쑥 자라요.",
      "domain": "유동추론",
      "confidence": 0.65
    }
  ],
  "today_tip": "오늘은 블록 놀이를 해보세요. 시공간 능력과 처리속도를 동시에 자극할 수 있어요.",
  "streak": 7  // 연속 기록 일수
}
```

#### 주간 리포트 (P0)

```json
{
  "week": "2026-W06",
  "child_id": "child_uuid",

  "radar_chart": {
    "언어이해": 72,        // 0~100 스케일 (백분위 아닌 상대적 발달 점수)
    "시공간": 85,
    "유동추론": 68,
    "작업기억": 74,
    "처리속도": 80
  },

  "trend_comparison": {
    "vs_last_week": {
      "언어이해": +3,
      "시공간": +5,
      "유동추론": +2,
      "작업기억": -1,
      "처리속도": +8
    }
  },

  "highlight": "이번 주는 시공간 능력이 눈에 띄게 성장했어요! 퍼즐과 블록 놀이를 꾸준히 한 효과가 나타나고 있어요.",

  "weak_area_suggestion": {
    "domain": "유동추론",
    "message": "패턴 찾기 놀이를 추가해보세요. 규칙을 찾는 연습이 유동추론에 도움이 돼요.",
    "recommended_activities": ["패턴블록", "숨은그림찾기", "분류놀이"]
  },

  "activity_summary": {
    "total_logs": 14,
    "photos_analyzed": 8,
    "questions_recorded": 5,
    "books_read": 3
  }
}
```

#### 발달 밴드 예측 (P1)

```json
{
  "prediction": {
    "overall_band": "상위 20~30%",
    "display": "또래 중에서 높은 편이에요 ⭐⭐⭐⭐",
    "disclaimer": "이 예측은 전문 검사를 대체하지 않으며, 일상 관찰 기반 참고 지표입니다.",

    "domain_bands": {
      "언어이해": { "band": "상위 15~25%", "trend": "상승" },
      "시공간": { "band": "상위 10~20%", "trend": "안정" },
      "유동추론": { "band": "상위 30~40%", "trend": "상승" },
      "작업기억": { "band": "상위 25~35%", "trend": "안정" },
      "처리속도": { "band": "상위 20~30%", "trend": "상승" }
    },

    "confidence_level": "moderate",
    "data_points_used": 142,
    "minimum_for_prediction": 50        // 최소 50개 데이터 포인트 필요
  }
}
```

#### 교구 추천 (P1)

```json
{
  "recommendations": [
    {
      "reason": "유동추론 강화에 도움돼요",
      "product_name": "러닝리소스 패턴블록 250pc",
      "age_fit": "4~7세",
      "price_range": "₩25,000~₩35,000",
      "links": {
        "coupang": "https://link.coupang.com/...",      // 파트너스 링크
        "naver": "https://search.shopping.naver.com/..."  // 어필리에이트 링크
      },
      "parent_reviews_summary": "패턴 만들기에 좋고, 수학적 사고력 발달에 효과적이라는 후기가 많아요."
    }
  ]
}
```

---

## 4. 기술 스택

### 4.1 아키텍처 개요

```
┌─────────────────────────────────────────────────────────┐
│                    Client Layer                          │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │   PWA (Web)  │  │  토스 미니앱  │  │ 카카오 알림톡 │  │
│  │  Next.js 14  │  │   (P2)       │  │   (알림)      │  │
│  └──────┬───────┘  └──────┬───────┘  └───────┬───────┘  │
└─────────┼─────────────────┼──────────────────┼──────────┘
          │                 │                  │
          ▼                 ▼                  ▼
┌─────────────────────────────────────────────────────────┐
│                    API Gateway                           │
│              Cloudflare Workers / Edge                    │
│              (Rate Limiting, Auth, CDN)                   │
└─────────────────────┬───────────────────────────────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
┌──────────────┐ ┌─────────┐ ┌──────────────┐
│  App Server  │ │ AI      │ │ Media        │
│  (API)       │ │ Engine  │ │ Processing   │
│              │ │         │ │              │
│  Hono.js /   │ │ Python  │ │ Image:       │
│  Node.js     │ │ FastAPI │ │  Sharp +     │
│              │ │         │ │  GPT-4V      │
│  Cloudflare  │ │ Modal / │ │              │
│  Workers     │ │ Railway │ │ Video:       │
│              │ │         │ │  FFmpeg +    │
│              │ │         │ │  Whisper(P2) │
└──────┬───────┘ └────┬────┘ └──────┬───────┘
       │              │             │
       ▼              ▼             ▼
┌─────────────────────────────────────────────────────────┐
│                    Data Layer                             │
│  ┌──────────────┐  ┌─────────┐  ┌────────────────────┐  │
│  │  Supabase    │  │  Redis  │  │  Cloudflare R2     │  │
│  │  (PostgreSQL)│  │ (Cache) │  │  (Media Storage)   │  │
│  │  + Auth      │  │ Upstash │  │  → 분석 후 삭제    │  │
│  │  + RLS       │  │         │  │                    │  │
│  └──────────────┘  └─────────┘  └────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### 4.2 상세 기술 스택

| 레이어 | 기술 | 선택 근거 |
|---|---|---|
| **프론트엔드** | Next.js 14 (App Router) + TypeScript | PWA 지원, SSR/ISR, 토스 미니앱 호환 |
| **UI 프레임워크** | Tailwind CSS + shadcn/ui | 빠른 개발, 모바일 퍼스트 |
| **차트** | Recharts + D3.js | 레이더 차트, 트렌드 그래프 |
| **상태 관리** | Zustand + TanStack Query | 경량, 서버 상태 캐싱 |
| **API 서버** | Hono.js on Cloudflare Workers | 엣지 배포, 한국 리전 레이턴시 최소 |
| **AI 서버** | Python FastAPI on Modal/Railway | GPU 접근, ML 라이브러리 생태계 |
| **DB** | Supabase (PostgreSQL 15) | Auth/RLS 내장, 실시간 구독, 무료 티어 |
| **캐시** | Upstash Redis | 서버리스 Redis, 리포트 캐싱 |
| **미디어 저장** | Cloudflare R2 | S3 호환, 이그레스 무료, 한국 근접 |
| **이미지 분석** | OpenAI GPT-4o (Vision) | 사진 → 구조화 데이터 변환 |
| **NLP 분석** | Claude 3.5 Sonnet / GPT-4o | 아이 질문 분석, 인사이트 생성 |
| **결제** | 토스페이먼츠 (정기결제) | 토스 생태계 시너지, 국내 최적 |
| **알림** | 카카오 알림톡 + FCM | 한국 도달률 최고 (알림톡) |
| **모니터링** | Sentry + Posthog | 에러 추적 + 프로덕트 애널리틱스 |
| **CI/CD** | GitHub Actions + Vercel/CF Pages | 자동 배포, Preview 환경 |

### 4.3 PWA 설정

```json
// manifest.json
{
  "name": "그로스렌즈 - AI 성장 트래커",
  "short_name": "그로스렌즈",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#FFF8F0",
  "theme_color": "#FF6B35",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "categories": ["education", "health"],
  "lang": "ko",
  "dir": "ltr"
}
```

### 4.4 토스 미니앱 호환 (P2)

```
- 앱인토스 SDK 적용 (React 기반)
- TDS (토스 디자인 시스템) 래핑
- TUBA 분석 도구 연동
- 토스 간편결제 네이티브 연동
- 웹뷰 기반이므로 Next.js 코드 대부분 재사용 가능
```

---

## 5. 데이터 모델

### 5.1 ERD (핵심 테이블)

```sql
-- ============================================
-- 사용자 & 아이 프로필
-- ============================================

CREATE TABLE users (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  kakao_id      VARCHAR(50) UNIQUE NOT NULL,
  email         VARCHAR(255),
  nickname      VARCHAR(50) NOT NULL,
  phone_hash    VARCHAR(64),                -- 본인인증 해시 (법정대리인 확인)
  consent_at    TIMESTAMPTZ NOT NULL,        -- 개인정보 동의 일시
  consent_version VARCHAR(10) NOT NULL,      -- 동의서 버전
  plan          VARCHAR(20) DEFAULT 'free',  -- free | basic | premium
  plan_expires  TIMESTAMPTZ,
  created_at    TIMESTAMPTZ DEFAULT now(),
  updated_at    TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE children (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       UUID REFERENCES users(id) ON DELETE CASCADE,
  nickname      VARCHAR(50) NOT NULL,        -- 실명 저장 ❌
  birth_year    INT NOT NULL,
  birth_month   INT NOT NULL,
  gender        VARCHAR(10),                 -- male | female | null
  created_at    TIMESTAMPTZ DEFAULT now(),

  CONSTRAINT chk_birth_year CHECK (birth_year BETWEEN 2018 AND 2026)
);

-- ============================================
-- 초기 프로필 (온보딩)
-- ============================================

CREATE TABLE onboarding_profiles (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  child_id      UUID UNIQUE REFERENCES children(id) ON DELETE CASCADE,

  -- 기질 질문 응답 (JSONB로 유연하게)
  temperament   JSONB NOT NULL,
  -- 예: {"new_env": "adaptive", "faster": ["verbal","memory"], "slower": ["motor"], "obsession": ["puzzle","books"]}

  has_wisc      BOOLEAN DEFAULT false,
  wisc_summary  TEXT,
  wisc_file_key VARCHAR(255),               -- R2 object key (P2)

  -- AI 생성 베이스라인
  baseline      JSONB,
  -- 예: {"언어이해": 70, "시공간": 75, "유동추론": 65, "작업기억": 68, "처리속도": 72}

  created_at    TIMESTAMPTZ DEFAULT now(),
  updated_at    TIMESTAMPTZ DEFAULT now()
);

-- ============================================
-- 일일 활동 로그
-- ============================================

CREATE TABLE daily_logs (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  child_id      UUID REFERENCES children(id) ON DELETE CASCADE,
  log_date      DATE NOT NULL,
  created_at    TIMESTAMPTZ DEFAULT now(),

  UNIQUE(child_id, log_date)
);

CREATE TABLE activities (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  daily_log_id  UUID REFERENCES daily_logs(id) ON DELETE CASCADE,

  type          VARCHAR(30) NOT NULL,        -- puzzle | reading | question | activity | writing
  detail        JSONB NOT NULL,              -- 타입별 구조화 데이터
  -- puzzle:   {"piece_count": 72, "time_min": 48, "helped": false}
  -- reading:  {"book_title": "구름빵", "alone": false, "duration_min": 20, "note": "..."}
  -- question: {"quote": "왜 달은 낮에도 있어?", "context": "산책 중"}
  -- activity: {"category": "art", "duration_min": 40, "note": "..."}
  -- writing:  {"content": "ㄱㄴㄷ 따라쓰기"}

  photo_keys    TEXT[],                      -- R2 object keys
  photo_analysis JSONB,                      -- AI 분석 결과

  -- AI 매핑 결과
  domain_scores JSONB,
  -- 예: {"시공간": 8, "처리속도": 7, "작업기억": 6}  (0~10 단일 활동 스코어)

  created_at    TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_activities_type ON activities(type);
CREATE INDEX idx_activities_daily_log ON activities(daily_log_id);

-- ============================================
-- 감정/훈육 메모
-- ============================================

CREATE TABLE emotion_logs (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  daily_log_id  UUID UNIQUE REFERENCES daily_logs(id) ON DELETE CASCADE,
  child_mood    VARCHAR(20),                 -- good | normal | fussy | upset
  discipline_note TEXT,
  parent_mood   VARCHAR(20),                 -- tired | ok | good
  created_at    TIMESTAMPTZ DEFAULT now()
);

-- ============================================
-- AI 분석 결과
-- ============================================

CREATE TABLE daily_insights (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  child_id      UUID REFERENCES children(id) ON DELETE CASCADE,
  insight_date  DATE NOT NULL,
  insights      JSONB NOT NULL,              -- 일간 인사이트 배열
  today_tip     TEXT,
  model_version VARCHAR(20) NOT NULL,        -- AI 모델 버전 추적
  created_at    TIMESTAMPTZ DEFAULT now(),

  UNIQUE(child_id, insight_date)
);

CREATE TABLE weekly_reports (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  child_id      UUID REFERENCES children(id) ON DELETE CASCADE,
  week_start    DATE NOT NULL,               -- ISO week 월요일
  radar_scores  JSONB NOT NULL,              -- 5영역 레이더 차트 데이터
  trend_data    JSONB NOT NULL,              -- 주간 변화 추이
  highlight     TEXT NOT NULL,
  weak_area     JSONB,
  activity_summary JSONB NOT NULL,
  model_version VARCHAR(20) NOT NULL,
  created_at    TIMESTAMPTZ DEFAULT now(),

  UNIQUE(child_id, week_start)
);

CREATE TABLE development_predictions (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  child_id      UUID REFERENCES children(id) ON DELETE CASCADE,
  predicted_at  DATE NOT NULL,
  overall_band  VARCHAR(30) NOT NULL,        -- "상위 20~30%"
  domain_bands  JSONB NOT NULL,
  confidence    VARCHAR(20) NOT NULL,        -- low | moderate | high
  data_points   INT NOT NULL,
  model_version VARCHAR(20) NOT NULL,
  created_at    TIMESTAMPTZ DEFAULT now()
);

-- ============================================
-- 교구 추천
-- ============================================

CREATE TABLE product_recommendations (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  child_id      UUID REFERENCES children(id) ON DELETE CASCADE,
  recommended_at DATE NOT NULL,
  products      JSONB NOT NULL,              -- 추천 상품 배열
  reason_domain VARCHAR(30),                 -- 추천 이유 영역
  created_at    TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE affiliate_clicks (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       UUID REFERENCES users(id),
  recommendation_id UUID REFERENCES product_recommendations(id),
  platform      VARCHAR(20) NOT NULL,        -- coupang | naver
  clicked_at    TIMESTAMPTZ DEFAULT now(),
  converted     BOOLEAN DEFAULT false,
  commission    DECIMAL(10,2)
);

-- ============================================
-- 구독 & 결제
-- ============================================

CREATE TABLE subscriptions (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id       UUID REFERENCES users(id) ON DELETE CASCADE,
  plan          VARCHAR(20) NOT NULL,
  status        VARCHAR(20) NOT NULL,        -- active | cancelled | expired
  billing_key   VARCHAR(255),                -- 토스페이먼츠 빌링키
  started_at    TIMESTAMPTZ NOT NULL,
  expires_at    TIMESTAMPTZ NOT NULL,
  cancelled_at  TIMESTAMPTZ,
  created_at    TIMESTAMPTZ DEFAULT now()
);

-- ============================================
-- RLS (Row Level Security) 정책
-- ============================================

ALTER TABLE children ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users can only access own children"
  ON children FOR ALL
  USING (user_id = auth.uid());

ALTER TABLE daily_logs ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users access logs via own children"
  ON daily_logs FOR ALL
  USING (child_id IN (SELECT id FROM children WHERE user_id = auth.uid()));

-- (모든 child_id 참조 테이블에 동일 패턴 적용)
```

### 5.2 미디어 저장 정책

```yaml
media_policy:
  storage: Cloudflare R2
  bucket: growthlens-media-{env}
  
  photo:
    max_size: 10MB
    formats: [jpg, jpeg, png, heic, webp]
    processing:
      - resize: 1280x1280 (max dimension)
      - strip_exif: true                   # 위치정보 제거
      - compress: quality 80
    retention:
      analyzed: true → delete after 24h    # ⚠️ 분석 후 삭제
      thumbnail: keep (200x200, anonymized) # 썸네일만 보관
    
  video:  # P2
    max_size: 100MB
    max_duration: 180s
    formats: [mp4, mov]
    processing:
      - transcode: h264, 720p
      - extract_audio: whisper STT
    retention:
      analyzed: true → delete after 1h     # 더 빠른 삭제
```

---

## 6. AI 엔진 설계

### 6.1 발달심리 프레임워크

GrowthLens의 AI 엔진은 K-WISC-V(한국 웩슬러 아동 지능검사 5판)의 **5개 기본지표**를 기반으로 일상 활동을 매핑합니다.

```
K-WISC-V 기본지표          일상 활동 매핑 (프록시)
─────────────────          ──────────────────────
1. 언어이해(VCI)      ←    아이 질문, 독서, 이야기 만들기, 어휘 사용
2. 시공간(VSI)        ←    퍼즐, 블록, 그림, 모양 구분
3. 유동추론(FRI)      ←    패턴 인식, "왜?" 질문, 규칙 발견, 모방 놀이
4. 작업기억(WMI)      ←    다단계 지시 수행, 퍼즐 복잡도, 기억력 놀이
5. 처리속도(PSI)      ←    퍼즐 완성 시간, 글씨 속도, 반응 시간

추가 트래킹 (WISC 외):
6. 정서 안정도         ←    감정 메모, 훈육 빈도
7. 사회성              ←    역할놀이, 또래 상호작용 기록
8. 대근육/소근육       ←    신체활동, 그림 세밀함
```

### 6.2 분석 파이프라인

```
[인풋]                    [처리]                      [아웃풋]
─────                    ──────                      ──────

활동 로그 ──┐
            │
사진 ───────┤    ┌─────────────────┐
            ├──▶│ 1. 구조화 엔진   │──▶ 구조화된 활동 데이터
아이 질문 ──┤    │   (GPT-4o)      │
            │    └────────┬────────┘
감정 메모 ──┘             │
                          ▼
                 ┌─────────────────┐
                 │ 2. 영역 매핑 엔진│──▶ 활동별 5영역 점수
                 │   (규칙 기반    │     (0~10 스케일)
                 │    + ML 보정)   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ 3. 시계열 분석   │──▶ 주간/월간 트렌드
                 │   (이동평균 +   │     레이더 차트 데이터
                 │    가중치)      │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ 4. 예측 엔진    │──▶ 발달 밴드 예측
                 │   (베이지안     │     "상위 20~30%"
                 │    + 연령 표준) │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ 5. 인사이트     │──▶ 일간 인사이트
                 │   생성 엔진     │     주간 리포트
                 │   (Claude 3.5)  │     교구 추천
                 └─────────────────┘
```

### 6.3 영역 매핑 엔진 상세

```python
# domain_mapper.py — 규칙 기반 매핑 + LLM 보정

ACTIVITY_DOMAIN_MAP = {
    "puzzle": {
        "시공간":   {"weight": 0.35, "factor": "piece_count"},
        "처리속도": {"weight": 0.30, "factor": "inverse_time"},
        "작업기억": {"weight": 0.20, "factor": "complexity"},
        "유동추론": {"weight": 0.15, "factor": "pattern_type"},
    },
    "reading": {
        "언어이해": {"weight": 0.50, "factor": "comprehension"},
        "작업기억": {"weight": 0.20, "factor": "story_length"},
        "유동추론": {"weight": 0.15, "factor": "questions_asked"},
        "정서":     {"weight": 0.15, "factor": "engagement"},
    },
    "question": {
        "언어이해": {"weight": 0.35, "factor": "sentence_complexity"},
        "유동추론": {"weight": 0.35, "factor": "logical_depth"},
        "호기심":   {"weight": 0.30, "factor": "topic_novelty"},
    },
    # ... 각 활동 타입별 매핑
}

class DomainScorer:
    """활동 데이터 → 5영역 점수 변환"""
    
    def score_puzzle(self, detail: dict, child_age_months: int) -> dict:
        """퍼즐 활동 스코어링"""
        # 연령 대비 난이도 계수
        age_norm = self.get_age_norm("puzzle", child_age_months)
        
        # 조각 수 → 시공간 점수
        piece_score = min(10, (detail["piece_count"] / age_norm["expected_pieces"]) * 7)
        
        # 완성 시간 → 처리속도 점수 (빠를수록 높음)
        if detail.get("completion_time_min"):
            expected_time = age_norm["expected_time_min"] * (detail["piece_count"] / age_norm["expected_pieces"])
            speed_score = min(10, (expected_time / detail["completion_time_min"]) * 7)
        else:
            speed_score = 5  # 시간 미입력 시 중립
        
        # 도움 여부 → 작업기억 보정
        memory_score = piece_score * (1.0 if not detail.get("helped") else 0.7)
        
        return {
            "시공간": round(piece_score, 1),
            "처리속도": round(speed_score, 1),
            "작업기억": round(memory_score, 1),
            "유동추론": round(piece_score * 0.6, 1),  # 퍼즐 패턴에서 유동추론 간접 측정
        }

    def score_question(self, detail: dict, child_age_months: int) -> dict:
        """아이 질문 스코어링 — LLM 기반"""
        prompt = f"""
        아이 나이: {child_age_months}개월
        아이가 한 질문: "{detail['quote']}"
        상황: {detail.get('context', '없음')}
        
        다음 영역별로 0~10점을 매기세요:
        1. 언어이해: 문장 구조의 복잡도, 어휘 수준
        2. 유동추론: 인과관계 이해, 논리적 사고 수준
        3. 호기심: 질문 주제의 깊이와 독창성
        
        JSON으로 반환: {{"언어이해": N, "유동추론": N, "호기심": N, "분석": "한줄 설명"}}
        """
        return self.llm_call(prompt)
```

### 6.4 연령 기준 표준 (Age Norms)

```python
# age_norms.py — 한국 아동 발달 기준 데이터

AGE_NORMS = {
    # 만 4세 (48~59개월)
    48: {
        "puzzle": {
            "expected_pieces": 24,
            "expected_time_min": 15,
            "advanced_pieces": 48,
        },
        "reading": {
            "expected_level": "그림책 함께 읽기",
            "advanced_level": "간단한 글자 인식",
        },
        "question": {
            "expected_complexity": "단순 why 질문",
            "advanced_complexity": "인과관계 질문",
        },
        "writing": {
            "expected": "직선/원 따라 그리기",
            "advanced": "자기 이름 쓰기",
        },
    },
    # 만 5세 (60~71개월)
    60: {
        "puzzle": {
            "expected_pieces": 48,
            "expected_time_min": 25,
            "advanced_pieces": 72,
        },
        "reading": {
            "expected_level": "간단한 글자 읽기",
            "advanced_level": "짧은 문장 혼자 읽기",
        },
        "question": {
            "expected_complexity": "인과관계 질문",
            "advanced_complexity": "추상적/가정 질문",
        },
        "writing": {
            "expected": "자기 이름 + 기본 자음/모음",
            "advanced": "간단한 단어 쓰기",
        },
    },
    # 만 6세 (72~83개월)
    72: {
        "puzzle": {
            "expected_pieces": 72,
            "expected_time_min": 40,
            "advanced_pieces": 100,
        },
        "reading": {
            "expected_level": "짧은 문장 혼자 읽기",
            "advanced_level": "챕터북 시작",
        },
        "question": {
            "expected_complexity": "추상적 질문",
            "advanced_complexity": "메타인지 질문 (왜 그렇게 생각해?)",
        },
        "writing": {
            "expected": "간단한 문장 쓰기",
            "advanced": "일기 쓰기",
        },
    },
}
```

### 6.5 예측 엔진

```python
# prediction_engine.py

class DevelopmentPredictor:
    """
    일상 데이터 → 발달 밴드 예측
    
    방법론:
    1. 각 활동의 영역별 점수를 시계열로 수집
    2. 연령 표준 대비 상대 위치 계산
    3. 베이지안 업데이트로 사전 분포(온보딩) → 사후 분포(데이터 축적)
    4. 신뢰도에 따라 밴드 폭 조절
    """
    
    MIN_DATA_POINTS = 50    # 예측 최소 조건
    
    def predict_band(self, child_id: str) -> dict:
        # 1. 데이터 수집
        scores = self.get_domain_scores_timeseries(child_id)
        data_points = sum(len(v) for v in scores.values())
        
        if data_points < self.MIN_DATA_POINTS:
            return {"status": "insufficient_data", "data_points": data_points}
        
        # 2. 영역별 트렌드 점수 계산 (가중 이동평균)
        domain_trends = {}
        for domain, series in scores.items():
            # 최근 데이터에 더 높은 가중치
            weights = self.exponential_weights(len(series), decay=0.95)
            weighted_avg = np.average(series, weights=weights)
            domain_trends[domain] = weighted_avg
        
        # 3. 연령 표준 대비 백분위 추정
        child_age = self.get_child_age_months(child_id)
        percentiles = {}
        for domain, score in domain_trends.items():
            norm = AGE_NORMS[self.nearest_age_key(child_age)]
            percentile = self.score_to_percentile(score, norm, domain)
            percentiles[domain] = percentile
        
        # 4. 밴드 변환 (점수 ❌, 구간으로)
        bands = {}
        for domain, pct in percentiles.items():
            bands[domain] = self.percentile_to_band(pct)
            # 예: 75~80 → "상위 20~30%"
        
        # 5. 전체 밴드 (가중 평균)
        overall = np.mean(list(percentiles.values()))
        overall_band = self.percentile_to_band(overall)
        
        # 6. 신뢰도
        confidence = self.calculate_confidence(data_points, len(scores))
        
        return {
            "overall_band": overall_band,
            "domain_bands": bands,
            "confidence": confidence,
            "data_points": data_points,
        }
    
    def percentile_to_band(self, percentile: float) -> str:
        """정확한 점수 대신 넓은 밴드로 표현 (부모 감정 배려)"""
        if percentile >= 90: return "상위 10% 이내"
        if percentile >= 80: return "상위 10~20%"
        if percentile >= 70: return "상위 20~30%"
        if percentile >= 60: return "상위 30~40%"
        if percentile >= 50: return "평균 이상"
        if percentile >= 40: return "평균 수준"
        if percentile >= 30: return "평균 수준"
        return "조금 더 관심이 필요해요"  # 부정적 표현 최소화
    
    def calculate_confidence(self, data_points: int, domains_covered: int) -> str:
        if data_points >= 200 and domains_covered >= 5:
            return "high"
        if data_points >= 100 and domains_covered >= 4:
            return "moderate"
        return "low"
```

### 6.6 인사이트 생성 엔진

```python
# insight_generator.py

DAILY_INSIGHT_PROMPT = """
당신은 아동 발달 전문가이자 따뜻한 육아 멘토입니다.
아래 데이터를 보고, 부모(엄마)에게 전달할 일간 인사이트를 생성하세요.

## 규칙
1. 전문 용어 사용 ❌ → 엄마가 이해하는 쉬운 말로
2. 긍정적 톤 우선 → 부족한 부분은 "이것도 해보세요" 식으로
3. IQ 점수/수치 절대 언급 ❌ → "잘하고 있어요", "성장 중이에요"
4. 감정 메모가 있으면 → 공감 먼저, 조언은 부드럽게
5. 한줄 인사이트 1~3개 + 오늘의 팁 1개

## 아이 정보
- 닉네임: {nickname}
- 나이: 만 {age}세 ({months}개월)
- 이번 주 트렌드: {weekly_trend}

## 오늘 기록
{today_activities}

## 감정 메모
{emotion_memo}

## JSON 형식으로 출력:
{{
  "insights": [
    {{"type": "progress|observation|encouragement", "icon": "emoji", "message": "...", "domain": "..."}}
  ],
  "today_tip": "..."
}}
"""

WEEKLY_REPORT_PROMPT = """
당신은 아동 발달 전문가입니다.
이번 주 데이터를 종합 분석하여 주간 리포트를 생성하세요.

## 규칙
1. 레이더 차트 데이터: 5영역 0~100 점수 (절대 점수 아닌 상대적 발달 수준)
2. 하이라이트: 가장 성장이 두드러진 영역 칭찬
3. 약한 영역: 부정적 표현 대신 "함께 키워볼 영역" + 구체적 활동 제안
4. 부모 노력 인정: "이번 주 {n}번이나 기록해주셨네요!"

## 이번 주 데이터
{week_data}

## 지난 주 대비
{last_week_comparison}
"""
```

### 6.7 사진 분석 파이프라인

```python
# photo_analyzer.py

PHOTO_ANALYSIS_PROMPT = """
이 사진은 {age}세 아이의 {activity_type} 활동 결과물입니다.

분석해주세요:
1. 완성도 (0~10): 조각이 다 맞춰졌는지, 빈 곳은 없는지
2. 복잡도 (0~10): 조각 수, 패턴 복잡성
3. 세밀함 (0~10): (그림인 경우) 색칠 꼼꼼함, 선의 정확성
4. 창의성 (0~10): (그림인 경우) 독창적 표현 여부
5. 발달 관찰: 이 연령 대비 주목할 점

JSON으로 반환:
{{"completeness": N, "complexity": N, "precision": N, "creativity": N, "observation": "..."}}
"""

class PhotoAnalyzer:
    def analyze(self, photo_url: str, activity_type: str, child_age: int) -> dict:
        # 1. 이미지 전처리 (리사이즈, EXIF 제거)
        processed = self.preprocess(photo_url)
        
        # 2. GPT-4o Vision 분석
        result = self.vision_model.analyze(
            image=processed,
            prompt=PHOTO_ANALYSIS_PROMPT.format(
                age=child_age // 12,
                activity_type=activity_type
            )
        )
        
        # 3. 원본 이미지 삭제 (분석 완료 후)
        self.delete_original(photo_url)
        
        # 4. 결과만 저장
        return result
```

---

## 7. 수익 모델 상세

### 7.1 구독 플랜

| 항목 | 무료 | 베이직 (₩9,900/월) | 프리미엄 (₩19,900/월) |
|---|---|---|---|
| **일일 기록** | 3개/일 | 무제한 | 무제한 |
| **사진 분석** | 10장/월 | 무제한 | 무제한 |
| **영상 분석** | ❌ | ❌ | 3개/월 |
| **일간 인사이트** | 간략 버전 | 간략 버전 | **상세 버전** |
| **주간 리포트** | ❌ | ✅ | ✅ |
| **발달 밴드 예측** | ❌ | ❌ | ✅ |
| **교구 추천** | 기본 | **맞춤 추천** | **맞춤 + 가격 비교** |
| **양육 피드백** | ❌ | ❌ | ✅ |
| **월간 심화 리포트** | ❌ | ❌ | ✅ |
| **데이터 보관** | 3개월 | 1년 | 무제한 |
| **아이 프로필** | 1명 | 2명 | 3명 |
| **광고** | 배너 있음 | 없음 | 없음 |

### 7.2 어필리에이트 커머스

```yaml
affiliate_model:
  coupang_partners:
    commission_rate: 3~8%       # 카테고리별 상이
    교구_category: ~3%
    도서_category: ~3%
    cookie_duration: 24h
    
  naver_shopping:
    commission_rate: 2~5%
    integration: 네이버 쇼핑 검색 API + 어필리에이트
    
  revenue_estimation:
    avg_order_value: ₩30,000
    conversion_rate: 5%          # 추천 → 클릭 → 구매
    avg_commission: ₩1,200/건
    monthly_recommendations: 4/user
    
    # 유료 가입자 3,000명 기준
    monthly_affiliate: 3,000 × 4 × 0.05 × ₩1,200 = ₩720,000/월
```

### 7.3 미래 수익원 (Phase 2+)

| 수익원 | 시기 | 예상 기여도 |
|---|---|---|
| B2B: 어린이집/유치원 대시보드 | Month 6+ | 기관당 ₩50,000/월 |
| 교구 브랜드 스폰서 추천 | Month 4+ | CPM ₩5,000~10,000 |
| 발달 전문가 1:1 상담 중개 | Month 8+ | 건당 ₩5,000 수수료 |
| 데이터 인사이트 리포트 (B2B) | Year 2+ | 익명화 통계, 교구 업체 판매 |

---

## 8. Day 1~30 실행 일정

### Phase 0: 사전 준비 (Day 1~3)

| Day | Task | 담당 | 산출물 |
|---|---|---|---|
| 1 | PRD 최종 리뷰 & 확정 | CEO + PO | 확정 PRD |
| 1 | Supabase 프로젝트 생성, GitHub 레포 셋업 | DEV | 개발 환경 |
| 2 | 디자인 시스템 정의 (컬러/폰트/컴포넌트) | DEV | Figma/코드 |
| 2 | 데이터 모델 DDL 실행 + RLS 설정 | DEV | DB 스키마 |
| 3 | AI 프롬프트 초안 (인사이트/리포트) | PO + DEV | 프롬프트 문서 |
| 3 | 카카오 소셜 로그인 앱 등록 | DEV | OAuth 설정 |

### Phase 1: 핵심 기능 구현 (Day 4~14)

| Day | Task | 담당 | 산출물 |
|---|---|---|---|
| 4~5 | 카카오 로그인 + 회원가입 플로우 (법정대리인 동의 포함) | DEV | F-005 |
| 5~6 | 아이 프로필 생성 + 온보딩 설문 UI | DEV | F-001, F-006 |
| 7~9 | 일일 활동 기록 (텍스트 + 사진 업로드) | DEV | F-002 |
| 9~10 | AI 영역 매핑 엔진 (규칙 기반 v1) | DEV | 매핑 엔진 |
| 10~11 | 일간 인사이트 생성 + 표시 | DEV | F-003 |
| 12~14 | 주간 리포트 (레이더 차트 + 트렌드) | DEV | F-004 |

### Phase 2: 수익화 + 완성도 (Day 15~24)

| Day | Task | 담당 | 산출물 |
|---|---|---|---|
| 15~16 | 토스페이먼츠 정기결제 연동 | DEV | F-007 |
| 16~17 | 플랜별 기능 제한 (미들웨어) | DEV | 접근 제어 |
| 18~19 | 사진 AI 분석 (GPT-4o Vision) | DEV | F-101 |
| 19~20 | 교구 추천 엔진 + 쿠팡/네이버 링크 | DEV | F-103 |
| 21~22 | 알림 시스템 (카카오 알림톡 + FCM) | DEV | F-104 |
| 22~23 | 독서 기록 특화 (책 자동완성) | DEV | F-105 |
| 24 | 전체 통합 테스트 | DEV + PO | QA 리포트 |

### Phase 3: 런칭 준비 (Day 25~30)

| Day | Task | 담당 | 산출물 |
|---|---|---|---|
| 25 | 개인정보 처리방침 + 서비스 약관 작성 | PO + 법률 | 법률 문서 |
| 26 | 동탄 맘카페 사전 테스터 모집 (30명) | PO | 베타 유저 |
| 27~28 | 베타 테스트 + 피드백 수집 | ALL | 피드백 |
| 29 | 크리티컬 버그 수정 | DEV | 안정화 |
| 30 | **소프트 런칭** (동탄 맘카페 오픈) | ALL | 🚀 런칭 |

---

## 9. 비용 산출 + BEP

### 9.1 월간 고정 비용 (MVP 단계)

| 항목 | 비용/월 | 비고 |
|---|---|---|
| Supabase Pro | $25 (≈₩33,000) | 8GB DB, 250GB 전송 |
| Cloudflare Workers | $5 (≈₩7,000) | 10M 요청/월 포함 |
| Cloudflare R2 | $5~15 (≈₩10,000~20,000) | 미디어 저장 (분석 후 삭제) |
| Upstash Redis | $10 (≈₩13,000) | 서버리스 캐시 |
| Vercel Pro | $20 (≈₩26,000) | 프론트엔드 호스팅 |
| 도메인 + SSL | ₩3,000 | 연간 ₩36,000 |
| **인프라 소계** | **≈₩92,000/월** | |

### 9.2 변동 비용 (AI API)

| API | 비용 | 사용량 가정 (1,000 유저) |
|---|---|---|
| GPT-4o (텍스트) | $2.50/1M input, $10/1M output | 일간 인사이트 × 1,000 = ₩200,000/월 |
| GPT-4o Vision | $2.50/1M input + 이미지 | 사진 분석 × 5,000장 = ₩250,000/월 |
| Claude 3.5 Sonnet | $3/1M input, $15/1M output | 주간 리포트 × 1,000 = ₩150,000/월 |
| 카카오 알림톡 | ₩7.5/건 | 일 1건 × 1,000 × 30일 = ₩225,000/월 |
| **AI/알림 소계** | **≈₩825,000/월** | **(유저 1,000명 기준)** |

### 9.3 유저당 변동 비용

```
AI 분석 비용/유저/월 ≈ ₩600 (인사이트 + 리포트)
사진 분석 비용/유저/월 ≈ ₩250 (평균 5장/월)
알림 비용/유저/월 ≈ ₩225
─────────────────────────
유저당 변동 비용 ≈ ₩1,075/월

무료 유저 → 순수 비용 (₩1,075)
베이직 유저 → 마진 ₩9,900 - ₩1,075 = ₩8,825 (89%)
프리미엄 유저 → 마진 ₩19,900 - ₩1,500 = ₩18,400 (92%)
  (프리미엄은 영상 분석 추가 ₩425)
```

### 9.4 BEP (손익분기점) 분석

```
월 고정 비용: ₩92,000 (인프라) + ₩0 (MVP 단계 인건비 제외)
유저당 변동 비용: ₩1,075/월

가정: 무료 70%, 베이직 20%, 프리미엄 10%

전체 유저 N명일 때:
- 수입 = N × (0.20 × ₩9,900 + 0.10 × ₩19,900) = N × ₩3,970
- 비용 = ₩92,000 + N × ₩1,075
- BEP: N × ₩3,970 = ₩92,000 + N × ₩1,075
       N × ₩2,895 = ₩92,000
       N ≈ 32명

→ 유료 전환 포함 총 32명이면 인프라 비용 BEP
→ 인건비(CEO 1인 풀타임 가정 ₩5,000,000/월) 포함 시:
   N × ₩2,895 = ₩5,092,000
   N ≈ 1,759명 (총 유저, 이 중 유료 528명)

→ 어필리에이트 추가 시 BEP 더 빨라짐
```

### 9.5 12개월 재무 프로젝션

| 월 | 총 유저 | 유료 유저 | MRR | 비용 | 손익 |
|---|---|---|---|---|---|
| M1 | 100 | 15 | ₩149K | ₩199K | -₩50K |
| M2 | 300 | 60 | ₩476K | ₩414K | +₩62K |
| M3 | 700 | 175 | ₩1,390K | ₩843K | +₩547K |
| M6 | 2,000 | 600 | ₩4,770K | ₩2,242K | +₩2,528K |
| M9 | 4,000 | 1,200 | ₩9,540K | ₩4,392K | +₩5,148K |
| M12 | 8,000 | 2,400 | ₩19,080K | ₩8,692K | +₩10,388K |

> *인건비 미포함 기준. 인건비 포함 시 M6~M8에 BEP 도달 예상.*

---

## 10. KPI

### 10.1 North Star Metric

> **주간 활성 기록 가구 수 (WAR: Weekly Active Recorders)**  
> = 해당 주에 1개 이상 활동을 기록한 유니크 가구 수

### 10.2 핵심 KPI 대시보드

| 카테고리 | KPI | 목표 (M3) | 목표 (M6) | 목표 (M12) |
|---|---|---|---|---|
| **Acquisition** | 신규 가입 | 200/주 | 400/주 | 800/주 |
| | CAC (Customer Acquisition Cost) | ₩0 (오가닉) | ₩3,000 | ₩5,000 |
| **Activation** | 온보딩 완료율 | 80% | 85% | 90% |
| | 첫 기록까지 시간 | < 10분 | < 5분 | < 3분 |
| **Retention** | D7 리텐션 | 50% | 60% | 65% |
| | D30 리텐션 | 30% | 40% | 50% |
| | 주간 기록 빈도 | 3회/주 | 4회/주 | 5회/주 |
| **Revenue** | 유료 전환율 | 20% | 25% | 30% |
| | MRR | ₩1.4M | ₩4.8M | ₩19M |
| | ARPU (유료) | ₩12,000 | ₩13,000 | ₩14,000 |
| | Churn Rate (월) | < 10% | < 8% | < 5% |
| **Engagement** | 일간 인사이트 열람률 | 70% | 80% | 85% |
| | 주간 리포트 열람률 | 60% | 70% | 80% |
| | 교구 추천 클릭률 | 15% | 20% | 25% |
| **Quality** | 인사이트 유용성 평점 | 4.0/5 | 4.3/5 | 4.5/5 |
| | NPS | 30 | 45 | 60 |

### 10.3 건강 지표 (Guard Rails)

| 지표 | 경고 기준 | 대응 |
|---|---|---|
| 일간 활성률 | < 40% | 알림 최적화, UX 개선 |
| 사진 업로드 실패율 | > 5% | 인프라 점검 |
| AI 응답 지연 | > 5초 | 캐싱/모델 최적화 |
| 1-star 리뷰 | > 5개/주 | 긴급 UX 리서치 |
| 개인정보 관련 민원 | 1건이라도 | 즉시 법률 리뷰 |

---

## 11. 리스크 + 법률

### 11.1 법률 컴플라이언스

#### 개인정보보호법 (만 14세 미만)

```
┌──────────────────────────────────────────────────────┐
│  아동 개인정보 처리 체크리스트                          │
├──────────────────────────────────────────────────────┤
│                                                      │
│  ✅ 법정대리인(부모) 동의 필수                         │
│     → 가입 시 본인인증(PASS/카카오) 후 동의            │
│     → 동의서 버전 관리 + 갱신 알림                     │
│                                                      │
│  ✅ 수집 항목 최소화                                   │
│     → 아이 실명 수집 ❌ (닉네임만)                     │
│     → 사진: 분석 후 24시간 내 삭제                     │
│     → 영상: 분석 후 1시간 내 삭제                      │
│     → EXIF(위치정보) 업로드 시 즉시 제거               │
│                                                      │
│  ✅ 개인정보 처리방침 필수 고지 항목                     │
│     → 수집 목적, 항목, 보유기간, 제3자 제공,           │
│        파기 절차, 법정대리인 권리                       │
│                                                      │
│  ✅ 법정대리인 권리 보장                               │
│     → 열람/정정/삭제/처리정지 요청 → 72시간 내 처리    │
│     → 동의 철회 → 즉시 데이터 삭제                    │
│                                                      │
│  ✅ 위반 시 제재                                       │
│     → 5년 이하 징역 또는 5,000만원 이하 벌금           │
│     → 매출액 3% 이하 과징금                            │
│                                                      │
│  ⚠️ 개인정보 영향평가 검토 (선제적)                    │
│     → 5만명 이상 민감정보 시 법적 의무                  │
│     → MVP 단계에서도 자발적 수행 권장                   │
│                                                      │
└──────────────────────────────────────────────────────┘
```

#### 아동복지법 / 아동학대 관련

```
⚠️ 서비스가 아동 발달 "지연"을 탐지할 경우:
→ 의료 진단 절대 ❌
→ "전문가 상담을 추천드려요" 표현만 사용
→ 발달 장애 암시 표현 금지
→ 면책 문구 모든 리포트에 포함:
  "이 분석은 전문 의료 진단을 대체하지 않습니다."
```

#### 전자상거래법 (교구 추천)

```
✅ 어필리에이트 링크 공개 의무
→ "이 링크를 통해 구매 시 서비스 운영에 도움이 됩니다" 표기
→ 광고/제휴 표시 의무 준수
```

### 11.2 리스크 매트릭스

| 리스크 | 확률 | 영향 | 대응 |
|---|---|---|---|
| **개인정보 유출** | 낮음 | 치명적 | RLS, 암호화, 분석 후 삭제, 침투 테스트 |
| **AI 오분석 (발달 과대/과소 평가)** | 중간 | 높음 | 면책 문구, 밴드 표현, 최소 데이터 포인트 기준 |
| **부모 불안 유발** | 중간 | 높음 | UX 가이드라인: 긍정 우선, 비교 최소화, 전문가 연결 |
| **낮은 리텐션** | 높음 | 높음 | 알림 최적화, 게이미피케이션(연속기록 뱃지), 간편 기록 UX |
| **LLM 비용 폭증** | 중간 | 중간 | 캐싱, 배치 처리, 오픈소스 모델 전환 플랜 |
| **쿠팡파트너스 정책 변경** | 낮음 | 낮음 | 네이버 등 다채널 확보 |
| **경쟁사 진입** | 중간 | 중간 | 데이터 해자 선점, 커뮤니티 구축 |
| **부정적 언론 보도 (AI+아동)** | 낮음 | 높음 | 투명한 정책, 전문가 자문위원회 구성 |

### 11.3 대응 전략

#### 개인정보 보호 기술적 조치

```yaml
security_measures:
  encryption:
    at_rest: AES-256 (Supabase default)
    in_transit: TLS 1.3
    
  access_control:
    database: Row Level Security (Supabase RLS)
    api: JWT + API key rotation (90일)
    admin: 2FA 필수
    
  data_minimization:
    photo: 분석 완료 → 24h 내 삭제
    video: 분석 완료 → 1h 내 삭제
    exif: 업로드 시 즉시 제거
    child_name: 닉네임만 저장
    
  audit:
    logging: 모든 데이터 접근 로그
    retention: 로그 1년 보관
    review: 분기별 보안 감사
    
  incident_response:
    detection: Sentry + 이상 접근 알림
    notification: 유출 인지 후 72시간 내 사용자 통보 (법적 의무)
    recovery: 데이터 백업 일 1회, 복구 목표 시간 4시간
```

---

## 12. 확장 로드맵

### Phase 1: MVP → PMF (Month 1~3)

```
M1: 동탄 맘카페 소프트 런칭 (100 가구)
M2: 피드백 반영 → 사진 분석, 교구 추천 추가
M3: 수도권 확대 (분당/판교/송파), 700 가구 목표
    → PMF 검증: D30 리텐션 30%+, NPS 30+
```

### Phase 2: Growth (Month 4~6)

```
M4: 발달 밴드 예측 기능 출시 (프리미엄)
    영상 분석 베타
    교구 브랜드 스폰서 추천 시작
M5: 카카오톡 채널 연동 (기록 유도)
    맘카페 바이럴 캠페인
    인플루언서 맘 협업 (무료 프리미엄 제공)
M6: 전국 확대, 2,000 가구
    B2B: 어린이집 3곳 파일럿
    토스 미니앱 개발 착수
```

### Phase 3: Scale (Month 7~12)

```
M7~8:  토스 미니앱 출시 → 토스 3,000만 유저 노출
M8~9:  자사 기존 서비스 통합
       - PrintPlay → "이번 주 추천 프린트 활동"
       - TaleMe → "아이 질문으로 만든 동화"
       - GrowCoach → "발달 기반 습관 추천"
M9~10: 발달 전문가 1:1 상담 중개
M11:   다국어 지원 준비 (영어/일본어)
M12:   8,000 가구, ARR ₩2.3억
```

### Phase 4: Platform (Year 2)

```
Q1: 글로벌 출시 (영어 → 미국/싱가포르)
Q2: AI 모델 자체 학습 (축적 데이터 기반 파인튜닝)
    → 더 이상 범용 LLM 의존 ❌
Q3: B2B 대시보드 정식 출시 (유치원/어린이집)
Q4: 시리즈 A 라운드
    → 목표: 50,000 가구, ARR ₩10억+
```

### Phase 5: Vision (Year 3+)

```
- 학령기 확장 (7~12세): 학습 성과 + 인지발달 연계
- 발달 위험 조기 탐지 → 소아정신과 연계 (B2B2C)
- 아시아 시장 확대 (일본/대만/동남아)
- 교육 AI 플랫폼으로 진화
  "부모의 모든 교육 결정을 돕는 AI"
```

---

## 부록

### A. 용어 정의

| 용어 | 정의 |
|---|---|
| K-WISC-V | 한국 웩슬러 아동 지능검사 5판. 6~16세 대상 표준화 지능검사 |
| 언어이해(VCI) | 언어적 개념 형성, 추론, 표현 능력 |
| 시공간(VSI) | 시각적 자극의 분석, 합성, 공간 관계 파악 |
| 유동추론(FRI) | 새로운 상황에서 규칙을 발견하고 적용하는 능력 |
| 작업기억(WMI) | 정보를 일시적으로 저장하고 조작하는 능력 |
| 처리속도(PSI) | 단순 시각 정보를 빠르고 정확하게 처리하는 능력 |
| 발달 밴드 | IQ 점수 대신 "상위 N~M%" 구간으로 표현하는 방식 |
| PWA | Progressive Web App. 웹 기술로 네이티브 앱 경험 제공 |
| RLS | Row Level Security. DB 행 단위 접근 제어 |

### B. 참고 문헌

1. K-WISC-V 한국 웩슬러 아동 지능검사 5판 매뉴얼 (인싸이트, 2020)
2. 개인정보보호위원회, "아동·청소년 개인정보보호 가이드라인" (2023)
3. 개인정보보호법 제22조 (법정대리인 동의)
4. 한국아동패널 II (한국보건사회연구원, 2024)
5. Gardner, H. "Frames of Mind: The Theory of Multiple Intelligences" (1983)

### C. 변경 이력

| 버전 | 날짜 | 변경 내용 | 작성자 |
|---|---|---|---|
| v1.0 | 2026-02-07 | 초안 작성 | PO Agent |

---

> **다음 단계:**  
> 1. CEO 리뷰 및 피드백 반영  
> 2. DEV에게 핸드오프 → Phase 0 (Day 1~3) 착수  
> 3. 개인정보 처리방침 법률 검토 의뢰  
> 4. 동탄 맘카페 테스터 사전 모집 시작
