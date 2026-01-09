"""
프로그래머스 Lv0 #120886 - A로 B 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/120886

[복습] 2차 - 2026-01-02

[문제]
문자열 before와 after가 매개변수로 주어질 때,
before의 순서를 바꾸어 after를 만들 수 있으면 1을,
만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

[제한]
- 0 < before의 길이 == after의 길이 < 1,000
- before와 after는 모두 소문자로 이루어져 있습니다.
"""


def solution_v1(before: str, after: str) -> int:
    """
    [Approach] 정렬 후 비교로 애너그램 판별
    [Time] O(n log n)  [Space] O(n) - 정렬된 리스트
    """
    return int(sorted(before) == sorted(after))


def solution_v2(before: str, after: str) -> int:
    """
    [Approach] Counter로 문자 빈도 비교
    [Time] O(n)  [Space] O(k) - k는 고유 문자 수
    """
    from collections import Counter

    return int(Counter(before) == Counter(after))


# 기본 솔루션 지정
solution = solution_v1
