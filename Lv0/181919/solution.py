"""
프로그래머스 Lv0 #181919 - 콜라츠 수열 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/181919

[문제]
모든 자연수 x 에 대해서 현재 값이 x 이면 x 가 짝수일 때는 2로 나누고,
x 가 홀수일 때는 3 * x + 1 로 바꾸는 계산을 계속해서 반복하면 언젠가는
반드시 x 가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.

그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다.
계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1에 도달한다는 것이 알려져 있습니다.

임의의 1,000 보다 작거나 같은 양의 정수 n 이 주어질 때 초기값이 n 인 콜라츠 수열을 return 하는
solution 함수를 완성해 주세요.

[제한]
- 1 ≤ n ≤ 1,000
"""


def solution_v1(n: int) -> list[int]:
    """
    [Approach] while 루프로 콜라츠 연산을 반복, 1 도달 시 종료 후 마지막 원소 추가
    [Time] O(k)  [Space] O(k)  # k: 수열 길이 (n에 따라 다름, n≤1000에서 최대 수백 회)
    """
    answer = []
    while n > 1:
        answer.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    answer.append(n)
    return answer


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
