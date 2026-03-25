"""
프로그래머스 Lv0 #181929 - 원소들의 곱과 합
https://school.programmers.co.kr/learn/courses/30/lessons/181929

[문제]
정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다
작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

[제한]
- 2 ≤ num_list의 길이 ≤ 10
- 1 ≤ num_list의 원소 ≤ 9
"""


def solution_v1(num_list: list[int]) -> int:
    """
    [Approach] math.prod로 곱, sum으로 합을 구한 뒤 비교 결과를 int로 변환
    [Time] O(n)  [Space] O(1)
    """
    from math import prod

    return int(prod(num_list) < sum(num_list) ** 2)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
