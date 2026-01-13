"""
프로그래머스 Lv0 #181862 - 세 개의 구분자
https://school.programmers.co.kr/learn/courses/30/lessons/181862

[복습] 2차 - 2026-01-02

[문제]
임의의 문자열이 주어졌을 때 문자 "a", "b", "c"를 구분자로 사용해 문자열을 나누고자 합니다.

예를 들어 주어진 문자열이 "baconlettucetomato"라면 나눠진 문자열 목록은
["onlettu", "etom", "to"] 가 됩니다.

문자열 myStr이 주어졌을 때 위 예시와 같이 "a", "b", "c"를 사용해 나눠진 문자열을
순서대로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

단, 두 구분자 사이에 다른 문자가 없을 경우에는 아무것도 저장하지 않으며,
return할 배열이 빈 배열이라면 ["EMPTY"]를 return 합니다.

[제한]
- 1 ≤ myStr의 길이 ≤ 1,000,000
- myStr은 알파벳 소문자로 이루어진 문자열 입니다.
"""


def solution_v1(myStr: str) -> list[str]:
    """
    [Approach] 정규식 split + 문자 클래스: [abc]로 분리 후 빈 문자열 필터링
    [Time] O(n) - 문자열 한 번 순회
    [Space] O(n) - 분리된 결과 리스트 저장
    """
    import re

    answer = [s for s in re.split(r"[abc]", myStr) if s]
    return answer if answer else ["EMPTY"]


def solution_v2(myStr: str) -> list[str]:
    """
    [Approach] translate + split: 구분자를 공백으로 치환 후 split()으로 분리
    [Time] O(n) - translate와 split 각각 O(n)
    [Space] O(n) - 변환된 문자열과 결과 리스트
    """
    answer = myStr.translate(str.maketrans("abc", "   ")).split()
    return answer if answer else ["EMPTY"]


solution = solution_v2
