"""
프로그래머스 Lv0 #181946 - 문자열 붙여서 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/181946

[문제]
두 개의 문자열 str1, str2 가 공백으로 구분되어 입력으로 주어집니다.
str1 과 str2 를 이어서 출력하는 코드를 작성해 보세요.

[제한]
- 1 ≤ str1, str2 의 길이 ≤ 10
"""


def solution_v1(str1: str, str2: str) -> str:
    """
    [Approach] + 연산자로 두 문자열 직접 연결
    [Time] O(n)  [Space] O(n)
    """
    return str1 + str2


solution = solution_v1
