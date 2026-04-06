"""
프로그래머스 Lv0 #340200 - [PCCE 기출문제] 8번 / 닉네임 규칙
https://school.programmers.co.kr/learn/courses/30/lessons/340200

[문제]
온라인 서비스를 이용하기 위해서 닉네임이 필요합니다. 이때 닉네임이 될 수 있는 조건은 다음과 같습니다.
- 닉네임의 길이가 4자 이상 8자 이하여야합니다.
- 닉네임에는 소문자 l과 w, 대문자 O와 W를 사용할 수 없습니다.
- 이외의 영어 대소문자와 숫자는 모두 사용이 가능합니다.

주어진 solution 함수는 사용할 수 없는 닉네임 nickname을 받아 사용할 수 있는 닉네임으로
바꿔주는 함수입니다. 닉네임을 변경하는 규칙은 다음과 같으며 첫 번째 규칙부터 순서대로 적용합니다.
1. 소문자 l을 대문자 I로 변경합니다.
2. 소문자 w를 두 개의 소문자 v, 즉 vv로 변경합니다.
3. 대문자 W를 두 개의 대문자 V, 즉 VV로 변경합니다.
4. 대문자 O를 숫자 0으로 변경합니다.
5. 수정된 닉네임의 길이가 4 미만일 경우 뒤에 소문자 o를 길이가 4가 될 때까지 이어붙입니다.
6. 수정된 닉네임의 길이가 8보다 클 경우 8번째 문자까지만 사용합니다.

주어진 solution 함수에는 위의 규칙 중 올바르게 적용되지 않는 것이 있습니다.
solution 함수가 올바르게 작동하도록 한 줄을 수정해주세요.

[제한]
- 1 ≤ nickname의 길이 ≤ 10
- nickname은 영어 대소문자와 숫자로만 이루어져있습니다.
"""


def solution_v1(nickname: str) -> str:
    """
    [Approach] 문자열 순회하며 교체 규칙 적용, while로 최소 길이 패딩, 슬라이싱으로 최대 길이 제한
    [Time] O(n)  [Space] O(n)
    """
    answer = ""
    for c in nickname:
        if c == "l":
            answer += "I"
        elif c == "w":
            answer += "vv"
        elif c == "W":
            answer += "VV"
        elif c == "O":
            answer += "0"
        else:
            answer += c
    while len(answer) < 4:
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer


solution = solution_v1
