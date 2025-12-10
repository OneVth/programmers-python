"""
프로그래머스 Lv0 #120862 - 최댓값 만들기 (2)
https://school.programmers.co.kr/learn/courses/30/lessons/120862

[문제]
정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

[제한]
- -10,000 ≤ numbers의 원소 ≤ 10,000
- 2 ≤ numbers의 길이 ≤ 100
"""


def solution_v1(numbers: list[int]) -> int:
    """
    [Approach] 정렬 후 양 끝 비교: 최솟값 두 개 곱 vs 최댓값 두 개 곱
    [Time] O(n log n) - 정렬
    [Space] O(n) - sorted()가 새 리스트 생성
    """
    from math import prod

    sorted_numbers = sorted(numbers)
    return max(prod(sorted_numbers[:2]), prod(sorted_numbers[-2:]))


# 기본 솔루션 지정
solution = solution_v1
