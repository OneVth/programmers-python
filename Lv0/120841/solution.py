"""
프로그래머스 Lv0 #120841 - 점의 위치 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120841

[문제]
사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다.
사분면은 1부터 4까지 번호를 매깁니다.

- x 좌표와 y 좌표가 모두 양수이면 제1사분면에 속합니다.
- x 좌표가 음수, y 좌표가 양수이면 제2사분면에 속합니다.
- x 좌표와 y 좌표가 모두 음수이면 제3사분면에 속합니다.
- x 좌표가 양수, y 좌표가 음수이면 제4사분면에 속합니다.

x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다.
좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록
solution 함수를 완성해주세요.

[제한]
- dot의 길이 = 2
- dot[0]은 x좌표를, dot[1]은 y좌표를 나타냅니다
- -500 ≤ dot의 원소 ≤ 500
- dot의 원소는 0이 아닙니다.
"""


def solution_v1(dot: list[int]) -> int:
    """
    [Approach] 중첩 if문으로 x, y 부호 판별
    [Time] O(1)  [Space] O(1)
    ✅ 직관적인 조건 분기
    """
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        else:
            return 4
    else:
        if dot[1] > 0:
            return 2
        else:
            return 3


def solution_v2(dot: list[int]) -> int:
    """
    [Approach] 딕셔너리 + 튜플 키 매핑
    [Time] O(1)  [Space] O(1)
    ✅ 조건문 없이 해시 조회로 해결
    """
    quad = {(True, True): 1, (False, True): 2, (False, False): 3, (True, False): 4}
    return quad[(dot[0] > 0, dot[1] > 0)]


def solution_v3(dot: list[int]) -> int:
    """
    [Approach] 수학 공식으로 사분면 계산
    [Time] O(1)  [Space] O(1)
    ⚠️ 학습용 - 공식 유도: 3 + x_pos - y_pos - 2*x_pos*y_pos
    """
    x_pos = int(dot[0] > 0)
    y_pos = int(dot[1] > 0)
    return 3 + x_pos - y_pos - 2 * x_pos * y_pos


def solution_v4(dot: list[int]) -> int:
    """
    [Approach] 2D 리스트 인덱싱
    [Time] O(1)  [Space] O(1)
    ✅ Boolean을 인덱스로 활용
    """
    #       y<0  y>0
    quad = [[3, 2],   # x<0
            [4, 1]]   # x>0
    return quad[dot[0] > 0][dot[1] > 0]


solution = solution_v2
