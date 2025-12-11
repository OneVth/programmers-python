"""
프로그래머스 Lv0 #120846 - 합성수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/120846

[복습] 1차 - 2025-12-10

[문제]
약수의 개수가 세 개 이상인 수를 합성수라고 합니다.
자연수 n이 매개변수로 주어질 때 n 이하의 합성수의 개수를 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 100
"""


def solution_v1(n: int) -> int:
    """
    [Approach] 소수 개수 세고 빼기 (√i 최적화)
    [Time] O(n√n)  [Space] O(1)
    ⚠️ 버그: range(4, n) → range(4, n+1), int(n**0.5) → int(i**0.5)
    """
    if n <= 1:
        return 0

    primes = 2  # 2, 3
    for i in range(4, n + 1):  # n도 포함해야 함
        for j in range(2, int(i**0.5) + 1):  # i의 제곱근까지 확인
            if i % j == 0:
                break
        else:
            primes += 1

    return n - primes - 1


def solution_v2(n: int) -> int:
    """
    [Approach] 에라토스테네스의 체
    [Time] O(n log log n)  [Space] O(n)
    ✅ 대량의 소수 판별에 가장 효율적
    """
    table = [True] * (n + 1)
    table[0] = table[1] = False

    for i in range(2, int(n**0.5) + 1):  # √n까지만 확인하면 충분
        if table[i]:
            for j in range(i * i, n + 1, i):  # i*i부터 시작 (최적화)
                table[j] = False

    return n - sum(table) - 1


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
