"""
프로그래머스 Lv0 #340204 - [PCCE 기출문제] 4번 / 병과분류
https://school.programmers.co.kr/learn/courses/30/lessons/340204

[문제]
퓨쳐종합병원에서는 접수한 환자가 진료받을 병과에 따라 자동으로 환자 코드를
부여해 주는 프로그램이 있습니다. 환자 코드의 마지막 네 글자를 보면 환자가
어디 병과에서 진료를 받아야 할지 알 수 있습니다.

마지막 글자       병과
"_eye"           "Ophthalmologyc"
"head"           "Neurosurgery"
"infl"           "Orthopedics"
"skin"           "Dermatology"

환자의 코드를 나타내는 문자열 code를 입력받아 위 표에 맞는 병과를 출력합니다.
위 표의 단어로 끝나지 않는다면 "direct recommendation"를 출력합니다.

[제한]
- 4 ≤ code의 길이 ≤ 20
- code는 영어 소문자와 숫자, 언더바("_")로 이루어져 있습니다.

[원본 C++ 빈칸 채우기 코드]
int main(void) {
    string code;
    cin >> code;
    string last_four_words = code.substr(code.size()-4, 4);
    if(last_four_words == ___){ cout << "Ophthalmologyc"; }
    else if(___){ cout << "Neurosurgery"; }
    else if(___){ cout << "Orthopedics"; }
    ___ { cout << "Dermatology"; }
    ___ { cout << "direct recommendation"; }
    return 0;
}
"""


def solution_v1(code: str) -> str:
    """
    [Approach] 마지막 4글자를 슬라이싱으로 추출한 후 if/elif 체인으로 분기.
    원본 C++ 빈칸 채우기 코드의 구조를 그대로 Python으로 옮긴 형태.
    [Time] O(1)   (code 길이 ≤ 20, 비교 횟수도 상수)
    [Space] O(1)  (last_four_words 슬라이스만 사용)
    """
    last_four_words = code[-4:]

    if last_four_words == "_eye":
        return "Ophthalmologyc"
    elif last_four_words == "head":
        return "Neurosurgery"
    elif last_four_words == "infl":
        return "Orthopedics"
    elif last_four_words == "skin":
        return "Dermatology"
    else:
        return "direct recommendation"


solution = solution_v1
