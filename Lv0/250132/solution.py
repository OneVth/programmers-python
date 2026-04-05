"""
프로그래머스 Lv0 #250132 - [PCCE 기출문제] 2번 / 피타고라스의 정리
https://school.programmers.co.kr/learn/courses/30/lessons/250132

[문제]
직각삼각형이 주어졌을 때 빗변의 제곱은 다른 두 변을 각각 제곱한 것의 합과 같습니다.
(피타고라스의 정리: a² + b² = c²)

직각삼각형의 한 변의 길이 a와 빗변의 길이 c가 주어질 때,
다른 한 변의 길이의 제곱 b_square를 return합니다.
즉, b_square = c² - a²

[제한]
- 1 ≤ a < c ≤ 100
"""


def solution_v1(a: int, c: int) -> int:
    """
    [Approach] 피타고라스 정리 b² = c² - a² 직접 계산
    [Time] O(1)  [Space] O(1)
    """
    b_square = c**2 - a**2
    return b_square


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
