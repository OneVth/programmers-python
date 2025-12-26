"""
프로그래머스 Lv0 #181843 - 부분 문자열인지 확인하기
https://school.programmers.co.kr/learn/courses/30/lessons/181843

[문제]
부분 문자열이란 문자열에서 연속된 일부분에 해당하는 문자열을 의미합니다.
예를 들어, 문자열 "ana", "ban", "anana", "banana", "n"는 모두 문자열 "banana"의
부분 문자열이지만, "aaa", "bnana", "wxyz"는 모두 "banana"의 부분 문자열이 아닙니다.

문자열 my_string과 target이 매개변수로 주어질 때, target이 문자열 my_string의
부분 문자열이라면 1을, 아니라면 0을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ my_string의 길이 ≤ 100
- my_string은 영소문자로만 이루어져 있습니다.
- 1 ≤ target의 길이 ≤ 100
- target은 영소문자로만 이루어져 있습니다.
"""


def solution_v1(my_string: str, target: str) -> int:
    """
    [Approach] in 연산자로 target이 my_string에 포함되는지 확인
    [Time] O(n * m) - n: my_string 길이, m: target 길이
    [Space] O(1)
    """
    return int(target in my_string)


def solution_v2(my_string: str, target: str) -> int:
    """
    [Approach] 슬라이딩 윈도우 방식 - 리스트로 변환 후 앞에서부터 비교하며 pop
    [Time] O(n * m) - 매 반복마다 슬라이스 비교
    [Space] O(n) - 리스트 변환
    """
    str_list = list(my_string)

    for _ in range(len(my_string)):
        if str_list[: len(target)] == list(target):
            return 1
        str_list.pop(0)

    return 0


# ✅ 기본 솔루션 지정
solution = solution_v2
