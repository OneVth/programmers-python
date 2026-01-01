"""
프로그래머스 Lv0 #181865 - 간단한 식 계산하기
https://school.programmers.co.kr/learn/courses/30/lessons/181865

[복습] 1차 - 2025-12-31

[문제]
문자열 binomial이 매개변수로 주어집니다.
binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수,
op는 '+', '-', '*' 중 하나입니다.
주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.

[제한]
- 0 ≤ a, b ≤ 40,000
- 0을 제외하고 a, b는 0으로 시작하지 않습니다.
"""


def solution_v1(binomial: str) -> int:
    """
    [Approach] operator 모듈로 연산자를 함수로 매핑
    [Time] O(n) - 문자열 파싱
    [Space] O(1) - 고정 크기 딕셔너리
    """
    import operator

    op_dict = {"+": operator.add, "-": operator.sub, "*": operator.mul}

    a, op, b = binomial.split()
    return op_dict[op](int(a), int(b))


solution = solution_v1
