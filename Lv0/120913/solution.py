"""
프로그래머스 Lv0 #120913 - 잘라서 배열로 저장하기
https://school.programmers.co.kr/learn/courses/30/lessons/120913

[문제]
문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서
저장한 배열을 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ my_str의 길이 ≤ 100
- 1 ≤ n ≤ my_str의 길이
- my_str은 알파벳 소문자, 대문자, 숫자로 이루어져 있습니다.

[유의사항]
- 마지막에 남은 문자열이 n보다 짧으면 그대로 배열에 저장합니다.
"""


def solution_v1(my_str: str, n: int) -> list[str]:
    """
    [Approach] 청크 인덱스 계산 - i번째 청크의 시작/끝 위치 계산
    [Time] O(m)  [Space] O(m) - m: 문자열 길이
    """
    return [my_str[i * n : (i + 1) * n] for i in range(((len(my_str) - 1) // n + 1))]


def solution_v2(my_str: str, n: int) -> list[str]:
    """
    [Approach] range step 활용 - n씩 건너뛰며 슬라이싱
    [Time] O(m)  [Space] O(m)
    """
    return [my_str[i : i + n] for i in range(0, len(my_str), n)]


solution = solution_v2
