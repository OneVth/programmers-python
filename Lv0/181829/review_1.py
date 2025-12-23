"""
프로그래머스 Lv0 #181829 - 이차원 배열 대각선 순회하기
https://school.programmers.co.kr/learn/courses/30/lessons/181829

[복습] 1차 - 2025-12-17

[문제]
2차원 정수 배열 board와 정수 k가 주어집니다.
i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 return 하는
solution 함수를 완성해 주세요.

[제한]
- 1 ≤ board의 길이 ≤ 100
- 1 ≤ board[i]의 길이 ≤ 100
  - 1 ≤ board[i][j] ≤ 10,000
  - 모든 board[i]의 길이는 같습니다.
- 0 ≤ k < board의 길이 + board[i]의 길이
"""


def solution(board: list[list[int]], k: int) -> int:
    """
    [Approach] 이중 루프로 i+j <= k 조건 만족하는 원소 합산
    [Time] O(n * m) - n은 행, m은 열 개수
    [Space] O(1) - 추가 공간 없음
    """
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                answer += board[i][j]
            else:
                break

    return answer
