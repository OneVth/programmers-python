"""
프로그래머스 Lv0 #120890 - 가까운 수
https://school.programmers.co.kr/learn/courses/30/lessons/120890

[문제]
정수 배열 array와 정수 n이 매개변수로 주어질 때,
array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ array의 길이 ≤ 100
- 1 ≤ array의 원소 ≤ 100
- 1 ≤ n ≤ 100
- 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.
"""


def solution_v1(array: list[int], n: int) -> int:
    """
    [Approach] 튜플 키 정렬 - (거리, 값) 기준으로 정렬 후 첫 번째 반환
    [Time] O(n log n) - 정렬
    [Space] O(n) - 정렬된 리스트
    """
    sorted_arr = sorted(array, key=lambda x: (abs(x - n), x))
    return sorted_arr[0]


# 기본 솔루션 지정
solution = solution_v1
