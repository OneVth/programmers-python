"""
프로그래머스 Lv0 #181873 - 특정한 문자를 대문자로 바꾸기
https://school.programmers.co.kr/learn/courses/30/lessons/181873

[문제]
영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가
매개변수로 주어질 때, my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼
문자열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 <= my_string의 길이 <= 1,000
"""


def solution_v1(my_string: str, alp: str) -> str:
    """
    [Approach] for 루프로 각 문자를 순회하며 조건부 대문자 변환 후 join
    [Time] O(N)  [Space] O(N)
    """
    temp = []
    for c in my_string:
        if c == alp:
            temp.append(c.upper())
        else:
            temp.append(c)

    return "".join(temp)

def solution_v2(my_string: str, alp: str) -> str:
    """
    [Approach] 리스트 컴프리헨션으로 조건부 대문자 변환 후 join
    [Time] O(N)  [Space] O(N)
    """
    return "".join([c.upper() if c == alp else c for c in my_string])

def solution_v3(my_string: str, alp: str) -> str:
    """
    [Approach] str.replace()로 해당 문자를 대문자로 일괄 치환
    [Time] O(N)  [Space] O(N)
    """
    return my_string.replace(alp, alp.upper())

solution = solution_v2