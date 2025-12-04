"""
프로그래머스 Lv0 #120811 - 중앙값 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120811

[문제]
중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값.
정수 배열 array가 매개변수로 주어질 때, 중앙값을 반환

[제한]
- array의 길이는 홀수
- 0 < array의 길이 < 100
- -1,000 < array의 원소 < 1,000
"""


def solution_v1(array: list[int]) -> int:
    """
    [Approach] 정렬 후 중앙 인덱스 접근
    [Time] O(n log n)  [Space] O(n)
    """
    sorted_arr = sorted(array)
    return sorted_arr[len(array) // 2]


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
