"""
프로그래머스 Lv0 #120851 - 숨어있는 숫자의 덧셈 (1)
https://school.programmers.co.kr/learn/courses/30/lessons/120851

[복습] 1차 - 2025-12-10

[문제]
문자열 my_string이 매개변수로 주어집니다.
my_string 안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ my_string의 길이 ≤ 1,000
- my_string은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.

[유의]
- 연속된 숫자도 각각 한 자리 숫자로 취급합니다.
"""


def solution_v1(my_string: str) -> int:
    """
    [Approach] Generator Expression + isdigit()
    [Time] O(n)  [Space] O(1)
    ✅ Lazy evaluation로 메모리 효율적
    """
    return sum(int(c) for c in my_string if c.isdigit())


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
