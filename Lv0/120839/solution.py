"""
프로그래머스 Lv0 #120839 - 가위 바위 보
https://school.programmers.co.kr/learn/courses/30/lessons/120839

[문제]
가위는 2, 바위는 0, 보는 5로 표현합니다.
가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때,
rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을
return하도록 solution 함수를 완성해보세요.

[제한]
- 0 < rsp의 길이 ≤ 100
- rsp와 길이가 같은 문자열을 return 합니다.
- rsp는 숫자 0, 2, 5로 이루어져 있습니다.
"""


def solution_v1(rsp: str) -> str:
    """
    [Approach] 딕셔너리 매핑 + list comprehension
    [Time] O(n)  [Space] O(n)
    ✅ 직관적이고 매핑 관계가 명확함
    """
    win = {"0": "5", "2": "0", "5": "2"}
    return "".join([win[c] for c in rsp])


def solution_v2(rsp: str) -> str:
    """
    [Approach] str.translate + maketrans
    [Time] O(n)  [Space] O(1)
    ✅ C 레벨 최적화, 1글자→1글자 매핑에 최적
    """
    return rsp.translate(str.maketrans("025", "502"))


solution = solution_v2
