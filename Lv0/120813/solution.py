"""
프로그래머스 Lv0 #120813 - 짝수는 싫어요
https://school.programmers.co.kr/learn/courses/30/lessons/120813

[문제]
정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 반환

[제한]
- 1 ≤ n ≤ 100
"""


def solution_v1(n: int) -> list[int]:
    """
    [Approach] range step=2 활용
    [Time] O(n)  [Space] O(n)
    ✅ 가장 효율적 - 처음부터 홀수만 생성
    """
    return [x for x in range(1, n + 1, 2)]


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
