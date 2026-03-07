"""
프로그래머스 Lv0 #181880 - 1로 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/181880

[문제]
정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면,
마지막엔 1이 됩니다. 예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.

- 10 / 2 = 5
- (5 - 1) / 2 = 2
- 2 / 2 = 1

위와 같이 3번의 나누기 연산으로 1이 되었습니다.

정수들이 담긴 리스트 num_list가 주어질 때, num_list의 모든 원소를 1로 만들기
위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.

[제한]
- 3 <= num_list의 길이 <= 15
- 1 <= num_list의 원소 <= 30
"""


def solution_v1(num_list: list[int]) -> int:
    """
    [Approach] bit_length를 이용한 수학적 풀이. 2로 나누는 횟수 = 비트 길이 - 1
    [Time] O(n)  [Space] O(1)
    """
    return sum(i.bit_length() - 1 for i in num_list)


def solution_v2(num_list: list[int]) -> int:
    """
    [Approach] while 루프로 직접 시뮬레이션. 1이 될 때까지 2로 나누며 카운트
    [Time] O(n * log(max_val))  [Space] O(1)
    """
    answer = 0

    for i in num_list:
        while i != 1:
            i //= 2
            answer += 1

    return answer


solution = solution_v2