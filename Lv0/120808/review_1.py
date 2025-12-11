"""
프로그래머스 Lv0 #120808 - 분수의 덧셈
https://school.programmers.co.kr/learn/courses/30/lessons/120808

[복습] 1차 - 2025-12-10

[문제]
첫 번째 분수 numer1/denom1과 두 번째 분수 numer2/denom2를 더한 값을
기약 분수로 나타내어 [분자, 분모] 형태로 반환

[제한]
- 0 < numer1, denom1, numer2, denom2 < 1,000
"""


from fractions import Fraction
from math import gcd


def solution_v1(numer1: int, denom1: int, numer2: int, denom2: int) -> list[int]:
    """
    [Approach] fractions.Fraction 내장 모듈 활용
    [Time] O(log(min(numer, denom)))  [Space] O(1)
    ✅ 가장 Pythonic - 자동으로 기약분수 처리
    """
    answer = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    return [answer.numerator, answer.denominator]


def solution_v2(numer1: int, denom1: int, numer2: int, denom2: int) -> list[int]:
    """
    [Approach] 통분 후 GCD로 기약분수 변환
    [Time] O(log(min(numer, denom)))  [Space] O(1)
    ✅ 수학적 원리 직접 구현
    """
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    g = gcd(numer, denom)

    return [numer // g, denom // g]

def solution_v3(numer1: int, denom1: int, numer2: int, denom2: int) -> list[int]:
    """
    [Approach] 유클리드 호제법 직접 구현
    [Time] O(log(min(numer, denom)))  [Space] O(1)
    ✅ 라이브러리 없이 GCD 원리 구현 - 면접 대비용
    """
    def my_gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    g = my_gcd(numer, denom)

    return [numer // g, denom // g]


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v3