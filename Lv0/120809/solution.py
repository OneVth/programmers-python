"""
프로그래머스 Lv0 #120809 - 배열 두 배 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/120809

[문제]
정수 배열 numbers가 매개변수로 주어질 때,
numbers의 각 원소에 두 배한 원소를 가진 배열을 반환

[제한]
- -10,000 ≤ numbers의 원소 ≤ 10,000
- 1 ≤ numbers의 길이 ≤ 1,000
"""


def solution_v1(numbers: list[int]) -> list[int]:
    """
    [Approach] 인덱스 기반 for문 + append
    [Time] O(n)  [Space] O(n)
    """
    answer = []
    for i in range(len(numbers)):
        answer.append(2 * numbers[i])
    return answer


def solution_v2(numbers: list[int]) -> list[int]:
    """
    [Approach] 값 기반 for문 + append
    [Time] O(n)  [Space] O(n)
    ✨ v1보다 Pythonic (인덱스 불필요)
    """
    answer = []
    for num in numbers:
        answer.append(2 * num)
    return answer


def solution_v3(numbers: list[int]) -> list[int]:
    """
    [Approach] 리스트 컴프리헨션
    [Time] O(n)  [Space] O(n)
    ✅ 가장 Pythonic하고 빠름
    """
    return [num * 2 for num in numbers]


def solution_v4(numbers: list[int]) -> list[int]:
    """
    [Approach] map + lambda
    [Time] O(n)  [Space] O(n)
    [Original] list(map(lambda x: x * 2, numbers))
    """
    return list(map(lambda x: x * 2, numbers))


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v3
