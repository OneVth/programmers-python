"""
프로그래머스 Lv0 #181916 - 주사위 게임 3
https://school.programmers.co.kr/learn/courses/30/lessons/181916

[문제]
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라
다음과 같은 점수를 얻습니다.

- 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
- 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면
  (10 × p + q)²점을 얻습니다.
- 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면
  (p + q) × |p - q|점을 얻습니다.
- 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른
  q, r(q ≠ r)이라면 q × r점을 얻습니다.
- 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.

네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를
return 하는 solution 함수를 작성해 주세요.

[제한]
- a, b, c, d는 1 이상 6 이하의 정수입니다.
"""


def solution_v1(a: int, b: int, c: int, d: int) -> int:
    """
    [Approach] Counter로 고유값 개수(len)와 최대 빈도수로 5가지 케이스 분기
               len=1: 모두 같음 / len=2: 3+1 또는 2+2 / len=3: 2+1+1 / len=4: 모두 다름
    [Time] O(1)  [Space] O(1)
    """
    from collections import Counter

    counter = Counter((a, b, c, d))
    len_counter = len(counter)

    nums = list(counter.keys())
    cnt = list(counter.values())

    if len_counter == 1:
        return 1111 * nums[0]
    elif len_counter == 2:
        if max(cnt) == 3:
            temp = counter.most_common()
            return (10 * temp[0][0] + temp[1][0]) ** 2
        else:
            return (nums[0] + nums[1]) * abs(nums[0] - nums[1])
    elif len_counter == 3:
        temp = counter.most_common()
        return temp[1][0] * temp[2][0]
    else:
        return min(nums)


# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
