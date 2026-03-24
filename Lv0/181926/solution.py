"""
프로그래머스 Lv0 #181926 - 수 조작하기 1
https://school.programmers.co.kr/learn/courses/30/lessons/181926

[문제]
정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로
이루어져 있으며, control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.

- "w" : n이 1 커집니다.
- "s" : n이 1 작아집니다.
- "d" : n이 10 커집니다.
- "a" : n이 10 작아집니다.

위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는
solution 함수를 완성해 주세요.

[제한]
- -100,000 ≤ n ≤ 100,000
- 1 ≤ control의 길이 ≤ 100,000
- control은 알파벳 소문자 "w", "a", "s", "d"로 이루어진 문자열입니다.
"""


def solution_v1(n: int, control: str) -> int:
    """
    [Approach] 문자 → 델타값 딕셔너리로 매핑 후 n에 순차 누적
    [Time] O(n)  [Space] O(1)
    """
    answer = n
    tab = {"w": 1, "s": -1, "d": 10, "a": -10}
    for c in control:
        answer += tab[c]
    return answer


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
