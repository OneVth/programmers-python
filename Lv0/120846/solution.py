"""
프로그래머스 Lv0 #120846 - 합성수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/120846

[문제]
약수의 개수가 세 개 이상인 수를 합성수라고 합니다.
자연수 n이 매개변수로 주어질 때 n 이하의 합성수의 개수를 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 100
"""


def solution_v1(n: int) -> int:
    """
    [Approach] 소수 개수 세고 빼기 (√n 최적화)
    [Time] O(n√n)  [Space] O(1)
    ✅ 합성수 = 전체 - 소수 - 1
    """
    primes = 0
    for i in range(2, n + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            primes += 1

    return n - primes - 1  # 1은 합성수가 아님


def solution_v2(n: int) -> int:
    """
    [Approach] 소수 개수 세고 빼기 (브루트포스)
    [Time] O(n²)  [Space] O(1)
    """
    primes = 0
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes += 1

    return n - primes - 1


def solution_v3(n: int) -> int:
    """
    [Approach] 약수 개수 직접 세기
    [Time] O(n²)  [Space] O(1)
    ⚠️ 직관적이지만 비효율적
    """

    def count_divisors(x: int) -> int:
        return sum(1 for i in range(1, x + 1) if x % i == 0)

    return sum(1 for i in range(1, n + 1) if count_divisors(i) > 2)


def solution_v4(n: int) -> int:
    """
    [Approach] 에라토스테네스의 체
    [Time] O(n log log n)  [Space] O(n)
    ✅ 대량의 소수 판별에 가장 효율적
    """
    if n < 4:
        return 0

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    prime_count = sum(is_prime)
    return n - prime_count - 1  # 전체 - 소수 - 1


solution = solution_v4
