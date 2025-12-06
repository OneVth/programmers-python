"""
프로그래머스 Lv0 #120836 - 순서쌍의 개수
https://school.programmers.co.kr/learn/courses/30/lessons/120836

[문제]
순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다.
자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를
return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 1,000,000
"""


def solution_v1(n: int) -> int:
    """
    [Approach] 1~n 전체 순회하며 약수 개수 세기
    [Time] O(n)  [Space] O(1)
    ⚠️ 단순하지만 n이 크면 비효율
    """
    return sum(1 for i in range(1, n + 1) if n % i == 0)


def solution_v2(n: int) -> int:
    """
    [Approach] √n까지만 탐색 (약수 쌍 활용)
    [Time] O(√n)  [Space] O(1)
    ✅ 최적화: i와 n//i가 쌍으로 존재 (완전제곱수 예외 처리)
    """
    answer = 0

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                answer += 1
            else:
                answer += 2

    return answer


def solution_v3(n: int) -> int:
    """
    [Approach] filter + lambda 함수형
    [Time] O(n)  [Space] O(n)
    ⚠️ list 생성으로 메모리 추가 사용
    """
    return len(list(filter(lambda i: n % i == 0, range(1, n + 1))))


solution = solution_v2
