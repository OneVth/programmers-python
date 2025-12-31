"""
프로그래머스 Lv0 #181867 - x 사이의 개수
https://school.programmers.co.kr/learn/courses/30/lessons/181867

[문제]
문자열 myString이 주어집니다. myString을 문자 "x"를 기준으로 나눴을 때
나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는
solution 함수를 완성해 주세요.

[제한]
- 1 ≤ myString의 길이 ≤ 100,000
  - myString은 알파벳 소문자로 이루어진 문자열입니다.
"""


def solution_v1(myString: str) -> list[int]:
    """
    [Approach] split + len: "x"로 분할 후 각 부분 길이 계산
    [Time] O(n)  [Space] O(n)
    """
    return [len(x) for x in myString.split("x")]


solution = solution_v1
