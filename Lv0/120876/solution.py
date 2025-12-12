"""
프로그래머스 Lv0 #120876 - 겹치는 선분의 길이
https://school.programmers.co.kr/learn/courses/30/lessons/120876

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
    [Approach] 구간 카운팅 - 각 단위 구간이 몇 개의 선분에 포함되는지 카운트
               좌표 범위 -100~100을 인덱스 0~200으로 오프셋 매핑
    [Time] O(N * L) - N: 선분 개수(3), L: 최대 선분 길이(200)
    [Space] O(201) - 고정 크기 카운팅 배열
    """
    overlap_num = [0] * 201

    for start, end in lines:
        for i in range(start + 100, end + 100):
            overlap_num[i] += 1

    return sum(1 for count in overlap_num if count > 1)


def solution_v2(lines: list[list[int]]) -> int:
    """
    [Approach] 집합 연산 - 각 선분을 점 집합으로 변환 후 교집합 합집합 활용
               (A∩B) ∪ (B∩C) ∪ (A∩C) = 2개 이상 겹치는 점들의 집합
    [Time] O(N * L) - 집합 생성 및 교집합/합집합 연산
    [Space] O(N * L) - 3개의 집합 저장
    """
    sets = [set(range(start, end)) for start, end in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


def solution_v3(lines: list[list[int]]) -> int:
    """
    [Approach] 집합 연산 (명시적) - solution_v2와 동일한 로직을 풀어서 작성
               가독성을 위해 각 선분을 개별 변수로 분리
    [Time] O(N * L) - 집합 생성 및 교집합/합집합 연산
    [Space] O(N * L) - 3개의 집합 저장
    """
    s1 = set(range(lines[0][0], lines[0][1]))
    s2 = set(range(lines[1][0], lines[1][1]))
    s3 = set(range(lines[2][0], lines[2][1]))
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))


solution = solution_v2
