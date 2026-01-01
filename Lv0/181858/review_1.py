"""
프로그래머스 Lv0 #181858 - 무작위로 K개의 수 뽑기
https://school.programmers.co.kr/learn/courses/30/lessons/181858

[복습] 1차 - 2025-12-31

[문제]
랜덤으로 서로 다른 k개의 수를 저장한 배열을 만드려고 합니다.
적절한 방법이 떠오르지 않기 때문에 일정한 범위 내에서 무작위로 수를 뽑은 후,
지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가하는 방식으로 만들기로 합니다.

정수 배열 arr가 주어집니다. 문제에서의 무작위의 수는 arr에 저장된 순서대로
주어질 예정이라고 했을 때, 완성될 배열을 return 하는 solution 함수를 완성해 주세요.

단, 완성될 배열의 길이가 k보다 작으면 나머지 값을 전부 -1로 채워서 return 합니다.

[제한]
- 1 ≤ arr의 길이 ≤ 100,000
  - 0 ≤ arr의 원소 ≤ 100,000
- 1 ≤ k ≤ 1,000
"""


def solution_v1(arr: list[int], k: int) -> list[int]:
    """
    [Approach] dict.fromkeys()로 순서 유지 중복 제거 후 k개 슬라이싱
    [Time] O(n) - 딕셔너리 생성
    [Space] O(n) - 중복 제거된 리스트
    """
    answer = list(dict.fromkeys(arr))
    if len(answer) < k:
        answer += [-1] * (k - len(answer))

    return answer[:k]


solution = solution_v1
