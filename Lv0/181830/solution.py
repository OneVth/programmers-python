"""
프로그래머스 Lv0 #181830 - 정사각형으로 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/181830

[문제]
이차원 정수 배열 arr이 매개변수로 주어집니다.
arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고,
열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한
이차원 배열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ arr의 길이 ≤ 100
- 1 ≤ arr의 원소의 길이 ≤ 100
  - arr의 모든 원소의 길이는 같습니다.
- 1 ≤ arr의 원소의 원소 ≤ 1,000
"""


def solution_v1(arr: list[list[int]]) -> list[list[int]]:
    """
    [Approach] In-place 수정: 행/열 부족 시 직접 0 추가
    [Time] O(m²) where m = max(rows, cols)
    [Space] O(1) - 원본 배열 직접 수정 (추가 행/열 제외)
    """
    rows = len(arr)
    cols = len(arr[0])

    if rows > cols:
        for row in arr:
            for _ in range(rows - cols):
                row.append(0)
    elif cols > rows:
        for _ in range(cols - rows):
            arr.append([0] * cols)

    return arr


def solution_v2(arr: list[list[int]]) -> list[list[int]]:
    """
    [Approach] 새 정사각형 배열 생성 후 원본 값 복사
    [Time] O(m²) where m = max(rows, cols)
    [Space] O(m²) - 새 배열 생성
    """
    rows = len(arr)
    cols = len(arr[0])
    m = max(rows, cols)

    answer = [[0] * m for _ in range(m)]

    for i in range(rows):
        for j in range(cols):
            answer[i][j] = arr[i][j]

    return answer


solution = solution_v2
