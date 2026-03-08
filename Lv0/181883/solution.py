"""
프로그래머스 Lv0 #181883 - 수열과 구간 쿼리 1
https://school.programmers.co.kr/learn/courses/30/lessons/181883

[문제]
정수 배열 arr와 2차원 정수 배열 queries가 주어집니다.
queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴입니다.

각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.

위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

[제한]
- 1 ≤ arr의 길이 ≤ 1,000
  - 0 ≤ arr의 원소 ≤ 1,000,000
- 1 ≤ queries의 길이 ≤ 1,000
  - 0 ≤ s ≤ e < arr의 길이
"""


def solution_v1(arr: list[int], queries: list[list[int]]) -> list[int]:
    """
    [Approach] 각 쿼리 [s, e]마다 해당 구간을 순회하며 +1
    [Time] O(N * Q)  [Space] O(N)
    """
    answer = list(arr)
    for query in queries:
        for i in range(query[0], query[1] + 1):
            answer[i] = answer[i] + 1
    return answer


solution = solution_v1
