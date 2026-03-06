"""
프로그래머스 Lv0 #181877 - 대문자로 바꾸기
https://school.programmers.co.kr/learn/courses/30/lessons/181877

[문제]
알파벳으로 이루어진 문자열 myString이 주어집니다.
모든 알파벳을 대문자로 변환하여 return 하는 solution 함수를 완성해 주세요.

[제한]
- 1 <= myString의 길이 <= 100,000
  - myString은 알파벳으로 이루어진 문자열입니다.
"""


def solution_v1(myString: str) -> str:
    """
    [Approach] str.upper() 내장 메서드로 전체 대문자 변환
    [Time] O(n)  [Space] O(n)
    """
    return myString.upper()


solution = solution_v1
