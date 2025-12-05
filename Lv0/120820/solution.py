"""
프로그래머스 Lv0 #120820 - 나이 출력
https://school.programmers.co.kr/learn/courses/30/lessons/120820

[문제]
머쓱이는 선생님이 몇 년도에 태어났는지 궁금해졌습니다.
2022년 기준 선생님의 나이 age가 주어질 때,
선생님의 출생 연도를 return 하는 solution 함수를 완성해주세요.

[제한]
- 0 < age ≤ 120
- 나이는 태어난 연도에 1살이며 매년 1월 1일마다 1살씩 증가합니다.
"""


def solution_v1(age: int) -> int:
    """
    [Approach] 한국식 나이 계산: 2022년 기준 - 나이 + 1
    [Time] O(1)  [Space] O(1)
    """
    return 2022 - age + 1

solution = solution_v1
