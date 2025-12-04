"""
프로그래머스 Lv0 #120814 - 피자 나눠 먹기 (1)
https://school.programmers.co.kr/learn/courses/30/lessons/120814

[문제]
피자 한 판에 7조각. n명이 최소 한 조각 이상 먹으려면 몇 판 필요한지 반환

[제한]
- 1 ≤ n ≤ 100
"""
from math import ceil


def solution_v1(n: int) -> int:
    """
    [Approach] divmod로 몫/나머지 분리
    [Time] O(1)  [Space] O(1)
    """
    q, r = divmod(n, 7)
    return q if r == 0 else q + 1


def solution_v2(n: int) -> int:
    """
    [Approach] (n-1)//k + 1 올림 공식
    [Time] O(1)  [Space] O(1)
    ✅ 정수 연산만 사용
    """
    return (n - 1) // 7 + 1


def solution_v3(n: int) -> int:
    """
    [Approach] (n+k-1)//k 올림 공식
    [Time] O(1)  [Space] O(1)
    ✅ 정수 연산만 사용 (다른 형태)
    """
    return (n + 6) // 7


def solution_v4(n: int) -> int:
    """
    [Approach] math.ceil 사용
    [Time] O(1)  [Space] O(1)
    ⚠️ 실수 연산 포함 (부동소수점 오차 가능)
    """
    return ceil(n / 7)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
