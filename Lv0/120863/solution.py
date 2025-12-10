"""
프로그래머스 Lv0 #120863 - 다항식 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/120863

[문제]
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다.
다항식을 계산할 때는 동류항끼리 계산해 정리합니다.
덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때,
동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요.
같은 식이라면 가장 짧은 수식을 return 합니다.

[제한]
- 0 < polynomial에 있는 수 < 100
- polynomial에 변수는 'x'만 존재합니다.
- polynomial은 양의 정수, 공백, 'x', '+'로 이루어져 있습니다.
- 항과 연산기호 사이에는 항상 공백이 존재합니다.
- 공백은 연속되지 않으며 시작이나 끝에는 공백이 없습니다.
- 하나의 항에서 변수가 숫자 앞에 오는 경우는 없습니다.
- 0으로 시작하는 수는 없습니다.
- 문자와 숫자 사이의 곱하기는 생략합니다.
- polynomial에는 일차 항과 상수항만 존재합니다.
- 계수 1은 생략합니다.
- 결괏값에 상수항은 마지막에 둡니다.
- 0 < polynomial의 길이 < 50
"""


def solution_v1(polynomial: str) -> str:
    """
    [Approach] replace로 x 제거 후 계수 추출, walrus 연산자(:=) 활용
    [Time] O(n) - n은 항의 개수
    [Space] O(n) - split 결과 리스트
    """
    tokens = polynomial.split(" + ")

    constant = 0
    coefficient = 0
    for x in tokens:
        if "x" in x:
            coefficient += 1 if not (r := x.replace("x", "")) else int(r)
        else:
            constant += int(x)

    answer = ""
    if coefficient == 0:
        answer = f"{constant}"
    elif constant == 0:
        answer = "x" if coefficient == 1 else f"{coefficient}x"
    else:
        answer = (
            f"x + {constant}" if coefficient == 1 else f"{coefficient}x + {constant}"
        )

    return answer


def solution_v2(polynomial: str) -> str:
    """
    [Approach] isdigit()으로 상수/일차항 분류, 슬라이싱으로 계수 추출
    [Time] O(n) - n은 항의 개수
    [Space] O(n) - split 결과 리스트
    """
    tokens = polynomial.split(" + ")

    constant = 0
    coefficient = 0
    for x in tokens:
        if x.isdigit():
            constant += int(x)
        else:
            coefficient += 1 if x == "x" else int(x[:-1])

    answer = ""
    if coefficient == 0:
        answer = f"{constant}"
    elif constant == 0:
        answer = "x" if coefficient == 1 else f"{coefficient}x"
    else:
        answer = (
            f"x + {constant}" if coefficient == 1 else f"{coefficient}x + {constant}"
        )

    return answer


# 기본 솔루션 지정
solution = solution_v2
