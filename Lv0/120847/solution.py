"""
프로그래머스 Lv0 #120847 - 최댓값 만들기(1)
https://school.programmers.co.kr/learn/courses/30/lessons/120847

[문제]
정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록
solution 함수를 완성해주세요.

[제한]
- 0 ≤ numbers의 원소 ≤ 10,000
- 2 ≤ numbers의 길이 ≤ 100
"""


def solution_v1(numbers: list[int]) -> int:
    """
    [Approach] 정렬 후 마지막 두 개 곱하기
    [Time] O(n log n)  [Space] O(n)
    """
    from math import prod

    return prod(sorted(numbers)[-2:])


def solution_v2(numbers: list[int]) -> int:
    """
    [Approach] heapq.nlargest로 상위 2개 추출
    [Time] O(n)  [Space] O(1)
    ✅ k가 작을 때 정렬보다 효율적
    """
    from heapq import nlargest

    a, b = nlargest(2, numbers)
    return a * b


solution = solution_v2
