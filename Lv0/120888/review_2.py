"""
프로그래머스 Lv0 #120888 - 중복된 문자 제거
https://school.programmers.co.kr/learn/courses/30/lessons/120888

[복습] 2차 - 2026-01-02

[문제]
문자열 my_string이 매개변수로 주어집니다.
my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ my_string ≤ 110
- my_string은 대문자, 소문자, 공백으로 구성되어 있습니다.
- 대문자와 소문자를 구분합니다.
- 공백(" ")도 하나의 문자로 구분합니다.
- 중복된 문자 중 가장 앞에 있는 문자를 남깁니다.
"""


def solution_v1(my_string: str) -> str:
    """
    [Approach] set으로 중복 체크하며 순서 보존 리스트 구축
    [Time] O(n)  [Space] O(k) - k는 고유 문자 수
    """
    answer = []
    seen = set()
    for c in my_string:
        if c not in seen:
            answer.append(c)
            seen.add(c)
    return "".join(answer)

def solution_v2(my_string: str) -> str:
    return "".join(dict.fromkeys(my_string))

# 기본 솔루션 지정
solution = solution_v2
