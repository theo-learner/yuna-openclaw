# Execution Cron Guard Policy

목적: 실행형 자동화 잡은 반드시 Guard 경유로 실행한다.

## 필수 규칙
- 배포/변경/자동 실행 커맨드는 직접 실행 금지
- 아래 래퍼를 통해서만 실행:

```bash
bash docs/governance/monitoring/run_guarded_action.sh \
  --gate docs/business/feature/gajae-bip-service/pm/GATE.md \
  --evidence docs/task/attendant.md \
  -- <actual command>
```

## 예시 (금지 / 허용)
- 금지: `cd repo && <actual command>`
- 허용: 위 guarded wrapper 경유 실행

## 운영 포인트
- 승인 대기(BLOCKED)는 정책상 정상 차단 상태
- 런타임 오류만 에러로 간주
- 회사 채널에는 에러 원문 미출력, Theo DM으로만 에스컬레이션
