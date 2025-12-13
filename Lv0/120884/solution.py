"""
프로그래머스 Lv0 #120884 - 치킨 쿠폰
https://school.programmers.co.kr/learn/courses/30/lessons/120884

[문제]
프로그래머스 치킨은 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다.
쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고,
서비스 치킨에도 쿠폰이 발급됩니다.
시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때
받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.

[제한]
- chicken은 정수입니다.
- 0 ≤ chicken ≤ 1,000,000
"""


def solution_v1(chicken: int) -> int:
    """
    [Approach] 시뮬레이션 - 쿠폰 10장당 서비스 치킨 1마리 교환 반복
               서비스 치킨에서 받은 쿠폰 + 남은 쿠폰으로 다음 라운드 진행
    [Time] O(log N) - 매 라운드 쿠폰이 약 1/10로 감소
    [Space] O(1)
    """
    coupons = chicken
    services = 0
    while coupons >= 10:
        n, r = divmod(coupons, 10)
        services += n
        coupons = n + r

    return services


solution = solution_v1
