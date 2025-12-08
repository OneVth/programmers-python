"""
문제: 숨어있는 숫자의 덧셈 (1)
난이도: Lv0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120851

설명:
문자열 my_string이 매개변수로 주어집니다.
my_string 안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

제한사항:
- 1 ≤ my_string의 길이 ≤ 1,000
- my_string은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.

유의사항:
- 연속된 숫자도 각각 한 자리 숫자로 취급합니다.
"""


def solution_v1(my_string: str) -> int:
    """
    [Approach] 제너레이터 표현식 - isdigit() 필터링 후 합계
    [Time] O(n) - 문자열 순회
    [Space] O(1) - 제너레이터로 메모리 효율적
    """
    return sum(int(i) for i in my_string if i.isdigit())


solution = solution_v1
