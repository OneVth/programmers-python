"""
프로그래머스 Lv0 #120875 - 평행
https://school.programmers.co.kr/learn/courses/30/lessons/120875

[문제]
점 네 개의 좌표를 담은 이차원 배열 dots가 다음과 같이 매개변수로 주어집니다.
- [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]

주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을,
없으면 0을 return 하도록 solution 함수를 완성해보세요.

[제한]
- dots의 길이 = 4
- dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
  - 0 ≤ x, y ≤ 100
- 서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
- 두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
- 임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.
"""

from fractions import Fraction


def solution_v1(dots: list[list[int]]) -> int:
    """
    [Approach] 유효한 선분 쌍 3가지만 비교, Fraction으로 기울기 계산
    [Time] O(1) - 고정된 3가지 조합만 확인
    [Space] O(1)
    """
    # 점을 중복 사용하지 않는 유효한 선분 쌍 3가지
    cases = [[(0, 1), (2, 3)], [(0, 2), (1, 3)], [(0, 3), (1, 2)]]

    for case in cases:
        x1, y1 = dots[case[0][0]][0], dots[case[0][0]][1]
        x2, y2 = dots[case[0][1]][0], dots[case[0][1]][1]
        if y1 == y2:
            continue
        grad1 = Fraction(x1 - x2, y1 - y2)

        x3, y3 = dots[case[1][0]][0], dots[case[1][0]][1]
        x4, y4 = dots[case[1][1]][0], dots[case[1][1]][1]
        if y3 == y4:
            continue
        grad2 = Fraction(x3 - x4, y3 - y4)

        if grad1 == grad2:
            return 1

    return 0


def solution_v2(dots: list[list[int]]) -> int:
    """
    [Approach] 교차 곱셈으로 기울기 비교 (나눗셈 없이 정수 연산만 사용)
    [Time] O(1)  [Space] O(1)
    """
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    # 기울기 비교: dy1/dx1 == dy2/dx2 ⟺ dy1 * dx2 == dy2 * dx1
    answer1 = (y1 - y2) * (x3 - x4) == (y3 - y4) * (x1 - x2)  # (0-1, 2-3)
    answer2 = (y2 - y4) * (x1 - x3) == (y1 - y3) * (x2 - x4)  # (1-3, 0-2)
    answer3 = (y2 - y3) * (x1 - x4) == (y1 - y4) * (x2 - x3)  # (1-2, 0-3)

    return 1 if answer1 or answer2 or answer3 else 0


# 기본 솔루션 지정
solution = solution_v2
