"""
프로그래머스 Lv0 #120840 - 구슬을 나누는 경우의 수
https://school.programmers.co.kr/learn/courses/30/lessons/120840

[문제]
머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 구슬은 모두 다르게 생겼습니다.
머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share가
매개변수로 주어질 때, balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든
경우의 수를 return 하는 solution 함수를 완성해주세요.

[제한]
- 1 ≤ balls ≤ 30
- 1 ≤ share ≤ 30
- 구슬을 고르는 순서는 고려하지 않습니다.
- share ≤ balls

[힌트]
서로 다른 n개 중 m개를 뽑는 경우의 수 공식:
nCm = n! / (m! * (n-m)!)
"""

from math import comb, factorial


def solution_v1(balls: int, share: int) -> int:
    """
    [Approach] math.comb 내장 함수
    [Time] O(min(r, n-r))  [Space] O(1)
    ✅ Python 3.8+ 최적 방법, 내부 최적화 적용
    """
    return comb(balls, share)


def solution_v2(balls: int, share: int) -> int:
    """
    [Approach] math.factorial로 공식 직접 계산
    [Time] O(n)  [Space] O(1)
    ⚠️ 큰 수 계산 3번 (n!, r!, (n-r)!)
    """
    return factorial(balls) // (factorial(balls - share) * factorial(share))


def solution_v3(balls: int, share: int) -> int:
    """
    [Approach] 반복문으로 팩토리얼 직접 구현
    [Time] O(n)  [Space] O(1)
    ✅ 재귀 없이 안전하게 구현
    """

    def my_factorial(n: int) -> int:
        if n <= 1:
            return 1

        result = 1
        for i in range(1, n + 1):
            result *= i

        return result

    return my_factorial(balls) // (my_factorial(balls - share) * my_factorial(share))


solution = solution_v3
