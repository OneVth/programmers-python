"""
프로그래머스 Lv0 #181857 - 배열의 길이를 2의 거듭제곱으로 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/181857

[문제]
정수 배열 arr이 매개변수로 주어집니다.
arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다.
arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ arr의 길이 ≤ 1,000
- 1 ≤ arr의 원소 ≤ 1,000
"""


def solution_v1(arr: list[int]) -> list[int]:
    """
    [Approach] 비트 시프트로 2의 거듭제곱 찾기 + 리스트 컴프리헨션으로 패딩
    [Time] O(n)  [Space] O(n) - 결과 배열
    """
    length = len(arr)

    ex = 1
    while ex < length:
        ex <<= 1

    answer = [arr[i] if i < length else 0 for i in range(ex)]
    return answer


def solution_v2(arr: list[int]) -> list[int]:
    """
    [Approach] bit_length()로 필요한 2의 거듭제곱 계산 + 리스트 연결로 패딩
    [Time] O(n)  [Space] O(n) - 결과 배열
    """
    target = 1 << (len(arr) - 1).bit_length()
    return arr + [0] * (target - len(arr))


solution = solution_v2
