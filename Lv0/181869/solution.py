"""
프로그래머스 Lv0 #181869 - 공백으로 구분하기 1
https://school.programmers.co.kr/learn/courses/30/lessons/181869

[문제]
단어가 공백 한 개로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때,
my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는
solution 함수를 작성해 주세요.

[제한]
- my_string은 영소문자와 공백으로만 이루어져 있습니다.
- 1 ≤ my_string의 길이 ≤ 1,000
- my_string의 맨 앞과 맨 뒤에 글자는 공백이 아닙니다.
"""


def solution_v1(my_string: str) -> list[str]:
    """
    [Approach] str.split()으로 공백 기준 분리
    [Time] O(n)  [Space] O(n)
    """
    return my_string.split()


solution = solution_v1
