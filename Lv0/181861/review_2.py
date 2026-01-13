"""
프로그래머스 Lv0 #181861 - 배열의 원소만큼 추가하기
https://school.programmers.co.kr/learn/courses/30/lessons/181861

[복습] 2차 - 2026-01-02

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
    [Approach] 리스트 반복 연산: 각 원소 a를 a번 반복하여 확장
    [Time] O(n * m) - n은 arr 길이, m은 원소의 평균값
    [Space] O(n * m) - 결과 리스트 크기
    """
    answer = []
    for i in arr:
        answer += [i] * i

    return answer


def solution_v2(arr: list[int]) -> list[int]:
    """
    [Approach] itertools.chain: 제너레이터를 평탄화하여 단일 리스트로 변환
    [Time] O(n * m) - n은 arr 길이, m은 원소의 평균값
    [Space] O(n * m) - 결과 리스트 크기 (chain 자체는 lazy evaluation)
    """
    from itertools import chain

    return list(chain.from_iterable([a] * a for a in arr))


solution = solution_v2
