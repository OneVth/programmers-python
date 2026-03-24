"""
프로그래머스 Lv0 #181928 - 이어 붙인 수
https://school.programmers.co.kr/learn/courses/30/lessons/181928

[문제]
정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와
짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

[제한]
- 2 ≤ num_list의 길이 ≤ 10
- 1 ≤ num_list의 원소 ≤ 9
- num_list에는 적어도 한 개씩의 짝수와 홀수가 있습니다.
"""


def solution_v1(num_list: list[int]) -> int:
    """
    [Approach] 홀짝 분리 후 각각 문자열로 이어붙여 정수 변환 후 합산
    [Time] O(n)  [Space] O(n)
    """
    odd = []
    even = []
    for i in num_list:
        if i % 2 == 0:
            even.append(str(i))
        else:
            odd.append(str(i))
    return int("".join(odd)) + int("".join(even))


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
