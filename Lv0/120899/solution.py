"""
프로그래머스 Lv0 #120899 - 가장 큰 수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/120899

[문제]
정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을
return 하도록 solution 함수를 완성해보세요.

[제한]
- 1 ≤ array의 길이 ≤ 100
- 0 ≤ array 원소 ≤ 1,000
- array에 중복된 숫자는 없습니다.
"""


def solution_v1(array: list[int]) -> list[int]:
    """
    [Approach] 내장 함수 활용 - max()로 최댓값, index()로 위치 찾기
    [Time] O(n) - max O(n) + index O(n)  [Space] O(1)
    """
    m = max(array)
    return [m, array.index(m)]


def solution_v2(array: list[int]) -> list[int]:
    """
    [Approach] 단일 순회 - enumerate로 인덱스와 값을 동시에 추적
    [Time] O(n)  [Space] O(1)
    """
    idx = -1
    m = -1
    for i, v in enumerate(array):
        if v > m:
            m = v
            idx = i

    return [m, idx]


solution = solution_v2
