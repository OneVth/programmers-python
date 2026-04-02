"""
프로그래머스 Lv0 #250127 - [PCCE 기출문제] 7번 / 가습기
https://school.programmers.co.kr/learn/courses/30/lessons/250127

[문제]
상우가 사용하는 가습기에는 "auto", "target", "minimum"의 세 가지 모드가 있습니다.
가습기의 가습량은 0~5단계로 구분되며 각 모드 별 동작 방식은 다음과 같습니다.

"auto" 모드
- 습도가 0 이상 10 미만인 경우 : 5단계
- 습도가 10 이상 20 미만인 경우 : 4단계
- 습도가 20 이상 30 미만인 경우 : 3단계
- 습도가 30 이상 40 미만인 경우 : 2단계
- 습도가 40 이상 50 미만인 경우 : 1단계
- 습도가 50 이상인 경우 : 0단계

"target" 모드
- 습도가 설정값 미만일 경우 : 3단계
- 습도가 설정값 이상일 경우 : 1단계

"minimum" 모드
- 습도가 설정값 미만일 경우 : 1단계
- 습도가 설정값 이상일 경우 : 0단계

mode_type, 현재 공기 중 습도 humidity, 설정값 val_set이 주어질 때
현재 가습기가 몇 단계로 작동 중인지 return하도록 solution 함수를 완성해 주세요.

[제한]
- mode_type은 "auto", "target", "minimum" 세 가지 중 하나의 값을 갖습니다.
- 0 ≤ humidity, val_set ≤ 100
"""


def solution_v1(mode_type: str, humidity: int, val_set: int) -> int:
    """
    [Approach] 모드별 헬퍼 함수(func1/func2/func3)로 로직 분리 후 mode_type으로 dispatch
               C++ 빈칸채우기 원본 구조를 그대로 Python으로 옮긴 방식
    [Time] O(1) - 입력 크기와 무관한 고정된 조건 분기
    [Space] O(1)
    """
    def func1(humidity, val_set):
        if humidity < val_set:
            return 3
        return 1

    def func2(humidity):
        if humidity >= 50:
            return 0
        elif humidity >= 40:
            return 1
        elif humidity >= 30:
            return 2
        elif humidity >= 20:
            return 3
        elif humidity >= 10:
            return 4
        else:
            return 5

    def func3(humidity, val_set):
        if humidity < val_set:
            return 1
        return 0

    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)
    elif mode_type == "target":
        answer = func1(humidity, val_set)
    elif mode_type == "minimum":
        answer = func3(humidity, val_set)
    return answer


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
