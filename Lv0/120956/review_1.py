"""
프로그래머스 Lv0 #120956 - 옹알이 (1)
https://school.programmers.co.kr/learn/courses/30/lessons/120956

[복습] 1차 - 2025-12-17

[문제]
머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다.
조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩
사용해 조합한(이어 붙인) 발음밖에 하지 못합니다.
문자열 배열 babbling이 매개변수로 주어질 때,
머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ babbling의 길이 ≤ 100
- 1 ≤ babbling[i]의 길이 ≤ 15
- babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장합니다.
- 문자열은 알파벳 소문자로만 이루어져 있습니다.

[유의사항]
- 네 가지를 붙여 만들 수 있는 발음 이외에는 어떤 발음도 할 수 없는 것으로 규정합니다.
- 예: "woowo"는 "woo"는 발음할 수 있지만 "wo"를 발음할 수 없기 때문에 불가능
"""


def solution_v1(babbling: list[str]) -> int:
    """
    [Approach] 발음 가능한 단어를 공백으로 치환 후 빈 문자열 확인
    [Time] O(n * m) - n은 babbling 길이, m은 각 문자열 평균 길이
    [Space] O(m) - 치환된 문자열 저장
    """
    answer = 0
    for s in babbling:
        for word in ["aya", "ye", "woo", "ma"]:
            if word in s:
                s = s.replace(word, " ")

        if not s.strip():
            answer += 1

    return answer


def solution_v2(babbling: list[str]) -> int:
    """
    [Approach] 정규식으로 발음 조합 패턴 매칭
    [Time] O(n * m) - 정규식 매칭
    [Space] O(1) - 컴파일된 패턴만 저장
    """
    import re

    pattern = re.compile(r"^(aya|ye|woo|ma)+$")
    return sum(1 for word in babbling if pattern.match(word))


solution = solution_v2
