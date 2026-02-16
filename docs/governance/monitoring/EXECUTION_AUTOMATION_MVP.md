# Execution Automation MVP (Priority A/B/C)

목적: 문서 규칙(헌법/게이트/보고 규정)을 실행 규칙으로 강제 연결한다.

## A) Gate Engine (Pre-Action Check)

- 파일: `gate_precheck.py`
- 역할: `GATE.md`에서 **INPROGRESS + CEO WAITING** 상태를 차단
- 사용 예시:

```bash
python3 docs/governance/monitoring/gate_precheck.py \
  --gate docs/business/feature/gajae-bip-service/pm/GATE.md
```

- 결과:
  - `PASS` => 다음 액션 진행 가능
  - `BLOCKED` => CEO 승인 전까지 실행 중단

---

## B) Evidence Enforcer (Completion Proof)

- 파일: `evidence_check.py`
- 역할: 완료 보고서/태스크 문서에 GitHub Commit/PR URL 증빙이 있는지 검사
- 사용 예시:

```bash
python3 docs/governance/monitoring/evidence_check.py --file docs/task/attendant.md
```

- 결과:
  - `PASS` => 증빙 충족
  - `FAIL` => 증빙 누락, 완료 처리 금지

---

## C) Failure Escalation & Channel Hygiene

운영 규칙(이미 적용):
- 회사 채널 발행 잡은 에러 발생 시 `NO_REPLY`(에러 원문 비노출)
- 실패 상세는 CEO DM으로만 보고

권장 추가:
1. 회사 채널 크론 프롬프트에 `오류 원문 출력 금지` 고정 문구 유지
2. 실패 시 `message.send(channel=telegram,target=1266746900)`로 별도 통지
3. 같은 실패 세트 중복 알림 억제(state file)

---

## 즉시 적용 순서 (10분)

1. Gate check 실행 (차단 여부 확인)
2. Evidence check 실행 (증빙 누락 방지)
3. PASS일 때만 배포/공지/자동화 명령 실행

예시 래퍼:

```bash
python3 docs/governance/monitoring/gate_precheck.py --gate <GATE.md> && \
python3 docs/governance/monitoring/evidence_check.py --file <REPORT.md> && \
<actual action command>
```
