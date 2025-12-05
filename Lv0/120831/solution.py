"""
프로그래머스 Lv0 #120831 - 짝수의 합
https://school.programmers.co.kr/learn/courses/30/lessons/120831

[문제]
정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록
solution 함수를 작성해주세요.

[제한]
- 0 < n ≤ 1000
"""


def solution_v1(n: int) -> int:
    """
    [Approach] 전체 순회 + 조건 필터링
    [Time] O(n)  [Space] O(1)
    ⚠️ 모든 숫자 순회 후 짝수만 필터링
    """
    return sum(x for x in range(1, n + 1) if x % 2 == 0)


def solution_v2(n: int) -> int:
    """
    [Approach] step=2로 짝수만 생성
    [Time] O(n/2)  [Space] O(1)
    ✅ 짝수만 직접 생성하여 순회 절반
    """
    return sum(i for i in range(0, n + 1, 2))


def solution_v3(n: int) -> int:
    """
    [Approach] 등차수열 합 공식
    [Time] O(1)  [Space] O(1)
    ✅ 수학 공식으로 순회 없이 즉시 계산
    """
    k = n // 2
    return k * (k + 1)


solution = solution_v3
