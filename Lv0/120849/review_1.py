"""
프로그래머스 Lv0 #120849 - 모음 제거
https://school.programmers.co.kr/learn/courses/30/lessons/120849

[복습] 1차 - 2025-12-10

[문제]
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.
문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을
return하도록 solution 함수를 완성해주세요.

[제한]
- my_string은 소문자와 공백으로 이루어져 있습니다.
- 1 ≤ my_string의 길이 ≤ 1,000
"""


def solution_v1(my_string: str) -> str:
    """
    [Approach] str.translate - 삭제용 maketrans
    [Time] O(n)  [Space] O(n)
    ✅ C레벨 최적화, 가장 빠름
    """
    return my_string.translate(str.maketrans("", "", "aeiou"))


def solution_v2(my_string: str) -> str:
    """
    [Approach] 정규표현식 re.sub
    [Time] O(n)  [Space] O(n)
    ✅ 복잡한 패턴에 유연함
    """
    import re

    return re.sub(r"[aeiou]", "", my_string)


def solution_v3(my_string: str) -> str:
    """
    [Approach] replace 체이닝
    [Time] O(5n) = O(n)  [Space] O(n)
    ⚠️ 5번 순회, 중간 문자열 5개 생성
    """
    return (
        my_string.replace("a", "")
        .replace("e", "")
        .replace("i", "")
        .replace("o", "")
        .replace("u", "")
    )


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v3