"""
프로그래머스 Lv0 #181933 - flag에 따라 다른 값 반환하기
https://school.programmers.co.kr/learn/courses/30/lessons/181933

[문제]
두 정수 a, b 와 boolean 변수 flag 가 매개변수로 주어질 때,
flag 가 true면 a+b 를 false면 a-b 를 return 하는 solution 함수를 작성해 주세요.

[제한]
- -1,000 ≤ a, b ≤ 1,000
"""


def solution_v1(a: int, b: int, flag: bool) -> int:
    """
    [Approach] 삼항 조건 표현식으로 flag에 따라 덧셈/뺄셈 분기
    [Time] O(1)  [Space] O(1)
    """
    return (a + b) if flag else (a - b)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
