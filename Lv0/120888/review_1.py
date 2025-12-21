"""
프로그래머스 Lv0 #120888 - 중복된 문자 제거
https://school.programmers.co.kr/learn/courses/30/lessons/120888

[복습] 1차 - 2025-12-17

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
    [Approach] 리스트로 순서 유지하며 중복 제거
               - 이미 등장한 문자인지 리스트에서 확인
               - 순서 보장, 첫 등장 문자만 유지
    [Time] O(n²) - 리스트 `in` 검사가 O(n)
    [Space] O(n) - 결과 리스트
    """
    answer = []
    for c in my_string:
        if c not in answer:
            answer.append(c)

    return "".join(answer)


def solution_v2(my_string: str) -> str:
    """
    [Approach] dict.fromkeys()로 순서 유지 중복 제거
               - Python 3.7+ dict는 삽입 순서 보장
               - fromkeys()는 중복 키 무시
    [Time] O(n) - dict 삽입 O(1) × n
    [Space] O(n) - dict 저장
    """
    return "".join(dict.fromkeys(my_string))


def solution_v3(my_string: str) -> str:
    """
    [Approach] set으로 O(1) 중복 검사 + 리스트로 순서 유지
               - seen set: 빠른 중복 확인
               - answer 리스트: 순서 보존
    [Time] O(n) - set `in` 검사 O(1)
    [Space] O(n) - set + 리스트
    """
    seen = set()
    answer = []
    for c in my_string:
        if c not in seen:
            seen.add(c)
            answer.append(c)
    return "".join(answer)


solution = solution_v3
