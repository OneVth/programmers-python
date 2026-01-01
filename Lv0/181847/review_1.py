"""
프로그래머스 Lv0 #181847 - 0 떼기
https://school.programmers.co.kr/learn/courses/30/lessons/181847

[복습] 1차 - 2025-12-31

[문제]
정수로 이루어진 문자열 n_str이 주어질 때,
n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록
solution 함수를 완성해주세요.

[제한]
- 2 ≤ n_str ≤ 10
- n_str이 "0"으로만 이루어진 경우는 없습니다.
"""


def solution_v1(n_str: str) -> str:
    """
    [Approach] lstrip()으로 왼쪽 0 제거
    [Time] O(n) - 문자열 길이만큼 순회
    [Space] O(n) - 새 문자열 생성
    """
    return n_str.lstrip("0")


solution = solution_v1
