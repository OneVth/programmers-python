"""
프로그래머스 Lv0 #120819 - 아이스 아메리카노
https://school.programmers.co.kr/learn/courses/30/lessons/120819

[문제]
머쓱이는 추운 날에도 아이스 아메리카노만 마십니다.
아이스 아메리카노는 한잔에 5,500원입니다.
머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때,
머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을
순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

[제한]
- 0 < money ≤ 1,000,000
"""


def solution_v1(money: int) -> list[int]:
    """
    [Approach] divmod로 몫(잔 수)과 나머지(거스름돈) 동시 계산
    [Time] O(1)  [Space] O(1)
    """
    return [*divmod(money, 5500)]


def solution_v2(money: int) -> list[int]:
    """
    [Approach] //와 %로 몫과 나머지 각각 계산
    [Time] O(1)  [Space] O(1)
    """
    return [money // 5500, money % 5500]


solution = solution_v1
