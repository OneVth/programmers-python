"""
프로그래머스 Lv0 #181915 - 글자 이어 붙여 문자열 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/181915

[문제]
문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다.
my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인
문자열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ my_string의 길이 ≤ 1,000
- my_string의 원소는 영소문자로 이루어져 있습니다.
- 1 ≤ index_list의 길이 ≤ 1,000
- 0 ≤ index_list의 원소 < my_string의 길이
"""


def solution_v1(my_string: str, index_list: list[int]) -> str:
    """
    [Approach] index_list 순서대로 my_string에서 문자를 꺼내 join으로 이어 붙임
    [Time] O(N)  [Space] O(N)
    """
    return "".join(my_string[i] for i in index_list)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
