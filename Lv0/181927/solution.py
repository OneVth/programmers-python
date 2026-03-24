"""
프로그래머스 Lv0 #181927 - 마지막 두 원소
https://school.programmers.co.kr/learn/courses/30/lessons/181927

[문제]
정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서
그전 원소를 뺀 값을, 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한
값을 추가하여 return하도록 solution 함수를 완성해주세요.

[제한]
- 2 ≤ num_list의 길이 ≤ 10
- 1 ≤ num_list의 원소 ≤ 9
"""


def solution_v1(num_list: list[int]) -> list[int]:
    """
    [Approach] 마지막 두 원소 비교 후 조건에 따라 새 값을 복사본에 추가
    [Time] O(n)  [Space] O(n)
    """
    answer = list(num_list)
    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.append(num_list[-1] * 2)
    return answer


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
