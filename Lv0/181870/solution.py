"""
프로그래머스 Lv0 #181870 - ad 제거하기
https://school.programmers.co.kr/learn/courses/30/lessons/181870

[문제]
문자열 배열 strArr가 주어집니다. 배열 내의 문자열 중 "ad"라는 부분 문자열을
포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로
return 하는 solution 함수를 완성해 주세요.

[제한]
- 1 ≤ strArr의 길이 ≤ 1,000
  - 1 ≤ strArr의 원소의 길이 ≤ 20
  - strArr의 원소는 알파벳 소문자로 이루어진 문자열입니다.
"""


def solution_v1(strArr: list[str]) -> list[str]:
    """
    [Approach] 리스트 컴프리헨션 + in 연산자로 부분 문자열 필터링
    [Time] O(n * m)  [Space] O(n)
    - n: strArr 길이, m: 각 원소의 평균 길이
    """
    return [s for s in strArr if "ad" not in s]


solution = solution_v1
