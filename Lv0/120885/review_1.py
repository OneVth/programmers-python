"""
프로그래머스 Lv0 #120885 - 이진수 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/120885

[복습] 1차 - 2025-12-17

[문제]
이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때,
두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

[제한]
- return 값은 이진수를 의미하는 문자열입니다.
- 1 ≤ bin1, bin2의 길이 ≤ 10
- bin1과 bin2는 0과 1로만 이루어져 있습니다.
- bin1과 bin2는 "0"을 제외하고 0으로 시작하지 않습니다.
"""


def solution_v1(bin1: str, bin2: str) -> str:
    """
    [Approach] 진법 변환 내장 함수 활용
               - int(x, 2): 이진수 문자열 → 정수
               - bin(): 정수 → '0b...' 형태 문자열
               - [2:]: '0b' 접두사 제거
    [Time] O(n) - 문자열 길이에 비례
    [Space] O(n) - 결과 문자열
    """
    return bin(int(bin1, 2) + int(bin2, 2))[2:]


def solution_v2(bin1: str, bin2: str) -> str:
    """
    [Approach] format() 함수로 직접 이진수 변환
               - format(n, 'b'): 접두사 없이 이진수 문자열 반환
               - 슬라이싱 불필요로 더 깔끔한 코드
    [Time] O(n) - 문자열 길이에 비례
    [Space] O(n) - 결과 문자열
    """
    return format(int(bin1, 2) + int(bin2, 2), "b")


solution = solution_v2
