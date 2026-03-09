"""
프로그래머스 Lv0 #181888 - n개 간격의 원소들
https://school.programmers.co.kr/learn/courses/30/lessons/181888

[문제]
정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터
마지막 원소까지 n개 간격으로 저장되어있는 원소들을 차례로 담은 리스트를
return하도록 solution 함수를 완성해주세요.

[제한]
- 5 <= num_list의 길이 <= 20
- 1 <= num_list의 원소 <= 9
- 1 <= n <= 4
"""


def solution_v1(num_list: list[int], n: int) -> list[int]:
    """
    [Approach] 슬라이싱 step으로 n개 간격 원소 추출
    [Time] O(n/step)  [Space] O(n/step)
    """
    return num_list[::n]


solution = solution_v1
