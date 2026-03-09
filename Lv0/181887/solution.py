"""
프로그래머스 Lv0 #181887 - 홀수 vs 짝수
https://school.programmers.co.kr/learn/courses/30/lessons/181887

[문제]
정수 리스트 num_list가 주어집니다. 가장 첫 번째 원소를 1번 원소라고 할 때,
홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록
solution 함수를 완성해주세요. 두 값이 같을 경우 그 값을 return합니다.

[제한]
- 5 <= num_list의 길이 <= 50
- -9 <= num_list의 원소 <= 9
"""


def solution_v1(num_list: list[int]) -> int:
    """
    [Approach] 슬라이싱으로 홀수/짝수 번째 분리 후 합 비교
    [Time] O(n)  [Space] O(n)
    """
    return max(sum(num_list[::2]), sum(num_list[1::2]))


solution = solution_v1
