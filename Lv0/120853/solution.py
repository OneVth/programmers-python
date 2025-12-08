"""
문제: 컨트롤 제트
난이도: Lv0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120853

설명:
숫자와 "Z"가 공백으로 구분되어 담긴 문자열이 주어집니다.
문자열에 있는 숫자를 차례대로 더하려고 합니다.
이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다.
숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록
solution 함수를 완성해보세요.

제한사항:
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
    [Approach] while 루프 - Z와 직전 숫자를 리스트에서 제거
    [Time] O(n²) - while 루프 * index 탐색
    [Space] O(n) - 토큰 리스트 저장
    """
    tokens = s.split(" ")

    while "Z" in tokens:
        tokens.pop(tokens.index("Z") - 1)
        tokens.pop(tokens.index("Z"))

    return sum(int(i) for i in tokens)


def solution_v2(s: str) -> int:
    """
    [Approach] v1과 동일 - map() 사용 버전
    [Time] O(n²) - while 루프 * index 탐색
    [Space] O(n) - 토큰 리스트 저장
    """
    tokens = s.split(" ")

    while "Z" in tokens:
        tokens.pop(tokens.index("Z") - 1)
        tokens.pop(tokens.index("Z"))

    return sum(map(int, tokens))


def solution_v3(s: str) -> int:
    """
    [Approach] 순회 + 조건부 덧셈/뺄셈 (walrus operator 활용)
    [Time] O(n) - 단일 순회
    [Space] O(n) - 토큰 리스트 저장
    """
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i - 1])
    return answer


def solution_v4(s: str) -> int:
    """
    [Approach] 스택 - Z면 pop, 숫자면 push
    [Time] O(n) - 단일 순회
    [Space] O(n) - 스택 저장
    """
    stack = []
    for a in s.split(" "):
        if a != "Z":
            stack.append(int(a))
        else:
            stack.pop()

    return sum(stack)


solution = solution_v4
