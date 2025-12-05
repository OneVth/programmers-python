"""
프로그래머스 Lv0 #120821 - 배열 뒤집기
https://school.programmers.co.kr/learn/courses/30/lessons/120821

[문제]
정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ num_list의 길이 ≤ 1,000
- 0 ≤ num_list의 원소 ≤ 1,000
"""


def solution_v1(num_list: list[int]) -> list[int]:
    """
    [Approach] reversed() 이터레이터를 list로 변환
    [Time] O(n)  [Space] O(n)
    """
    return list(reversed(num_list))


def solution_v2(num_list: list[int]) -> list[int]:
    """
    [Approach] 슬라이싱 [::-1]
    [Time] O(n)  [Space] O(n)
    ✅ 가장 파이썬다운 방식
    """
    return num_list[::-1]


def solution_v3(num_list: list[int]) -> list[int]:
    """
    [Approach] in-place reverse
    [Time] O(n)  [Space] O(1)
    ⚠️ 원본 배열 수정됨
    """
    num_list.reverse()
    return num_list


def solution_v4(num_list: list[int]) -> list[int]:
    """
    [Approach] pop으로 뒤에서부터 추출
    [Time] O(n)  [Space] O(n)
    ⚠️ 원본 배열 수정됨 (비움)
    """
    answer = []
    while num_list:
        answer.append(num_list.pop())
    return answer


solution = solution_v2
