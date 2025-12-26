"""
프로그래머스 Lv0 #181839 - 주사위 게임 1
https://school.programmers.co.kr/learn/courses/30/lessons/181839

[문제]
1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다.
두 주사위를 굴렸을 때 나온 숫자를 각각 a, b라고 했을 때 얻는 점수는 다음과 같습니다.

- a와 b가 모두 홀수라면 a² + b² 점을 얻습니다.
- a와 b 중 하나만 홀수라면 2 × (a + b) 점을 얻습니다.
- a와 b 모두 홀수가 아니라면 |a - b| 점을 얻습니다.

두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return 하는
solution 함수를 작성해 주세요.

[제한]
- a와 b는 1 이상 6 이하의 정수입니다.
"""


def solution_v1(a: int, b: int) -> int:
    """
    [Approach] 홀수 여부를 판별 후 조건 분기 - 짝짝/홀홀/혼합 순서로 처리
    [Time] O(1)  [Space] O(1)
    """
    is_odd_a = a % 2
    is_odd_b = b % 2

    if not is_odd_a and not is_odd_b:
        return abs(a - b)

    if is_odd_a and is_odd_b:
        return a**2 + b**2
    else:
        return 2 * (a + b)


def solution_v2(a: int, b: int) -> int:
    """
    [Approach] 홀수 개수를 세어 분기 - 2/1/0개로 명확한 케이스 구분
    [Time] O(1)  [Space] O(1)
    """
    odd = (a % 2) + (b % 2)
    if odd == 2:
        return a**2 + b**2
    elif odd == 1:
        return 2 * (a + b)
    else:
        return abs(a - b)


# ✅ 기본 솔루션 지정
solution = solution_v2
