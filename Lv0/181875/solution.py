"""
프로그래머스 Lv0 #181875 - 배열에서 문자열 대소문자 변환하기
https://school.programmers.co.kr/learn/courses/30/lessons/181875

[문제]
문자열 배열 strArr가 주어집니다.
모든 원소가 알파벳으로만 이루어져 있을 때,
배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로,
짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서
반환하는 solution 함수를 완성해 주세요.

[제한]
- 1 <= strArr <= 20
  - 1 <= strArr의 원소의 길이 <= 20
  - strArr의 원소는 알파벳으로 이루어진 문자열입니다.
"""


def solution_v1(strArr: list[str]) -> list[str]:
    """
    [Approach] enumerate로 인덱스 추적, 홀짝에 따라 upper/lower 적용
    [Time] O(n * m)  [Space] O(n * m)  (n: 배열 길이, m: 문자열 평균 길이)
    """
    answer = []
    for i, s in enumerate(strArr):
        if i % 2 == 0:
            answer.append(s.lower())
        else:
            answer.append(s.upper())

    return answer


solution = solution_v1
