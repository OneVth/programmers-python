"""
프로그래머스 Lv0 #120825 - 문자 반복 출력하기
https://school.programmers.co.kr/learn/courses/30/lessons/120825

[문제]
문자열 my_string과 정수 n이 매개변수로 주어질 때,
my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록
solution 함수를 완성해보세요.

[제한]
- 2 ≤ my_string 길이 ≤ 5
- 2 ≤ n ≤ 10
- my_string은 영어 대소문자로 이루어져 있습니다.
"""


def solution_v1(my_string: str, n: int) -> str:
    """
    [Approach] join + generator expression
    [Time] O(m*n)  [Space] O(m*n)
    ✅ Pythonic, 효율적
    """
    return "".join(x * n for x in my_string)


def solution_v2(my_string: str, n: int) -> str:
    """
    [Approach] 문자열 누적 연결
    [Time] O(m*n)  [Space] O(m*n)
    ⚠️ 문자열 immutable → 매번 새 객체 생성
    """
    answer = ""
    for c in my_string:
        answer += c * n

    return answer


solution = solution_v1
