"""
프로그래머스 Lv0 #120868 - 삼각형의 완성조건 (2)
https://school.programmers.co.kr/learn/courses/30/lessons/120868

[복습] 1차 - 2025-12-17

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
    Range 길이 활용 - 한 줄 솔루션

    [Approach]
    삼각 부등식에서 x의 범위: |a-b| < x < a+b
    - 하한: max(sides) - min(sides) + 1 (정수이므로 +1)
    - 상한: sum(sides) - 1 (미만이므로 range에서 자동 제외)
    - range(start, end)의 길이가 곧 정답

    [Time] O(1)  [Space] O(1)
    """
    return len(range(max(sides) - min(sides) + 1, sum(sides)))


# 기본 솔루션
solution = solution_v1
