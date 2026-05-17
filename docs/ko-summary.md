# Safe Code Agent 한국어 정리

Safe Code Agent는 AI 코딩 에이전트가 코드를 더 안전하게 수정하도록 돕는 코딩 스킬입니다.

핵심 원칙은 간단합니다.

```text
목표 이해 -> 코드 조사 -> 실행 흐름 시뮬레이션 -> 최소 수정 -> 검증 -> 불확실성 보고
```

이 스킬은 AI가 코드를 너무 많이 고치거나, 원인을 확인하지 않은 채 구현하거나, 검증 없이 완료했다고 말하는 문제를 줄이기 위해 설계됐습니다.

## 핵심 설명

Safe Code Agent는 AI 코딩 에이전트에게 다음 행동을 강제합니다.

- 수정 전에 관련 코드를 먼저 읽기
- 불필요한 리팩터링이나 과한 변경 줄이기
- 요청된 동작에 필요한 최소 수정만 하기
- 검증 결과를 명확히 구분하기
- 확인하지 못한 부분은 불확실성으로 남기기
- 위험한 작업 승인 전에는 사전 설계 보고를 먼저 하기

## 언제 쓰는가

다음 작업에 적합합니다.

- 위험한 리팩터링
- 여러 파일에 걸친 변경
- 검증이 중요한 작업
- 계약, fallback, schema, precedence 로직
- agentic coding workflow
- 실수 비용이 큰 코드 변경

반대로 아주 작은 작업에는 무겁게 느껴질 수 있습니다.

- 한 줄 수정
- 단순 오타 수정
- 버리는 실험 코드
- 검증보다 속도가 더 중요한 작업

이런 경우에는 더 가벼운 기본 프롬프트를 쓰는 편이 낫습니다.

## 빠른 사용법

1. `skills/safe-code-agent/SKILL.md`를 코딩 에이전트 설정에 추가합니다.
2. 필요하면 `AGENTS.md`의 가벼운 기본 규칙을 프로젝트 지침에 넣습니다.
3. 에이전트에게 코드 수정 전에 먼저 코드를 조사하라고 요구합니다.
4. 위험한 작업 전에는 pre-approval plan을 요구합니다.
5. 변경 후에는 검증 결과와 남은 불확실성을 보고하게 합니다.

예시 대상:

- `CLAUDE.md`
- project `AGENTS.md`
- agent system prompt
- custom coding workflow prompt

## 포지셔닝

Safe Code Agent는 모든 코딩 프롬프트를 대체하려는 스킬이 아닙니다.

안전성, 검증, 변경 범위 통제가 중요한 상황을 위한 스킬입니다.

| 상황 | 추천 전략 |
|---|---|
| 일상적인 코딩 | Karpathy-style lightweight rules |
| 위험한 리팩터링 | Safe Code Agent |
| 여러 파일 변경 | Safe Code Agent |
| 요구사항이 불명확함 | Grill Me-style questioning |
| 구현 전 설계 검토 | Grill Me-style questioning |
| 최종 검증 | Safe Code Agent |

## Pre-Approval Planning

v0.2.2에서 추가된 핵심 기능입니다.

AI 에이전트가 위험한 작업을 진행하기 전에 단순히 "진행할까요?"라고 묻는 대신, 승인 전에 다음 내용을 먼저 설명해야 합니다.

- Task Contract
- 선택한 mode와 gate
- 조사할 파일 또는 실행 경로
- 예상 변경 지점
- 변경하지 않을 범위
- 왜 승인이 필요한지
- 승인 후 어떻게 검증할지

승인 질문은 다음처럼 구체적이어야 합니다.

```text
Approval needed: <specific action>
Scope: <files/commands/effects>
Risk: <main risk>
Verification after approval: <commands/checks>
Proceed?
```

즉, 사용자가 구현 세부를 잘 몰라도 AI가 먼저 승인 범위와 리스크를 설명해야 합니다.

## 왜 필요한가

AI 코딩 에이전트의 실패는 자주 같은 패턴으로 나타납니다.

- 목표를 이해하기 전에 코드부터 수정함
- 필요한 것보다 너무 많이 고침
- 원인을 확인하지 않고 추측함
- 관련 코드를 충분히 조사하지 않음
- 실제 검증 없이 테스트가 통과했다고 말함
- 불확실한 부분을 숨김

Safe Code Agent는 이런 실패 가능성을 줄이기 위한 작업 루프입니다.

## 강제하는 것

- 관련 코드 조사 후 수정
- 위험한 작업 전 pre-approval plan 출력
- 기존 스타일과 아키텍처 보존
- 최소 안전 수정 선택
- 추론과 검증 결과 분리
- 명시적인 검증 라벨 사용
- 남은 불확실성 보고

## 고급 문서

고급 문서는 매번 읽는 문서가 아닙니다.

특정 위험 신호가 있을 때만 사용합니다.

| 상황 | 사용할 문서 |
|---|---|
| 테스트나 빌드 통과를 주장하지만 출력이 없음 | `docs/advanced/runtime-enforcement.md` |
| 프로토타입 코드가 핵심 로직이 되기 시작함 | `docs/advanced/prototype-to-production.md` |
| 보고서는 깔끔하지만 근거가 약함 | `docs/advanced/structured-hallucination.md` |
| auth, payment, data deletion, migration, public API, persistence를 건드림 | `docs/advanced/runtime-enforcement.md` 검토 |

## 주의

이 저장소는 코딩 에이전트를 위한 prompt/skill 설계입니다.

런타임 강제 시스템이 아니고, 벤치마크 결과도 아닙니다.

코드의 실제 안전성은 여전히 코드 리뷰, 테스트, 실행 검증으로 확인해야 합니다.

## License

MIT
