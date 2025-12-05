"""
프로그래머스 Lv0 #120830 - 양꼬치
https://school.programmers.co.kr/learn/courses/30/lessons/120830

[문제]
머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다.
양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다.
정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면
총 얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.

[제한]
- 0 < n < 1,000
- n / 10 ≤ k < 1,000
- 서비스로 받은 음료수는 모두 마십니다.
"""


def solution_v1(n: int, k: int) -> int:
    """
    [Approach] 총액 - 서비스 금액
    [Time] O(1)  [Space] O(1)
    ✅ 직관적: 전체 계산 후 할인 차감
    """
    total = n * 12000 + k * 2000
    services = (n // 10) * 2000
    return total - services


def solution_v2(n: int, k: int) -> int:
    """
    [Approach] 실제 결제할 음료수만 계산
    [Time] O(1)  [Space] O(1)
    ✅ 서비스 음료 제외한 실제 음료만 계산
    """
    service = n // 10
    drink = max(0, k - service)
    return 12000 * n + 2000 * drink


solution = solution_v1
