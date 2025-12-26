"""
프로그래머스 Lv0 #181842 - 부분 문자열
https://school.programmers.co.kr/learn/courses/30/lessons/181842

[문제]
어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다.
예를 들어 문자열 "abc"는 문자열 "aabcc"의 부분 문자열입니다.

문자열 str1과 str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을
부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ str1 ≤ str2 ≤ 20
- str1과 str2는 영어 소문자로만 이루어져 있습니다.
"""


def solution_v1(str1: str, str2: str) -> int:
    """
    [Approach] in 연산자로 부분 문자열 포함 여부 확인 후 int 변환
    [Time] O(n * m) - n: str2 길이, m: str1 길이 (문자열 매칭)
    [Space] O(1)
    """
    return int(str1 in str2)


# ✅ 기본 솔루션 지정
solution = solution_v1
