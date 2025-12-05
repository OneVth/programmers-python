"""
프로그래머스 Lv0 #120816 - 피자 나눠 먹기 (3)
https://school.programmers.co.kr/learn/courses/30/lessons/120816

[문제]
피자 한 판에 slice 조각. n명이 최소 한 조각 이상 먹으려면 몇 판 필요한지 반환

[제한]
- 2 ≤ slice ≤ 10
- 1 ≤ n ≤ 100
"""
from math import ceil


def solution_v1(slice: int, n: int) -> int:
    """
    [Approach] 브루트포스 - 조각 수가 n 이상이 될 때까지
    [Time] O(n/slice)  [Space] O(1)
    """
    answer = 1
    total = slice * answer
    while total < n:
        answer += 1
        total = slice * answer
    return answer


def solution_v2(slice: int, n: int) -> int:
    """
    [Approach] math.ceil 사용
    [Time] O(1)  [Space] O(1)
    ⚠️ 실수 연산 포함 (부동소수점 오차 가능)
    """
    return ceil(n / slice)


def solution_v3(slice: int, n: int) -> int:
    """
    [Approach] (n+k-1)//k 올림 공식
    [Time] O(1)  [Space] O(1)
    ✅ 정수 연산만 사용
    """
    return (n + slice - 1) // slice


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v3
