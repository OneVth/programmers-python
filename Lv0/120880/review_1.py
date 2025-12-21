"""
프로그래머스 Lv0 #120880 - 특이한 정렬
https://school.programmers.co.kr/learn/courses/30/lessons/120880

[복습] 1차 - 2025-12-17

[문제]
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다.
이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다.
정수가 담긴 배열 numlist와 정수 n이 주어질 때
numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 10,000
- 1 ≤ numlist의 원소 ≤ 10,000
- 1 ≤ numlist의 길이 ≤ 100
- numlist는 중복된 원소를 갖지 않습니다.
"""


def solution_v1(numlist: list[int], n: int) -> list[int]:
    """
    [Approach] 튜플 키를 이용한 다중 조건 정렬
               - 1차 기준: n과의 거리 (오름차순)
               - 2차 기준: 값 자체 (내림차순, -x로 구현)
    [Time] O(n log n) - 정렬 알고리즘
    [Space] O(n) - sorted가 새 리스트 생성
    """
    return sorted(numlist, key=lambda x: (abs(x - n), -x))


solution = solution_v1
