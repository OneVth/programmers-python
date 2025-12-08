"""
문제: 소인수분해
난이도: Lv0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120852

설명:
소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다.
예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다.
따라서 12의 소인수는 2와 3입니다.
자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을
return하도록 solution 함수를 완성해주세요.

제한사항:
- 2 ≤ n ≤ 10,000
"""


def solution_v1(n: int) -> list[int]:
    """
    [Approach] 에라토스테네스의 체 + 약수 체크
    [Time] O(n log log n) - 체 생성이 지배적
    [Space] O(n) - 소수 테이블 저장
    """
    prime_tab = [True] * (n + 1)
    prime_tab[0] = prime_tab[1] = False
    prime_factors = []

    for i in range(2, n + 1):
        if prime_tab[i]:
            j = 2
            while i * j <= n:
                prime_tab[i * j] = False
                j += 1

            if n % i == 0:
                prime_factors.append(i)

    return prime_factors


def solution_v2(n: int) -> list[int]:
    """
    [Approach] 직접 분해 - 2부터 √n까지 나눠보기
    [Time] O(√n) - 최악의 경우 √n까지 순회
    [Space] O(log n) - 소인수 개수 (최대 log n개)
    """
    factors = []
    d = 2

    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1

    if n > 1:
        factors.append(n)

    return factors


solution = solution_v2
