"""
프로그래머스 Lv0 #120837 - 개미 군단
https://school.programmers.co.kr/learn/courses/30/lessons/120837

[복습] 1차 - 2025-12-10

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
    [Approach] 그리디 - 한 줄 수식
    [Time] O(1)  [Space] O(1)
    ✅ 가장 효율적, 동전 문제가 그리디 적용 가능한 경우
    """
    return hp // 5 + (hp % 5) // 3 + (hp % 5 % 3)


def solution_v2(hp: int) -> int:
    """
    [Approach] DP - 동전 교환 문제 패턴
    [Time] O(hp)  [Space] O(hp)
    ✅ 그리디가 안 되는 동전 조합에도 적용 가능 (범용적)
    """
    dp = [float("inf")] * (hp + 1)
    dp[0] = 0

    for i in range(1, hp + 1):
        if i >= 5:
            dp[i] = min(dp[i - 5] + 1, dp[i])
        if i >= 3:
            dp[i] = min(dp[i - 3] + 1, dp[i])
        dp[i] = min(dp[i - 1] + 1, dp[i])

    return dp[hp]


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
