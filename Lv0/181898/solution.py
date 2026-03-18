"""
프로그래머스 Lv0 #181898 - 가까운 1 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/181898

[문제]
정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다.
정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를
찾아서 반환하는 solution 함수를 완성해 주세요.
단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.

[제한]
- 3 <= arr의 길이 <= 100,000
  - arr의 원소는 전부 1 또는 0입니다.
"""


def solution_v1(arr: list[int], idx: int) -> int:
    """
    [Approach] idx부터 순회하며 첫 번째 1의 인덱스를 반환하는 선형 탐색
    [Time] O(n)  [Space] O(1)
    """
    length = len(arr)
    if length < idx:
        return -1

    for i in range(idx, length):
        if arr[i] == 1:
            return i

    return -1


def solution_v2(arr: list[int], idx: int) -> int:
    """
    [Approach] list.index()의 start 파라미터를 활용한 내장 메서드 풀이
    [Time] O(n)  [Space] O(1)
    """
    try:
        return arr.index(1, idx)
    except ValueError:
        return -1


solution = solution_v2
