"""
프로그래머스 Lv0 #120904 - 숫자 찾기
https://school.programmers.co.kr/learn/courses/30/lessons/120904

[문제]
정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면
num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록
solution 함수를 완성해보세요.

[제한]
- 0 < num < 1,000,000
- 0 ≤ k < 10
- num에 k가 여러 개 있으면 가장 처음 나타나는 자리를 return 합니다.
"""


def solution_v1(num: int, k: int) -> int:
    """
    [Approach] index() + 예외처리 - 없으면 ValueError 발생
    [Time] O(n)  [Space] O(n) - 문자열 변환
    """
    try:
        return str(num).index(str(k)) + 1
    except Exception:
        return -1


def solution_v2(num: int, k: int) -> int:
    """
    [Approach] enumerate 순회 - 각 자릿수를 순회하며 비교
    [Time] O(n)  [Space] O(n)
    """
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i + 1

    return -1


def solution_v3(num: int, k: int) -> int:
    """
    [Approach] find() + 조건식 - 존재 여부 확인 후 find()
    [Time] O(n)  [Space] O(n)
    """
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1


def solution_v4(num: int, k: int) -> int:
    """
    [Approach] find() 최적화 - 한 번 순회 후 결과로 분기
    [Time] O(n)  [Space] O(n)
    """
    idx = str(num).find(str(k))
    return idx + 1 if idx != -1 else -1


solution = solution_v1
