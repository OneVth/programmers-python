"""
프로그래머스 Lv0 #181850 - 정수 부분
https://school.programmers.co.kr/learn/courses/30/lessons/181850

[문제]
실수 flo가 매개 변수로 주어질 때,
flo의 정수 부분을 return하도록 solution 함수를 완성해주세요.

[제한]
- 0 ≤ flo ≤ 100
"""


def solution_v1(flo: float) -> int:
    """
    [Approach] int()로 실수의 정수 부분 추출 (0 방향 버림)
    [Time] O(1)
    [Space] O(1)
    """
    return int(flo)


solution = solution_v1
