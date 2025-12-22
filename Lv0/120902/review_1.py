"""
프로그래머스 Lv0 #120902 - 문자열 계산하기
https://school.programmers.co.kr/learn/courses/30/lessons/120902

[복습] 1차 - 2025-12-17

[문제]
my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로
주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

[제한]
- 연산자는 +, -만 존재합니다.
- 문자열의 시작과 끝에는 공백이 없습니다.
- 0으로 시작하는 숫자는 주어지지 않습니다.
- 잘못된 수식은 주어지지 않습니다.
- 5 ≤ my_string의 길이 ≤ 100
- my_string을 계산한 결과값은 1 이상 100,000 이하입니다.
  - my_string의 중간 계산 값은 -100,000 이상 100,000 이하입니다.
  - 계산에 사용하는 숫자는 1 이상 20,000 이하인 자연수입니다.
  - my_string에는 연산자가 적어도 하나 포함되어 있습니다.
- return type은 정수형입니다.
- my_string의 숫자와 연산자는 공백 하나로 구분되어 있습니다.
"""


def solution_v1(my_string: str) -> int:
    """
    [Approach] 뺄셈을 음수 덧셈으로 변환 후 합계 계산
    [Time] O(n)  [Space] O(n) - 분할된 토큰 저장
    """
    exp = my_string.replace(" - ", " + -")
    return sum(int(c) for c in exp.split(" + "))


def solution_v2(my_string: str) -> int:
    """
    [Approach] 후위 표기법 변환 후 스택 기반 계산
    [Time] O(n)  [Space] O(n) - 후위 표현식 및 스택
    """
    post_exp = []
    op = []

    for c in my_string.split(" "):
        if c in "+-":
            if op:
                post_exp.append(op.pop())
            op.append(c)
        else:
            post_exp.append(int(c))

    while op:
        post_exp.append(op.pop())

    stack = []
    for i in post_exp:
        if i == "+" or i == "-":
            if i == "+":
                result = stack.pop(-2) + stack.pop(-1)
            else:
                result = stack.pop(-2) - stack.pop(-1)
            stack.append(result)
        else:
            stack.append(i)

    return stack[0]


solution = solution_v2
