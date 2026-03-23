"""
프로그래머스 Lv0 #181923 - 수열과 구간 쿼리 2
https://school.programmers.co.kr/learn/courses/30/lessons/181923

[문제]
정수 배열 arr 와 2차원 정수 배열 queries 이 주어집니다.
queries 의 원소는 각각 하나의 query 를 나타내며, [s, e, k] 꼴입니다.
각 query 마다 순서대로 s ≤ i ≤ e 인 모든 i 에 대해
k 보다 크면서 가장 작은 arr[i] 를 찾습니다.
각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.

[제한]
- 1 ≤ arr 의 길이 ≤ 1,000
  - 0 ≤ arr 의 원소 ≤ 1,000,000
- 1 ≤ queries 의 길이 ≤ 1,000
  - 0 ≤ s ≤ e < arr 의 길이
  - 0 ≤ k ≤ 1,000,000
"""

import bisect


def solution_v1(arr: list[int], queries: list[list[int]]) -> list[int]:
    """
    [Approach] 구간을 정렬 후 bisect_right로 k 초과 최솟값의 인덱스를 이진탐색
    [Time] O(q * n log n)  [Space] O(n)  — q=queries 길이, n=구간 길이
    """
    answer = []
    for s, e, k in queries:
        sorted_arr = sorted(arr[s : e + 1])
        idx = bisect.bisect_right(sorted_arr, k)
        if idx >= len(sorted_arr):
            answer.append(-1)
        else:
            answer.append(sorted_arr[idx])

    return answer


def solution_v2(arr: list[int], queries: list[list[int]]) -> list[int]:
    """
    [Approach] 구간을 필터링해 k 초과 원소 리스트를 만들고 min으로 최솟값 반환
    [Time] O(q * n)  [Space] O(n)  — q=queries 길이, n=구간 길이
    """
    answer = []
    for s, e, k in queries:
        bigger = [i for i in arr[s : e + 1] if i > k]
        answer.append(-1 if not bigger else min(bigger))

    return answer


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
