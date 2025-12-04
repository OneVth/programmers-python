"""
프로그래머스 Lv0 #120807 - 숫자 비교하기
https://school.programmers.co.kr/learn/courses/30/lessons/120807

[문제]
정수 num1과 num2가 매개변수로 주어질 때,
두 수가 같으면 1, 다르면 -1을 반환

[제한]
- 0 ≤ num1 ≤ 10,000
- 0 ≤ num2 ≤ 10,000
"""


def solution_v1(num1: int, num2: int) -> int:
    """
    [Approach] 삼항 연산자 (조건부 표현식)
    [Time] O(1)  [Space] O(1)
    """
    return 1 if num1 == num2 else -1

def solution_v2(num1: int, num2: int) -> int:
    """
    [Approach] 명시적 if문 + 변수 초기화
    [Time] O(1)  [Space] O(1)
    """
    answer = -1
    if num1 == num2:
        answer = 1
    return answer

# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
