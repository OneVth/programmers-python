"""
프로그래머스 Lv0 #181889 - n 번째 원소까지
https://school.programmers.co.kr/learn/courses/30/lessons/181889

[문제]
정수 리스트 num_list와 정수 n이 주어질 때,
num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를 담은 리스트를
return하도록 solution 함수를 완성해주세요.

[제한]
- 2 ≤ num_list의 길이 ≤ 30
- 1 ≤ num_list의 원소 ≤ 9
- 1 ≤ n ≤ num_list의 길이
"""


def solution_v1(num_list: list[int], n: int) -> list[int]:
    """
    [Approach] 슬라이싱으로 첫 번째~n번째 원소 추출
    [Time] O(n)  [Space] O(n)
    """
    return num_list[:n]


solution = solution_v1
