"""
프로그래머스 Lv0 #181896 - 첫 번째로 나오는 음수
https://school.programmers.co.kr/learn/courses/30/lessons/181896

[문제]
정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록
solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.

[제한]
- 5 ≤ num_list의 길이 ≤ 100
- -10 ≤ num_list의 원소 ≤ 100
"""


def solution_v1(num_list: list[int]) -> int:
    """
    [Approach] 인덱스 기반 순회 - range로 인덱스 접근하며 음수 탐색
    [Time] O(n) - 최악의 경우 전체 순회
    [Space] O(1) - 추가 공간 없음
    """
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i

    return -1


solution = solution_v1
