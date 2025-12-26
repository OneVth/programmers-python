"""
프로그래머스 Lv0 #181840 - 정수 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/181840

[문제]
정수 리스트 num_list와 찾으려는 정수 n이 주어질 때,
num_list 안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.

[제한]
- 3 ≤ num_list의 길이 ≤ 100
- 1 ≤ num_list의 원소 ≤ 100
- 1 ≤ n ≤ 100
"""


def solution_v1(num_list: list[int], n: int) -> int:
    """
    [Approach] in 연산자로 포함 여부 확인 후 int 변환
    [Time] O(n) - 리스트 선형 탐색
    [Space] O(1)
    """
    return int(n in num_list)


# ✅ 기본 솔루션 지정
solution = solution_v1
