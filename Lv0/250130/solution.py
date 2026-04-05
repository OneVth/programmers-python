"""
프로그래머스 Lv0 #250130 - [PCCE 기출문제] 4번 / 저축
https://school.programmers.co.kr/learn/courses/30/lessons/250130

[문제]
진우는 돈을 모으기 위해 저축을 하려고 합니다. 목표 금액은 100만 원이며,
첫 달에 일정 금액을 넣은 뒤 70만 원까지는 매월 조금씩 저축하다가
70만 원 이후부터는 월 저축량을 늘려 빠르게 목표 금액을 달성하고자 합니다.

- start: 첫 달에 저축하는 금액
- before: 두 번째 달부터 70만 원 이상 모일 때까지 매월 저축 금액
- after: 100만 원 이상 모일 때까지 매월 저축 금액

100만 원 이상을 모을 때까지 걸리는 개월 수를 return합니다.

[제한]
- 0 ≤ start ≤ 99
- 1 ≤ before ≤ after ≤ 25
"""


def solution_v1(start: int, before: int, after: int) -> int:
    """
    [Approach] 70만원/100만원 기준으로 두 단계 while 루프로 시뮬레이션
    [Time] O(n)  [Space] O(1)
    """
    money = start
    month = 1
    while money < 70:
        money += before
        month += 1
    while money < 100:
        money += after
        month += 1

    return month


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
