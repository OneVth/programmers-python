"""
프로그래머스 Lv0 #120803 - 두 수의 차 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120803

[문제]
정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 반환

[제한]
- -50,000 ≤ num1 ≤ 50,000
- -50,000 ≤ num2 ≤ 50,000
"""


def solution_v1(num1: int, num2: int) -> int:
    """
    [Approach] 단순 뺄셈
    [Time] O(1)  [Space] O(1)
    """
    return num1 - num2


def solution_v2(num1: int, num2: int) -> int:
    """
    [Approach] 람다 스타일 (인라인)
    [Time] O(1)  [Space] O(1)
    [Original] lambda num1, num2: num1 - num2
    """
    return num1 - num2


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
