"""
프로그래머스 Lv0 #120897 - 약수 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120897

[복습] 1차 - 2025-12-17

[문제]
정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 10,000
"""


def solution_v1(n: int) -> list[int]:
    """
    [Approach] 제곱근까지 순회 + 조건문으로 제곱수 중복 방지
    [Time] O(√n)  [Space] O(√n) - 약수 개수
    """
    answer = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                answer.append(i)
            else:
                answer.append(i)
                answer.append(n // i)
    return sorted(answer)


def solution_v2(n: int) -> list[int]:
    """
    [Approach] 제곱근까지 순회 + set으로 중복 자동 제거
    [Time] O(√n)  [Space] O(√n) - 약수 개수
    """
    answer = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            answer.add(i)
            answer.add(n // i)

    return sorted(list(answer))


solution = solution_v2
