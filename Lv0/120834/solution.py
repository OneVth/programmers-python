"""
프로그래머스 Lv0 #120834 - 외계행성의 나이
https://school.programmers.co.kr/learn/courses/30/lessons/120834

[문제]
우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다.
입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다.
a는 0, b는 1, c는 2, ..., j는 9입니다.
예를 들어 23살은 cd, 51살은 fb로 표현합니다.
나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록
solution 함수를 완성해주세요.

[제한]
- age는 자연수입니다.
- age ≤ 1,000
- PROGRAMMERS-962 행성은 알파벳 소문자만 사용합니다.
"""


def solution_v1(age: int) -> str:
    """
    [Approach] dict 매핑 테이블
    [Time] O(d)  [Space] O(1)
    ✅ 명시적 매핑, 가독성 좋음 (d = 자릿수)
    """
    s_age = str(age)
    mapping = {
        "0": "a",
        "1": "b",
        "2": "c",
        "3": "d",
        "4": "e",
        "5": "f",
        "6": "g",
        "7": "h",
        "8": "i",
        "9": "j",
    }

    return "".join(mapping[x] for x in s_age)


def solution_v2(age: int) -> str:
    """
    [Approach] chr() + int 연산
    [Time] O(d)  [Space] O(1)
    ✅ 간결함, ASCII 코드 활용 (97 = ord('a'))
    """
    return "".join(chr(int(i) + 97) for i in str(age))


def solution_v3(age: int) -> str:
    """
    [Approach] str.translate() + maketrans()
    [Time] O(d)  [Space] O(1)
    ✅ 내장 메서드 활용, 가장 Pythonic
    """
    return str(age).translate(str.maketrans("0123456789", "abcdefghij"))


solution = solution_v2
