"""
프로그래머스 Lv0 #120921 - 문자열 밀기
https://school.programmers.co.kr/learn/courses/30/lessons/120921

[문제]
문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로
이동시키면 "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가
매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를
return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

[제한]
- 0 < A의 길이 = B의 길이 < 100
- A, B는 알파벳 소문자로 이루어져 있습니다.
"""

from collections import deque


def solution_v1(A: str, B: str) -> int:
    """
    [Approach] deque로 직접 회전 - 매번 밀고 비교
    [Time] O(n²)  [Space] O(n) - n: 문자열 길이
    """

    temp = deque(A)
    for i in range(len(temp)):
        if "".join(temp) == B:
            return i

        temp.appendleft(temp.pop())

    return -1


def solution_v2(A: str, B: str) -> int:
    """
    [Approach] 문자열 2배 트릭 - (B*2)에서 A 위치 = 회전 횟수
    [Time] O(n)  [Space] O(n)
    """
    return (B * 2).find(A)


def solution_v3(A: str, B: str) -> int:
    """
    [Approach] deque.rotate() + 직접 비교 - join 없이 deque끼리 비교
    [Time] O(n²)  [Space] O(n)
    """
    a, b = deque(A), deque(B)
    for i in range(len(A)):
        if a == b:
            return i
        a.rotate(1)

    return -1


solution = solution_v2
