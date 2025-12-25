"""
프로그래머스 Lv0 #181832 - 정수를 나선형으로 배치하기
https://school.programmers.co.kr/learn/courses/30/lessons/181832

[문제]
양의 정수 n이 매개변수로 주어집니다.
n × n 배열에 1부터 n²까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한
이차원 배열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ n ≤ 30
"""


def solution_v1(n: int) -> list[list[int]]:
    """
    [Approach] ㄱ자 패턴 시뮬레이션 - 바깥 껍질부터 2i-1개씩 채움
    [Time] O(n²)  [Space] O(n²)

    각 레이어에서 가로 i-1개 + 세로 i개 = 2i-1개씩 채움
    flag로 진행 방향(시계/반시계) 전환
    """
    h, v = 0, 0
    cnt = 1
    flag = True
    answer = [[0] * n for _ in range(n)]

    for i in range(n, 0, -1):
        for j in range(2 * i - 1):
            answer[v][h] = cnt
            cnt += 1

            if j < i - 1:
                if flag:
                    h += 1
                else:
                    h -= 1
            else:
                if flag:
                    v += 1
                else:
                    v -= 1

        if flag:
            v -= 1
            h -= 1
        else:
            v += 1
            h += 1
        flag = not flag

    return answer


def solution_v2(n: int) -> list[list[int]]:
    """
    [Approach] 4방향 벡터 시뮬레이션 - 벽/채워진 칸 만나면 회전
    [Time] O(n²)  [Space] O(n²)
    """
    answer = [[None] * n for _ in range(n)]
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y, m = 0, 0, 0
    for i in range(1, n**2 + 1):
        answer[y][x] = i
        if (
            y + dir[m][0] >= n
            or x + dir[m][1] >= n
            or answer[y + dir[m][0]][x + dir[m][1]]
        ):
            m = (m + 1) % len(dir)
        y, x = y + dir[m][0], x + dir[m][1]

    return answer


solution = solution_v2
