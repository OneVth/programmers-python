"""
프로그래머스 Lv0 #181854 - 배열의 길이에 따라 다른 연산하기
https://school.programmers.co.kr/learn/courses/30/lessons/181854

[문제]
정수 배열 arr과 정수 n이 매개변수로 주어집니다.
arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을,
arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을
return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ arr의 길이 ≤ 1,000
- 1 ≤ arr의 원소 ≤ 1,000
- 1 ≤ n ≤ 1,000
"""


def solution_v1(arr: list[int], n: int) -> list[int]:
    """
    [Approach] 원본 배열 직접 수정 (in-place)
    [Time] O(n) - 배열 순회
    [Space] O(1) - 추가 공간 없음 (원본 수정)
    [Note] 원본 arr이 변경됨 - 부작용 주의
    """
    l = len(arr)
    if l % 2 == 1:
        for i in range(l):
            if i % 2 == 0:
                arr[i] += n
    else:
        for i in range(l):
            if i % 2 == 1:
                arr[i] += n

    return arr


def solution_v2(arr: list[int], n: int) -> list[int]:
    """
    [Approach] 새 리스트 생성하여 결과 저장
    [Time] O(n) - 배열 순회
    [Space] O(n) - 새 리스트 생성
    """
    answer = []
    l = len(arr)

    if l % 2 == 1:
        for i in range(l):
            if i % 2 == 0:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    else:
        for i in range(l):
            if i % 2 == 1:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])

    return answer


solution = solution_v2
