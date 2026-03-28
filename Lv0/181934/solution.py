"""
프로그래머스 Lv0 #181934 - 조건 문자열
https://school.programmers.co.kr/learn/courses/30/lessons/181934

[문제]
문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.
두 수가 n과 m이라면
- ">", "=" : n >= m
- "<", "=" : n <= m
- ">", "!" : n > m
- "<", "!" : n < m

두 문자열 ineq와 eq가 주어집니다.
ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다.
두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ n, m ≤ 100
"""


def solution_v1(ineq: str, eq: str, n: int, m: int) -> int:
    """
    [Approach] ineq/eq 조합을 if-elif 체인으로 4가지 경우 분기
    [Time] O(1)  [Space] O(1)
    """
    if ineq == ">" and eq == "=":
        return int(n >= m)
    elif ineq == "<" and eq == "=":
        return int(n <= m)
    elif ineq == ">" and eq == "!":
        return int(n > m)
    elif ineq == "<" and eq == "!":
        return int(n < m)


def solution_v2(ineq: str, eq: str, n: int, m: int) -> int:
    """
    [Approach] ineq+eq를 키로 딕셔너리 매핑 — 분기 대신 데이터로 표현
    [Time] O(1)  [Space] O(1)
    """
    ops = {">=": n >= m, "<=": n <= m, ">!": n > m, "<!": n < m}
    return int(ops[ineq + eq])


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
