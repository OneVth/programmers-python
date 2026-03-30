"""
프로그래머스 Lv0 #181943 - 문자열 겹쳐쓰기
https://school.programmers.co.kr/learn/courses/30/lessons/181943

[문제]
문자열 my_string, overwrite_string 과 정수 s 가 주어집니다.
문자열 my_string 의 인덱스 s 부터 overwrite_string 의 길이만큼을
문자열 overwrite_string 으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- my_string 와 overwrite_string 은 숫자와 알파벳으로 이루어져 있습니다.
- 1 ≤ overwrite_string 의 길이 ≤ my_string 의 길이 ≤ 1,000
- 0 ≤ s ≤ my_string 의 길이 - overwrite_string 의 길이
"""


def solution_v1(my_string: str, overwrite_string: str, s: int) -> str:
    """
    [Approach] 문자열 슬라이싱으로 앞/뒤를 분리해 overwrite_string 삽입
    [Time] O(n)  [Space] O(n)
    """
    return (
        my_string[:s] + overwrite_string + my_string[s + len(overwrite_string) :]
    )


solution = solution_v1
