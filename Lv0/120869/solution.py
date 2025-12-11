"""
프로그래머스 Lv0 #120869 - 외계어 사전
https://school.programmers.co.kr/learn/courses/30/lessons/120869

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
    count 검증 + for-else

    [Approach] 각 단어에서 spell의 모든 문자가 정확히 1번씩 등장하는지 확인
    [Time] O(d * s * w) - d: dic 크기, s: spell 크기, w: 단어 길이
    [Space] O(1)
    """
    for word in dic:
        if len(word) != len(spell):
            continue
        for c in spell:
            if word.count(c) != 1:
                break
        else:
            return 1
    return 2


def solution_v2(spell: list[str], dic: list[str]) -> int:
    """
    sorted 비교

    [Approach] spell을 정렬한 것과 단어를 정렬한 것이 같은지 비교
    [Time] O(d * s log s) - s: spell 크기
    [Space] O(s)
    """
    target = sorted(spell)
    return 1 if any(sorted(word) == target for word in dic) else 2


def solution_v3(spell: list[str], dic: list[str]) -> int:
    """
    set 비교 (길이 체크 필수)

    [Approach] spell을 set으로 만들고, 단어도 set으로 만들어 비교
               단, 길이가 같아야 중복 문자가 없음을 보장
    [Time] O(d * s)
    [Space] O(s)
    """
    spell_set = set(spell)
    for word in dic:
        if len(word) == len(spell) and set(word) == spell_set:
            return 1
    return 2


# 기본 솔루션
solution = solution_v2
