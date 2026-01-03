"""
프로그래머스 Lv0 #120860 - 직사각형 넓이 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120860

[복습] 2차 - 2026-01-02

[문제]
2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다.
직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열
dots가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.

[제한]
- dots의 길이 = 4
- dots의 원소의 길이 = 2
- -256 < dots[i]의 원소 < 256
- 잘못된 입력은 주어지지 않습니다.
"""


def solution(dots: list[list[int]]) -> int:
    """
    [Approach] 좌표 정렬로 꼭짓점 위치 고정 후 너비/높이 계산
    [Time] O(1) - 4개 원소 정렬은 상수 시간
    [Space] O(1)
    """
    sorted_dots = sorted(dots)
    # 정렬 후: [좌하, 좌상, 우하, 우상]
    return abs(sorted_dots[0][1] - sorted_dots[1][1]) * abs(
        sorted_dots[0][0] - sorted_dots[2][0]
    )
