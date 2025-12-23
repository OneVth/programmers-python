"""
프로그래머스 Lv0 #120921 - 문자열 밀기
https://school.programmers.co.kr/learn/courses/30/lessons/120921

[복습] 1차 - 2025-12-17

[문제]
문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로
이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가
매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를
return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

[제한]
- 0 < A의 길이 = B의 길이 < 100
- A, B는 알파벳 소문자로 이루어져 있습니다.
"""


def solution_v1(A: str, B: str) -> int:
    """
    [Approach] B를 두 번 이어붙인 문자열에서 A의 위치 = 밀기 횟수
    [Time] O(n) - find()의 평균 시간복잡도 (n은 문자열 길이)
    [Space] O(n) - B+B 문자열 생성
    """
    return (B + B).find(A)


def solution_v2(A: str, B: str) -> int:
    """
    [Approach] deque의 rotate()로 실제 문자열 회전 시뮬레이션
    [Time] O(n²) - n번 회전, 각 비교 O(n)
    [Space] O(n) - deque 2개 생성
    """
    from collections import deque

    a, b = deque(A), deque(B)
    for i in range(len(A)):
        if a == b:
            return i
        a.rotate(1)

    return -1


solution = solution_v2
