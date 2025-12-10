"""
프로그래머스 Lv0 #120866 - 안전지대
https://school.programmers.co.kr/learn/courses/30/lessons/120866

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
    [Approach] 별도 safe_mat 생성, 명시적 8방향 딕셔너리 사용
    [Time] O(n²)  [Space] O(n²) - safe_mat 배열
    """
    direction = {
        "e": (1, 0),
        "w": (-1, 0),
        "s": (0, -1),
        "n": (0, 1),
        "ne": (1, 1),
        "nw": (-1, 1),
        "se": (1, -1),
        "sw": (-1, -1),
    }

    n = len(board[0])
    safe_mat = [[True] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                safe_mat[i][j] = False
                for dx, dy in direction.values():
                    if 0 <= (ny := i + dy) < n and 0 <= (nx := j + dx) < n:
                        safe_mat[ny][nx] = False

    return sum(sum(safe_mat[i]) for i in range(n))


def solution_v2(board: list[list[int]]) -> int:
    """
    [Approach] set으로 위험 좌표 수집, 중복 자동 제거
    [Time] O(n²)  [Space] O(k) - k는 위험 좌표 수
    """
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i + di, j + dj) for di in [-1, 0, 1] for dj in [-1, 0, 1])
    return n * n - sum(0 <= i < n and 0 <= j < n for i, j in danger)


def solution_v3(board: list[list[int]]) -> int:
    """
    [Approach] 원본 board를 -1로 마킹하여 위험지역 표시
    [Time] O(n²)  [Space] O(1) - in-place 수정
    [Note] 원본 board가 변경됨 (부작용 있음)
    """
    answer = 0

    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[row][col] == 1:
                for j in range(max(col - 1, 0), min(col + 2, len(board))):
                    for i in range(max(row - 1, 0), min(row + 2, len(board))):
                        if board[i][j] == 1:
                            continue
                        board[i][j] = -1

    for i in board:
        answer += i.count(0)

    return answer


# 기본 솔루션 지정
solution = solution_v2
