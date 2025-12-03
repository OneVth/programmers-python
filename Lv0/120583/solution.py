"""
프로그래머스 Lv0 #120583 - 배열의 값 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/120583

[문제]
정수 배열 array와 정수 n이 주어질 때, array에 n이 몇 개 있는지 반환

[제한]
- 1 ≤ array의 길이 ≤ 100
- 0 ≤ array의 원소 ≤ 1,000
- 0 ≤ n ≤ 1,000
"""


def solution_v1(array: list[int], n: int) -> int:
    """
    [Approach] 내장 count 메서드
    [Time] O(n)  [Space] O(1)
    """
    return array.count(n)


def solution_v2(array: list[int], n: int) -> int:
    """
    [Approach] 수동 반복
    [Time] O(n)  [Space] O(1)
    """
    count = 0
    for item in array:
        if item == n:
            count += 1
    return count


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
