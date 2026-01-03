"""
프로그래머스 Lv0 #120848 - 팩토리얼
https://school.programmers.co.kr/learn/courses/30/lessons/120848

[복습] 2차 - 2026-01-02

[문제]
i 팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다.
예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다.
정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록
solution 함수를 완성해주세요.
- i! ≤ n

[제한]
- 0 < n ≤ 3,628,800
"""


def solution(n: int) -> int:
    """
    [Approach] 점진적 팩토리얼 계산으로 i! ≤ n인 최대 i 탐색
    [Time] O(1) - 최대 10회 반복 (10! = 3,628,800)
    [Space] O(1)
    """
    i, v = 1, 1
    while v < n:
        i += 1
        v *= i

    if v == n:
        return i
    return i - 1
