"""
프로그래머스 Lv0 #181871 - 문자열이 몇 번 등장하는지 세기
https://school.programmers.co.kr/learn/courses/30/lessons/181871

[문제]
문자열 myString과 pat이 주어집니다.
myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

[제한]
- 1 ≤ myString ≤ 1000
- 1 ≤ pat ≤ 10
"""


def solution_v1(myString: str, pat: str) -> int:
    """
    [Approach] 슬라이딩 윈도우 - 첫 글자 일치 시 슬라이스 비교
    [Time] O(n * m)  [Space] O(m)
    - n: myString 길이, m: pat 길이
    """
    answer = 0
    length = len(pat)

    for i, c in enumerate(myString):
        if pat[0] == c:
            if myString[i : i + length] == pat:
                answer += 1

    return answer


def solution_v2(myString: str, pat: str) -> int:
    """
    [Approach] 슬라이딩 윈도우 - startswith로 비교
    [Time] O(n * m)  [Space] O(n)
    - myString[i:]가 매번 새 문자열을 생성하여 v1보다 공간 비효율
    """
    answer = 0

    for i, c in enumerate(myString):
        if pat[0] == c:
            if myString[i:].startswith(pat):
                answer += 1

    return answer


def solution_v3(myString: str, pat: str) -> int:
    """
    [Approach] str.find 반복 호출 - 매칭 위치부터 1칸 뒤에서 재탐색
    [Time] O(n * m)  [Space] O(n)
    - C 내부 구현의 find를 활용하여 실측 성능 우수
    """
    answer = 0

    idx = 0
    for i in range(len(myString)):
        temp = str.find(myString[idx:], pat)
        if temp != -1:
            answer += 1
            idx += temp + 1
        else:
            break

    return answer


def solution_v4(myString: str, pat: str) -> int:
    """
    [Approach] str.find(pat, start)로 슬라이싱 없이 탐색
    [Time] O(n * m)  [Space] O(1)
    - v3 개선: 슬라이싱 제거로 메모리 할당 없음
    """
    answer = 0
    idx = 0
    while (idx := myString.find(pat, idx)) != -1:
        answer += 1
        idx += 1

    return answer

solution = solution_v4
