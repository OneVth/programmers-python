"""
프로그래머스 Lv0 #120922 - 종이 자르기
https://school.programmers.co.kr/learn/courses/30/lessons/120922

[복습] 1차 - 2025-12-17

[문제]
머쓱이는 큰 종이를 1 x 1 크기로 자르려고 합니다. 예를 들어 2 x 2 크기의 종이를
1 x 1 크기로 자르려면 최소 가위질 세 번이 필요합니다.
정수 M, N이 매개변수로 주어질 때, M x N 크기의 종이를 최소로 가위질 해야하는
횟수를 return 하도록 solution 함수를 완성해보세요.

[제한]
- 0 < M, N < 100
- 종이를 겹쳐서 자를 수 없습니다.

[힌트]
- 가로로 자르면 종이가 몇 조각이 되는가?
- 세로로 자르면 각 조각을 몇 번 잘라야 하는가?
"""


def solution_v1(M: int, N: int) -> int:
    """
    [Approach] 수학적 공식 - 조각 수(M*N)에서 1을 빼면 자르기 횟수
    [Time] O(1)  [Space] O(1)
    """
    return M * N - 1


def solution_v2(M: int, N: int) -> int:
    """
    [Approach] DP - 모든 분할 방법 중 최소 횟수 탐색
    [Time] O(M²N + MN²)  [Space] O(MN)
    """
    dp = [[0] * (N + 1) for _ in range(M + 1)]

    for m in range(1, M + 1):
        for n in range(1, N + 1):
            if m == 1 and n == 1:
                dp[m][n] = 0
            else:
                candidates = []
                for i in range(1, m):
                    candidates.append(1 + dp[i][n] + dp[m - i][n])
                for j in range(1, n):
                    candidates.append(1 + dp[m][j] + dp[m][n - j])
                dp[m][n] = min(candidates)

    return dp[M][N]


def solution_v3(M: int, N: int) -> int:
    """
    [Approach] 재귀 분할 - 긴 변을 반으로 나누며 자르기
    [Time] O(MN)  [Space] O(log(max(M,N))) 재귀 스택
    """
    def get_cut_count(w: int, h: int) -> int:
        if w == 1 and h == 1:
            return 0

        if w < h:
            w, h = h, w

        return 1 + get_cut_count(w // 2, h) + get_cut_count(w - w // 2, h)

    return get_cut_count(M, N)


solution = solution_v3
