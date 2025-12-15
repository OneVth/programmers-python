"""
프로그래머스 Lv0 #120897 - 약수 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120897

[문제]
정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 10,000
"""


def solution_v1(n: int) -> list[int]:
    """
    [Approach] 브루트포스 - 1부터 n까지 모든 수로 나눠서 약수 판별
    [Time] O(n)  [Space] O(k) where k = 약수의 개수
    """
    return [i for i in range(1, n + 1) if n % i == 0]


def solution_v2(n: int) -> list[int]:
    """
    [Approach] 제곱근 최적화 - √n까지만 탐색하고 짝이 되는 약수 함께 추가
    [Time] O(√n log n) - 탐색 O(√n) + 정렬 O(k log k)  [Space] O(k)
    """
    answer = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            answer.append(i)
            if i != n // i:
                answer.append(n // i)

    return sorted(answer)


def solution_v3(n: int) -> list[int]:
    """
    [Approach] 제곱근 최적화 + Set - 중복을 set으로 자동 제거
    [Time] O(√n log n) - 탐색 O(√n) + 정렬 O(k log k)  [Space] O(k)
    """
    answer = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            answer.add(i)
            answer.add(n // i)

    return sorted(list(answer))


solution = solution_v3
