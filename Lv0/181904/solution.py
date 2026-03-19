"""
프로그래머스 Lv0 #181904 - 세로 읽기
https://school.programmers.co.kr/learn/courses/30/lessons/181904

[문제]
문자열 my_string 과 두 정수 m, c 가 주어집니다.
my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌
글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

[제한]
- my_string은 영소문자로 이루어져 있습니다.
- 1 ≤ m ≤ my_string의 길이 ≤ 1,000
- m은 my_string 길이의 약수로만 주어집니다.
- 1 ≤ c ≤ m
"""


def solution(my_string: str, m: int, c: int) -> str:
    """
    [Approach] 슬라이싱 [c-1::m] — c번째 열의 시작 인덱스(c-1)부터 m 간격으로 추출
    [Time] O(n/m)  [Space] O(n/m)
    """
    return my_string[c - 1::m]
