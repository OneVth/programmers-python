"""
프로그래머스 Lv0 #181855 - 문자열 묶기
https://school.programmers.co.kr/learn/courses/30/lessons/181855

[복습] 2차 - 2026-01-02

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
    [Approach] Counter로 길이별 빈도수 계산 후 최댓값 반환
    [Time] O(n)  [Space] O(k) - k는 고유한 문자열 길이 수 (최대 30)
    """
    from collections import Counter

    counter = Counter(len(s) for s in strArr)
    return max(counter.values())


solution = solution_v1
