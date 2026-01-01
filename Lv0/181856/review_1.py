"""
프로그래머스 Lv0 #181856 - 배열 비교하기
https://school.programmers.co.kr/learn/courses/30/lessons/181856

[복습] 1차 - 2025-12-31

[문제]
이 문제에서 두 정수 배열의 대소관계를 다음과 같이 정의합니다.
- 두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
- 배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여
  다르다면 더 큰 쪽이 크고, 같다면 같습니다.

두 정수 배열 arr1과 arr2가 주어질 때, 위에서 정의한 배열의 대소관계에 대하여
arr2가 크다면 -1, arr1이 크다면 1, 두 배열이 같다면 0을 return 하는
solution 함수를 작성해 주세요.

[제한]
- 1 ≤ arr1의 길이 ≤ 100
- 1 ≤ arr2의 길이 ≤ 100
- 1 ≤ arr1의 원소 ≤ 100
- 1 ≤ arr2의 원소 ≤ 100
- 문제에서 정의한 배열의 대소관계가 일반적인 프로그래밍 언어에서 정의된
  배열의 대소관계와 다를 수 있는 점에 유의해주세요.
"""


def solution_v1(arr1: list[int], arr2: list[int]) -> int:
    """
    [Approach] 길이 우선 비교, 같으면 합 비교 (cmp 패턴 사용)
    [Time] O(n) - 합 계산
    [Space] O(1) - 상수 공간
    """
    arr1_len = len(arr1)
    arr2_len = len(arr2)

    if arr1_len != arr2_len:
        return (arr1_len > arr2_len) - (arr1_len < arr2_len)

    arr1_sum = sum(arr1)
    arr2_sum = sum(arr2)
    return (arr1_sum > arr2_sum) - (arr1_sum < arr2_sum)


def solution_v2(arr1: list[int], arr2: list[int]) -> int:
    """
    [Approach] 튜플 비교로 다중 기준 정렬 활용
    [Time] O(n) - 합 계산
    [Space] O(1) - 튜플 2개만 생성
    """
    t1, t2 = (len(arr1), sum(arr1)), (len(arr2), sum(arr2))
    return (t1 > t2) - (t1 < t2)


solution = solution_v2
