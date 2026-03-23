"""
프로그래머스 Lv0 #181922 - 수열과 구간 쿼리 4
https://school.programmers.co.kr/learn/courses/30/lessons/181922

[문제]
정수 배열 arr 와 2차원 정수 배열 queries 가 주어집니다.
queries 의 원소는 각각 하나의 query 를 나타내며, [s, e, k] 꼴입니다.
각 query 마다 순서대로 s ≤ i ≤ e 인 모든 i 에 대해
i 가 k 의 배수이면 arr[i] 에 1을 더합니다.
위 규칙에 따라 queries 를 처리한 이후의 arr 를 return 하는 solution 함수를 완성해 주세요.

[제한]
- 1 ≤ arr 의 길이 ≤ 1,000
  - 0 ≤ arr 의 원소 ≤ 1,000,000
- 1 ≤ queries 의 길이 ≤ 1,000
  - 0 ≤ s ≤ e < arr 의 길이
  - 0 ≤ k ≤ 5
"""


def solution_v1(arr: list[int], queries: list[list[int]]) -> list[int]:
    """
    [Approach] 각 쿼리를 인덱스로 분해 후 구간 내 k 배수 인덱스에 +1
    [Time] O(q * n)  [Space] O(n)  — q=queries 길이, n=arr 길이
    """
    answer = list(arr)
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        for i in range(s, e + 1):
            if i % k == 0:
                answer[i] += 1
    return answer


def solution_v2(arr: list[int], queries: list[list[int]]) -> list[int]:
    """
    [Approach] 튜플 언패킹으로 v1을 간결하게 표현
    [Time] O(q * n)  [Space] O(n)  — q=queries 길이, n=arr 길이
    """
    answer = list(arr)
    for s, e, k in queries:
        for i in range(s, e + 1):
            if i % k == 0:
                answer[i] += 1
    return answer


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
