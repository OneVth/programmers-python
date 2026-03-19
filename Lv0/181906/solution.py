"""
프로그래머스 Lv0 #181906 - 접두사인지 확인하기
https://school.programmers.co.kr/learn/courses/30/lessons/181906

[문제]
어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다.
예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
문자열 my_string 과 is_prefix 가 주어질 때,
is_prefix 가 my_string 의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ my_string의 길이 ≤ 100
- 1 ≤ is_prefix의 길이 ≤ 100
- my_string과 is_prefix는 영소문자로만 이루어져 있습니다.
"""


def solution_v1(my_string: str, is_prefix: str) -> int:
    """
    [Approach] find()가 0을 반환하면 접두사 — not 0 = True 이용
               find()는 없으면 -1, 중간 발견이면 양수 → 모두 falsy 처리
    [Time] O(n)  [Space] O(1)
    """
    return 1 if not my_string.find(is_prefix) else 0


def solution_v2(my_string: str, is_prefix: str) -> int:
    """
    [Approach] startswith() 직접 사용 후 int 변환
    [Time] O(k)  [Space] O(1)  (k = len(is_prefix))
    """
    return int(my_string.startswith(is_prefix))

solution = solution_v2