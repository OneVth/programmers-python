"""
프로그래머스 Lv0 #181944 - 홀짝 구분하기
https://school.programmers.co.kr/learn/courses/30/lessons/181944

[문제]
자연수 n 이 입력으로 주어졌을 때 만약 n 이 짝수이면 "n is even"을,
홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

[제한]
- 1 ≤ n ≤ 1,000
"""


def solution_v1(n: int) -> str:
    """
    [Approach] n % 2로 홀짝 판별 후 포맷 문자열 반환
    [Time] O(1)  [Space] O(1)
    """
    if n % 2 == 0:
        return f"{n} is even"
    else:
        return f"{n} is odd"


solution = solution_v1
