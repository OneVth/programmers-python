"""
프로그래머스 Lv0 #181833 - 특별한 이차원 배열 1
https://school.programmers.co.kr/learn/courses/30/lessons/181833

[문제]
정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를
return 하는 solution 함수를 작성해 주세요.
- arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.

[제한]
- 1 ≤ n ≤ 100
"""


def solution_v1(n: int) -> list[list[int]]:
    """
    [Approach] 0으로 초기화 후 대각선만 1로 설정
    [Time] O(n²)  [Space] O(n²)
    """
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        answer[i][i] = 1

    return answer


solution = solution_v1
