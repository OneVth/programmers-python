"""
프로그래머스 Lv0 #120876 - 겹치는 선분의 길이
https://school.programmers.co.kr/learn/courses/30/lessons/120876

[복습] 1차 - 2025-12-17

[문제]
선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가
[[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가
매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록
solution 함수를 완성해보세요.

예시) lines가 [[0, 2], [-3, -1], [-2, 1]]일 때:
선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.

[제한]
- lines의 길이 = 3
- lines의 원소의 길이 = 2
- 모든 선분은 길이가 1 이상입니다.
- lines의 원소는 [a, b] 형태이며, a, b는 각각 선분의 양 끝점입니다.
  - -100 ≤ a < b ≤ 100
"""


def solution_v1(lines: list[list[int]]) -> int:
    """
    [Approach] 스위핑 - 각 단위 구간에 겹치는 선분 수 카운트
    [Time] O(R * N) - R: 좌표 범위(최대 200), N: 선분 수(3)
    [Space] O(1) - 상수 공간만 사용
    """
    left = min(line[0] for line in lines)
    right = max(line[1] for line in lines)
    overlap_length = 0

    for i in range(left, right):
        # 단위 구간 [i, i+1)에 겹치는 선분 수 카운트
        overlap_count = sum(1 for a, b in lines if a <= i < b)
        if overlap_count >= 2:
            overlap_length += 1

    return overlap_length


def solution_v2(lines: list[list[int]]) -> int:
    """
    [Approach] 집합 연산 - 각 선분을 정수 집합으로 변환 후 교집합 합집합
    [Time] O(R) - R: 좌표 범위(최대 200)
    [Space] O(R) - 집합 저장 공간
    """
    sets = [set(range(start, end)) for start, end in lines]
    return len((sets[0] & sets[1]) | (sets[0] & sets[2]) | (sets[1] & sets[2]))


# 기본 솔루션 지정
solution = solution_v2
