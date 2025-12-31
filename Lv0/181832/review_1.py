"""
프로그래머스 Lv0 #181832 - 정수를 나선형으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/181832

[복습] 1차 - 2025-12-31

[문제]
양의 정수 n이 매개변수로 주어집니다.
n × n 배열에 1부터 n²까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한
이차원 배열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ n ≤ 30
"""


def solution_v1(n: int) -> list[list[int]]:
    """
    [Approach] ㄱ자 패턴 시뮬레이션 - 각 레이어에서 가로(k-1) + 세로(k) = 2k-1개씩 채움
    [Time] O(n²)  [Space] O(n²)
    """
    mat = [[0] * n for _ in range(n)]

    flag = True
    v = 1
    i, j = 0, 0
    for k in range(n, 0, -1):
        for l in range(1, 2 * k):
            mat[i][j] = v
            v += 1

            if flag:
                if l < k:
                    j += 1
                else:
                    i += 1
            else:
                if l < k:
                    j -= 1
                else:
                    i -= 1

        if flag:
            i -= 1
            j -= 1
        else:
            i += 1
            j += 1

        flag = not flag

    return mat


def solution_v2(n: int) -> list[list[int]]:
    """
    [Approach] 4방향 벡터 + 경계/방문 체크로 방향 전환
    [Time] O(n²)  [Space] O(n²)
    """
    mat = [[None] * n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상

    y, x = 0, 0
    d = 0  # 현재 방향 인덱스
    for i in range(1, n**2 + 1):
        mat[y][x] = i

        # 다음 위치 계산
        ny = y + directions[d][0]
        nx = x + directions[d][1]

        # 경계 벗어나거나 이미 방문한 곳이면 방향 전환
        if ny < 0 or ny >= n or nx < 0 or nx >= n or mat[ny][nx]:
            d = (d + 1) % 4
            ny = y + directions[d][0]
            nx = x + directions[d][1]

        y, x = ny, nx

    return mat


solution = solution_v2
