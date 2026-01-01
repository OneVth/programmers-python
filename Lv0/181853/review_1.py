"""
프로그래머스 Lv0 #181853 - 뒤에서 5등까지
https://school.programmers.co.kr/learn/courses/30/lessons/181853

[복습] 1차 - 2025-12-31

[문제]
정수로 이루어진 리스트 num_list가 주어집니다.
num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를
return하도록 solution 함수를 완성해주세요.

[제한]
- 6 ≤ num_list의 길이 ≤ 30
- 1 ≤ num_list의 원소 ≤ 100
"""


def solution_v1(num_list: list[int]) -> list[int]:
    """
    [Approach] 정렬 후 앞에서 5개 슬라이싱
    [Time] O(n log n) - 정렬 비용
    [Space] O(n) - 정렬된 새 리스트 생성
    """
    return sorted(num_list)[:5]


def solution_v2(num_list: list[int]) -> list[int]:
    """
    [Approach] heapq.nsmallest()로 가장 작은 5개 추출
    [Time] O(n log k) - k=5로 고정, 실질적으로 O(n)
    [Space] O(k) - 크기 5의 힙 유지
    """
    import heapq

    return heapq.nsmallest(5, num_list)


solution = solution_v2
