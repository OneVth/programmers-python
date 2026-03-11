"""
프로그래머스 Lv0 #181894 - 2의 영역
https://school.programmers.co.kr/learn/courses/30/lessons/181894

[문제]
정수 배열 arr가 주어집니다.
배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return합니다.
단, arr에 2가 없는 경우 [-1]을 return 합니다.

[제한]
- 1 ≤ arr의 길이 ≤ 100,000
  - 1 ≤ arr의 원소 ≤ 10
"""


def solution_v1(arr: list[int]) -> list[int]:
    """
    [Approach] 첫 번째 2부터 끝까지 복사 후, 뒤에서 2가 아닌 원소를 pop으로 제거
    [Time] O(N)  [Space] O(N)
    """
    if 2 not in arr:
        return [-1]

    answer = []
    for i in range(arr.index(2), len(arr)):
        answer.append(arr[i])

    while answer[-1] != 2:
        answer.pop()

    return answer


solution = solution_v1
