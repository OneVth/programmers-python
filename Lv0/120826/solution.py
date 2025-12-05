"""
프로그래머스 Lv0 #120826 - 특정 문자 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/120826

[문제]
문자열 my_string과 문자 letter이 매개변수로 주어집니다.
my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ my_string의 길이 ≤ 100
- letter은 길이가 1인 영문자입니다.
- my_string과 letter은 알파벳 대소문자로 이루어져 있습니다.
- 대문자와 소문자를 구분합니다.
"""


def solution_v1(my_string: str, letter: str) -> str:
    """
    [Approach] str.replace() 내장 메서드
    [Time] O(n)  [Space] O(n)
    ✅ 가장 간결하고 효율적
    """
    return my_string.replace(letter, "")


def solution_v2(my_string: str, letter: str) -> str:
    """
    [Approach] join + generator expression 필터링
    [Time] O(n)  [Space] O(n)
    ✅ 조건부 필터링에 유연함
    """
    return "".join(x for x in my_string if x != letter)


solution = solution_v1
