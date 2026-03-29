"""
프로그래머스 Lv0 #181939 - 더 크게 합치기
https://school.programmers.co.kr/learn/courses/30/lessons/181939

[문제]
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다.
예를 들면 다음과 같습니다.
- 12 ⊕ 3 = 123
- 3 ⊕ 12 = 312

양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는
solution 함수를 완성해 주세요.
단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

[제한]
- 1 ≤ a, b < 10,000
"""


def solution_v1(a: int, b: int) -> int:
    """
    [Approach] str() 명시적 변환으로 두 정수를 이어 붙여 max() 비교
    [Time] O(log a + log b)  [Space] O(log a + log b)  ← 문자열 자릿수에 비례
    """
    return max(int(str(a) + str(b)), int(str(b) + str(a)))


def solution_v2(a: int, b: int) -> int:
    """
    [Approach] f-string으로 문자열 이어 붙이기를 더 간결하게 표현
    [Time] O(log a + log b)  [Space] O(log a + log b)
    """
    return max(int(f"{a}{b}"), int(f"{b}{a}"))


solution = solution_v2
