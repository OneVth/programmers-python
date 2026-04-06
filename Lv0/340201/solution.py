"""
프로그래머스 Lv0 #340201 - [PCCE 기출문제] 7번 / 버스
https://school.programmers.co.kr/learn/courses/30/lessons/340201

[문제]
영진이는 약속장소에 가기 위해 버스를 타려고 합니다. 버스에는 좌석이 총 seat개만큼 있습니다.
기점에서 출발한 버스가 영진이가 기다리는 정거장에 도착하기 전에 방문하는 각 정거장에서
승/하차한 승객 정보가 주어질 때, 영진이가 버스에 탄 순간 빈 좌석은 몇 개인지 구해주세요.

- 영진이가 기다리는 정거장에서는 영진이가 제일 먼저 버스에 탑승합니다.
- 이전 정거장에서 버스에 탑승한 승객들은 남는 좌석이 있다면 항상 앉는다고 가정합니다.
- 기점에서 출발하는 버스에는 승객이 0명 타고 있습니다.
- passengers의 원소는 "On"(승차), "Off"(하차), "-"(패딩, 의미 없음)입니다.

[제한]
- 1 ≤ seat ≤ 30
- 1 ≤ passengers의 길이 ≤ 10
- 1 ≤ passengers[i]의 길이 ≤ 20
- passengers[i]의 길이는 모두 동일합니다.
- passengers[i]의 원소는 "On", "Off" 또는 "-"입니다.
"""


def solution_v1(seat: int, passengers: list[list[str]]) -> int:
    """
    [Approach] C++ 원본 빈칸 구조를 Python으로 이식. func3(Off 카운트), func4(On 카운트)로
               정거장별 승/하차 집계 후, func1로 음수 방지(max(0, x))하여 남은 좌석 반환
    [Time] O(n*m)  [Space] O(1)
    """

    def func1(num):
        if 0 > num:
            return 0
        else:
            return num

    def func2(num):
        if num > 0:
            return 0
        else:
            return num

    def func3(station):
        num = 0
        for people in station:
            if people == "Off":
                num += 1
        return num

    def func4(station):
        num = 0
        for people in station:
            if people == "On":
                num += 1
        return num

    num_passenger = 0
    for station in passengers:
        num_passenger += func4(station)
        num_passenger -= func3(station)

    answer = func1(seat - num_passenger)

    return answer


solution = solution_v1
