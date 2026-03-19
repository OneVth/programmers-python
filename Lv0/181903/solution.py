"""
프로그래머스 Lv0 #181903 - qr code
https://school.programmers.co.kr/learn/courses/30/lessons/181903

[문제]
두 정수 q, r 과 문자열 code 가 주어질 때,
code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를
앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 0 ≤ r < q ≤ 20
- r < code의 길이 ≤ 1,000
- code는 영소문자로만 이루어져 있습니다.
"""


def solution_v1(q: int, r: int, code: str) -> str:
    """
    [Approach] range(r, len(code), q)로 나머지가 r인 인덱스를 직접 생성 후 join
    [Time] O(n/q)  [Space] O(n/q)
    """
    return "".join(code[i] for i in range(r, len(code), q))


def solution_v2(q: int, r: int, code: str) -> str:
    """
    [Approach] 문자열 슬라이싱 code[r::q] — 시작 r, 스텝 q
    [Time] O(n/q)  [Space] O(n/q)
    """
    return code[r::q]


solution = solution_v2
