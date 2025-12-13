"""
프로그래머스 Lv0 #120882 - 등수 매기기
https://school.programmers.co.kr/learn/courses/30/lessons/120882

[문제]
영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다.
영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때,
영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록
solution 함수를 완성해주세요.

[제한]
- 0 ≤ score[0], score[1] ≤ 100
- 1 ≤ score의 길이 ≤ 10
- score의 원소 길이는 2입니다.
- score는 중복된 원소를 갖지 않습니다.

[참고]
- 공동 등수가 있을 경우 다음 등수는 건너뜀 (예: 공동 2등 2명 → 다음은 4등)
"""


def solution_v1(score: list[list[int]]) -> list[int]:
    """
    [Approach] 딕셔너리 매핑 - 정렬 후 점수→등수 매핑 테이블 생성
               공동 등수 처리를 위해 cur_rank와 next_rank 분리 관리
    [Time] O(N log N) - 정렬
    [Space] O(N) - 딕셔너리와 리스트
    """
    sums = [sum(s) for s in score]
    sorted_scores = sorted(sums, reverse=True)

    result = dict()
    cur_score = -1
    cur_rank = 1
    next_rank = 1
    for score_sum in sorted_scores:
        if cur_score == score_sum:
            next_rank += 1
            result[score_sum] = cur_rank
        else:
            cur_rank = next_rank
            result[score_sum] = cur_rank
            next_rank += 1

        cur_score = score_sum

    return [result[s] for s in sums]


def solution_v2(score: list[list[int]]) -> list[int]:
    """
    [Approach] index 활용 - 정렬된 리스트에서 index()로 등수 계산
               index()는 첫 번째 위치를 반환하므로 공동 등수 자동 처리
    [Time] O(N² log N) - 정렬 O(N log N) + N번의 index O(N)
    [Space] O(N) - 정렬된 리스트
    """
    sums = [sum(s) for s in score]
    sorted_sums = sorted(sums, reverse=True)
    return [sorted_sums.index(s) + 1 for s in sums]


def solution_v3(score: list[list[int]]) -> list[int]:
    """
    [Approach] enumerate + 딕셔너리 - 첫 등장 인덱스만 저장하여 공동 등수 처리
               v1보다 간결하고, v2보다 효율적 (O(N) vs O(N²))
    [Time] O(N log N) - 정렬
    [Space] O(N) - 딕셔너리와 리스트
    """
    sums = [sum(s) for s in score]
    sorted_sums = sorted(sums, reverse=True)
    rank_dict = dict()
    for i, r in enumerate(sorted_sums):
        if r not in rank_dict:
            rank_dict[r] = i + 1

    return [rank_dict[s] for s in sums]


solution = solution_v3
