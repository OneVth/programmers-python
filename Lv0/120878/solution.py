"""
프로그래머스 Lv0 #120878 - 유한소수 판별하기
https://school.programmers.co.kr/learn/courses/30/lessons/120878

[문제]
소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다.
분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다.
유한소수가 되기 위한 분수의 조건은 다음과 같습니다.
- 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.

두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을,
무한소수라면 2를 return하도록 solution 함수를 완성해주세요.

[제한]
- a, b는 정수
- 0 < a ≤ 1,000
- 0 < b ≤ 1,000

[힌트]
- 분자와 분모의 최대공약수로 약분하면 기약분수를 만들 수 있습니다.
- 정수도 유한소수로 분류합니다.
"""


def solution_v1(a: int, b: int) -> int:
    """
    [Approach] Fraction 라이브러리 활용 - 자동으로 기약분수 분모 추출 후
               2와 5로 나누어 떨어지는지 확인
    [Time] O(log b) - 분모를 2, 5로 나누는 반복
    [Space] O(1)
    """
    from fractions import Fraction

    denom = Fraction(a, b).denominator
    while denom % 5 == 0:
        denom //= 5
    while denom % 2 == 0:
        denom //= 2

    if denom == 1:
        return 1

    return 2


def solution_v2(a: int, b: int) -> int:
    """
    [Approach] math.gcd 활용 - 직접 기약분수 분모 계산 후
               2와 5로 나누어 떨어지는지 확인 (v1보다 간결)
    [Time] O(log b) - gcd 계산 + 분모 나누기 반복
    [Space] O(1)
    """
    from math import gcd

    b //= gcd(a, b)
    while b % 5 == 0:
        b //= 5
    while b % 2 == 0:
        b //= 2

    return 1 if b == 1 else 2


solution = solution_v2
