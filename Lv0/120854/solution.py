"""
문제: 배열 원소의 길이
난이도: Lv0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120854

설명:
문자열 배열 strlist가 매개변수로 주어집니다.
strlist 각 원소의 길이를 담은 배열을 return하도록 solution 함수를 완성해주세요.

제한사항:
- 1 ≤ strlist 원소의 길이 ≤ 100
- strlist는 알파벳 소문자, 대문자, 특수문자로 구성되어 있습니다.
"""


def solution_v1(strlist: list[str]) -> list[int]:
    """
    [Approach] 리스트 컴프리헨션 - 각 문자열의 len() 적용
    [Time] O(n) - n개 문자열 순회
    [Space] O(n) - 결과 리스트 저장
    """
    return [len(s) for s in strlist]


def solution_v2(strlist: list[str]) -> list[int]:
    """
    [Approach] map() 함수 - len을 각 원소에 매핑
    [Time] O(n) - n개 문자열 순회
    [Space] O(n) - 결과 리스트 저장
    """
    return list(map(len, strlist))


solution = solution_v1
