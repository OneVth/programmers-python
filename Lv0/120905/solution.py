"""
프로그래머스 Lv0 #120905 - n의 배수 고르기
https://school.programmers.co.kr/learn/courses/30/lessons/120905

[문제]
정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가
아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 10,000
- 1 ≤ numlist의 크기 ≤ 100
- 1 ≤ numlist의 원소 ≤ 100,000
"""


def solution_v1(n: int, numlist: list[int]) -> list[int]:
    """
    [Approach] 리스트 컴프리헨션 - 조건부 필터링
    [Time] O(m)  [Space] O(k) - m: numlist 길이, k: n의 배수 개수
    """
    return [x for x in numlist if x % n == 0]


def solution_v2(n: int, numlist: list[int]) -> list[int]:
    """
    [Approach] filter() 함수 - 함수형 프로그래밍 스타일
    [Time] O(m)  [Space] O(k)
    """
    return list(filter(lambda v: v % n == 0, numlist))


solution = solution_v1
