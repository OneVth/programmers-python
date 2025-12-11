"""
프로그래머스 Lv0 #120848 - 팩토리얼
https://school.programmers.co.kr/learn/courses/30/lessons/120848

[복습] 1차 - 2025-12-10

[문제]
i 팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다.
예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다.
정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록
solution 함수를 완성해주세요.
- i! ≤ n

[제한]
- 0 < n ≤ 3,628,800
"""

from math import factorial


def solution_v1(n: int) -> int:
    """
    [Approach] math.factorial + while 루프
    [Time] O(i² log i)  [Space] O(1)
    ⚠️ 매번 팩토리얼 재계산 (비효율)
    """
    i = 0
    while factorial(i) <= n:
        i += 1

    return i - 1


def solution_v2(n: int) -> int:
    """
    [Approach] 누적 곱으로 팩토리얼 계산
    [Time] O(i)  [Space] O(1)
    ✅ 이전 결과 재활용하여 효율적
    """
    i, fact = 1, 1
    while fact <= n:
        i += 1
        fact *= i

    return i - 1


def solution_v3(n: int) -> int:
    """
    [Approach] 팩토리얼 테이블 + 이분탐색
    [Time] O(log 11) = O(1)  [Space] O(1)
    ✅ 테이블 미리 계산, 탐색은 이분탐색
    """
    from bisect import bisect_right

    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    return bisect_right(factorials, n) - 1


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
