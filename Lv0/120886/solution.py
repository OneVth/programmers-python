"""
프로그래머스 Lv0 #120886 - A로 B 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/120886

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
    [Approach] 딕셔너리 빈도수 비교 - before의 문자 빈도 저장 후 after와 비교
               after에 없는 문자가 있거나 빈도가 다르면 0 반환
    [Time] O(N²) - 각 문자마다 count() 호출 (N번 순회)
    [Space] O(K) - K: 고유 문자 수
    """
    dic = dict()
    for c in before:
        if c not in dic.keys():
            dic[c] = before.count(c)

    for c in after:
        if c not in dic.keys():
            return 0
        if dic[c] != after.count(c):
            dic.get()
            return 0

    return 1


def solution_v2(before: str, after: str) -> int:
    """
    [Approach] 정렬 비교 - 두 문자열을 정렬하면 애너그램은 동일해짐
    [Time] O(N log N) - 정렬
    [Space] O(N) - 정렬된 리스트
    """
    return 1 if sorted(after) == sorted(before) else 0


def solution_v3(before: str, after: str) -> int:
    """
    [Approach] Counter 비교 - 문자 빈도수 딕셔너리 직접 비교
               가장 효율적이고 파이썬스러운 방법
    [Time] O(N) - 각 문자열 한 번씩 순회
    [Space] O(K) - K: 고유 문자 수
    """
    from collections import Counter

    return Counter(before) == Counter(after)


def solution_v4(before: str, after: str) -> int:
    dic_before = dict()
    for c in before:
        dic_before[c] = dic_before.get(c, 0) + 1

    dic_after = dict()
    for c in after:
        dic_after[c] = dic_after.get(c, 0) + 1

    return 1 if dic_before == dic_after else 0


solution = solution_v4
