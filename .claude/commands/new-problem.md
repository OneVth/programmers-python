# New Problem Setup

새로운 문제 풀이 환경을 생성합니다.

## 입력
$ARGUMENTS

형식: `Lv{레벨}/{문제번호}` (예: `Lv0/120819`)

## 작업 내용

### 1. 프로그래머스에서 데이터 수집 (Playwright 사용)

URL: `https://school.programmers.co.kr/learn/courses/30/lessons/{문제번호}`

수집할 정보:
- 문제 제목
- 문제 설명
- 제한 조건
- 입출력 예시 (테스트케이스)

### 2. 폴더 및 파일 생성

생성 경로: `Lv{레벨}/{문제번호}/`

**solution.py**
```python
"""
프로그래머스 Lv{레벨} #{문제번호} - {제목}
https://school.programmers.co.kr/learn/courses/30/lessons/{문제번호}

[문제]
{프로그래머스에서 가져온 문제 설명}

[제한]
{프로그래머스에서 가져온 제한 조건}
"""


def solution():
    pass
```

**testcases.json**
```json
{
  "problem_id": {문제번호},
  "title": "{제목}",
  "testcases": [
    {
      "inputs": [...],
      "expected": ...
    }
  ]
}
```

### 3. 완료 후 안내

- 생성된 파일 경로 출력
- 다음 단계 안내: 문제 풀기 → `/format-solution`으로 정리

## 주의사항

- 이미 폴더가 존재하면 덮어쓰지 않고 경고
- Playwright 브라우저는 작업 완료 후 닫기
