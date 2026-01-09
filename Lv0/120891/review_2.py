"""
프로그래머스 Lv0 #120891 - 369게임
https://school.programmers.co.kr/learn/courses/30/lessons/120891

[복습] 2차 - 2026-01-02

[문제]
머쓱이는 친구들과 369게임을 하고 있습니다.
369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는
숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다.

머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때,
머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

[제한]
- 1 ≤ order ≤ 1,000,000
"""


def solution_v1(order: int) -> int:
    """
    [Approach] Counter로 각 숫자 빈도 계산 후 3,6,9 합산
    [Time] O(d)  [Space] O(d) - d는 자릿수
    """
    from collections import Counter

    counter = Counter(str(order))
    return sum(counter[c] for c in "369")


def solution_v2(order: int) -> int:
    """
    [Approach] 각 자릿수가 3,6,9인지 직접 체크하여 합산
    [Time] O(d)  [Space] O(1) - d는 자릿수
    """
    return sum(c in "369" for c in str(order))


# 기본 솔루션 지정
solution = solution_v2
