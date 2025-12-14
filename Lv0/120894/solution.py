"""
프로그래머스 Lv0 #120894 - 영어가 싫어요
https://school.programmers.co.kr/learn/courses/30/lessons/120894

[문제]
영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다.
문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록
solution 함수를 완성해 주세요.

[제한]
- numbers는 소문자로만 구성되어 있습니다.
- numbers는 "zero", "one", "two", "three", "four", "five", "six", "seven",
  "eight", "nine" 들이 공백 없이 조합되어 있습니다.
- 1 ≤ numbers의 길이 ≤ 50
- "zero"는 numbers의 맨 앞에 올 수 없습니다.
"""


def solution_v1(numbers: str) -> int:
    """
    [Approach] dict 매핑 - 영어 단어를 숫자 문자로 치환
    [Time] O(10 * n) = O(n) - 10개 단어에 대해 replace
    [Space] O(n) - 결과 문자열
    """
    table = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    answer = numbers
    for num in table.keys():
        answer = answer.replace(num, table[num])
    return int(answer)


def solution_v2(numbers: str) -> int:
    """
    [Approach] 리스트 인덱스 활용 - enumerate로 인덱스가 곧 숫자
    [Time] O(n)  [Space] O(n)
    """
    words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    answer = numbers
    for i, num in enumerate(words):
        answer = answer.replace(num, str(i))

    return int(answer)


solution = solution_v2
