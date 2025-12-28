"""
프로그래머스 Lv0 #181855 - 문자열 묶기
https://school.programmers.co.kr/learn/courses/30/lessons/181855

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
    [Approach] 딕셔너리로 길이별 문자열 그룹화 후 최대 그룹 크기 반환
    [Time] O(n)  [Space] O(n)
    """
    temp = dict()
    for s in strArr:
        value = temp.get(len(s), [])
        value.append(s)
        temp[len(s)] = value

    return max(map(len, temp.values()))


def solution_v2(strArr: list[str]) -> int:
    """
    [Approach] 고정 크기 배열(31)로 길이별 카운트 - 제한조건 활용
    [Time] O(n)  [Space] O(1) - 고정 크기 31
    """
    answer = [0] * 31
    for s in strArr:
        answer[len(s)] += 1

    return max(answer)


def solution_v3(strArr: list[str]) -> int:
    """
    [Approach] 딕셔너리로 길이별 카운트 (dict.get 활용)
    [Time] O(n)  [Space] O(k) - k는 고유 길이 수 (최대 30)
    """
    d = dict()
    for s in strArr:
        d[len(s)] = d.get(len(s), 0) + 1

    return max(d.values())


def solution_v4(strArr: list[str]) -> int:
    """
    [Approach] Counter로 길이별 빈도 계산 - 가장 Pythonic한 방식
    [Time] O(n)  [Space] O(k) - k는 고유 길이 수 (최대 30)
    """
    from collections import Counter

    c = Counter(len(s) for s in strArr)
    return max(c.values())


solution = solution_v4
