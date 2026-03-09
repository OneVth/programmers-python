"""
프로그래머스 Lv0 #181886 - 5명씩
https://school.programmers.co.kr/learn/courses/30/lessons/181886

[문제]
최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서있는 사람들의 이름이 담긴
문자열 리스트 names가 주어질 때, 앞에서 부터 5명씩 묶은 그룹의 가장 앞에
서있는 사람들의 이름을 담은 리스트를 return하도록 solution 함수를 완성해주세요.
마지막 그룹이 5명이 되지 않더라도 가장 앞에 있는 사람의 이름을 포함합니다.

[제한]
- 5 <= names의 길이 <= 30
- 1 <= names의 원소의 길이 <= 10
- names의 원소는 영어 알파벳 소문자로만 이루어져 있습니다.
"""


def solution_v1(names: list[str]) -> list[str]:
    """
    [Approach] range step으로 매 5번째 인덱스 접근
    [Time] O(n/5)  [Space] O(n/5)
    """
    return [names[i] for i in range(0, len(names), 5)]


def solution_v2(names: list[str]) -> list[str]:
    """
    [Approach] 슬라이싱 step으로 매 5번째 원소 추출
    [Time] O(n/5)  [Space] O(n/5)
    """
    return names[::5]


solution = solution_v2
