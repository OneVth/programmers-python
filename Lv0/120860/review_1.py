"""
프로그래머스 Lv0 #120860 - 직사각형 넓이 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120860

[복습] 1차 - 2025-12-10

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


def solution_v1(dots: list[list[int]]) -> int:
    """
    [Approach] zip으로 좌표 분리 후 범위 계산
    [Time] O(n)  [Space] O(n)
    ⚠️ zip(dots[0], dots[1], ...) 대신 zip(*dots) 사용 권장
    """
    xpos, ypos = zip(dots[0], dots[1], dots[2], dots[3])

    return (max(xpos) - min(xpos)) * (max(ypos) - min(ypos))


def solution_v2(dots: list[list[int]]) -> int:
    """
    [Approach] zip(*dots) 언패킹으로 좌표 분리
    [Time] O(n)  [Space] O(n)
    ✅ 더 간결하고 일반화 가능
    """
    xs, ys = zip(*dots)

    return (max(xs) - min(xs)) * (max(ys) - min(ys))


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
