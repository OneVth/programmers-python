"""
프로그래머스 Lv0 #120815 - 피자 나눠 먹기 (2)
https://school.programmers.co.kr/learn/courses/30/lessons/120815

[문제]
피자 한 판에 6조각. n명이 피자를 남기지 않고 똑같이 나눠먹으려면
최소 몇 판 필요한지 반환

[제한]
- 1 ≤ n ≤ 100
"""
from math import gcd, lcm


def solution_v1(n: int) -> int:
    """
    [Approach] 브루트포스 - 조각 수가 n으로 나눠지는지 확인
    [Time] O(n)  [Space] O(1)
    """
    answer = 1
    slices = 6 * answer

    while slices % n != 0:
        answer += 1
        slices = 6 * answer

    return answer


def solution_v2(n: int) -> int:
    """
    [Approach] LCM(최소공배수) 활용
    [Time] O(log(min(n, 6)))  [Space] O(1)
    ✅ 수학적 풀이 - LCM(n, 6) / 6 = 필요한 판 수
    [Original] (n * 6) // gcd(n, 6) // 6
    """
    return lcm(n, 6) // 6


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
