"""
프로그래머스 Lv0 #181892 - n 번째 원소부터
https://school.programmers.co.kr/learn/courses/30/lessons/181892

[문제]
정수 리스트 num_list와 정수 n이 주어질 때,
n번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록
solution 함수를 완성해주세요.

[제한]
- 2 ≤ num_list의 길이 ≤ 30
- 1 ≤ num_list의 원소 ≤ 9
- 1 ≤ n ≤ num_list의 길이
"""


def solution_v1(num_list: list[int], n: int) -> list[int]:
    """
    [Approach] 슬라이싱: 1-based n을 0-based로 변환 후 끝까지 슬라이스
    [Time] O(k), k = len(num_list) - n + 1  [Space] O(k)
    """
    return num_list[n - 1:]


solution = solution_v1
