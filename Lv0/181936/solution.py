"""
프로그래머스 Lv0 #181936 - 공배수
https://school.programmers.co.kr/learn/courses/30/lessons/181936

[문제]
정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을
아니라면 0을 return하도록 solution 함수를 완성해주세요.

[제한]
- 10 ≤ number ≤ 100
- 2 ≤ n, m < 10
"""


def solution_v1(number: int, n: int, m: int) -> int:
    """
    [Approach] 나머지 연산으로 두 배수 조건을 and로 검사 후 삼항 연산자로 반환
    [Time] O(1)  [Space] O(1)
    """
    return 1 if number % n == 0 and number % m == 0 else 0


def solution_v2(number: int, n: int, m: int) -> int:
    """
    [Approach] bool → int 변환을 이용해 조건식 결과를 직접 반환
    [Time] O(1)  [Space] O(1)
    Note: & 연산자는 == 보다 우선순위가 높으므로 괄호 필수
    """
    return int((number % n == 0) & (number % m == 0))


def solution_v3(number: int, n: int, m: int) -> int:
    """
    [Approach] n과 m의 LCM을 구해 한 번의 나머지 연산으로 공배수 판별
              lcm(n, m)의 배수 ⟺ n의 배수이면서 m의 배수
    [Time] O(log(min(n,m)))  [Space] O(1)  ← gcd 계산 비용
    """
    from math import lcm
    return int(number % lcm(n, m) == 0)


solution = solution_v1