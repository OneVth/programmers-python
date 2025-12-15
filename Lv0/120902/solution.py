"""
프로그래머스 Lv0 #120902 - 문자열 계산하기
https://school.programmers.co.kr/learn/courses/30/lessons/120902

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
    [Approach] 스택 기반 계산기 - 피연산자/연산자 스택으로 순차 계산
    [Time] O(n)  [Space] O(n)
    """
    post_eval = []
    operators = []
    for c in my_string.split():
        if c == "+" or c == "-":
            if operators:
                op = operators.pop()
                value = 0
                if op == "+":
                    value = str(int(post_eval.pop(-2)) + int(post_eval.pop(-1)))
                else:
                    value = str(int(post_eval.pop(-2)) - int(post_eval.pop(-1)))
                post_eval.append(value)

            operators.append(c)
        else:
            post_eval.append(c)

    while operators:
        op = operators.pop()
        value = 0
        if op == "+":
            value = str(int(post_eval.pop(-2)) + int(post_eval.pop(-1)))
        else:
            value = str(int(post_eval.pop(-2)) - int(post_eval.pop(-1)))
        post_eval.append(value)

    return int(post_eval[0])


def solution_v2(my_string: str) -> int:
    """
    [Approach] 순차 계산 - 토큰을 2칸씩 건너뛰며 연산자+피연산자 처리
    [Time] O(n)  [Space] O(n) - split으로 토큰 리스트 생성
    """
    tokens = my_string.split()
    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        op, num = tokens[i], int(tokens[i + 1])
        result = result + num if op == "+" else result - num
    return result


solution = solution_v1
