"""
프로그래머스 Lv0 #120844 - 배열 회전시키기
https://school.programmers.co.kr/learn/courses/30/lessons/120844

[문제]
정수가 담긴 배열 numbers와 문자열 direction이 매개변수로 주어집니다.
배열 numbers의 원소를 direction 방향으로 한 칸씩 회전시킨 배열을 return하도록
solution 함수를 완성해주세요.

[제한]
- 3 ≤ numbers의 길이 ≤ 20
- direction은 "left"와 "right" 둘 중 하나입니다.
"""


def solution_v1(numbers: list[int], direction: str) -> list[int]:
    """
    [Approach] deque의 popleft/appendleft 활용
    [Time] O(n)  [Space] O(n)
    """
    from collections import deque

    answer = deque(numbers)
    if direction == "left":
        answer.append(answer.popleft())
    else:
        answer.appendleft(answer.pop())

    return list(answer)


def solution_v2(numbers: list[int], direction: str) -> list[int]:
    """
    [Approach] 리스트 메서드 조합 (insert/pop/remove)
    [Time] O(n)  [Space] O(1)
    ⚠️ 원본 배열을 수정함 (side effect)
    """
    if direction == "left":
        numbers.append(numbers[0])
        numbers.pop(0)
    else:
        numbers.insert(0, numbers[-1])
        numbers.pop()

    return numbers


def solution_v3(numbers: list[int], direction: str) -> list[int]:
    """
    [Approach] 슬라이싱으로 새 배열 생성
    [Time] O(n)  [Space] O(n)
    ✅ 가장 Pythonic하고 간결
    """
    return (
        [numbers[-1]] + numbers[:-1]
        if direction == "right"
        else numbers[1:] + [numbers[0]]
    )


def solution_v4(numbers: list[int], direction: str) -> list[int]:
    """
    [Approach] deque.rotate() 내장 메서드
    [Time] O(n)  [Space] O(n)
    ✅ 회전 전용 메서드, 의도가 명확함
    """
    from collections import deque

    answer = deque(numbers)
    if direction == "right":
        answer.rotate(1)
    else:
        answer.rotate(-1)

    return list(answer)


solution = solution_v3
