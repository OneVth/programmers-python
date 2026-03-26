"""
프로그래머스 Lv0 #181930 - 주사위 게임 2
https://school.programmers.co.kr/learn/courses/30/lessons/181930

[문제]
1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각
a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

- 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
- 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면
  (a + b + c) × (a² + b² + c²) 점을 얻습니다.
- 세 숫자가 모두 같다면
  (a + b + c) × (a² + b² + c²) × (a³ + b³ + c³) 점을 얻습니다.

세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

[제한]
- a, b, c는 1 이상 6 이하의 정수입니다.
"""


def solution_v1(a: int, b: int, c: int) -> int:
    """
    [Approach] set의 크기로 케이스 분기 (모두 같음/두 개 같음/모두 다름)
    [Time] O(1)  [Space] O(1)
    """
    l = len({a, b, c})
    if l == 1:
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif l == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)
    else:
        return a + b + c


solution = solution_v1
