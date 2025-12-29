"""
프로그래머스 Lv0 #181861 - 배열의 원소만큼 추가하기
https://school.programmers.co.kr/learn/courses/30/lessons/181861

[문제]
아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 양의 정수 배열 arr가 매개변수로 주어질 때,
arr의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 X의 맨 뒤에 a를 a번 추가하는 일을
반복한 뒤의 배열 X를 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ arr의 길이 ≤ 100
- 1 ≤ arr의 원소 ≤ 100
"""


def solution_v1(arr: list[int]) -> list[int]:
    """
    [Approach] 반복문으로 리스트 확장 - 원소 a를 a번 추가
    [Time] O(n * m) - n: 배열 길이, m: 원소 평균값  [Space] O(n * m)
    """
    stk = []
    for i in arr:
        stk += [i] * i
    return stk


def solution_v2(arr: list[int]) -> list[int]:
    """
    [Approach] 리스트 컴프리헨션 + sum으로 중첩 리스트 펼치기
    [Time] O(n² * m) - sum의 리스트 연결이 O(n)  [Space] O(n * m)
    """
    return sum([[a] * a for a in arr], [])


def solution_v3(arr: list[int]) -> list[int]:
    """
    [Approach] itertools.chain으로 중첩 이터러블 펼치기 (효율적)
    [Time] O(n * m)  [Space] O(n * m)
    """
    from itertools import chain

    return list(chain.from_iterable([a] * a for a in arr))


solution = solution_v3
