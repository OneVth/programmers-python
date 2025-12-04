"""
프로그래머스 Lv0 #120812 - 최빈값 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120812

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
    [Approach] dict + 수동 카운팅 + 정렬
    [Time] O(n²)  [Space] O(n)
    ⚠️ array.count()가 O(n)이고 n번 호출
    """
    dic = dict()
    for num in array:
        dic[num] = array.count(num)

    sorted_tu = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    if len(sorted_tu) > 1:
        if sorted_tu[0][1] == sorted_tu[1][1]:
            return -1

    return sorted_tu[0][0]


def solution_v2(array: list[int]) -> int:
    """
    [Approach] 카운팅 배열 (0~1000 범위)
    [Time] O(n + 1001)  [Space] O(1001)
    ✨ 정렬 없이 해결
    """
    idx = [0] * 1001
    for i in array:
        idx[i] += 1
    if idx.count(max(idx)) > 1:
        return -1
    return idx.index(max(idx))


def solution_v3(array: list[int]) -> int:
    """
    [Approach] Counter.most_common()
    [Time] O(n log n)  [Space] O(n)
    ✅ 가장 간결하고 Pythonic
    """
    mc = Counter(array).most_common(2)

    if len(mc) > 1:
        if mc[0][1] == mc[1][1]:
            return -1

    return mc[0][0]


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v3
