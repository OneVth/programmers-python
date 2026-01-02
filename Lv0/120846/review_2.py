"""
프로그래머스 Lv0 #120846 - 합성수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/120846

[복습] 2차 - 2026-01-02

[문제]
약수의 개수가 세 개 이상인 수를 합성수라고 합니다.
자연수 n이 매개변수로 주어질 때 n 이하의 합성수의 개수를 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 100
"""


def solution_v1(n: int) -> int:
    """
    [Approach] 소수 카운팅 후 빼기 - √i까지 나눠보며 소수 판별
    [Time] O(n√n)  [Space] O(1)
    ✅ 합성수 = 전체(n) - 소수 - 1 (1은 소수도 합성수도 아님)
    """
    primes = 1  # 2는 소수
    for i in range(3, n + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            primes += 1

    return n - primes - 1


def solution_v2(n: int) -> int:
    """
    [Approach] 에라토스테네스 체 - 소수의 배수를 모두 제거
    [Time] O(n log log n)  [Space] O(n)
    ✅ 범위 내 여러 소수 판별 시 최적
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return n - sum(is_prime) - 1


# 기본 솔루션 지정
solution = solution_v2
