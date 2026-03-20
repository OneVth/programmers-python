"""
프로그래머스 Lv0 #181913 - 문자열 여러 번 뒤집기
https://school.programmers.co.kr/learn/courses/30/lessons/181913

[문제]
문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다.
queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다.
my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- my_string은 영소문자로만 이루어져 있습니다.
- 1 ≤ my_string의 길이 ≤ 1,000
- queries의 원소는 [s, e]의 형태로 0 ≤ s ≤ e < my_string의 길이를 만족합니다.
- 1 ≤ queries의 길이 ≤ 1,000
"""


def solution_v1(my_string: str, queries: list[list[int]]) -> str:
    """
    [Approach] 각 쿼리마다 문자열을 3조각으로 분리 후 중간 부분 역순으로 재조합
    [Time] O(q * n)  [Space] O(n)
    """
    answer = list(my_string)
    for s, e in queries:
        answer = answer[:s] + answer[s : e + 1][::-1] + answer[e + 1 :]

    return "".join(answer)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
