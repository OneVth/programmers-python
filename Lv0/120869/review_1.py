"""
프로그래머스 Lv0 #120869 - 외계어 사전
https://school.programmers.co.kr/learn/courses/30/lessons/120869

[복습] 1차 - 2025-12-17

[문제]
PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다.
알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다.
spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1,
존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.

[제한]
- spell과 dic의 원소는 알파벳 소문자로만 이루어져있습니다.
- 2 ≤ spell의 크기 ≤ 10
- spell의 원소의 길이는 1입니다.
- 1 ≤ dic의 크기 ≤ 10
- 1 ≤ dic의 원소의 길이 ≤ 10
- spell의 원소를 모두 사용해 단어를 만들어야 합니다.
- spell의 원소를 모두 사용해 만들 수 있는 단어는 dic에 두 개 이상 존재하지 않습니다.
- dic과 spell 모두 중복된 원소를 갖지 않습니다.
"""


def solution_v1(spell: list[str], dic: list[str]) -> int:
    """
    Set 비교 - 문자 집합 일치 확인

    [Approach]
    spell의 문자 집합과 dic의 각 단어 문자 집합을 비교.
    중복이 없으므로 set 동등 비교로 충분함.

    [Time] O(n * m) - n: dic 길이, m: 단어 최대 길이
    [Space] O(m) - set 저장 공간
    """
    spell_set = set(spell)

    for word in dic:
        if len(spell_set) != len(word):
            continue

        if spell_set == set(word):
            return 1

    return 2


def solution_v2(spell: list[str], dic: list[str]) -> int:
    """
    정렬 비교 + any - 한 줄 솔루션

    [Approach]
    정렬된 문자 리스트가 같으면 같은 문자 구성.
    any로 매칭되는 단어가 하나라도 있는지 확인.

    [Time] O(n * m log m) - 각 단어 정렬
    [Space] O(m) - 정렬된 리스트
    """
    sorted_spell = sorted(spell)
    return 1 if any(sorted_spell == sorted(word) for word in dic) else 2


# 기본 솔루션
solution = solution_v2
