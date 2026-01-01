"""
프로그래머스 Lv0 #181855 - 문자열 묶기
https://school.programmers.co.kr/learn/courses/30/lessons/181855

[복습] 1차 - 2025-12-31

[문제]
문자열 배열 strArr이 주어집니다.
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때
가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.

[제한]
- 1 ≤ strArr의 길이 ≤ 100,000
  - 1 ≤ strArr의 원소의 길이 ≤ 30
  - strArr의 원소들은 알파벳 소문자로 이루어진 문자열입니다.
"""


def solution_v1(strArr: list[str]) -> int:
    """
    [Approach] 길이별로 문자열 그룹화 후 최대 그룹 크기 반환
    [Time] O(n) - 한 번 순회
    [Space] O(n) - 문자열들을 리스트로 저장
    """
    answer = dict()

    for s in strArr:
        temp = answer.get(len(s), [])
        temp.append(s)
        answer[len(s)] = temp

    return max(map(len, answer.values()))


def solution_v2(strArr: list[str]) -> int:
    """
    [Approach] Counter로 길이별 개수만 카운트
    [Time] O(n) - 한 번 순회
    [Space] O(k) - k: 서로 다른 길이 개수 (최대 30)
    """
    from collections import Counter

    return max(Counter(len(s) for s in strArr).values())


solution = solution_v2
