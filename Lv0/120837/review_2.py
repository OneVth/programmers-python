"""
프로그래머스 Lv0 #120837 - 개미 군단
https://school.programmers.co.kr/learn/courses/30/lessons/120837

[복습] 2차 - 2026-01-02

[문제]
개미 군단이 사냥을 나가려고 합니다. 개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다.
장군개미는 5의 공격력을, 병정개미는 3의 공격력을, 일개미는 1의 공격력을 가지고 있습니다.
예를 들어 체력 23의 여치를 사냥하려고 할 때, 일개미 23마리를 데리고 가도 되지만,
장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다.
사냥감의 체력 hp가 매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면
몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.

[제한]
- hp는 자연수입니다.
- 0 ≤ hp ≤ 1000
"""


def solution_v1(hp: int) -> int:
    """
    [Approach] 그리디 - 큰 공격력(5)부터 최대한 사용, 나머지를 순차 처리
    [Time] O(1)  [Space] O(1)
    ✅ 5, 3, 1로 모든 자연수 표현 가능하므로 그리디 성립
    """
    return (hp // 5) + (hp % 5 // 3) + (hp % 5 % 3)


def solution_v2(hp: int) -> int:
    """
    [Approach] DP - tab[i]: 체력 i를 처리하는 최소 개미 수
    [Time] O(n)  [Space] O(n)
    ⚠️ 이 문제에서는 오버킬이지만 동전 교환 문제 연습용
    """
    tab = [float("inf")] * (hp + 1)
    tab[0] = 0
    tab[1] = 1

    for i in range(1, hp + 1):
        if i >= 5:
            tab[i] = min(tab[i - 5] + 1, tab[i])
        elif i >= 3:
            tab[i] = min(tab[i - 3] + 1, tab[i])

        tab[i] = min(tab[i - 1] + 1, tab[i])

    return tab[hp]


# 기본 솔루션 지정
solution = solution_v1
