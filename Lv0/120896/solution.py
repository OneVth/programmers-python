"""
프로그래머스 Lv0 #120896 - 한 번만 등장한 문자
https://school.programmers.co.kr/learn/courses/30/lessons/120896

[문제]
문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를
사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

[제한]
- 0 < s의 길이 < 1,000
- s는 소문자로만 이루어져 있습니다.
"""


from collections import Counter


def solution_v1(s: str) -> str:
    """
    [Approach] Counter + 필터링 - 빈도 1인 문자만 추출 후 정렬
    [Time] O(n + k log k) - n: 문자열 길이, k: 고유 문자 수 (최대 26)
    [Space] O(k) - Counter 저장 공간
    """
    counter = Counter(s)
    return "".join(sorted(c for c in counter if counter[c] == 1))


solution = solution_v1
