"""
프로그래머스 Lv0 #181872 - 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/181872

[문제]
문자열 myString과 pat가 주어집니다.
myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는
solution 함수를 완성해 주세요.

[제한]
- 5 <= myString <= 20
- 1 <= pat <= 5
  - pat은 반드시 myString의 부분 문자열로 주어집니다.
- myString과 pat에 등장하는 알파벳은 대문자와 소문자를 구분합니다.
"""


def solution_v1(myString: str, pat: str) -> str:
    """
    [Approach] rindex()로 pat의 마지막 등장 위치를 찾아 슬라이싱
    [Time] O(N*M)  [Space] O(N)
    """
    idx = myString.rindex(pat)
    return myString[:idx] + pat


solution = solution_v1
