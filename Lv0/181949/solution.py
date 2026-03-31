"""
프로그래머스 Lv0 #181949 - 대소문자 바꿔서 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/181949

[문제]
영어 알파벳으로 이루어진 문자열 str이 주어집니다.
각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

[제한]
- 1 ≤ str의 길이 ≤ 20
- str은 알파벳으로 이루어진 문자열입니다.
"""


def solution_v1(str: str) -> str:
    """
    [Approach] 파이썬 내장 swapcase() 메서드 활용
    [Time] O(n)  [Space] O(n)
    """
    return str.swapcase()


solution = solution_v1
