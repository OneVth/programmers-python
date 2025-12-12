"""
프로그래머스 Lv0 #120880 - 특이한 정렬
https://school.programmers.co.kr/learn/courses/30/lessons/120880

[문제]
정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다.
이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다.
정수가 담긴 배열 numlist와 정수 n이 주어질 때
numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 10,000
- 1 ≤ numlist의 원소 ≤ 10,000
- 1 ≤ numlist의 길이 ≤ 100
- numlist는 중복된 원소를 갖지 않습니다.
"""


def solution_v1(numlist: list[int], n: int) -> list[int]:
    """
    [Approach] bisect 삽입 정렬 - 먼저 값 기준 내림차순 정렬 후,
               거리 기준으로 올바른 위치에 삽입 (거리 같으면 큰 값이 앞)
    [Time] O(N² log N) - 정렬 O(N log N) + N번의 bisect/insert O(N)
    [Space] O(N) - answer, abs_answer 리스트
    """
    from bisect import bisect_left

    sorted_list = sorted(numlist, reverse=True)  # 큰 수부터 처리
    answer = []
    abs_answer = []

    for i in sorted_list:
        v = abs(i - n)
        idx = bisect_left(abs_answer, v)

        answer.insert(idx, i)
        abs_answer.insert(idx, v)

    return answer


def solution_v2(numlist: list[int], n: int) -> list[int]:
    """
    [Approach] 다중 키 정렬 - 튜플을 key로 사용하여 한 번에 정렬
               (거리 오름차순, 값 내림차순)
    [Time] O(N log N) - Python Timsort
    [Space] O(N) - 정렬 결과 저장
    """
    return sorted(numlist, key=lambda x: (abs(x - n), -x))


solution = solution_v2
