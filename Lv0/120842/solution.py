"""
프로그래머스 Lv0 #120842 - 2차원으로 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/120842

[문제]
정수 배열 num_list와 정수 n이 매개변수로 주어집니다.
num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.

num_list가 [1, 2, 3, 4, 5, 6, 7, 8]로 길이가 8이고 n이 2이므로
num_list를 2 * 4 배열로 다음과 같이 변경합니다.
2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.

[제한]
- num_list의 길이는 n의 배수개입니다.
- 0 ≤ num_list의 길이 ≤ 150
- 2 ≤ n < num_list의 길이
"""


def solution_v1(num_list: list[int], n: int) -> list[list[int]]:
    """
    [Approach] 2중 for문 + 인덱스 계산
    [Time] O(len)  [Space] O(len)
    ⚠️ 명시적이지만 장황함
    """
    rows = len(num_list) // n
    answer = [[0] * n for _ in range(rows)]

    for i in range(rows):
        for j in range(n):
            answer[i][j] = num_list[i * n + j]

    return answer


def solution_v2(num_list: list[int], n: int) -> list[list[int]]:
    """
    [Approach] 중첩 list comprehension
    [Time] O(len)  [Space] O(len)
    ⚠️ 한 줄이지만 가독성 낮음
    """
    return [[num_list[i * n + j] for j in range(n)] for i in range(len(num_list) // n)]


def solution_v3(num_list: list[int], n: int) -> list[list[int]]:
    """
    [Approach] 슬라이싱 + range step
    [Time] O(len)  [Space] O(len)
    ✅ Pythonic하고 가독성 좋음
    """
    answer = []

    for i in range(0, len(num_list), n):
        answer.append(num_list[i : i + n])

    return answer


def solution_v4(num_list: list[int], n: int) -> list[list[int]]:
    """
    [Approach] NumPy reshape 활용
    [Time] O(len)  [Space] O(len)
    ✅ NumPy 사용 시 가장 간결, -1은 자동 계산
    """
    import numpy as np

    return np.array(num_list).reshape(-1, n).tolist()


solution = solution_v4
