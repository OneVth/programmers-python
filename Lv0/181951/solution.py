"""
프로그래머스 Lv0 #181951 - a와 b 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/181951

[문제]
정수 a와 b가 주어집니다.
각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

[제한]
- -100,000 ≤ a, b ≤ 100,000
"""


def solution_v1(a: int, b: int) -> str:
    """
    [Approach] f-string으로 포맷된 문자열 반환
    [Time] O(1)  [Space] O(1)
    """
    return f"a = {a}\nb = {b}"


solution = solution_v1
