"""
프로그래머스 Lv0 #120818 - 옷가게 할인 받기
https://school.programmers.co.kr/learn/courses/30/lessons/120818

[문제]
옷가게에서 10만 원 이상 구매 시 5%, 30만 원 이상 구매 시 10%, 50만 원 이상 구매 시 20% 할인.
price가 주어질 때 지불 금액을 반환 (소수점 이하 버림)

[제한]
- 10 ≤ price ≤ 1,000,000
- price는 10원 단위
"""


def solution_v1(price: int) -> int:
    """
    [Approach] if-elif 분기
    [Time] O(1)  [Space] O(1)
    """
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    return price


def solution_v2(price: int) -> int:
    """
    [Approach] dict + 순회
    [Time] O(1)  [Space] O(1)
    ⚠️ Python 3.7+ 필요 (dict 삽입 순서 보장)
    """
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for threshold, rate in discount_rates.items():
        if price >= threshold:
            return int(price * rate)


def solution_v3(price: int) -> int:
    """
    [Approach] list of tuples + 순회
    [Time] O(1)  [Space] O(1)
    ✅ 순서 보장이 명시적, 버전 독립적
    """
    discount_rates = [(500000, 0.8), (300000, 0.9), (100000, 0.95), (0, 1)]
    for threshold, rate in discount_rates:
        if price >= threshold:
            return int(price * rate)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v3
