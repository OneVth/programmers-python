"""
프로그래머스 Lv0 #250129 - [PCCE 기출문제] 5번 / 산책
https://school.programmers.co.kr/learn/courses/30/lessons/250129

[문제]
여름이는 강아지를 산책시키려고 합니다. 여름이는 2차원 좌표평면에서 동/서/남/북 방향으로
1m 단위로 이동하면서 강아지를 산책시킵니다. 산책루트가 담긴 문자열 route가 주어질 때,
도착점의 위치를 return하도록 solution 함수를 완성해 주세요.

- "N"은 북쪽으로 1만큼 움직입니다.
- "S"는 남쪽으로 1만큼 움직입니다. (북쪽으로 -1만큼 움직인 것과 같습니다.)
- "E"는 동쪽으로 1만큼 움직입니다.
- "W"는 서쪽으로 1만큼 움직입니다. (동쪽으로 -1만큼 움직인 것과 같습니다.)

출발점으로부터 [동쪽으로 떨어진 거리, 북쪽으로 떨어진 거리] 형태로 return합니다.

[제한]
- 1 ≤ route의 길이 ≤ 20
- route는 "N", "S", "E", "W"로만 이루어져 있습니다.
"""


def solution_v1(route: str) -> list[int]:
    """
    [Approach] 방향별 if/elif 분기로 east/north 누적
    [Time] O(n)  [Space] O(1)
    """
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S":
            north -= 1
        elif i == "E":
            east += 1
        elif i == "W":
            east -= 1

    return [east, north]


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
