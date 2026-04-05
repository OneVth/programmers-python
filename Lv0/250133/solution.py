"""
프로그래머스 Lv0 #250133 - [PCCE 기출문제] 1번 / 출력
https://school.programmers.co.kr/learn/courses/30/lessons/250133

[문제]
주어진 초기 코드는 변수에 데이터를 저장하고 출력하는 코드입니다.
아래와 같이 출력되도록 빈칸을 채워 코드를 완성해 주세요.

출력 예시:
Spring is beginning
13
310

- msg = "Spring is beginning" → 그대로 출력
- val1 = 3 → val1 + 10 = 13 출력
- val2 = "3" → val2 + "10" = "310" (문자열 연결) 출력

[제한]
- 입력 없음 (고정 출력 문제)
"""


def solution_v1() -> str:
    """
    [Approach] 세 변수를 선언 후 "\n".join()으로 출력 문자열 조합
    [Time] O(1)  [Space] O(1)
    """
    string_msg = "Spring is beginning"
    int_val = 3
    string_val = "3"

    return "\n".join([string_msg, str(int_val + 10), string_val + "10"])


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
