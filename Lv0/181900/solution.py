"""
프로그래머스 Lv0 #181900 - 글자 지우기
https://school.programmers.co.kr/learn/courses/30/lessons/181900

[문제]
문자열 my_string과 정수 배열 indices가 주어질 때,
my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고
이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 <= indices의 길이 < my_string의 길이 <= 100
- my_string은 영소문자로만 이루어져 있습니다
- 0 <= indices의 원소 < my_string의 길이
- indices의 원소는 모두 서로 다릅니다.
"""


def solution_v1(my_string: str, indices: list[int]) -> str:
    """
    [Approach] enumerate로 순회하며 indices에 없는 글자만 수집
    [Time] O(n * m)  [Space] O(n)  (n=문자열 길이, m=indices 길이)
    """
    answer = []
    for i, c in enumerate(my_string):
        if i not in indices:
            answer.append(c)

    return "".join(answer)


def solution_v2(my_string: str, indices: list[int]) -> str:
    """
    [Approach] set 변환 + 제너레이터 표현식으로 O(1) lookup 최적화
    [Time] O(n + m)  [Space] O(m)  (n=문자열 길이, m=indices 길이)
    """
    exclude = set(indices)
    return "".join(c for i, c in enumerate(my_string) if i not in exclude)


solution = solution_v2
