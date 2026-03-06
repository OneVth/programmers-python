"""
프로그래머스 Lv0 #181879 - 길이에 따른 연산
https://school.programmers.co.kr/learn/courses/30/lessons/181879

[문제]
정수가 담긴 리스트 num_list가 주어질 때,
리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을
10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.

[제한]
- 2 <= num_list의 길이 <= 20
- 1 <= num_list의 원소 <= 9
- num_list의 원소를 모두 곱했을 때 2,147,483,647를 넘는 입력은 주어지지 않습니다.
"""


def solution_v1(num_list: list[int]) -> int:
    """
    [Approach] functools.reduce로 곱셈, 길이 기준 분기
    [Time] O(n)  [Space] O(1)
    """
    from functools import reduce

    if len(num_list) > 10:
        return sum(num_list)
    return reduce(lambda acc, x: acc * x, num_list)


def solution_v2(num_list: list[int]) -> int:
    """
    [Approach] math.prod()로 곱셈, 길이 기준 분기
    [Time] O(n)  [Space] O(1)
    """
    from math import prod

    if len(num_list) > 10:
        return sum(num_list)
    return prod(num_list)


solution = solution_v2
