# 🗂️ 도메인 인덱스 (Domain Index): [GOVERNANCE]

## 1. 개요 (Overview)
본 문서는 가재 컴퍼니의 운영 질서와 무결성을 관리하는 **[거버넌스 레이어]**의 통합 지도입니다. 인사, 감사, 공정 승인 현황을 중앙 관제합니다.

## 2. 핵심 거버넌스 자산 (Core Assets)

| 구분 | 경로 (Path) | 설명 (Description) |
| :--- | :--- | :--- |
| **인사 관리** | [`personnel/`](./personnel/) | 11인 가재의 인사 카드 및 평가 기록 |
| **무결성 감사** | [`personnel/audit/`](./personnel/audit/) | 날짜별 시스템 무결성 검수 로그 (AUDIT) |
| **실행 자동화(MVP)** | [`monitoring/EXECUTION_AUTOMATION_MVP.md`](./monitoring/EXECUTION_AUTOMATION_MVP.md) | Gate 체크/증빙 강제/실패 에스컬레이션 운영 가이드 |
| **실행형 크론 Guard 정책** | [`monitoring/EXECUTION_CRON_GUARD_POLICY.md`](./monitoring/EXECUTION_CRON_GUARD_POLICY.md) | 실행형 자동화 잡의 Guard 경유 의무 규정 |
| **로컬 Guard 감사/상태감시** | [`monitoring/local_guard_audit.py`](./monitoring/local_guard_audit.py), [`monitoring/gate_status_watch.py`](./monitoring/gate_status_watch.py) | cron API 호출 없이 로컬 상태 기반 감시 |
| **운영 Runbook** | [`monitoring/OPERATIONS_RUNBOOK.md`](./monitoring/OPERATIONS_RUNBOOK.md) | 장애/재시도/비활성화/복구 표준 절차 |
| **자율성 검증 체크리스트** | [`monitoring/AUTONOMY_VALIDATION_CHECKLIST.md`](./monitoring/AUTONOMY_VALIDATION_CHECKLIST.md) | NO_REPLY/예외보고 체계 정량 검증 템플릿 |
| **공정 인덱스** | [하단 현황판](#-전사-공정-승인-현황) | 전사 피쳐별 승인 관문(GATE.md) 직결 |

---

## 🚦 전사 공정 승인 현황 (Approval Status)

| 프로젝트명 | 현재 단계 | CEO 승인 | 바로가기 |
| :--- | :--- | :--- | :--- |
| **[GAJAE-BIP] Service-MVP v1.7** | 5. RFE/RFK | ⏳ WAITING | [GATE.md](../business/feature/gajae-bip-service/pm/GATE.md) |

---
**지휘 지침:** "질서는 지능의 힘이며, 인덱스는 성역의 규율이다." ⚔️🚀
