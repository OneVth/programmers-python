"""
프로그래머스 Lv0 #120835 - 진료 순서 정하기
https://school.programmers.co.kr/learn/courses/30/lessons/120835

[문제]
외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다.
정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로
진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

[제한]
- 중복된 원소는 없습니다.
- 1 ≤ emergency의 길이 ≤ 10
- 1 ≤ emergency의 원소 ≤ 100
"""


def solution_v1(emergency: list[int]) -> list[int]:
    """
    [Approach] 정렬 후 순위 배정 (명시적 루프)
    [Time] O(n²)  [Space] O(n)
    ⚠️ index()가 O(n)이므로 전체 O(n²)
    """
    answer = [0 for i in range(len(emergency))]
    rank = 1

    sorted_emergency = sorted(emergency, reverse=True)
    for e in sorted_emergency:
        answer[emergency.index(e)] = rank
        rank += 1

    return answer


def solution_v2(emergency: list[int]) -> list[int]:
    """
    [Approach] 정렬 후 index로 순위 조회
    [Time] O(n²)  [Space] O(n)
    ⚠️ index()가 O(n)이므로 전체 O(n²)
    """
    sorted_emergency = sorted(emergency, reverse=True)
    return [sorted_emergency.index(e) + 1 for e in emergency]


def solution_v3(emergency: list[int]) -> list[int]:
    """
    [Approach] 딕셔너리로 순위 매핑
    [Time] O(n log n)  [Space] O(n)
    ✅ 정렬 O(n log n) + 조회 O(1) × n
    """
    dict_emergency = {e: i + 1 for i, e in enumerate(sorted(emergency, reverse=True))}
    return [dict_emergency[e] for e in emergency]


solution = solution_v3
