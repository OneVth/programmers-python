"""
프로그래머스 Lv0 #181845 - 문자열로 변환
https://school.programmers.co.kr/learn/courses/30/lessons/181845

[문제]
정수 n이 주어질 때, n을 문자열로 변환하여 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 10000
"""


def solution_v1(n: int) -> str:
    """
    [Approach] str() 내장 함수로 정수를 문자열로 변환
    [Time] O(log n) - 자릿수만큼 처리
    [Space] O(log n) - 결과 문자열 길이
    """
    return str(n)


solution = solution_v1
