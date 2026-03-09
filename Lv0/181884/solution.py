"""
프로그래머스 Lv0 #181884 - n보다 커질 때까지 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/181884

[문제]
정수 배열 numbers와 정수 n이 매개변수로 주어집니다.
numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간
이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 <= numbers의 길이 <= 100
- 1 <= numbers의 원소 <= 100
- 0 <= n < numbers의 모든 원소의 합
"""


def solution_v1(numbers: list[int], n: int) -> int:
    """
    [Approach] 누적합 - 앞에서부터 순회하며 합이 n을 초과하면 중단
    [Time] O(n)  [Space] O(1)
    """
    answer = 0

    for i in numbers:
        if answer > n:
            break

        answer += i

    return answer


solution = solution_v1

