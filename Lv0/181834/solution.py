"""
프로그래머스 Lv0 #181834 - l로 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/181834

[문제]
알파벳 소문자로 이루어진 문자열 myString이 주어집니다.
알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는
solution 함수를 완성해 주세요.

[제한]
- 1 ≤ myString ≤ 100,000
- myString은 알파벳 소문자로 이루어진 문자열입니다.
"""


def solution_v1(myString: str) -> str:
    """
    [Approach] 조건부 표현식 - 'l'보다 작으면 'l'로 치환
    [Time] O(n)  [Space] O(n)
    """
    return "".join(c if c >= "l" else "l" for c in myString)


def solution_v2(myString: str) -> str:
    """
    [Approach] max() 활용 - 문자의 ASCII 비교로 더 큰 값 선택
    [Time] O(n)  [Space] O(n)
    """
    return "".join(max(c, "l") for c in myString)


solution = solution_v2
