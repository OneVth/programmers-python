"""
프로그래머스 Lv0 #181902 - 문자 개수 세기
https://school.programmers.co.kr/learn/courses/30/lessons/181902

[문제]
알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때,
my_string에서 'A'의 개수, 'B'의 개수, ..., 'Z'의 개수,
'a'의 개수, 'b'의 개수, ..., 'z'의 개수를
순서대로 담은 길이 52의 정수 배열을 return 하는
solution 함수를 작성해 주세요.

[제한]
- 1 <= my_string의 길이 <= 1,000
"""


def solution_v1(my_string: str) -> list[int]:
    """
    [Approach] ord()와 isupper()로 문자를 52칸 배열 인덱스에 매핑
    [Time] O(n)  [Space] O(1)  (고정 52칸)
    """
    answer = [0] * 52
    for c in my_string:
        if c.isupper():
            answer[ord(c) - 65] += 1
        else:
            answer[ord(c) - 97 + 26] += 1

    return answer


def solution_v2(my_string: str) -> list[int]:
    """
    [Approach] dict.fromkeys()로 A-Z, a-z 순서 딕셔너리를 만들어 카운팅
    [Time] O(n)  [Space] O(1)  (고정 52키)
    """
    answer = dict.fromkeys("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 0)
    for c in my_string:
        answer[c] += 1

    return list(answer.values())


solution = solution_v2
