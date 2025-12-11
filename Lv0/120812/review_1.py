"""
프로그래머스 Lv0 #120812 - 최빈값 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120812

[복습] 1차 - 2025-12-10

[문제]
최빈값은 주어진 값 중에서 가장 자주 나타나는 값.
정수 배열 array가 매개변수로 주어질 때, 최빈값을 반환.
최빈값이 여러 개면 -1을 반환

[제한]
- 0 < array의 길이 < 100
- 0 ≤ array의 원소 < 1000
"""


def solution_v1(array: list[int]) -> int:
    """
    [Approach] 카운팅 배열 - 인덱스를 요소로, 값을 빈도수로 사용
    [Time] O(n²)  [Space] O(1001) = O(1)
    ⚠️ array.count()가 O(n)이고 n번 호출
    """
    freq = [0] * 1001
    for i in array:
        freq[i] = array.count(i)

    max_freq = max(freq)
    if freq.count(max_freq) > 1:
        return -1

    for i in range(1001):
        if freq[i] == max_freq:
            return i


def solution_v2(array: list[int]) -> int:
    """
    [Approach] dict 카운팅 + 정렬로 최빈값 탐색
    [Time] O(n² + n log n)  [Space] O(n)
    ⚠️ array.count() 중복 호출, 정렬 비용
    """
    temp = dict()

    for i in array:
        temp[i] = array.count(i)

    freq = sorted(list(temp.values()), reverse=True)

    if len(freq) <= 1:
        for i in array:
            if temp[i] == freq[0]:
                return i

    if freq[0] == freq[1]:
        return -1

    for i in array:
        if temp[i] == freq[0]:
            return i


def solution_v3(array: list[int]) -> int:
    """
    [Approach] 카운팅 배열 + 직접 증가 (O(n) 개선)
    [Time] O(n)  [Space] O(1001) = O(1)
    ✅ array.count() 대신 += 1로 효율적
    """
    idx = [0] * 1001
    for i in array:
        idx[i] += 1

    if idx.count(max(idx)) > 1:
        return -1

    return idx.index(max(idx))


def solution_v4(array: list[int]) -> int:
    """
    [Approach] dict + items() 정렬
    [Time] O(n² + n log n)  [Space] O(n)
    ⚠️ key=lambda x: dic[1] 오타 → x[1]이어야 함
    """
    dic = dict()

    for i in array:
        dic[i] = array.count(i)

    sorted_tu = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    if len(sorted_tu) > 1:
        if sorted_tu[0][1] == sorted_tu[1][1]:
            return -1

    return sorted_tu[0][0]


def solution_v5(array: list[int]) -> int:
    """
    [Approach] Counter.most_common()
    [Time] O(n log n)  [Space] O(n)
    ✅ 가장 Pythonic하고 간결한 방식
    """
    from collections import Counter

    mc = Counter(array).most_common(2)

    if len(mc) > 1:
        if mc[0][1] == mc[1][1]:
            return -1

    return mc[0][0]


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v3
