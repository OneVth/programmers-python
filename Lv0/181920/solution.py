"""
프로그래머스 Lv0 #181920 - 카운트 업
https://school.programmers.co.kr/learn/courses/30/lessons/181920

[문제]
정수 start_num와 end_num가 주어질 때,
start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록
solution 함수를 완성해주세요.

[제한]
- 0 ≤ start_num ≤ end_num ≤ 50
"""


def solution_v1(start_num: int, end_num: int) -> list[int]:
    """
    [Approach] range()로 start_num~end_num 범위 생성 후 리스트 변환
    [Time] O(n)  [Space] O(n)  — n = end_num - start_num + 1
    """
    return list(range(start_num, end_num + 1))


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
