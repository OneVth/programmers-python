"""
프로그래머스 Lv0 #181912 - 배열 만들기 5
https://school.programmers.co.kr/learn/courses/30/lessons/181912

[문제]
문자열 배열 intStrs와 정수 k, s, l이 주어집니다. intStrs의 원소는 숫자로 이루어져 있습니다.
배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로
변환합니다. 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수를
완성해 주세요.

[제한]
- 0 ≤ s < 100
- 1 ≤ l ≤ 8
- 10^(l-1) ≤ k < 10^l
- 1 ≤ intStrs의 길이 ≤ 10,000
  - s + l ≤ intStrs의 원소의 길이 ≤ 120
"""


def solution_v1(intStrs: list[str], k: int, s: int, l: int) -> list[int]:
    """
    [Approach] 순회하며 부분 문자열을 정수 변환 후 k 초과값만 수집
    [Time] O(n)  [Space] O(n)
    """
    answer = []
    for e in intStrs:
        token = int(e[s : s + l])
        if token > k:
            answer.append(token)

    return answer


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
