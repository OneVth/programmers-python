"""
프로그래머스 Lv0 #120887 - k의 개수
https://school.programmers.co.kr/learn/courses/30/lessons/120887

[문제]
1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다.
정수 i, j, k가 매개변수로 주어질 때,
i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.

[제한]
- 1 ≤ i < j ≤ 100,000
- 0 ≤ k ≤ 9
"""


def solution_v1(i: int, j: int, k: int) -> int:
    """
    [Approach] 문자열 변환 + 조건부 카운트 - 왈러스 연산자로 변환 후 in 체크
               k가 포함된 경우에만 count() 호출하여 약간의 최적화
    [Time] O(N * M) - N: 범위 크기, M: 숫자의 자릿수
    [Space] O(M) - 문자열 변환
    """
    cnt = 0
    k_str = str(k)
    for l in range(i, j + 1):
        if k_str in (l_str := str(l)):
            cnt += l_str.count(k_str)

    return cnt


def solution_v2(i: int, j: int, k: int) -> int:
    """
    [Approach] 제너레이터 + sum - 한 줄로 모든 숫자의 k 등장 횟수 합산
               간결하지만 매번 str(k) 변환 발생
    [Time] O(N * M) - N: 범위 크기, M: 숫자의 자릿수
    [Space] O(1) - 제너레이터 사용
    """
    return sum(str(i).count(str(k)) for i in range(i, j + 1))


solution = solution_v1
