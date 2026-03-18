"""
프로그래머스 Lv0 #181901 - 배열 만들기 1
https://school.programmers.co.kr/learn/courses/30/lessons/181901

[문제]
정수 n과 k가 주어졌을 때, 1 이상 n 이하의 정수 중에서
k의 배수를 오름차순으로 저장한 배열을 return 하는
solution 함수를 완성해 주세요.

[제한]
- 1 <= n <= 1,000,000
- 1 <= k <= min(1,000, n)
"""


def solution_v1(n: int, k: int) -> list[int]:
    """
    [Approach] range()의 step 파라미터로 k의 배수만 직접 생성
    [Time] O(n/k)  [Space] O(n/k)
    """
    return list(range(k, n + 1, k))


solution = solution_v1
