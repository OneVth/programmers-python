"""
프로그래머스 Lv0 #181852 - 뒤에서 5등 위로
https://school.programmers.co.kr/learn/courses/30/lessons/181852

[문제]
정수로 이루어진 리스트 num_list가 주어집니다.
num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를
return하도록 solution 함수를 완성해주세요.

[제한]
- 6 ≤ num_list의 길이 ≤ 30
- 1 ≤ num_list의 원소 ≤ 100
"""


def solution_v1(num_list: list[int]) -> list[int]:
    """
    [Approach] 정렬 후 인덱스 5부터 슬라이싱 (가장 작은 5개 제외)
    [Time] O(n log n) - 정렬
    [Space] O(n) - 정렬된 리스트
    """
    return sorted(num_list)[5:]


solution = solution_v1
