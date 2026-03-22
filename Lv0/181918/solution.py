"""
프로그래머스 Lv0 #181918 - 배열 만들기 4
https://school.programmers.co.kr/learn/courses/30/lessons/181918

[문제]
정수 배열 arr 가 주어집니다. arr 를 이용해 새로운 배열 stk 를 만드려고 합니다.

변수 i 를 만들어 초기값을 0으로 설정한 후 i 가 arr 의 길이보다 작으면 다음 작업을 반복합니다.

- 만약 stk 가 빈 배열이라면 arr[i] 를 stk 에 추가하고 i 에 1을 더합니다.
- stk 에 원소가 있고, stk 의 마지막 원소가 arr[i] 보다 작으면 arr[i] 를 stk 의 뒤에 추가하고 i 에 1을 더합니다.
- stk 에 원소가 있는데 stk 의 마지막 원소가 arr[i] 보다 크거나 같으면 stk 의 마지막 원소를 stk 에서 제거합니다.

위 작업을 마친 후 만들어진 stk 를 return 하는 solution 함수를 완성해 주세요.

[제한]
- 1 ≤ arr 의 길이 ≤ 100,000
- 1 ≤ arr 의 원소 ≤ 100,000
"""


def solution_v1(arr: list[int]) -> list[int]:
    """
    [Approach] while 루프로 문제 조건을 직접 시뮬레이션하는 단조 스택
    [Time] O(n)  [Space] O(n)
    """
    i = 0
    stk = []
    l = len(arr)

    while i < l:
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()

    return stk

def solution_v2(arr: list[int]) -> list[int]:
    """
    [Approach] for 루프 + 내부 while로 단조 증가 스택을 유지하는 표준 패턴
    [Time] O(n)  [Space] O(n)
    """
    stk = []
    i = 0

    for i in range(len(arr)):
        while stk and stk[-1] >= arr[i]:
            stk.pop()
        stk.append(arr[i])
    return stk

# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v2
