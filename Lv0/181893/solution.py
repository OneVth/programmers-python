"""
프로그래머스 Lv0 #181893 - 배열 조각하기
https://school.programmers.co.kr/learn/courses/30/lessons/181893

[문제]
정수 배열 arr와 query가 주어집니다.
query를 순회하면서 다음 작업을 반복합니다.
- 짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고
  배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
- 홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고
  배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.

위 작업을 마친 후 남은 arr의 부분 배열을 return합니다.

[제한]
- 5 ≤ arr의 길이 ≤ 100,000
  - 0 ≤ arr의 원소 ≤ 100
- 1 ≤ query의 길이 < min(50, arr의 길이 / 2)
  - query의 각 원소는 0보다 크거나 같고 남아있는 arr의 길이보다 작습니다.
"""


def solution_v1(arr: list[int], query: list[int]) -> list[int]:
    """
    [Approach] query 순회하며 짝수면 뒷부분, 홀수면 앞부분을 슬라이싱으로 잘라냄
    [Time] O(Q * N), Q = len(query), N = 슬라이스 평균 길이  [Space] O(N)
    """
    answer = list(arr)
    for i, x in enumerate(query):
        if i % 2 == 0:
            answer = answer[: x + 1]
        else:
            answer = answer[x:]

    return answer


def solution_v2(arr: list[int], query: list[int]) -> list[int]:
    """
    [Approach] start/end 인덱스만 추적하여 마지막에 한 번만 슬라이싱
    [Time] O(Q + K), Q = len(query), K = 결과 길이  [Space] O(K)
    """
    start = 0
    end = len(arr)
    for i, x in enumerate(query):
        if i % 2 == 0:
            end = start + x + 1
        else:
            start += x
    return arr[start:end]


solution = solution_v2
