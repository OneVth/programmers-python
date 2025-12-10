"""
프로그래머스 Lv0 #120864 - 숨어있는 숫자의 덧셈 (2)
https://school.programmers.co.kr/learn/courses/30/lessons/120864

[문제]
문자열 my_string이 매개변수로 주어집니다.
my_string은 소문자, 대문자, 자연수로만 구성되어있습니다.
my_string 안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ my_string의 길이 ≤ 1,000
- 1 ≤ my_string 안의 자연수 ≤ 1000
- 연속된 수는 하나의 숫자로 간주합니다.
- 000123과 같이 0이 선행하는 경우는 없습니다.
- 문자열에 자연수가 없는 경우 0을 return 해주세요.
"""


def solution_v1(my_string: str) -> int:
    """
    [Approach] 정규표현식으로 연속 숫자 추출
    [Time] O(n)  [Space] O(k) - k는 추출된 숫자 개수
    """
    import re

    nums = re.findall(r"\d+", my_string)
    return sum(int(i) for i in nums)


def solution_v2(my_string: str) -> int:
    """
    [Approach] 알파벳을 공백으로 치환 후 split
    [Time] O(n)  [Space] O(n) - 새 문자열 생성
    """
    s = "".join(i if i.isdigit() else " " for i in my_string)
    return sum(int(i) for i in s.split())


def solution_v3(my_string: str) -> int:
    """
    [Approach] 순회하며 숫자 누적, 문자 만나면 더하고 초기화
    [Time] O(n)  [Space] O(1) - 상수 공간
    [Note] 문자열 끝 숫자 처리를 위해 마지막에 temp 확인 필요
    """
    answer = 0

    temp = ""
    for c in my_string:
        if c.isdigit():
            temp += c
        else:
            if temp:
                answer += int(temp)
            temp = ""

    # 문자열이 숫자로 끝나는 경우 처리
    if temp:
        answer += int(temp)

    return answer


# 기본 솔루션 지정
solution = solution_v1
