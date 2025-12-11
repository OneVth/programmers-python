"""
프로그래머스 Lv0 #120866 - 안전지대
https://school.programmers.co.kr/learn/courses/30/lessons/120866

[복습] 1차 - 2025-12-10

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
    [Approach] Set으로 위험 좌표 수집 (중복 자동 제거)
    [Time] O(n²)  [Space] O(k) - k는 위험 좌표 수
    ✅ 원본 board 유지, 중첩 루프로 9방향 한 번에 처리
    """
    danger = set()

    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                danger.update((i + r, j + c) for r in [-1, 0, 1] for c in [-1, 0, 1])

    return n * n - sum(1 for i, j in danger if 0 <= i < n and 0 <= j < n)


def solution_v2(board: list[list[int]]) -> int:
    """
    [Approach] In-place 마킹 (-1로 위험지역 표시)
    [Time] O(n²)  [Space] O(1)
    ⚠️ 원본 board가 변경됨 (부작용)
    """
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for dy, dx in directions:
                    if (
                        0 <= i + dy < n
                        and 0 <= j + dx < n
                        and board[i + dy][j + dx] != 1
                    ):
                        board[i + dy][j + dx] = -1

    return sum(board[i].count(0) for i in range(n))


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
