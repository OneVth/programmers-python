"""
프로그래머스 Lv0 #120585 - 머쓱이보다 키 큰 사람
https://school.programmers.co.kr/learn/courses/30/lessons/120585

[문제]
정수 배열 array와 정수 height가 주어질 때, array에 height보다 큰 정수가 몇 개 있는지 반환

[제한]
- 1 ≤ array의 길이 ≤ 100
- 1 ≤ array의 원소 ≤ 200
- 1 ≤ height ≤ 200
"""


def solution_v1(array: list[int], height: int) -> int:
    """
    [Approach] 수동 반복 + 카운터
    [Time] O(n)  [Space] O(1)
    """
    result = 0
    for i in range(len(array)):
        if array[i] > height:
            result += 1
    return result


def solution_v2(array: list[int], height: int) -> int:
    """
    [Approach] 정렬 후 인덱스 탐색
    [Time] O(n log n)  [Space] O(n)
    ⚠️ 원본 배열 수정됨 (sort in-place)
    """
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)


def solution_v3(array: list[int], height: int) -> int:
    """
    [Approach] Generator + sum (Pythonic)
    [Time] O(n)  [Space] O(1)
    ✅ 가장 간결하고 효율적
    """
    return sum(1 for a in array if a > height)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v3
