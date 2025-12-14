"""
프로그래머스 Lv0 #120888 - 중복된 문자 제거
https://school.programmers.co.kr/learn/courses/30/lessons/120888

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
    [Approach] 문자열 누적 - 새 문자만 answer에 추가
    [Time] O(n²) - 매 문자마다 in 검사 O(n)
    [Space] O(n) - 결과 문자열
    """
    answer = ""
    for c in my_string:
        if c not in answer:
            answer += c

    return answer


def solution_v2(my_string: str) -> str:
    """
    [Approach] 리스트 누적 - v1과 동일하나 리스트 사용
    [Time] O(n²) - 매 문자마다 in 검사 O(n)
    [Space] O(n)
    """
    answer = []
    for c in my_string:
        if c not in answer:
            answer.append(c)

    return "".join(answer)


def solution_v3(my_string: str) -> str:
    """
    [Approach] dict.fromkeys() - 삽입 순서 유지하며 중복 제거
    [Time] O(n) - dict 삽입은 평균 O(1)
    [Space] O(n)
    """
    return "".join(dict.fromkeys(my_string))


def solution_v4(my_string: str) -> str:
    seen = set()
    result = []

    for c in my_string:
        if c not in seen:
            seen.add(c)
            result.append(c)

    return "".join(result)


solution = solution_v4
