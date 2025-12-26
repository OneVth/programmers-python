"""
프로그래머스 Lv0 #181836 - 그림 확대
https://school.programmers.co.kr/learn/courses/30/lessons/181836

[문제]
직사각형 형태의 그림 파일이 있고, 이 그림 파일은 1 × 1 크기의 정사각형 크기의 픽셀로 이루어져 있습니다.
이 그림 파일을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질 때,
이 그림 파일을 가로 세로로 k배 늘린 그림 파일을 나타내도록 문자열 배열을 return 하는
solution 함수를 작성해 주세요.

[제한]
- 1 ≤ picture의 길이 ≤ 20
- 1 ≤ picture의 원소의 길이 ≤ 20
- 모든 picture의 원소의 길이는 같습니다.
- picture의 원소는 '.'과 'x'로 이루어져 있습니다.
- 1 ≤ k ≤ 10
"""


def solution_v1(picture: list[str], k: int) -> list[str]:
    """
    [Approach] 각 행을 순회하며 문자별로 k번 반복(가로 확대) 후, 행 자체를 k번 추가(세로 확대)
    [Time] O(n * m * k²) - n: 행 수, m: 열 수, k: 확대 배율
    [Space] O(n * m * k²) - 결과 배열 크기
    """
    answer = []
    for line in picture:
        for _ in range(k):
            answer.append("".join(c * k for c in line))

    return answer


def solution_v2(picture: list[str], k: int) -> list[str]:
    """
    [Approach] 가로 확대 후 리스트 곱셈으로 세로 확대를 한 번에 처리
    [Time] O(n * m * k) - 가로 확대 문자열을 한 번만 생성, 리스트 곱셈은 참조 복사
    [Space] O(n * m * k²) - 결과 배열 크기
    """
    answer = []
    for line in picture:
        answer += ["".join(c * k for c in line)] * k
    return answer


# ✅ 기본 솔루션 지정
solution = solution_v2
