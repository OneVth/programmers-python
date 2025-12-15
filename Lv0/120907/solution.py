"""
프로그래머스 Lv0 #120907 - OX퀴즈
https://school.programmers.co.kr/learn/courses/30/lessons/120907

[문제]
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가
매개변수로 주어집니다. 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은
배열을 return하도록 solution 함수를 완성해주세요.

[제한]
- 연산 기호와 숫자 사이는 항상 하나의 공백이 존재합니다.
  단 음수를 표시하는 마이너스 기호와 숫자 사이에는 공백이 존재하지 않습니다.
- 1 ≤ quiz의 길이 ≤ 10
- X, Y, Z는 각각 0부터 9까지 숫자로 이루어진 정수를 의미하며,
  각 숫자의 맨 앞에 마이너스 기호가 하나 있을 수 있고 이는 음수를 의미합니다.
- X, Y, Z는 0을 제외하고는 0으로 시작하지 않습니다.
- -10,000 ≤ X, Y ≤ 10,000
- -20,000 ≤ Z ≤ 20,000
- [연산자]는 + 와 - 중 하나입니다.
"""


def solution_v1(quiz: list[str]) -> list[str]:
    """
    [Approach] 스택 기반 수식 평가 - 범용 계산기 구조
    [Time] O(n * m)  [Space] O(m) - n: quiz 길이, m: 수식 토큰 수
    """

    def evaluation(expression: str) -> int:
        operands = []
        operations = []
        for x in expression.split():
            if x == "+" or x == "-":
                if operations:
                    op = operations.pop()
                    if op == "+":
                        value = operands.pop(-2) + operands.pop(-1)
                    else:
                        value = operands.pop(-2) - operands.pop(-1)
                    operands.append(value)
                operations.append(x)
            else:
                operands.append(int(x))

        while operations:
            op = operations.pop()
            if op == "+":
                value = operands.pop(-2) + operands.pop(-1)
            else:
                value = operands.pop(-2) - operands.pop(-1)
            operands.append(value)

        return operands[0]

    answer = []
    for exp in quiz:
        left, right = exp.split(" = ")
        if evaluation(left) == int(right):
            answer.append("O")
        else:
            answer.append("X")

    return answer


def solution_v2(quiz: list[str]) -> list[str]:
    """
    [Approach] 직접 파싱 - split()으로 토큰 분리 후 연산자 분기
    [Time] O(n)  [Space] O(n)
    """
    answer = []
    for q in quiz:
        left, right = q.split(" = ")
        a, op, b = left.split()
        if op == "+":
            result = "O" if int(a) + int(b) == int(right) else "X"
        else:
            result = "O" if int(a) - int(b) == int(right) else "X"
        answer.append(result)
    return answer


solution = solution_v2
