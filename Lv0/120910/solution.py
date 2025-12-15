"""
프로그래머스 Lv0 #120910 - 세균 증식
https://school.programmers.co.kr/learn/courses/30/lessons/120910

[문제]
어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과
경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 10
- 1 ≤ t ≤ 15
"""


def solution_v1(n: int, t: int) -> int:
    """
    [Approach] 거듭제곱 연산 - n × 2^t
    [Time] O(log t)  [Space] O(1)
    """
    return n * (2**t)


def solution_v2(n: int, t: int) -> int:
    """
    [Approach] 비트 시프트 - n을 왼쪽으로 t비트 이동 (= n × 2^t)
    [Time] O(1)  [Space] O(1)
    """
    return n << t


solution = solution_v1
