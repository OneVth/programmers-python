"""
프로그래머스 Lv0 #120924 - 다음에 올 숫자
https://school.programmers.co.kr/learn/courses/30/lessons/120924

[문제]
등차수열 혹은 등비수열 common이 매개변수로 주어질 때,
마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

[제한]
- 2 < common의 길이 < 1,000
- -1,000 < common의 원소 < 2,000
- common의 원소는 모두 정수입니다.
- 등차수열 혹은 등비수열이 아닌 경우는 없습니다.
- 등비수열인 경우 공비는 0이 아닌 정수입니다.
"""


def solution_v1(common: list[int]) -> int:
    """
    [Approach] 인덱스 접근 - 공차/공비 판별 후 다음 항 계산
    [Time] O(1)  [Space] O(1)
    """
    if common[1] - common[0] == common[2] - common[1]:
        d = common[1] - common[0]
        return common[-1] + d
    else:
        r = common[1] // common[0]
        return common[-1] * r


def solution_v2(common: list[int]) -> int:
    """
    [Approach] 언패킹 - 첫 3개 원소로 수열 종류 판별
    [Time] O(1)  [Space] O(1)
    """
    a, b, c = common[:3]
    if c - b == b - a:
        return common[-1] + (b - a)
    else:
        return common[-1] * (b // a)


solution = solution_v2
