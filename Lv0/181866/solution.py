"""
프로그래머스 Lv0 #181866 - 문자열 잘라서 정렬하기
https://school.programmers.co.kr/learn/courses/30/lessons/181866

[문제]
문자열 myString이 주어집니다. "x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후
사전순으로 정렬한 배열을 return 하는 solution 함수를 완성해 주세요.
단, 빈 문자열은 반환할 배열에 넣지 않습니다.

[제한]
- 1 ≤ myString ≤ 100,000
  - myString은 알파벳 소문자로 이루어진 문자열입니다.
"""


def solution_v1(my_string: str) -> list[str]:
    """
    [Approach] split 후 빈 문자열 필터링 + 정렬을 한 줄로
    [Time] O(n log n)  [Space] O(n)
    - n: 분할된 부분문자열 개수
    """
    return sorted(s for s in my_string.split("x") if s)


solution = solution_v1
