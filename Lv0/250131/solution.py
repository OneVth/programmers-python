"""
프로그래머스 Lv0 #250131 - [PCCE 기출문제] 3번 / 나이 계산
https://school.programmers.co.kr/learn/courses/30/lessons/250131

[문제]
나이를 세는 방법은 여러 가지가 있습니다.
- 한국식 나이: 태어난 순간 1살, 해가 바뀔 때마다 1살씩 증가 → 현재 연도 - 출생 연도 + 1
- 연 나이: 태어난 순간 0살, 해가 바뀔 때마다 1살씩 증가 → 현재 연도 - 출생 연도

출생 연도 year와 나이 종류 age_type이 주어질 때 2030년에 몇 살인지 return합니다.
age_type이 "Korea"라면 한국식 나이를, "Year"라면 연 나이를 return합니다.

[제한]
- 1950 ≤ year ≤ 2030
- age_type은 "Korea" 또는 "Year"만 주어집니다.
"""


def solution_v1(year: int, age_type: str) -> int:
    """
    [Approach] if/elif 분기로 나이 계산식 선택
    [Time] O(1)  [Space] O(1)
    """
    if age_type == "Korea":
        answer = 2030 - year + 1
    elif age_type == "Year":
        answer = 2030 - year

    return answer


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1

