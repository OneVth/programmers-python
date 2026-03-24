"""
프로그래머스 Lv0 #181925 - 수 조작하기 2
https://school.programmers.co.kr/learn/courses/30/lessons/181925

[문제]
정수 배열 numLog가 주어집니다. 처음에 numLog[0]에서부터 시작해 "w", "a", "s", "d"로
이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.

- "w" : 수에 1을 더한다.
- "s" : 수에 1을 뺀다.
- "d" : 수에 10을 더한다.
- "a" : 수에 10을 뺀다.

그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다.
즉, numLog[i]는 numLog[0]으로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.

주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는
solution 함수를 완성해 주세요.

[제한]
- 2 ≤ numLog의 길이 ≤ 100,000
- -100,000 ≤ numLog[0] ≤ 100,000
- 1 ≤ i ≤ numLog의 길이인 모든 i에 대해 |numLog[i] - numLog[i - 1]|의 값은 1 또는 10
"""


def solution_v1(numLog: list[int]) -> str:
    """
    [Approach] 인접 원소 차이를 딕셔너리로 키 문자에 매핑하여 역추적
    [Time] O(n)  [Space] O(n)
    """
    answer = []
    tab = {1: "w", -1: "s", 10: "d", -10: "a"}
    for i in range(1, len(numLog)):
        d = numLog[i] - numLog[i - 1]
        answer.append(tab[d])
    return "".join(answer)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1


