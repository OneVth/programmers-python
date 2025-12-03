"""
프로그래머스 Lv0 #120802 - 두 수의 합 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120802

[문제]
정수 num1과 num2가 주어질 때, num1과 num2의 합을 반환

[제한]
- -50,000 ≤ num1 ≤ 50,000
- -50,000 ≤ num2 ≤ 50,000
"""


def solution_v1(num1: int, num2: int) -> int:
    """
    [Approach] 단순 덧셈
    [Time] O(1)  [Space] O(1)
    """
    return num1 + num2


def solution_v2(*args: int) -> int:
    """
    [Approach] 가변 인자 + sum()
    [Time] O(n)  [Space] O(1)
    [Original] lambda *x: sum(x)
    ✨ 인자 개수에 유연함
    """
    return sum(args)


def solution_v3(num1: int, num2: int) -> int:
    """
    [Approach] 람다 스타일 (인라인)
    [Time] O(1)  [Space] O(1)
    [Original] lambda x, y: x + y
    """
    return num1 + num2

# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
