"""
프로그래머스 Lv0 #120909 - 제곱수 판별하기
https://school.programmers.co.kr/learn/courses/30/lessons/120909

[문제]
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이
매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 1,000,000
"""


def solution_v1(n: int) -> int:
    """
    [Approach] 제곱근 역검증 - int 변환 후 다시 제곱하여 비교
    [Time] O(1)  [Space] O(1)
    """
    return 1 if int(n**0.5) ** 2 == n else 2


def solution_v2(n: int) -> int:
    """
    [Approach] is_integer() - float의 정수 여부 확인 메서드
    [Time] O(1)  [Space] O(1)
    """
    return 1 if (n**0.5).is_integer() else 2


solution = solution_v1
