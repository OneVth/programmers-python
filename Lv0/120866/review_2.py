"""
프로그래머스 Lv0 #120866 - 안전지대
https://school.programmers.co.kr/learn/courses/30/lessons/120866

[복습] 2차 - 2026-01-02

[문제]
지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설된 지역 1과,
지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때,
안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

[제한]
- board는 n * n 배열입니다.
- 1 ≤ n ≤ 100
- 지뢰는 1로 표시되어 있습니다.
- board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.
"""


def solution_v1(board: list[list[int]]) -> int:
    """
    [Approach] 지뢰 주변 9칸을 위험지역 set에 수집, 전체에서 차감
    [Time] O(n²)  [Space] O(n²) - 위험지역 좌표 set
    """
    n = len(board)
    danger = set()
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),  (0, 0),  (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for i in range(n):
        for j in range(n):
            if board[i][j]:
                danger.update((i + dy, j + dx) for dy, dx in directions)

    return n**2 - sum(1 for y, x in danger if 0 <= y < n and 0 <= x < n)


# 기본 솔루션 지정
solution = solution_v1
