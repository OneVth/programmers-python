"""
프로그래머스 Lv0 #181941 - 문자 리스트를 문자열로 변환하기
https://school.programmers.co.kr/learn/courses/30/lessons/181941

[문제]
문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인
문자열을 return 하는 solution함수를 작성해 주세요.

[제한]
- 1 ≤ arr의 길이 ≤ 200
- arr의 원소는 전부 알파벳 소문자로 이루어진 길이가 1인 문자열입니다.
"""


def solution_v1(arr: list[str]) -> str:
    """
    [Approach] join()으로 리스트 원소를 구분자 없이 이어 붙여 반환
    [Time] O(n)  [Space] O(n)  ← 최종 문자열 길이에 비례
    """
    return "".join(arr)


solution = solution_v1
