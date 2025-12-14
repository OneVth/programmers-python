"""
프로그래머스 Lv0 #120889 - 삼각형의 완성조건 (1)
https://school.programmers.co.kr/learn/courses/30/lessons/120889

[문제]
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.
- 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.

삼각형의 세 변의 길이가 담긴 배열 sides가 매개변수로 주어집니다.
세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록
solution 함수를 완성해주세요.

[제한]
- sides의 원소는 자연수입니다.
- sides의 길이는 3입니다.
- 1 ≤ sides의 원소 ≤ 1,000
"""


def solution_v1(sides: list[int]) -> int:
    """
    [Approach] max 활용 - 가장 긴 변 vs 나머지 합 (sum - max)
    [Time] O(n) - max, sum 각 1회
    [Space] O(1)
    """
    return 1 if max(sides) < sum(sides) - max(sides) else 2


def solution_v2(sides: list[int]) -> int:
    """
    [Approach] 정렬 후 비교 - 마지막 원소 vs 나머지 합
    [Time] O(n log n) - 정렬
    [Space] O(n) - 정렬된 리스트
    """
    sorted_sides = sorted(sides)
    return 1 if sorted_sides[-1] < sum(sorted_sides[:-1]) else 2


solution = solution_v2
