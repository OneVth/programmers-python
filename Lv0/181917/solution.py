"""
프로그래머스 Lv0 #181917 - 간단한 논리 연산
https://school.programmers.co.kr/learn/courses/30/lessons/181917

[문제]
boolean 변수 x1, x2, x3, x4 가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.

(x1 ∨ x2) ∧ (x3 ∨ x4)

[제한]
없음 (boolean 입력)
"""


def solution_v1(x1: bool, x2: bool, x3: bool, x4: bool) -> bool:
    """
    [Approach] 수식 (x1 ∨ x2) ∧ (x3 ∨ x4)를 Python 논리 연산자로 직접 표현
    [Time] O(1)  [Space] O(1)
    """
    return (x1 or x2) and (x3 or x4)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
