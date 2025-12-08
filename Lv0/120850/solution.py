"""
문제: 문자열 정렬하기 (1)
난이도: Lv0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120850

설명:
문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는
숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

제한사항:
- 1 ≤ my_string의 길이 ≤ 100
- my_string에는 숫자가 한 개 이상 포함되어 있습니다.
- my_string은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 있습니다.
"""


def solution_v1(my_string: str) -> list[int]:
    """
    [Approach] 리스트 컴프리헨션 - isdigit() 필터링 후 정렬
    [Time] O(n log n) - 정렬이 지배적
    [Space] O(n) - 숫자 리스트 저장
    """
    return sorted(int(c) for c in my_string if c.isdigit())


def solution_v2(my_string: str) -> list[int]:
    """
    [Approach] 정규표현식 - re.findall()로 숫자 추출 후 정렬
    [Time] O(n log n) - 정렬이 지배적
    [Space] O(n) - 숫자 리스트 저장
    """
    import re

    return sorted(int(c) for c in re.findall(r"\d", my_string))


def solution_v3(my_string: str) -> list[int]:
    """
    [Approach] 함수형 스타일 - filter + map + sorted
    [Time] O(n log n) - 정렬이 지배적
    [Space] O(n) - 숫자 리스트 저장
    """
    return sorted(map(int, filter(str.isdigit, my_string)))


solution = solution_v3
