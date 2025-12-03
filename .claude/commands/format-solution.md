# Solution Formatter

주어진 문제의 solution.py 파일을 표준 레이아웃으로 정리합니다.

## 대상 경로
$ARGUMENTS

## 작업 내용

1. **testcases.json**에서 문제 정보 추출 (problem_id, title)

2. **solution.py** 파일을 아래 레이아웃으로 정리:

```python
"""
프로그래머스 Lv{레벨} #{문제번호} - {제목}
https://school.programmers.co.kr/learn/courses/30/lessons/{문제번호}

[문제]
{문제 설명}

[제한]
- {제한조건들}
"""


def solution_v1(매개변수: 타입) -> 반환타입:
    """
    [Approach] {접근 방식}
    [Time] O(?)  [Space] O(?)
    """
    # 구현


def solution_v2(매개변수: 타입) -> 반환타입:
    """
    [Approach] {다른 접근 방식}
    [Time] O(?)  [Space] O(?)
    """
    # 구현


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
```

## 체크리스트

- [ ] 모듈 docstring에 문제 요약 추가
- [ ] 모든 함수에 타입 힌트 적용
- [ ] 각 솔루션의 시간/공간 복잡도 분석
- [ ] solution alias 설정
- [ ] runner.py로 테스트 실행하여 검증
