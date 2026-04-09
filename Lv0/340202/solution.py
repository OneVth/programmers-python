"""
프로그래머스 Lv0 #340202 - [PCCE 기출문제] 6번 / 물 부족
https://school.programmers.co.kr/learn/courses/30/lessons/340202

[문제]
ㅇㅇ시에는 저수지가 하나 있는데, 도시 내에서 사용하는 모든 물은 이 저수지에 저장된 물을 끌어와 사용합니다.
이상 기후로 인해 극심한 가뭄이 예고된 상황에서, 지난 달의 물 사용량과 이번달부터 일정 기간 동안의
월별 물 사용량의 변화를 예측한 값을 이용해 몇 달 뒤 물이 부족해지는지 예측하려고 합니다.

이번달부터의 월별 물 사용량 변화를 예측한 값은 리스트에 담겨 주어집니다.
리스트의 각 원소는 해당 월의 물 사용량이 전 달에 비해 몇 % 만큼 증가 또는 감소하는지를 나타냅니다.

현재 저수지에 저장된 물의 양을 나타내는 정수 storage와 지난 달 물 사용량을 나타내는 정수 usage,
월별 물 사용량이 전 달 대비 어떻게 변하는지 저장된 정수 리스트 change가 주어질 때
몇 달 뒤 물이 부족해지는지 return 하도록 solution 함수를 완성해 주세요.
가뭄이 끝날 때까지 저수지의 물이 남아 있다면 -1을 return합니다.

※ 디버깅(Debugging) 문제: 이미 완성된 코드에서 버그를 찾아 1줄만 수정하는 문제입니다.

[제한]
- 1,000 ≤ storage ≤ 1,000,000
- 500 ≤ usage ≤ 30,000
- 1 ≤ change의 길이 ≤ 30
  - -99 ≤ change[i] ≤ 500
  - change[i]가 양수: 물 사용량이 전 달보다 change[i]% 증가
  - change[i]가 음수: 물 사용량이 전 달보다 change[i]% 감소
  - change[i]가 0: 물 사용량이 전 달과 동일
  - 매달 물 사용량은 소수점 이하를 버린 정수로 계산
"""


def solution_v1(storage: int, usage: int, change: list[int]) -> int:
    """
    [Approach] 매달 사용량에 변화율 적용 후 누적합이 storage 초과 시 해당 인덱스 반환
    [Time] O(n)  [Space] O(1)
    """
    total_usage = 0
    for i, rate in enumerate(change):
        usage += int(usage * rate / 100)
        total_usage += usage
        if total_usage > storage:
            return i
    return -1


solution = solution_v1
