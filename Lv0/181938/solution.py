"""
프로그래머스 Lv0 #181938 - 두 수의 연산값 비교하기
https://school.programmers.co.kr/learn/courses/30/lessons/181938

[문제]
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다.
예를 들면 다음과 같습니다.
- 12 ⊕ 3 = 123
- 3 ⊕ 12 = 312

양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는
solution 함수를 완성해 주세요.
단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.

[제한]
- 1 ≤ a, b < 10,000
"""


def solution_v1(a: int, b: int) -> int:
    """
    [Approach] a⊕b를 초기값으로, 2*a*b가 더 크면 교체하는 명시적 비교
               같을 때 a⊕b 반환 조건을 < 연산자로 자연스럽게 처리
    [Time] O(log b)  [Space] O(log b)  ← str(b) 변환 자릿수에 비례
    """
    answer = int(str(a) + str(b))
    if answer < 2 * a * b:
        answer = 2 * a * b
    return answer


def solution_v2(a: int, b: int) -> int:
    """
    [Approach] max()로 두 값 비교를 한 줄로 압축
               max()는 같을 때 첫 번째 인자를 반환하므로 a⊕b 우선 조건 자동 충족
    [Time] O(log b)  [Space] O(log b)
    """
    return max(int(str(a) + str(b)), 2 * a * b)


solution = solution_v2
