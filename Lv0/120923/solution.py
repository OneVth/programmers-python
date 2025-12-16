"""
프로그래머스 Lv0 #120923 - 연속된 수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/120923

[문제]
연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다.
두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때,
정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

[제한]
- 1 ≤ num ≤ 100
- 0 ≤ total ≤ 1000
- num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.
"""


def solution_v1(num: int, total: int) -> list[int]:
    """
    [Approach] 등차수열 합 역산 - 첫항 x를 수학적으로 계산
    [Time] O(num)  [Space] O(num)
    """
    # total = x + (x+1) + ... + (x+num-1) = num*x + num*(num-1)/2
    # x = (total - num*(num-1)/2) / num = (total + num - num²) / (2*num)
    x = ((num - num**2) // 2 + total) // num
    return [x + i for i in range(num)]


def solution_v2(num: int, total: int) -> list[int]:
    """
    [Approach] 기준점 차이 계산 - 1~num 합과 total의 차이로 시작점 역산
    [Time] O(num)  [Space] O(num)
    """
    var = sum(range(num + 1))  # 1 + 2 + ... + num
    diff = total - var
    start_num = diff // num

    return [start_num + i + 1 for i in range(num)]


solution = solution_v1
