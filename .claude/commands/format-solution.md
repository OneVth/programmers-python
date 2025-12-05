# Solution Formatter

문제 풀이 후 solution.py 코드를 정리합니다.

## 대상 경로
$ARGUMENTS

## 작업 내용

### 1. 코드 분석

solution.py 파일을 읽고 사용자가 작성한 솔루션들을 분석합니다.

### 2. 코드 정리

**타입 힌트 추가**
```python
# Before
def solution(numbers):

# After
def solution_v1(numbers: list[int]) -> float:
```

**각 솔루션에 docstring 추가**
```python
def solution_v1(numbers: list[int]) -> float:
    """
    [Approach] {접근 방식 분석}
    [Time] O(?)  [Space] O(?)
    """
```

**solution alias 확인**
```python
# ✅ 기본 솔루션 지정 (runner.py와 호환)
solution = solution_v1
```

### 3. 하지 않는 일

- ❌ 모듈 docstring 수정 (이미 `/new-problem`에서 완성됨)
- ❌ testcases.json 수정
- ❌ 문제 설명/제한 조건 변경

## 체크리스트

- [ ] 모든 함수에 타입 힌트 적용
- [ ] 각 솔루션의 [Approach], [Time], [Space] 분석
- [ ] solution alias 설정 확인
- [ ] runner.py로 테스트 실행하여 검증
