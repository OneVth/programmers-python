"""
프로그래머스 Lv0 #120806 - 두 수의 나눗셈
https://school.programmers.co.kr/learn/courses/30/lessons/120806

[문제]
정수 num1과 num2가 매개변수로 주어질 때,
num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 반환

[제한]
- 0 < num1 ≤ 100
- 0 < num2 ≤ 100
"""


def solution_v1(num1: int, num2: int) -> int:
    """
    [Approach] 실수 나눗셈 후 1000 곱하고 int 변환
    [Time] O(1)  [Space] O(1)
    """
    return int(num1 / num2 * 1000)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
