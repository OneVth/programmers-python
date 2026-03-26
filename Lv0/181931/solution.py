"""
프로그래머스 Lv0 #181931 - 등차수열의 특정한 항만 더하기
https://school.programmers.co.kr/learn/courses/30/lessons/181931

[문제]
두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다.
첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때,
이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는
solution 함수를 작성해 주세요.

[제한]
- 1 ≤ a ≤ 100
- 1 ≤ d ≤ 100
- 1 ≤ included의 길이 ≤ 100
- included에는 true가 적어도 하나 존재합니다.
"""


def solution_v1(a: int, d: int, included: list[bool]) -> int:
    """
    [Approach] enumerate로 인덱스와 bool 동시 순회, generator expression으로 조건부 합산
    [Time] O(n)  [Space] O(1)
    """
    return sum(a + d * i for i, b in enumerate(included) if b)


solution = solution_v1
