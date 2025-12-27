"""
프로그래머스 Lv0 #181847 - 0 떼기
https://school.programmers.co.kr/learn/courses/30/lessons/181847

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
    [Approach] while 루프로 첫 번째 비-0 문자 인덱스 탐색 후 슬라이싱
    [Time] O(n) - 최악의 경우 전체 문자열 순회
    [Space] O(n) - 슬라이싱된 결과 문자열
    """
    idx = 0
    while n_str[idx] == "0":
        idx += 1

    return n_str[idx:]


def solution_v2(n_str: str) -> str:
    """
    [Approach] 정수 변환 후 다시 문자열로 (leading zeros 자동 제거)
    [Time] O(n) - int/str 변환
    [Space] O(n) - 결과 문자열
    """
    return str(int(n_str))


def solution_v3(n_str: str) -> str:
    """
    [Approach] lstrip으로 왼쪽 '0' 문자들 제거
    [Time] O(n) - 문자열 순회
    [Space] O(n) - 결과 문자열
    """
    return n_str.lstrip("0")


solution = solution_v1
