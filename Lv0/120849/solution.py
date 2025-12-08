"""
문제: 모음 제거
난이도: Lv0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849

설명:
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.
문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을
return하도록 solution 함수를 완성해주세요.

제한사항:
- my_string은 소문자와 공백으로 이루어져 있습니다.
- 1 ≤ my_string의 길이 ≤ 1,000
"""


def solution_v1(my_string: str) -> str:
    """
    [Approach] 리스트 컴프리헨션 - 모음이 아닌 문자만 필터링
    [Time] O(n) - 문자열 순회
    [Space] O(n) - 결과 문자열 저장
    """
    return "".join(c for c in my_string if c not in "aeiou")


def solution_v2(my_string: str) -> str:
    """
    [Approach] str.translate() - 변환 테이블로 모음 삭제
    [Time] O(n) - C 레벨 최적화로 가장 빠름
    [Space] O(n) - 결과 문자열 저장
    """
    return my_string.translate(str.maketrans("", "", "aeiou"))


def solution_v3(my_string: str) -> str:
    """
    [Approach] replace() 체이닝 - 각 모음을 순차적으로 제거
    [Time] O(5n) = O(n) - 5번의 전체 순회
    [Space] O(n) - 중간 문자열 5개 생성
    """
    return (
        my_string.replace("a", "")
        .replace("e", "")
        .replace("i", "")
        .replace("o", "")
        .replace("u", "")
    )


def solution_v4(my_string: str) -> str:
    """
    [Approach] 정규표현식 - 패턴 매칭으로 모음 제거
    [Time] O(n) - 정규식 엔진 처리
    [Space] O(n) - 결과 문자열 저장
    """
    import re

    return re.sub(r"[aeiou]", "", my_string)


solution = solution_v4
