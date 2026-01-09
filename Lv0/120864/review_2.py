"""
프로그래머스 Lv0 #120864 - 숨어있는 숫자의 덧셈 (2)
https://school.programmers.co.kr/learn/courses/30/lessons/120864

[복습] 2차 - 2026-01-02

[문제]
문자열 my_string이 매개변수로 주어집니다.
my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
my_string 안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ my_string의 길이 ≤ 1,000
- 1 ≤ my_string 안의 자연수 ≤ 1000
- 연속된 수는 하나의 숫자로 간주합니다.
- 000123과 같이 0이 선행하는 경우는 없습니다.
- 문자열에 자연수가 없는 경우 0을 return 해주세요.
"""

import re


def solution_v1(my_string: str) -> int:
    """
    [Approach] 정규표현식으로 비숫자 문자 기준 분리 후 합산
    [Time] O(n)  [Space] O(n) - 분리된 문자열 리스트
    """
    return sum(int(s) for s in re.split(r"\D", my_string) if s)


def solution_v2(my_string: str) -> int:
    """
    [Approach] 정규표현식으로 연속 숫자 패턴 직접 추출 후 합산
    [Time] O(n)  [Space] O(n) - 매칭된 숫자 리스트
    """
    return sum(int(s) for s in re.findall(r"\d+", my_string))


# 기본 솔루션 지정
solution = solution_v2
