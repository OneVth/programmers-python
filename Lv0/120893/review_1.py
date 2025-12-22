"""
프로그래머스 Lv0 #120893 - 대문자와 소문자
https://school.programmers.co.kr/learn/courses/30/lessons/120893

[복습] 1차 - 2025-12-17

[문제]
문자열 my_string이 매개변수로 주어질 때,
대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ my_string의 길이 ≤ 1,000
- my_string은 영어 대문자와 소문자로만 구성되어 있습니다.
"""


def solution_v1(my_string: str) -> str:
    """
    [Approach] 내장 메서드 swapcase()로 대소문자 일괄 변환
    [Time] O(n) - 문자열 길이만큼 순회
    [Space] O(n) - 새 문자열 생성
    """
    return my_string.swapcase()


# ✅ 기본 솔루션 지정
solution = solution_v1
