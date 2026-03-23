"""
프로그래머스 Lv0 #181921 - 배열 만들기 2
https://school.programmers.co.kr/learn/courses/30/lessons/181921

[문제]
정수 l 과 r 이 주어졌을 때, l 이상 r 이하의 정수 중에서
숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는
solution 함수를 완성해 주세요.
만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

[제한]
- 1 ≤ l ≤ r ≤ 1,000,000
"""


def solution_v1(l: int, r: int) -> list[int]:
    """
    [Approach] l~r 완전탐색 + 각 수의 자릿수 집합이 {"0","5"}의 부분집합인지 검사
    [Time] O(n * d)  [Space] O(k)  — n=r-l+1, d=자릿수, k=결과 개수
    """
    answer = []
    for i in range(l, r + 1):
        if {"0", "5"} == set(str(i)) or {"5"} == set(str(i)):
            answer.append(i)

    return answer if answer else [-1]


def solution_v2(l: int, r: int) -> list[int]:
    """
    [Approach] 부분집합 연산자(<=)로 자릿수 집합이 {"0","5"}에 속하는지 검사
    [Time] O(n * d)  [Space] O(k)  — n=r-l+1, d=자릿수, k=결과 개수
    """
    answer = []
    for i in range(l, r + 1):
        if set(str(i)) <= set(["0", "5"]):
            answer.append(i)
    return answer if answer else [-1]


def solution_v3(l: int, r: int) -> list[int]:
    """
    [Approach] 차집합이 공집합인지 확인 — 허용되지 않는 자릿수가 없음을 검사
    [Time] O(n * d)  [Space] O(k)  — n=r-l+1, d=자릿수, k=결과 개수
    """
    answer = []
    for i in range(l, r + 1):
        if not set(str(i)) - set(["0", "5"]):
            answer.append(i)
    return answer if answer else [-1]


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v3
