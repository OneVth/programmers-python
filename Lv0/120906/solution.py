"""
프로그래머스 Lv0 #120906 - 자릿수 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/120906

[문제]
정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록
solution 함수를 완성해주세요.

[제한]
- 0 ≤ n ≤ 1,000,000
"""


def solution_v1(n: int) -> int:
    """
    [Approach] 문자열 변환 - 각 자릿수를 문자로 분리 후 합산
    [Time] O(d)  [Space] O(d) - d: 자릿수 (최대 7)
    """
    return sum(int(x) for x in str(n))


def solution_v2(n: int) -> int:
    """
    [Approach] 수학적 접근 - 나머지/몫 연산으로 자릿수 추출
    [Time] O(d)  [Space] O(1)
    """
    temp = n
    result = 0
    while temp:
        result += temp % 10
        temp //= 10
    return result


solution = solution_v2
