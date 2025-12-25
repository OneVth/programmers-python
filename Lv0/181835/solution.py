"""
프로그래머스 Lv0 #181835 - 조건에 맞게 수열 변환하기 3
https://school.programmers.co.kr/learn/courses/30/lessons/181835

[문제]
정수 배열 arr와 자연수 k가 주어집니다.
만약 k가 홀수라면 arr의 모든 원소에 k를 곱하고,
k가 짝수라면 arr의 모든 원소에 k를 더합니다.
이러한 변환을 마친 후의 arr를 return 하는 solution 함수를 완성해 주세요.

[제한]
- 1 ≤ arr의 길이 ≤ 1,000,000
  - 1 ≤ arr의 원소의 값 ≤ 100
- 1 ≤ k ≤ 100
"""


def solution_v1(arr: list[int], k: int) -> list[int]:
    """
    [Approach] 조건 분기 후 리스트 컴프리헨션 - 짝수면 덧셈, 홀수면 곱셈
    [Time] O(n)  [Space] O(n)
    """
    if k % 2 == 0:
        return [i + k for i in arr]
    else:
        return [i * k for i in arr]


solution = solution_v1

