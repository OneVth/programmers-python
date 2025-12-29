"""
프로그래머스 Lv0 #181863 - rny_string
https://school.programmers.co.kr/learn/courses/30/lessons/181863

[문제]
'm'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다.
문자열 rny_string이 주어질 때, rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을
return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ rny_string의 길이 ≤ 100
- rny_string은 영소문자로만 이루어져 있습니다.
"""


def solution_v1(rny_string: str) -> str:
    """
    [Approach] str.replace()로 'm'을 "rn"으로 치환
    [Time] O(n)  [Space] O(n)
    """
    return rny_string.replace("m", "rn")


solution = solution_v1
