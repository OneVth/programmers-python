"""
프로그래머스 Lv0 #120875 - 평행
https://school.programmers.co.kr/learn/courses/30/lessons/120875

[복습] 1차 - 2025-12-17

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


def solution_v1(dots: list[list[int]]) -> int:
    """
    [Approach] 교차 곱으로 기울기 비교 - 4점을 2쌍으로 나누는 3가지 경우 검사
    [Time] O(1) - 고정된 4개의 점, 3가지 조합만 검사
    [Space] O(1) - 상수 공간만 사용
    """
    # 4점을 2개씩 짝짓는 경우의 수: (0-1, 2-3), (0-2, 1-3), (0-3, 1-2)
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = dots

    # 기울기 비교: (y2-y1)/(x2-x1) == (y4-y3)/(x4-x3) → 교차 곱으로 변환
    parallel_01_23 = (y2 - y1) * (x4 - x3) == (y4 - y3) * (x2 - x1)
    parallel_02_13 = (y3 - y1) * (x4 - x2) == (y4 - y2) * (x3 - x1)
    parallel_03_12 = (y4 - y1) * (x3 - x2) == (y3 - y2) * (x4 - x1)

    return 1 if (parallel_01_23 or parallel_02_13 or parallel_03_12) else 0


# 기본 솔루션 지정
solution = solution_v1
