"""
프로그래머스 Lv0 #181910 - 문자열의 뒤의 n글자
https://school.programmers.co.kr/learn/courses/30/lessons/181910

[문제]
문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진
문자열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- my_string은 숫자와 알파벳으로 이루어져 있습니다.
- 1 ≤ my_string의 길이 ≤ 1,000
- 1 ≤ n ≤ my_string의 길이
"""


def solution_v1(my_string: str, n: int) -> str:
    """
    [Approach] 음수 슬라이싱으로 뒤의 n글자 추출
    [Time] O(n)  [Space] O(n)
    """
    return my_string[-n:]


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
