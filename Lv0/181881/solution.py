"""
프로그래머스 Lv0 #181881 - 조건에 맞게 수열 변환하기 2
https://school.programmers.co.kr/learn/courses/30/lessons/181881

[문제]
정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은
짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.

이러한 작업을 x번 반복한 결과인 배열을 arr(x)라고 표현했을 때,
arr(x) = arr(x + 1)인 x가 항상 존재합니다. 이러한 x 중 가장 작은 값을
return 하는 solution 함수를 완성해 주세요.

단, 두 배열에 대한 "="는 두 배열의 크기가 서로 같으며, 같은 인덱스의
원소가 각각 서로 같음을 의미합니다.

[제한]
- 1 <= arr의 길이 <= 1,000,000
  - 1 <= arr의 원소의 값 <= 100
"""


def solution_v1(arr: list[int]) -> int:
    """
    [Approach] 매 반복마다 변환된 새 배열을 생성하고, 이전 배열과 비교하여 동일하면 반복 횟수 반환
    [Time] O(n * k) (k: 수렴까지 반복 횟수)  [Space] O(n)
    """
    prev = arr
    x = 0

    while True:
        curr = []
        for i in prev:
            if i >= 50 and i % 2 == 0:
                curr.append(i // 2)
            elif i < 50 and i % 2 == 1:
                curr.append(i * 2 + 1)
            else:
                curr.append(i)

        if prev == curr:
            return x

        prev = curr
        x += 1


def solution_v2(arr: list[int]) -> int:
    """
    [Approach] in-place 변환 + changed 플래그로 새 배열 생성/비교 없이 수렴 감지
    [Time] O(n * k)  [Space] O(1)
    """
    x = 0

    while True:
        changed = False
        for idx in range(len(arr)):
            val = arr[idx]
            if val >= 50 and val % 2 == 0:
                arr[idx] = val // 2
                changed = True
            elif val < 50 and val % 2 == 1:
                arr[idx] = val * 2 + 1
                changed = True

        if not changed:
            return x

        x += 1


solution = solution_v2
