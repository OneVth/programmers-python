"""
프로그래머스 Lv0 #120812 - 최빈값 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120812

[복습] 2차 - 2026-01-02

[문제]
최빈값은 주어진 값 중에서 가장 자주 나타나는 값.
정수 배열 array가 매개변수로 주어질 때, 최빈값을 반환.
최빈값이 여러 개면 -1을 반환

[제한]
- 0 < array의 길이 < 100
- 0 ≤ array의 원소 < 1000
"""
from collections import Counter


def solution_v1(array: list[int]) -> int:
    """
    [Approach] Counter + 수동 정렬 - 빈도순 내림차순 정렬 후 상위 2개 비교
    [Time] O(n log n) - 정렬  [Space] O(k) - k: 고유 원소 수
    """
    if len(array) <= 1:
        return array[0]

    sorted_counter = sorted(Counter(array).items(), key=lambda x: x[1], reverse=True)

    if sorted_counter[0][1] == sorted_counter[1][1]:
        return -1

    return sorted_counter[0][0]


def solution_v2(array: list[int]) -> int:
    """
    [Approach] Counter.most_common() - 내장 메서드로 상위 2개 추출
    [Time] O(n log k) - heapq 사용  [Space] O(k) - k: 고유 원소 수
    ✅ most_common(k)은 k개만 필요할 때 heapq로 최적화됨
    """
    if len(array) <= 1:
        return array[0]

    mc = Counter(array).most_common(2)

    if mc[0][1] == mc[1][1]:
        return -1

    return mc[0][0]


# 기본 솔루션 지정
solution = solution_v2
