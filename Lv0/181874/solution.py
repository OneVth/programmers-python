"""
프로그래머스 Lv0 #181874 - A 강조하기
https://school.programmers.co.kr/learn/courses/30/lessons/181874

[문제]
문자열 myString이 주어집니다.
myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고,
"A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여
return 하는 solution 함수를 완성하세요.

[제한]
- 1 <= myString의 길이 <= 20
  - myString은 알파벳으로 이루어진 문자열입니다.
"""


def solution_v1(myString: str) -> str:
    """
    [Approach] str.translate + str.maketrans로 문자 매핑 테이블을 만들어 일괄 변환
    [Time] O(n)  [Space] O(n)
    """
    return myString.translate(str.maketrans("aBCDEFGHIJKLMNOPQRSTUVWXYZ", "Abcdefghijklmnopqrstuvwxyz"))

def solution_v2(myString: str) -> str:
    """
    [Approach] lower()로 전체 소문자 변환 후 "a"만 "A"로 치환
    [Time] O(n)  [Space] O(n)
    """
    return myString.lower().replace("a", "A")


solution = solution_v2
