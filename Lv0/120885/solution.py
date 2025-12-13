"""
프로그래머스 Lv0 #120885 - 이진수 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/120885

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
    [Approach] 내장 함수 활용 - int(x, 2)로 10진수 변환 후 덧셈, bin()으로 이진수 변환
               bin() 결과의 '0b' 접두사 제거를 위해 [2:] 슬라이싱
    [Time] O(N) - N: 이진수 문자열 길이
    [Space] O(N) - 결과 문자열
    """
    return bin(int(bin1, 2) + int(bin2, 2))[2:]


def solution_v2(bin1: str, bin2: str) -> str:
    """
    [Approach] 수동 이진수 덧셈 - 문자열 뒤집어서 LSB부터 carry 처리하며 더함
               실제 이진수 덧셈 원리 구현 (면접에서 유용)
    [Time] O(N) - N: 더 긴 이진수 길이
    [Space] O(N) - 결과 문자열
    """
    bin1, bin2 = bin1[::-1], bin2[::-1]
    i, carry = 0, 0
    output = ""

    while i < len(bin1) or i < len(bin2) or carry:
        op1 = bin1[i] if i < len(bin1) else "0"
        op2 = bin2[i] if i < len(bin2) else "0"
        result = int(op1) + int(op2) + carry
        output += str(result % 2)
        carry = result // 2
        i += 1

    return output[::-1]


solution = solution_v2
