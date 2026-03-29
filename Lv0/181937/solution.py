"""
프로그래머스 Lv0 #181937 - n의 배수
https://school.programmers.co.kr/learn/courses/30/lessons/181937

[문제]
정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return
n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

[제한]
- 2 ≤ num ≤ 100
- 2 ≤ n ≤ 9
"""


def solution_v1(num: int, n: int) -> int:
    """
    [Approach] bool → int 변환으로 나머지 연산 결과를 직접 반환
    [Time] O(1)  [Space] O(1)
    """
    return int(num % n == 0)


solution = solution_v1
