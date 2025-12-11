"""
프로그래머스 Lv0 #120868 - 삼각형의 완성조건 (2)
https://school.programmers.co.kr/learn/courses/30/lessons/120868

[문제]
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.
- 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.

삼각형의 두 변의 길이가 담긴 배열 sides가 매개변수로 주어집니다.
나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

[제한]
- sides의 원소는 자연수입니다.
- sides의 길이는 2입니다.
- 1 ≤ sides의 원소 ≤ 1,000
"""


def solution_v1(sides: list[int]) -> int:
    """
    While loop - 경우를 나눠서 순회

    [Approach] longer가 최장변일 때와 x가 최장변일 때를 나눠서 카운트
    [Time] O(n) - n은 가능한 x의 개수 (최대 ~2000)
    [Space] O(1)
    """
    answer = 0
    longer = max(sides)
    shorter = min(sides)

    # longer가 제일 긴 변인 경우: longer - shorter < x <= longer
    x = longer - shorter + 1
    while longer < shorter + x and x <= longer:
        x += 1
        answer += 1

    # x가 제일 긴 변인 경우: longer < x < longer + shorter
    x = longer + 1
    rest = sum(sides)
    while x < rest:
        x += 1
        answer += 1

    return answer


def solution_v2(sides: list[int]) -> int:
    """
    수학적 계산 - O(1)

    [Approach]
    삼각 부등식: |a - b| < x < a + b
    - x가 최장변: longer < x < longer + shorter → (shorter - 1)개
    - x가 최장변 아님: longer - shorter < x <= longer → shorter개
    - 합계: 2 * shorter - 1 = 2 * min(sides) - 1

    [Time] O(1)  [Space] O(1)
    """
    return 2 * min(sides) - 1


# 기본 솔루션
solution = solution_v2
