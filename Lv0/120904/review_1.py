"""
프로그래머스 Lv0 #120904 - 숫자 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/120904

[복습] 1차 - 2025-12-17

[문제]
정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면
num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록
solution 함수를 완성해보세요.

[제한]
- 0 < num < 1,000,000
- 0 ≤ k < 10
- num에 k가 여러 개 있으면 가장 처음 나타나는 자리를 return 합니다.
"""


def solution_v1(num: int, k: int) -> int:
    """
    [Approach] 문자열 변환 후 find()로 인덱스 탐색, 1-based 보정
    [Time] O(n) - n은 자릿수  [Space] O(n) - 문자열 변환
    """
    answer = str(num).find(str(k))
    return answer + 1 if answer != -1 else -1


def solution_v2(num: int, k: int) -> int:
    """
    [Approach] enumerate로 순회하며 첫 일치 위치 반환 (early return)
    [Time] O(n) - n은 자릿수  [Space] O(n) - 문자열 변환
    """
    for i, c in enumerate(str(num)):
        if c == str(k):
            return i + 1

    return -1


# ✅ 기본 솔루션 지정
solution = solution_v2
