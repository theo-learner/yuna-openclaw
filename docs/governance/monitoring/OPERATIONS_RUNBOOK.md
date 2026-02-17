# Governance Automation Operations Runbook

목적: 가재 컴퍼니 자동화 운영에서 이상 상황이 발생했을 때, 재시도/비활성화/에스컬레이션을 표준화한다.

## 1) 적용 범위
- Guard 점검 계열 크론
  - `가재 Gate 상태 변화 감시 (30분)`
  - `가재 로컬 Guard 감사 (6시간)`
  - `가재 운영 Guard 일일 요약 (20:30)`
- 실행형 자동화 잡(배포/반영/데이터 동기화 등)

---

## 2) 상태 분류

### A. 정상 상태 (NO_ACTION)
- `GUARD_OK`, `LOCAL_GUARD_OK`, `NO_CHANGE`
- 조치: 없음 (`NO_REPLY` 유지)

### B. 운영 Finding (ACTION_REQUIRED)
- `GUARD_FINDINGS`, `LOCAL_GUARD_FINDINGS`, `BLOCKED_STATE`
- 조치:
  1. Theo DM으로만 보고
  2. 회사 채널 전송 금지
  3. 동일 finding 세트는 중복 억제

### C. 런타임 오류 (INCIDENT)
- `RUNTIME_ERROR`, 스크립트 실행 실패, 파일 없음, 파싱 실패
- 조치:
  1. 즉시 Theo DM 보고 (원인 1줄 + 영향 1줄)
  2. 동일 오류 3회 연속 시 해당 크론 임시 비활성화
  3. 원인 수정 후 수동 1회 검증 실행

---

## 3) 표준 대응 절차 (SOP)

### [S1] 재시도 (Retry)
- 조건: 일시적 실패(타임아웃, 외부 의존)
- 절차:
  1. 동일 명령 1회 수동 재실행
  2. 성공 시 상태 파일 갱신 후 종료
  3. 실패 시 [S2]로 전환

### [S2] 격리/비활성화 (Disable)
- 조건: 동일 런타임 오류 연속 3회 또는 노이즈성 장애 반복
- 절차:
  1. 문제 잡 `enabled=false`
  2. Theo DM으로 비활성화 사실/사유 보고
  3. 대체 루틴(로컬 검사 등)으로 임시 운영

### [S3] 복구 (Recovery)
- 조건: 스크립트/설정 수정 완료
- 절차:
  1. 수동 검증 1회 (`python3 ...`)
  2. 정상 결과 확인
  3. 크론 재활성화
  4. Theo DM으로 복구 완료 보고

---

## 4) 실행형 잡 Guard 강제 규칙

- 실행형 자동화 명령은 아래 래퍼 경유가 원칙:

```bash
bash docs/governance/monitoring/run_guarded_action.sh \
  --gate docs/business/feature/gajae-bip-service/pm/GATE.md \
  --evidence docs/task/attendant.md \
  -- <actual command>
```

- `BLOCKED`는 정책상 정상 차단이며 incident로 보지 않는다.
- `RUNTIME_ERROR`만 incident로 분류한다.

---

## 5) 알림 정책

- 기본: Theo DM only
- 회사 채널: 성공/요약 정보만 허용
- 금지: 에러 원문, 스택트레이스, 민감정보(API key/token/password)

---

## 6) 일일 운영 점검 체크리스트

1. Guard 일일 요약 수신 여부 확인
2. Gate 상태 변경 알림 유무 확인
3. Local Guard findings 잔존 여부 확인
4. 비활성화된 잡 존재 시 복구 계획 업데이트

---

## 7) 변경 이력
- 2026-02-17: 초기 Runbook 작성 (Governance Guard 운영 표준화)
