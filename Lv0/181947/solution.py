"""
프로그래머스 Lv0 #181947 - 덧셈식 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/181947

[문제]
두 정수 a, b 가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.
a + b = c

[제한]
- 1 ≤ a, b ≤ 100
"""


def solution_v1(a: int, b: int) -> str:
    """
    [Approach] f-string으로 a + b = c 형식 문자열 포맷
    [Time] O(1)  [Space] O(1)
    """
    return f"{a} + {b} = {a + b}"


solution = solution_v1
