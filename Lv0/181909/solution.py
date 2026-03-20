"""
프로그래머스 Lv0 #181909 - 접미사 배열
https://school.programmers.co.kr/learn/courses/30/lessons/181909

[문제]
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다.
예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string이 매개변수로 주어질 때, my_string의 모든 접미사를 사전순으로 정렬한
문자열 배열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- my_string은 알파벳 소문자로만 이루어져 있습니다.
- 1 ≤ my_string의 길이 ≤ 100
"""


def solution_v1(my_string: str) -> list[str]:
    """
    [Approach] 인덱스 순회로 모든 접미사 생성 후 정렬
    [Time] O(n² log n)  [Space] O(n²)
    """
    suffix = []
    for i in range(len(my_string)):
        suffix.append(my_string[i:])

    return sorted(suffix)


def solution_v2(my_string: str) -> list[str]:
    """
    [Approach] 제너레이터 표현식으로 접미사 생성 후 정렬 (v1의 one-liner 리팩토링)
    [Time] O(n² log n)  [Space] O(n²)
    """
    return sorted(my_string[i:] for i in range(len(my_string)))


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
