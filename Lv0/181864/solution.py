"""
프로그래머스 Lv0 #181864 - 문자열 바꿔서 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/181864

[문제]
문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다.
myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중
pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.

[제한]
- 1 ≤ myString의 길이 ≤ 100
- 1 ≤ pat의 길이 ≤ 10
  - myString과 pat는 문자 "A"와 "B"로만 이루어진 문자열입니다.
"""


def solution_v1(my_string: str, pat: str) -> int:
    """
    [Approach] translate로 A↔B 동시 치환 후 부분문자열 검사
    [Time] O(n+m)  [Space] O(n)
    - n: myString 길이, m: pat 길이
    """
    translated = my_string.translate(str.maketrans("AB", "BA"))
    return int(pat in translated)


solution = solution_v1
