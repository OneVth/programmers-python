"""
프로그래머스 Lv0 #181895 - 배열 만들기 3
https://school.programmers.co.kr/learn/courses/30/lessons/181895

[문제]
정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.

intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은 닫힌 구간입니다.
닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.

이때 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을
앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.

[제한]
- 1 ≤ arr의 길이 ≤ 100,000
  - 1 ≤ arr의 원소 < 100
- 1 ≤ a1 ≤ b1 < arr의 길이
- 1 ≤ a2 ≤ b2 < arr의 길이
"""


def solution_v1(arr: list[int], intervals: list[list[int]]) -> list[int]:
    """
    [Approach] 슬라이싱 - 각 구간을 슬라이싱으로 추출 후 연결
    [Time] O(n) - 슬라이싱이 구간 길이만큼 복사
    [Space] O(n) - 결과 리스트 저장
    """
    return arr[intervals[0][0] : intervals[0][1] + 1] + arr[intervals[1][0] : intervals[1][1] + 1]

def solution_v2(arr: list[int], intervals: list[list[int]]) -> list[int]:
    """
    [Approach] 반복문 + 누적 - 구간 개수에 관계없이 확장 가능한 구조
    [Time] O(n) - 전체 구간 요소 합산만큼 순회
    [Space] O(n) - 결과 리스트 저장
    """
    answer = []
    for i in range(len(intervals)):
        a, b = intervals[i]

        answer += arr[a:b + 1]

    return answer

def solution_v3(arr: list[int], intervals: list[list[int]]) -> list[int]:
    """
    [Approach] itertools.chain - 지연 평가로 이터러블 연결
    [Time] O(n) - 전체 요소 순회
    [Space] O(n) - 결과 리스트 저장 (중간 리스트 없음)
    """
    from itertools import chain
    return list(chain.from_iterable(arr[a: b + 1] for a, b in intervals))

solution = solution_v3
