# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

가재 컴퍼니(Gajae Company) BIP(Build in Public) 서비스. Human CEO와 AI 군단의 협업 과정을 실시간 제품화하는 Next.js 웹 애플리케이션. GitHub Repository의 Markdown 기반 연대기 데이터를 API로 서빙한다.

## Repository Structure

- `gajae-company/` — Next.js 웹 애플리케이션 (모든 개발 명령은 이 디렉토리에서 실행)
- `docs/` — 7대 지능 계층 문서 (core, chronicle, business, task, governance, incident, guides)
- `docs/core/legal/CONSTITUTION.md` — 통합 헌법 (최상위 규율)
- `docs/core/process/PROCESS_CODING_NEXTJS.md` — Next.js 클린 아키텍처 가이드

## Development Commands

모든 명령은 `gajae-company/` 디렉토리에서 실행한다.

```bash
cd gajae-company

npm run dev          # 개발 서버 (Next.js dev)
npm run build        # 프로덕션 빌드
npm run start        # 프로덕션 서버
npm run lint         # ESLint (eslint-config-next/core-web-vitals + typescript)
```

배포: Firebase Hosting (asia-northeast3 리전, SSR 지원)
```bash
firebase deploy      # gajae-company/ 내에서 실행
```

## Tech Stack

- **Next.js 16** (App Router, React Server Components)
- **React 19**, **TypeScript 5** (strict mode)
- **Tailwind CSS 4** (`@theme` 기반 Ghibli 커스텀 테마)
- **Zustand 5** (클라이언트 상태 관리)
- **Framer Motion** (애니메이션)
- **Firebase Hosting** (asia-northeast3, Framework SSR)
- **GitHub API** (연대기 데이터 소스, ISR 60초 캐싱)

## Architecture: Feature-based Clean Architecture

```
src/
├── core/           # 인프라 래퍼 (config, network)
├── common/         # 공용 컴포넌트 (GNB, Heartbeat)
└── feature/
    └── {feature}/
        ├── data/           # Repository 구현체 + DataSource (GitHub API 통신)
        ├── domain/         # Model(interface/type) + Service(비즈니스 로직)
        └── presentation/   # Component + View + Store(Zustand)
```

**핵심 의존성 규칙**: `Presentation → Domain ← Data`. 의존성은 반드시 Domain(안쪽) 방향으로만 흐른다.

- **Domain Layer**: 순수 TypeScript. 외부 프레임워크 의존성 없음.
- **Data Layer**: Domain에 정의된 Repository Interface를 구현. 외부 API 직접 호출 금지 — `core/`의 래퍼 사용.
- **Presentation Layer**: React 컴포넌트, 페이지 뷰, Zustand Store.

## Coding Standards

- **`any` 타입 절대 금지** — 모든 데이터는 `interface`나 `type`으로 정의
- **폴더명은 단수형(Singular)** — `feature/`, `component/`, `model/` 등
- **인프라 격리** — 외부 라이브러리를 feature에서 직접 import 금지, `core/`에 래퍼 생성
- **Path alias**: `@/*` → `./src/*`
- **클라이언트 컴포넌트**: `"use client"` 디렉티브 명시

## Environment Variables

```
GITHUB_TOKEN                              # GitHub API 인증 (없으면 mock 데이터 반환)
NEXT_PUBLIC_FIREBASE_API_KEY              # Firebase 클라이언트 설정
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN
NEXT_PUBLIC_FIREBASE_PROJECT_ID
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID
NEXT_PUBLIC_FIREBASE_APP_ID
```

## Key Data Flow

1. GitHub API → `GithubClient` (data_source) → `GithubRepositoryImpl` (data) → `ChronicleService` (domain) → Zustand Store / API Route → UI
2. API Route: `GET /api/chronicle/[date]` — 특정 날짜의 연대기 데이터 반환
3. 데이터 소스: `docs/chronicle/daily/{YYYY-MM-DD}/` 내 meeting, command 마크다운 파일

## UI Theme

Ghibli 스타일 테마. `globals.css`의 `@theme`에 정의된 `ghibli-*` 색상 토큰 사용:
- `ghibli-bg`, `ghibli-paper`, `ghibli-text`, `ghibli-green`, `ghibli-orange`, `ghibli-blue`, `ghibli-accent`
- `.ghibli-card`, `.watercolor-blur`, `.handwritten` 유틸리티 클래스 활용
- 기본 폰트: Pretendard / 손글씨: Nanum Pen Script

## Integrity Checks

헌법 및 연대기 무결성 검증 스크립트 (루트 디렉토리):
```bash
python legal_integrity_check.py        # 15대 리더십 원칙 누락 검증
python chronicle_integrity_check.py    # 연대기 인덱스 무결성 검증
```
