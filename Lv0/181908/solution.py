"""
프로그래머스 Lv0 #181908 - 접미사인지 확인하기
https://school.programmers.co.kr/learn/courses/30/lessons/181908

[문제]
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다.
예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string 과 is_suffix 가 주어질 때,
is_suffix 가 my_string 의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ my_string의 길이 ≤ 100
- 1 ≤ is_suffix의 길이 ≤ 100
- my_string과 is_suffix는 영소문자로만 이루어져 있습니다.
"""


def solution(my_string: str, is_suffix: str) -> int:
    """
    [Approach] endswith() 직접 사용 후 int 변환 — startswith()의 대칭 버전
    [Time] O(k)  [Space] O(1)  (k = len(is_suffix))
    """
    return int(my_string.endswith(is_suffix))
