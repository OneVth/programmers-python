"""
프로그래머스 Lv0 #120895 - 인덱스 바꾸기
https://school.programmers.co.kr/learn/courses/30/lessons/120895

[문제]
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼
문자열을 return 하도록 solution 함수를 완성해보세요.

[제한]
- 1 < my_string의 길이 < 100
- 0 ≤ num1, num2 < my_string의 길이
- my_string은 소문자로 이루어져 있습니다.
- num1 ≠ num2
"""


def solution_v1(my_string: str, num1: int, num2: int) -> str:
    """
    [Approach] 리스트 변환 후 스왑 - 문자열을 리스트로 변환, 인덱스 교환 후 join
    [Time] O(n)  [Space] O(n) - 리스트 변환 비용
    """
    list_str = list(my_string)
    list_str[num1], list_str[num2] = list_str[num2], list_str[num1]
    return "".join(list_str)


def solution_v2(my_string: str, num1: int, num2: int) -> str:
    """
    [Approach] 슬라이싱 조합 - 문자열을 부분으로 나눠 재구성
    [Time] O(n)  [Space] O(n)
    """
    if num1 > num2:
        num1, num2 = num2, num1

    return (
        my_string[:num1]
        + my_string[num2]
        + my_string[num1 + 1 : num2]
        + my_string[num1]
        + my_string[num2 + 1 :]
    )


solution = solution_v1
