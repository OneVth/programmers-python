"""
프로그래머스 Lv0 #181878 - 원하는 문자열 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/181878

[문제]
알파벳으로 이루어진 문자열 myString과 pat이 주어집니다.
myString의 연속된 부분 문자열 중 pat이 존재하면 1을
그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.
단, 알파벳 대문자와 소문자는 구분하지 않습니다.

[제한]
- 1 <= myString의 길이 <= 100,000
- 1 <= pat의 길이 <= 300
- myString과 pat은 모두 알파벳으로 이루어진 문자열입니다.
"""


def solution_v1(myString: str, pat: str) -> int:
    """
    [Approach] 양쪽 lower() 변환 후 find()로 부분 문자열 탐색
    [Time] O(n * m)  [Space] O(n)  (n: myString 길이, m: pat 길이)
    """
    return 1 if myString.lower().find(pat.lower()) != -1 else 0

def solution_v2(myString: str, pat: str) -> int:
    """
    [Approach] in 연산자로 포함 여부 확인 후 int() 변환
    [Time] O(n * m)  [Space] O(n)  (n: myString 길이, m: pat 길이)
    """
    return int(pat.lower() in myString.lower())

solution = solution_v2
