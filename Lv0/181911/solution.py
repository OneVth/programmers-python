"""
프로그래머스 Lv0 #181911 - 부분 문자열 이어 붙여 문자열 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/181911

[문제]
길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다.
parts[i]는 [s, e] 형태로, my_strings[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다.
각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는
solution 함수를 작성해 주세요.

[제한]
- 1 ≤ my_strings의 길이 = parts의 길이 ≤ 100
- 1 ≤ my_strings의 원소의 길이 ≤ 100
- parts[i]를 [s, e]라 할 때, 0 ≤ s ≤ e < my_strings[i]의 길이
"""


def solution_v1(my_strings: list[str], parts: list[list[int]]) -> str:
    """
    [Approach] range 인덱스 순회로 부분 문자열 추출 후 join
    [Time] O(n * m)  [Space] O(n * m)
    """
    answer = []
    for i in range(len(my_strings)):
        answer.append(my_strings[i][parts[i][0] : parts[i][1] + 1])
    return "".join(answer)


def solution_v2(my_strings: list[str], parts: list[list[int]]) -> str:
    """
    [Approach] enumerate + 언패킹으로 s, e를 명시적으로 분리
    [Time] O(n * m)  [Space] O(n * m)
    """
    answer = []
    for i, (s, e) in enumerate(parts):
        answer.append(my_strings[i][s : e + 1])
    return "".join(answer)


def solution_v3(my_strings: list[str], parts: list[list[int]]) -> str:
    """
    [Approach] zip + 제너레이터 표현식으로 one-liner 구현
    [Time] O(n * m)  [Space] O(n * m)
    """
    return "".join(x[y[0] : y[1] + 1] for x, y in zip(my_strings, parts))


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v3
