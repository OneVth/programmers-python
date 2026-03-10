"""
프로그래머스 Lv0 #181891 - 순서 바꾸기
https://school.programmers.co.kr/learn/courses/30/lessons/181891

[문제]
정수 리스트 num_list와 정수 n이 주어질 때,
num_list를 n번째 원소 이후의 원소들과 n번째까지의 원소들로 나눠
n번째 원소 이후의 원소들을 n번째까지의 원소들 앞에 붙인 리스트를
return하도록 solution 함수를 완성해주세요.

[제한]
- 2 ≤ num_list의 길이 ≤ 30
- 1 ≤ num_list의 원소 ≤ 9
- 1 ≤ n ≤ num_list의 길이
"""


def solution_v1(num_list: list[int], n: int) -> list[int]:
    """
    [Approach] 빈 리스트에 n번째 이후, n번째까지 순서로 extend하여 로테이션
    [Time] O(n)  [Space] O(n)
    """
    answer = []
    answer.extend(num_list[n:])
    answer.extend(num_list[:n])
    return answer

def solution_v2(num_list: list[int], n: int) -> list[int]:
    """
    [Approach] 슬라이싱 + 연결로 한 줄 로테이션
    [Time] O(n)  [Space] O(n)
    """
    return num_list[n:] + num_list[:n]

solution = solution_v2
