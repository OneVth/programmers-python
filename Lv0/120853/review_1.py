"""
프로그래머스 Lv0 #120853 - 컨트롤 제트
https://school.programmers.co.kr/learn/courses/30/lessons/120853

[복습] 1차 - 2025-12-10

[문제]
숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다.
문자열에 있는 숫자를 차례대로 더하려고 합니다.
이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다.
숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록
solution 함수를 완성해보세요.

[제한]
- 1 ≤ s의 길이 ≤ 200
- -1,000 < s의 원소 중 숫자 < 1,000
- s는 숫자, "Z", 공백으로 이루어져 있습니다.
- s에 있는 숫자와 "Z"는 서로 공백으로 구분됩니다.
- 연속된 공백은 주어지지 않습니다.
- 0을 제외하고는 0으로 시작하는 숫자는 없습니다.
- s는 "Z"로 시작하지 않습니다.
- s의 시작과 끝에는 공백이 없습니다.
- "Z"가 연속해서 나오는 경우는 없습니다.
"""


def solution_v1(s: str) -> int:
    """
    [Approach] 스택 + 음수 추가로 취소 구현
    [Time] O(n)  [Space] O(n)
    ✅ pop 대신 -값을 append → 합계에서 상쇄
    """
    stack = []
    for i in s.split():
        if i == "Z":
            stack.append(-stack[-1])
        else:
            stack.append(int(i))

    return sum(stack)


def solution_v2(s: str) -> int:
    """
    [Approach] 스택 + pop으로 실제 제거
    [Time] O(n)  [Space] O(n)
    ✅ 전통적인 스택 방식, 메모리 효율적
    """
    stack = []
    for i in s.split():
        if i == "Z":
            stack.pop()
        else:
            stack.append(int(i))

    return sum(stack)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
