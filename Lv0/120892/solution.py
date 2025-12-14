"""
프로그래머스 Lv0 #120892 - 암호 해독
https://school.programmers.co.kr/learn/courses/30/lessons/120892

[문제]
군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.
- 암호화된 문자열 cipher를 주고받습니다.
- 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.

문자열 cipher와 정수 code가 매개변수로 주어질 때
해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ cipher의 길이 ≤ 1,000
- 1 ≤ code ≤ cipher의 길이
- cipher는 소문자와 공백으로만 구성되어 있습니다.
- 공백도 하나의 문자로 취급합니다.
"""


def solution_v1(cipher: str, code: int) -> str:
    """
    [Approach] enumerate + 조건 필터링 - 1-indexed 배수 위치만 추출
    [Time] O(n)  [Space] O(n/code) - 결과 문자열
    """
    return "".join(c for i, c in enumerate(cipher) if (i + 1) % code == 0)


def solution_v2(cipher: str, code: int) -> str:
    """
    [Approach] 슬라이싱 - [start:stop:step]으로 간격 추출
    [Time] O(n/code)  [Space] O(n/code)
    """
    return cipher[code - 1 :: code]


solution = solution_v2
