"""
프로그래머스 Lv0 #181844 - 배열의 원소 삭제하기
https://school.programmers.co.kr/learn/courses/30/lessons/181844

[문제]
정수 배열 arr과 delete_list가 있습니다.
arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은 원소들은
기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요.

[제한]
- 1 ≤ arr의 길이 ≤ 100
- 1 ≤ arr의 원소 ≤ 1,000
- arr의 원소는 모두 서로 다릅니다.
- 1 ≤ delete_list의 길이 ≤ 100
- 1 ≤ delete_list의 원소 ≤ 1,000
- delete_list의 원소는 모두 서로 다릅니다.
"""


def solution_v1(arr: list[int], delete_list: list[int]) -> list[int]:
    """
    [Approach] 리스트 컴프리헨션으로 delete_list에 없는 원소만 필터링
    [Time] O(n*m) - arr 순회(n) × delete_list 조회(m)
    [Space] O(n) - 결과 리스트
    """
    return [x for x in arr if x not in delete_list]


def solution_v2(arr: list[int], delete_list: list[int]) -> list[int]:
    """
    [Approach] set 변환으로 조회 시간 O(1) 최적화
    [Time] O(n+m) - set 생성(m) + arr 순회(n)
    [Space] O(m+n) - delete_set(m) + 결과 리스트(n)
    """
    delete_set = set(delete_list)
    return [x for x in arr if x not in delete_set]


solution = solution_v2
