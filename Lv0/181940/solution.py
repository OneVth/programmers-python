"""
프로그래머스 Lv0 #181940 - 문자열 곱하기
https://school.programmers.co.kr/learn/courses/30/lessons/181940

[문제]
문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을
return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ my_string의 길이 ≤ 100
- my_string은 영소문자로만 이루어져 있습니다.
- 1 ≤ k ≤ 100
"""


def solution_v1(my_string: str, k: int) -> str:
    """
    [Approach] Python 문자열 * 연산자로 k번 반복
    [Time] O(n * k)  [Space] O(n * k)  ← 새 문자열 객체 생성
    """
    return my_string * k


solution = solution_v1
