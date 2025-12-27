"""
프로그래머스 Lv0 #181846 - 두 수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/181846

[문제]
0 이상의 두 정수가 문자열 a, b로 주어질 때,
a + b의 값을 문자열로 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ a의 길이 ≤ 100,000
- 1 ≤ b의 길이 ≤ 100,000
- a와 b는 숫자로만 이루어져 있습니다.
- a와 b는 정수 0이 아니라면 0으로 시작하지 않습니다.
"""


def solution_v1(a: str, b: str) -> str:
    """
    [Approach] Python 임의 정밀도 정수로 변환 후 덧셈
    [Time] O(n) - n은 자릿수, int 변환/덧셈/str 변환 모두 O(n)
    [Space] O(n) - 결과 문자열
    """
    return str(int(a) + int(b))


solution = solution_v1
