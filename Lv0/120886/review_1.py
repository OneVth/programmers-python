"""
프로그래머스 Lv0 #120886 - A로 B 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/120886

[복습] 1차 - 2025-12-17

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
    [Approach] 정렬 후 비교 (Anagram 판별)
               - 두 문자열을 정렬하면 같은 문자 구성이면 동일해짐
               - bool 결과가 int로 자동 변환 (True=1, False=0)
    [Time] O(n log n) - 정렬
    [Space] O(n) - 정렬된 리스트 저장
    """
    return sorted(before) == sorted(after)


def solution_v2(before: str, after: str) -> int:
    """
    [Approach] Counter를 이용한 문자 빈도 비교
               - 각 문자의 출현 횟수를 딕셔너리로 카운트
               - Counter 객체끼리 직접 비교 가능
    [Time] O(n) - 문자열 한 번 순회
    [Space] O(k) - k는 고유 문자 수 (최대 26)
    """
    from collections import Counter

    return Counter(before) == Counter(after)


solution = solution_v2
