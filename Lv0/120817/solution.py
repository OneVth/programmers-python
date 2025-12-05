"""
프로그래머스 Lv0 #120817 - 배열의 평균값
https://school.programmers.co.kr/learn/courses/30/lessons/120817

[문제]
정수 배열 numbers가 매개변수로 주어질 때, numbers의 평균값을 반환

[제한]
- 0 < numbers의 길이 < 100
- 0 < numbers의 원소 < 1,000
- 정답의 소수 부분이 .0 또는 .5인 경우만 입력
"""


def solution_v1(numbers: list[int]) -> float:
    """
    [Approach] sum / len
    [Time] O(n)  [Space] O(1)
    ✅ 외부 라이브러리 없이 해결
    """
    return sum(numbers) / len(numbers)


def solution_v2(numbers: list[int]) -> float:
    """
    [Approach] numpy.mean
    [Time] O(n)  [Space] O(1)
    ⚠️ numpy 의존성 - 코딩테스트에서 사용 불가할 수 있음
    """
    from numpy import mean
    return mean(numbers)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
