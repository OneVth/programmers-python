"""
프로그래머스 Lv0 #120833 - 배열 자르기
https://school.programmers.co.kr/learn/courses/30/lessons/120833

[문제]
정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때,
numbers의 num1번째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을
return 하도록 solution 함수를 완성해보세요.

[제한]
- 2 ≤ numbers의 길이 ≤ 30
- 0 ≤ numbers의 원소 ≤ 1,000
- 0 ≤ num1 < num2 < numbers의 길이
"""


def solution_v1(numbers: list[int], num1: int, num2: int) -> list[int]:
    """
    [Approach] 슬라이싱
    [Time] O(num2-num1)  [Space] O(num2-num1)
    ✅ num2 포함이므로 +1 필요
    """
    return numbers[num1 : num2 + 1]


solution = solution_v1
