"""
프로그래머스 Lv0 #120903 - 배열의 유사도
https://school.programmers.co.kr/learn/courses/30/lessons/120903

[문제]
두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때
같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ s1, s2의 길이 ≤ 100
- 1 ≤ s1, s2의 원소의 길이 ≤ 10
- s1과 s2의 원소는 알파벳 소문자로만 이루어져 있습니다
- s1과 s2는 각각 중복된 원소를 갖지 않습니다.
"""


def solution_v1(s1: list[str], s2: list[str]) -> int:
    """
    [Approach] Set 교집합 - 두 집합의 공통 원소 개수
    [Time] O(n + m)  [Space] O(n + m)
    """
    return len(set(s1) & set(s2))


def solution_v2(s1: list[str], s2: list[str]) -> int:
    """
    [Approach] 순회 카운트 - s1 원소가 s2에 있는지 확인
    [Time] O(n * m)  [Space] O(1)
    """
    return sum(1 for x in s1 if x in s2)


solution = solution_v1
