"""
프로그래머스 Lv0 #120808 - 분수의 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/120808

[문제]
첫 번째 분수 numer1/denom1과 두 번째 분수 numer2/denom2를 더한 값을
기약 분수로 나타내어 [분자, 분모] 형태로 반환

[제한]
- 0 < numer1, denom1, numer2, denom2 < 1,000
"""
from math import gcd
from fractions import Fraction


def solution_v1(numer1: int, denom1: int, numer2: int, denom2: int) -> list[int]:
    """
    [Approach] 브루트포스 공약수 탐색
    [Time] O(min(numer, denom))  [Space] O(n)
    ⚠️ 비효율적 - 모든 약수를 리스트에 저장
    """
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    divisors = []
    for i in range(1, min(numer, denom) + 1):
        if numer % i == 0 and denom % i == 0:
            divisors.append(i)

    if divisors:
        numer //= divisors[-1]
        denom //= divisors[-1]

    return [numer, denom]


def solution_v2(numer1: int, denom1: int, numer2: int, denom2: int) -> list[int]:
    """
    [Approach] GCD로 기약분수 변환
    [Time] O(log(min(numer, denom)))  [Space] O(1)
    ✅ 효율적
    """
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2

    g = gcd(numer, denom)
    numer //= g
    denom //= g

    return [numer, denom]


def solution_v3(numer1: int, denom1: int, numer2: int, denom2: int) -> list[int]:
    """
    [Approach] fractions.Fraction 내장 모듈
    [Time] O(log(min(numer, denom)))  [Space] O(1)
    ✅ 가장 Pythonic - 자동으로 기약분수 처리
    """
    answer = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    return [answer.numerator, answer.denominator]


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v3
