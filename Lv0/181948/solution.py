"""
프로그래머스 Lv0 #181948 - 특수문자 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/181948

[문제]
다음과 같이 출력하도록 코드를 작성해 주세요.

출력 예시:
!@#$%^&*(\'"<>?:;
"""


def solution_v1() -> str:
    """
    [Approach] raw string으로 백슬래시를 literal로 표현
    [Time] O(1)  [Space] O(1)
    """
    return r'!@#$%^&*(\'"<>?:;'


def solution_v2() -> str:
    """
    [Approach] 일반 문자열에서 \\\\ = \\, \\' = ' 이스케이프 조합
    [Time] O(1)  [Space] O(1)
    """
    return '!@#$%^&*(\\\'"<>?:;'

solution = solution_v1