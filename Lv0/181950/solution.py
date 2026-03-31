"""
프로그래머스 Lv0 #181950 - 문자열 반복해서 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/181950

[문제]
문자열 str과 정수 n이 주어집니다.
str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

[제한]
- 1 ≤ str의 길이 ≤ 10
- 1 ≤ n ≤ 5
"""


def solution_v1(str: str, n: int) -> str:
    """
    [Approach] 문자열 반복 연산자 * 활용
    [Time] O(n)  [Space] O(n)
    """
    return str * n


solution = solution_v1
