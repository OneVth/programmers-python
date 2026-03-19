"""
프로그래머스 Lv0 #181907 - 문자열의 앞의 n글자
https://school.programmers.co.kr/learn/courses/30/lessons/181907

[문제]
문자열 my_string 과 정수 n 이 매개변수로 주어질 때,
my_string 의 앞의 n 글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- my_string은 숫자와 알파벳으로 이루어져 있습니다.
- 1 ≤ my_string의 길이 ≤ 1,000
- 1 ≤ n ≤ my_string의 길이
"""


def solution(my_string: str, n: int) -> str:
    """
    [Approach] 슬라이싱 [:n] — 접두사의 정의 자체
    [Time] O(n)  [Space] O(n)
    """
    return my_string[:n]
