"""
프로그래머스 Lv0 #120823 - 직각삼각형 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/120823

[문제]
"*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 삼각형을 그리려고합니다.
정수 n이 주어지면 높이와 너비가 n인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.

[제한]
- 1 ≤ n ≤ 10

[입출력 예]
입력: 3
출력:
*
**
***
"""


def solution_v1(n: int) -> None:
    """
    [Approach] for문으로 각 줄 직접 print
    [Time] O(n²)  [Space] O(1)
    ⚠️ 프로그래머스 출력 문제용 (return 없음)
    """
    for i in range(1, n + 1):
        print("*" * i)


def solution_v2(n: int) -> str:
    """
    [Approach] join + 제너레이터 표현식
    [Time] O(n²)  [Space] O(n²)
    ✅ 문자열 반환 방식 (runner.py 테스트용)
    """
    return "\n".join("*" * i for i in range(1, n + 1))


solution = solution_v2
