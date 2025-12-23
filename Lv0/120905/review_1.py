"""
프로그래머스 Lv0 #120905 - n의 배수 고르기
https://school.programmers.co.kr/learn/courses/30/lessons/120905

[복습] 1차 - 2025-12-17

[문제]
정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가
아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 10,000
- 1 ≤ numlist의 크기 ≤ 100
- 1 ≤ numlist의 원소 ≤ 100,000
"""


def solution(n: int, numlist: list[int]) -> list[int]:
    """
    [Approach] 리스트 컴프리헨션으로 n의 배수만 필터링
    [Time] O(m) - m은 numlist 길이
    [Space] O(k) - k는 결과 배열 크기 (n의 배수 개수)
    """
    return [x for x in numlist if x % n == 0]
