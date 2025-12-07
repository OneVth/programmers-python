"""
프로그래머스 Lv0 #120845 - 주사위의 개수
https://school.programmers.co.kr/learn/courses/30/lessons/120845

[문제]
머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를
최대한 많이 채우고 싶습니다. 상자의 가로, 세로, 높이가 저장되어있는 배열 box와
주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때,
상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.

[제한]
- box의 길이는 3입니다.
- box[0] = 상자의 가로 길이
- box[1] = 상자의 세로 길이
- box[2] = 상자의 높이 길이
- 1 ≤ box의 원소 ≤ 100
- 1 ≤ n ≤ 50
- n ≤ box의 원소
- 주사위는 상자와 평행하게 넣습니다.
"""


def solution_v1(box: list[int], n: int) -> int:
    """
    [Approach] 직접 인덱싱하여 계산
    [Time] O(1)  [Space] O(1)
    """
    return (box[0] // n) * (box[1] // n) * (box[2] // n)


def solution_v2(box: list[int], n: int) -> int:
    """
    [Approach] math.prod + map + lambda
    [Time] O(1)  [Space] O(1)
    """
    from math import prod

    return prod(map(lambda v: v // n, box))


def solution_v3(box: list[int], n: int) -> int:
    """
    [Approach] math.prod + generator expression
    [Time] O(1)  [Space] O(1)
    ✅ 가장 간결하고 가독성 좋음
    """
    from math import prod

    return prod(x // n for x in box)


def solution_v4(box: list[int], n: int) -> int:
    """
    [Approach] functools.reduce로 누적 곱
    [Time] O(1)  [Space] O(1)
    ⚠️ prod()가 있으므로 굳이 reduce 불필요
    """
    from functools import reduce

    return reduce(lambda acc, x: acc * (x // n), box, 1)


solution = solution_v3
