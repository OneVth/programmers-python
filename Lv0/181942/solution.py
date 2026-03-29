"""
프로그래머스 Lv0 #181942 - 문자열 섞기
https://school.programmers.co.kr/learn/courses/30/lessons/181942

[문제]
길이가 같은 두 문자열 str1과 str2가 주어집니다.
두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는
문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

[제한]
- 1 ≤ str1의 길이 = str2의 길이 ≤ 10
- str1과 str2는 알파벳 소문자로 이루어진 문자열입니다.
"""


def solution_v1(str1: str, str2: str) -> str:
    """
    [Approach] 인덱스로 두 문자열을 동시에 순회하며 리스트에 번갈아 추가 후 join
    [Time] O(n)  [Space] O(n)
    """
    answer = []
    for i in range(len(str1)):
        answer.append(str1[i])
        answer.append(str2[i])
    return "".join(answer)


def solution_v2(str1: str, str2: str) -> str:
    """
    [Approach] zip()으로 두 문자열을 쌍으로 묶어 generator로 펼친 뒤 join
    [Time] O(n)  [Space] O(n)
    """
    return "".join(a + b for a, b in zip(str1, str2))


solution = solution_v2
