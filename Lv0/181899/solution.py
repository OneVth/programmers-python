"""
프로그래머스 Lv0 #181899 - 카운트 다운
https://school.programmers.co.kr/learn/courses/30/lessons/181899

[문제]
정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지
1씩 감소하는 수들을 차례로 담은 리스트를 return하도록
solution 함수를 완성해주세요.

[제한]
- 0 <= end_num <= start_num <= 50
"""


def solution_v1(start_num: int, end_num: int) -> list[int]:
    """
    [Approach] range()의 step=-1을 활용한 역순 수열 생성
    [Time] O(n)  [Space] O(n)
    """
    return list(range(start_num, end_num - 1, -1))


solution = solution_v1
