"""
프로그래머스 Lv0 #181838 - 날짜 비교하기
https://school.programmers.co.kr/learn/courses/30/lessons/181838

[문제]
정수 배열 date1과 date2가 주어집니다. 두 배열은 각각 날짜를 나타내며
[year, month, day] 꼴로 주어집니다.
각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.

만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는
solution 함수를 완성해 주세요.

[제한]
- date1의 길이 = date2의 길이 = 3
  - 0 ≤ year ≤ 10,000
  - 1 ≤ month ≤ 12
  - day는 month에 따라 가능한 날짜로 주어집니다.
"""


def solution_v1(date1: list[int], date2: list[int]) -> int:
    """
    [Approach] 연/월/일 순으로 비교하며 첫 번째 차이점에서 판정
    [Time] O(1) - 최대 3번 비교
    [Space] O(1)
    """
    for i in range(len(date1)):
        if date1[i] == date2[i]:
            continue

        if date1[i] < date2[i]:
            return 1
        else:
            return 0

    return 0


def solution_v2(date1: list[int], date2: list[int]) -> int:
    """
    [Approach] Python 리스트의 사전순 비교 활용 - 연/월/일 자동 순차 비교
    [Time] O(1)  [Space] O(1)
    """
    return int(date1 < date2)


# ✅ 기본 솔루션 지정
solution = solution_v2
