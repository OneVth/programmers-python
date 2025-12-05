"""
프로그래머스 Lv0 #120824 - 짝수 홀수 개수
https://school.programmers.co.kr/learn/courses/30/lessons/120824

[문제]
정수가 담긴 리스트 num_list가 주어질 때,
num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록
solution 함수를 완성해보세요.

[제한]
- 1 ≤ num_list의 길이 ≤ 100
- 0 ≤ num_list의 원소 ≤ 1,000
"""


def solution_v1(num_list: list[int]) -> list[int]:
    """
    [Approach] if-else로 짝수/홀수 분기
    [Time] O(n)  [Space] O(1)
    """
    answer = [0, 0]
    for i in num_list:
        if i % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    return answer


def solution_v2(num_list: list[int]) -> list[int]:
    """
    [Approach] i % 2를 인덱스로 활용
    [Time] O(n)  [Space] O(1)
    ✅ 짝수→0, 홀수→1이 인덱스와 일치하는 트릭
    """
    answer = [0, 0]
    for i in num_list:
        answer[i % 2] += 1

    return answer


def solution_v3(num_list: list[int]) -> list[int]:
    """
    [Approach] sum + generator로 짝수 세기
    [Time] O(n)  [Space] O(1)
    ✅ 홀수 = 전체 - 짝수 (한 번만 순회)
    """
    even_cnt = sum(1 for x in num_list if x % 2 == 0)
    return [even_cnt, len(num_list) - even_cnt]


solution = solution_v3
