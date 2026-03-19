"""
프로그래머스 Lv0 #181905 - 문자열 뒤집기
https://school.programmers.co.kr/learn/courses/30/lessons/181905

[문제]
문자열 my_string 과 정수 s, e 가 매개변수로 주어질 때,
my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는
solution 함수를 작성해 주세요.

[제한]
- my_string은 숫자와 알파벳으로만 이루어져 있습니다.
- 1 ≤ my_string의 길이 ≤ 1,000
- 0 ≤ s ≤ e < my_string의 길이
"""


def solution(my_string: str, s: int, e: int) -> str:
    """
    [Approach] 앞부분 + 구간 역슬라이스 + 뒷부분 조합: [:s] + [s:e+1][::-1] + [e+1:]
    [Time] O(n)  [Space] O(n)
    """
    return my_string[:s] + my_string[s:e + 1][::-1] + my_string[e + 1:]
