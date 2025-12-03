"""
프로그래머스 Lv0 #120804 - 두 수의 곱 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120804

[문제]
정수 num1, num2가 매개변수로 주어질 때, num1과 num2를 곱한 값을 반환

[제한]
- 0 ≤ num1 ≤ 100
- 0 ≤ num2 ≤ 100
"""


def solution_v1(num1: int, num2: int) -> int:
    """
    [Approach] 단순 곱셈 연산자 *
    [Time] O(1)  [Space] O(1)
    """
    return num1 * num2


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
