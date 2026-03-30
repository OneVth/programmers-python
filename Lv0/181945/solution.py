"""
프로그래머스 Lv0 #181945 - 문자열 돌리기
https://school.programmers.co.kr/learn/courses/30/lessons/181945

[문제]
문자열 str 이 주어집니다.
문자열을 시계방향으로 90도 돌려서 출력하는 코드를 작성해 보세요.
(각 문자를 한 줄씩 출력)

[제한]
- 1 ≤ str 의 길이 ≤ 10
"""


def solution_v1(str: str) -> str:
    """
    [Approach] "\n".join()으로 각 문자 사이에 줄바꿈 삽입
    [Time] O(n)  [Space] O(n)
    """
    return "\n".join(str)


solution = solution_v1
