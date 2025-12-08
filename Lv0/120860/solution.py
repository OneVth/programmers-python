"""
문제: 직사각형 넓이 구하기
난이도: Lv0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120860

설명:
2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다.
직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는 배열
dots가 매개변수로 주어질 때, 직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.

제한사항:
- dots의 길이 = 4
- dots의 원소의 길이 = 2
- -256 < dots[i]의 원소 < 256
- 잘못된 입력은 주어지지 않습니다.
"""


def solution_v1(dots: list[list[int]]) -> int:
    """
    [Approach] 피벗 좌표 기준 - 같은 x/y를 가진 점으로 가로/세로 계산
    [Time] O(n) - 좌표 순회
    [Space] O(1) - 상수 공간
    """
    pivot_x, pivot_y = dots[0]

    for i in range(1, len(dots)):
        if pivot_x == dots[i][0]:
            h = abs(pivot_y - dots[i][1])
        if pivot_y == dots[i][1]:
            w = abs(pivot_x - dots[i][0])

    return w * h


def solution_v2(dots: list[list[int]]) -> int:
    """
    [Approach] 리스트 min/max - 첫 번째 요소 기준 비교로 x 범위 획득
    [Time] O(n) - min/max 각각 순회
    [Space] O(1) - 상수 공간
    """
    return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])


def solution_v3(dots: list[list[int]]) -> int:
    """
    [Approach] zip(*) 언패킹 - x좌표/y좌표 분리 후 범위 계산
    [Time] O(n) - min/max 순회
    [Space] O(n) - 언패킹된 튜플 저장
    """
    xs, ys = zip(*dots)
    return (max(xs) - min(xs)) * (max(ys) - min(ys))


solution = solution_v3
