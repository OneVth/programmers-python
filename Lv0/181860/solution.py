"""
프로그래머스 Lv0 #181860 - 빈 배열에 추가, 삭제하기
https://school.programmers.co.kr/learn/courses/30/lessons/181860

[문제]
아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 길이가 같은 정수 배열 arr과 boolean 배열 flag가
매개변수로 주어질 때, flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] × 2 번
추가하고, flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는
solution 함수를 작성해 주세요.

[제한]
- 1 ≤ arr의 길이 = flag의 길이 ≤ 100
- arr의 모든 원소는 1 이상 9 이하의 정수입니다.
- 현재 X의 길이보다 더 많은 원소를 빼는 입력은 주어지지 않습니다.
"""


def solution_v1(arr: list[int], flag: list[bool]) -> list[int]:
    """
    [Approach] enumerate로 인덱스 접근 + extend로 배열 확장
    [Time] O(n * m) - n: 배열 길이, m: 추가되는 원소 수  [Space] O(n * m)
    """
    stk = []
    for i, b in enumerate(flag):
        if b:
            stk.extend([arr[i]] * (arr[i] * 2))
        else:
            stk = stk[:-arr[i]]

    return stk


def solution_v2(arr: list[int], flag: list[bool]) -> list[int]:
    """
    [Approach] zip으로 병렬 순회 + += 연산자로 확장
    [Time] O(n * m)  [Space] O(n * m)
    """
    stk = []
    for i, j in zip(arr, flag):
        if j:
            stk += [i] * i * 2
        else:
            stk = stk[:-i]
    return stk


solution = solution_v2
