"""
프로그래머스 Lv0 #120912 - 7의 개수
https://school.programmers.co.kr/learn/courses/30/lessons/120912

[문제]
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 정수 배열 array가 매개변수로
주어질 때, 7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요.

[제한]
- 1 ≤ array의 길이 ≤ 100
- 0 ≤ array의 원소 ≤ 100,000
"""


def solution_v1(array: list[int]) -> int:
    """
    [Approach] 개별 변환 - 각 숫자를 문자열로 변환 후 count 합산
    [Time] O(n * d)  [Space] O(d) - n: 배열 길이, d: 숫자 자릿수
    """
    return sum(str(x).count("7") for x in array)


def solution_v2(array: list[int]) -> int:
    """
    [Approach] 전체 변환 - 배열 자체를 문자열로 변환 후 count
    [Time] O(n * d)  [Space] O(n * d)
    """
    return str(array).count("7")


solution = solution_v1
