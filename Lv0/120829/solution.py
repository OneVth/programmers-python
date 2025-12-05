"""
프로그래머스 Lv0 #120829 - 각도기
https://school.programmers.co.kr/learn/courses/30/lessons/120829

[문제]
각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각,
180도는 평각으로 분류합니다. 각 angle이 매개변수로 주어질 때 예각일 때 1,
직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.

- 예각 : 0 < angle < 90
- 직각 : angle = 90
- 둔각 : 90 < angle < 180
- 평각 : angle = 180

[제한]
- 0 < angle ≤ 180
- angle은 정수입니다.
"""


def solution_v1(angle: int) -> int:
    """
    [Approach] 기본값 + 조건 분기
    [Time] O(1)  [Space] O(1)
    ✅ 기본값(예각=1) 설정 후 특수 케이스만 처리
    """
    answer = 1

    if angle == 180:
        answer = 4
    elif angle > 90:
        answer = 3
    elif angle == 90:
        answer = 2

    return answer


def solution_v2(angle: int) -> int:
    """
    [Approach] 중첩 if문 (이진 분할)
    [Time] O(1)  [Space] O(1)
    ✅ 90 기준 분할 → 각 구간 내 세부 분류
    """
    if angle > 90:
        if angle == 180:
            return 4
        return 3
    else:
        if angle == 90:
            return 2
        return 1


solution = solution_v1
