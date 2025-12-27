"""
프로그래머스 Lv0 #181849 - 문자열 정수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/181849

[문제]
한 자리 정수로 이루어진 문자열 num_str이 주어질 때,
각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

[제한]
- 3 ≤ num_str ≤ 100
"""


def solution_v1(num_str: str) -> int:
    """
    [Approach] 제너레이터 표현식으로 각 문자를 정수 변환 후 합산
    [Time] O(n) - 문자열 순회
    [Space] O(1) - 제너레이터는 메모리 상수
    """
    return sum(int(x) for x in num_str)


solution = solution_v1
