"""
프로그래머스 Lv0 #120871 - 저주의 숫자 3
https://school.programmers.co.kr/learn/courses/30/lessons/120871

[복습] 1차 - 2025-12-17

[문제]
3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다.
3x 마을 사람들의 숫자는 다음과 같습니다.

| 10진법 | 3x 마을에서 쓰는 숫자 | 10진법 | 3x 마을에서 쓰는 숫자 |
|--------|----------------------|--------|----------------------|
| 1      | 1                    | 6      | 8                    |
| 2      | 2                    | 7      | 10                   |
| 3      | 4                    | 8      | 11                   |
| 4      | 5                    | 9      | 14                   |
| 5      | 7                    | 10     | 16                   |

정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록
solution 함수를 완성해주세요.

[제한]
- 1 ≤ n ≤ 100
"""


def solution_v1(n: int) -> int:
    """
    [Approach] 시뮬레이션 - 3x 마을 숫자를 하나씩 생성하며 n번째 찾기
    [Time] O(n * m) - n: 입력값, m: 유효 숫자 간 평균 간격
    [Space] O(log n) - 숫자를 문자열로 변환할 때 사용
    """
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or "3" in str(answer):
            answer += 1
    return answer


# 기본 솔루션 지정
solution = solution_v1
