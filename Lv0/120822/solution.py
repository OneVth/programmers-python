"""
프로그래머스 Lv0 #120822 - 뒤집힌 문자열
https://school.programmers.co.kr/learn/courses/30/lessons/120822

[문제]
문자열 my_string이 매개변수로 주어집니다.
my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ my_string의 길이 ≤ 1,000
"""


def solution_v1(my_string: str) -> str:
    """
    [Approach] 슬라이싱 [::-1]
    [Time] O(n)  [Space] O(n)
    ✅ 가장 파이썬다운 방식
    """
    return my_string[::-1]


def solution_v2(my_string: str) -> str:
    """
    [Approach] reversed() + join()
    [Time] O(n)  [Space] O(n)
    """
    return "".join(reversed(my_string))


solution = solution_v1
