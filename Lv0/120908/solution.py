"""
프로그래머스 Lv0 #120908 - 문자열안에 문자열
https://school.programmers.co.kr/learn/courses/30/lessons/120908

[문제]
문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을
없다면 2를 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ str1의 길이 ≤ 100
- 1 ≤ str2의 길이 ≤ 100
- 문자열은 알파벳 대문자, 소문자, 숫자로 구성되어 있습니다.
"""


def solution_v1(str1: str, str2: str) -> int:
    """
    [Approach] in 연산자 - 부분 문자열 포함 여부 확인
    [Time] O(n * m)  [Space] O(1) - n: str1 길이, m: str2 길이
    """
    return 1 if str2 in str1 else 2


def solution_v2(str1: str, str2: str) -> int:
    """
    [Approach] find() 메서드 - 부분 문자열 위치 확인
    [Time] O(n * m)  [Space] O(1)
    """
    return 1 if str1.find(str2) != -1 else 2

solution = solution_v1