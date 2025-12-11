"""
프로그래머스 Lv0 #120815 - 피자 나눠 먹기 (2)
https://school.programmers.co.kr/learn/courses/30/lessons/120815

[복습] 1차 - 2025-12-10

[문제]
피자 한 판에 6조각. n명이 피자를 남기지 않고 똑같이 나눠먹으려면
최소 몇 판 필요한지 반환

[제한]
- 1 ≤ n ≤ 100
"""


from math import gcd, lcm


def solution_v1(n: int) -> int:
    """
    [Approach] LCM 내장 함수 활용 (Python 3.9+)
    [Time] O(log(min(6, n)))  [Space] O(1)
    ✅ 가장 간결하고 직관적
    """
    return lcm(6, n) // 6


def solution_v2(n: int) -> int:
    """
    [Approach] LCM = a*b/GCD 공식 활용
    [Time] O(log(min(6, n)))  [Space] O(1)
    ✅ Python 3.8 이하 호환, 수학 원리 직접 적용
    """
    return 6 * n // gcd(6, n) // 6


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
