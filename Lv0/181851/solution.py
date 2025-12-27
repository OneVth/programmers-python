"""
프로그래머스 Lv0 #181851 - 전국 대회 선발 고사
https://school.programmers.co.kr/learn/courses/30/lessons/181851

[문제]
0번부터 n-1번까지 n명의 학생 중 3명을 선발하는 전국 대회 선발 고사를 보았습니다.
등수가 높은 3명을 선발해야 하지만, 개인 사정으로 전국 대회에 참여하지 못하는 학생들이 있어
참여가 가능한 학생 중 등수가 높은 3명을 선발하기로 했습니다.

각 학생들의 선발 고사 등수를 담은 정수 배열 rank와
전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance가 매개변수로 주어집니다.
전국 대회에 선발된 학생 번호들을 등수가 높은 순서대로 각각 a, b, c번이라고 할 때
10000 × a + 100 × b + c를 return 하는 solution 함수를 작성해 주세요.

[제한]
- 3 ≤ rank의 길이 = attendance의 길이 ≤ 100
- rank[i]는 i번 학생의 선발 고사 등수를 의미합니다.
- rank의 원소는 1부터 n까지의 정수로 모두 서로 다릅니다.
- attendance[i]는 i번 학생의 전국 대회 참석 가능 여부를 나타냅니다.
  - attendance[i]가 true라면 참석 가능, false면 참석 불가능을 의미합니다.
- attendance의 원소 중 적어도 3개는 true입니다.
"""


def solution_v1(rank: list[int], attendance: list[bool]) -> int:
    """
    [Approach] zip으로 (등수, 참석여부) 쌍 생성 → 참석 가능자 필터링 → 등수 정렬 → index로 학생번호 역추적
    [Time] O(n log n) - 정렬 + O(n) index 호출 3번
    [Space] O(n) - 필터링된 리스트
    """
    candidates = list(sorted(filter(lambda x: x[1] == True, zip(rank, attendance))))
    nums, get_in = zip(*candidates)
    a, b, c = map(lambda v: rank.index(v), nums[:3])
    return 10000 * a + 100 * b + c


def solution_v2(rank: list[int], attendance: list[bool]) -> int:
    """
    [Approach] (등수, 학생번호) 튜플 리스트 생성 후 정렬, index 역추적 불필요
    [Time] O(n log n) - 정렬만
    [Space] O(n) - 필터링된 리스트
    """
    candidates = [(rank[i], i) for i in range(len(rank)) if attendance[i]]
    candidates.sort()
    a, b, c = [idx for _, idx in candidates[:3]]
    return 10000 * a + 100 * b + c


solution = solution_v1
