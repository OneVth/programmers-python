"""
프로그래머스 Lv0 #181831 - 특별한 이차원 배열 2
https://school.programmers.co.kr/learn/courses/30/lessons/181831

[문제]
n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때,
arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
- 0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]

[제한]
- 1 ≤ arr의 길이 = arr의 원소의 길이 ≤ 100
- 1 ≤ arr의 원소의 원소 ≤ 1,000
- 모든 arr의 원소의 길이는 같습니다.
"""


def solution_v1(arr: list[list[int]]) -> int:
    """
    [Approach] 모든 (i, j) 쌍 비교 - 단순 전체 검사
    [Time] O(n²)  [Space] O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                return 0

    return 1


def solution_v2(arr: list[list[int]]) -> int:
    """
    [Approach] 전치행렬과 비교 - zip(*arr)로 전치 후 동일성 검사
    [Time] O(n²)  [Space] O(n²) - 전치행렬 생성
    """
    return int(arr == list(map(list, zip(*arr))))


def solution_v3(arr: list[list[int]]) -> int:
    """
    [Approach] 상삼각만 비교 - i < j인 경우만 검사 (최적화)
    [Time] O(n²/2)  [Space] O(1)
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0

    return 1


solution = solution_v3
