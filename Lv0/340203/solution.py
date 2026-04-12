"""
프로그래머스 Lv0 #340203 - [PCCE 기출문제] 5번 / 심폐소생술
https://school.programmers.co.kr/learn/courses/30/lessons/340203

[문제]
심폐소생술은 다음과 같은 순서를 통해 실시합니다.

1. 심정지 및 무호흡 확인 [check]
2. 도움 및 119 신고 요청 [call]
3. 가슴압박 30회 시행 [pressure]
4. 인공호흡 2회 시행 [respiration]
5. 가슴압박, 인공호흡 반복 [repeat]

주어진 solution 함수는 심폐소생술을 하는 방법의 순서가 담긴 문자열들이
무작위 순서로 담긴 리스트 cpr이 주어질 때 각각의 방법이 몇 번째 단계인지
순서대로 담아 return하는 함수입니다.

[제한]
cpr은 다음 문자열들이 한 번씩 포함되어 있습니다.
"check", "call", "pressure", "respiration", "repeat"

[원본 C++ 빈칸 채우기 코드]
vector<int> solution(vector<string> cpr) {
    vector<int> answer = {0, 0, 0, 0, 0};
    vector<string> basic_order = {"check", "call", "pressure", "respiration", "repeat"};

    for(int i=0; i<___; i++){
        for(int j=0; j<___; j++){
            if(cpr[i] == basic_order[j]){
                answer[i] = ___;
                break;
            }
        }
    }
    return answer;
}
"""


def solution_v1(cpr: list[str]) -> list[int]:
    """
    [Approach] 이중 루프로 각 동작을 표준 순서 리스트와 선형 비교.
    원본 C++ 빈칸 채우기 코드의 구조를 그대로 Python으로 옮긴 형태.
    [Time] O(n * k)  (n=cpr 길이, k=basic_order 길이=5)
    [Space] O(n)     (결과 리스트)
    """
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i + 1)
    return answer


solution = solution_v1
