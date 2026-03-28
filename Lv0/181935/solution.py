"""
프로그래머스 Lv0 #181935 - 홀짝에 따라 다른 값 반환하기
https://school.programmers.co.kr/learn/courses/30/lessons/181935

[문제]
양의 정수 n이 매개변수로 주어질 때,
n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고
n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는
solution 함수를 작성해 주세요.

[제한]
- 1 ≤ n ≤ 100
"""


def solution_v1(n: int) -> int:
    """
    [Approach] range step=2로 홀수/짝수 수열 생성 후 sum() + 제너레이터로 합산
    [Time] O(n)  [Space] O(1)
    """
    return (
        sum(i**2 for i in range(2, n + 1, 2))
        if n % 2 == 0
        else sum(i for i in range(1, n + 1, 2))
    )


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
