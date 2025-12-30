"""
프로그래머스 Lv0 #181865 - 간단한 식 계산하기
https://school.programmers.co.kr/learn/courses/30/lessons/181865

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
    [Approach] split으로 파싱 후 조건문으로 연산 분기
    [Time] O(n)  [Space] O(1)
    - n: 문자열 길이 (split 비용)
    """
    a, op, b = binomial.split()
    a, b = int(a), int(b)

    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:  # op == "*"
        return a * b


def solution_v2(binomial: str) -> int:
    """
    [Approach] operator 모듈 + 딕셔너리 디스패치
    [Time] O(n)  [Space] O(1)
    - 조건문 없이 딕셔너리 매핑으로 연산 선택
    """
    import operator

    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    a, op, b = binomial.split()
    return ops[op](int(a), int(b))


solution = solution_v2
