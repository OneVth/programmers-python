"""
프로그래머스 Lv0 #181890 - 왼쪽 오른쪽
https://school.programmers.co.kr/learn/courses/30/lessons/181890

[문제]
문자열 리스트 str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장되어 있습니다.
str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면
해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를,
먼저 나오는 문자열이 "r"이라면
해당 문자열을 기준으로 오른쪽에 있는 문자열들을 순서대로 담은 리스트를
return하도록 solution 함수를 완성해주세요.
"l"이나 "r"이 없다면 빈 리스트를 return합니다.

[제한]
- 1 ≤ str_list의 길이 ≤ 20
- str_list는 "u", "d", "l", "r" 네 개의 문자열로 이루어져 있습니다.
"""


def solution_v1(str_list: list[str]) -> list[str]:
    """
    [Approach] 순회하며 "l" 또는 "r"을 먼저 만나면 early return으로 슬라이싱
    [Time] O(n)  [Space] O(n)
    """
    for i, c in enumerate(str_list):
        if c == "l":
            return str_list[:i]
        elif c == "r":
            return str_list[i + 1:]

    return []


solution = solution_v1
