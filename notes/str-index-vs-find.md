# Python index() vs find() 완벽 비교

## 핵심 차이점

| 특성 | `index()` | `find()` |
|------|-----------|----------|
| **찾지 못했을 때** | `ValueError` 발생 | `-1` 반환 |
| **사용 타입** | `str`, `list`, `tuple` | `str`만 |
| **역방향 검색** | `rindex()` | `rfind()` |
| **시간 복잡도** | O(n) | O(n) |

## 기본 사용법

```python
text = "hello world"

# 찾는 경우 - 동일한 결과
text.index("o")  # 4
text.find("o")   # 4

# 못 찾는 경우 - 핵심 차이!
text.index("z")  # ValueError: substring not found
text.find("z")   # -1
```

## 상세 비교

### 1. 문자열에서 사용

```python
s = "banana"

# 첫 번째 위치 찾기
s.index("a")  # 1
s.find("a")   # 1

# 시작 위치 지정 (start)
s.index("a", 2)  # 3 (인덱스 2부터 검색)
s.find("a", 2)   # 3

# 범위 지정 (start, end)
s.index("a", 2, 4)  # 3 (인덱스 2~3 범위에서 검색)
s.find("a", 2, 4)   # 3

# 역방향 검색 (오른쪽에서 왼쪽으로)
s.rindex("a")  # 5 (마지막 'a')
s.rfind("a")   # 5
```

### 2. 리스트/튜플에서 사용

```python
# 리스트 - index()만 사용 가능
nums = [10, 20, 30, 20, 40]
nums.index(20)     # 1 (첫 번째 20의 위치)
nums.index(20, 2)  # 3 (인덱스 2부터 검색)
# nums.find(20)    # AttributeError: 'list' object has no attribute 'find'

# 튜플도 동일
t = (1, 2, 3, 2)
t.index(2)  # 1
# t.find(2) # AttributeError
```

## 언제 무엇을 사용할까?

### index() 사용 - 반드시 존재해야 할 때

```python
# 존재하지 않으면 에러가 나야 하는 경우
def get_extension_position(filename):
    """확장자 점의 위치 반환 (없으면 에러)"""
    return filename.index(".")  # .이 없으면 ValueError

# 안전하게 사용하려면 예외 처리
def safe_index(s, sub):
    try:
        return s.index(sub)
    except ValueError:
        return -1
```

### find() 사용 - 존재 여부가 불확실할 때

```python
# 없을 수도 있는 경우 (권장)
def get_extension_position(filename):
    """확장자 점의 위치 반환 (없으면 -1)"""
    return filename.find(".")

# 조건문과 함께 사용
idx = text.find("target")
if idx != -1:
    # 찾은 경우 처리
    process(text, idx)
else:
    # 못 찾은 경우 처리
    handle_not_found()
```

## 코딩테스트 실전 패턴

### 패턴 1: 특정 문자 위치 찾기 (1-indexed)

```python
# 문제: 숫자에서 특정 숫자의 위치 반환 (1부터 시작, 없으면 -1)

# ❌ 비효율: in 체크 후 find (2번 순회)
def solution_v1(num, k):
    s = str(num)
    if str(k) in s:
        return s.find(str(k)) + 1
    return -1

# ✅ 효율: find 한 번으로 해결
def solution_v2(num, k):
    idx = str(num).find(str(k))
    return idx + 1 if idx != -1 else -1

# ✅ 대안: index + 예외처리
def solution_v3(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1
```

### 패턴 2: 모든 위치 찾기

```python
def find_all_positions(text, sub):
    """부분 문자열의 모든 위치 반환"""
    positions = []
    start = 0
    while True:
        idx = text.find(sub, start)
        if idx == -1:
            break
        positions.append(idx)
        start = idx + 1  # 겹치는 경우도 찾으려면 +1
        # start = idx + len(sub)  # 겹치지 않게 찾으려면
    return positions

# 예시
find_all_positions("ababa", "aba")  # [0, 2] (겹치는 경우 포함)
```

### 패턴 3: 문자열 파싱

```python
# URL에서 도메인 추출
def extract_domain(url):
    # "https://www.example.com/path"
    start = url.find("://")
    if start == -1:
        return None
    start += 3  # "://" 건너뛰기

    end = url.find("/", start)
    if end == -1:
        return url[start:]  # 경로가 없는 경우
    return url[start:end]

extract_domain("https://www.example.com/path")  # "www.example.com"
```

### 패턴 4: 리스트에서 값 찾기

```python
# 리스트는 find()가 없으므로 대안 필요

# 방법 1: index() + 예외처리
def list_find(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return -1

# 방법 2: enumerate 활용
def list_find_v2(lst, value):
    for i, v in enumerate(lst):
        if v == value:
            return i
    return -1

# 방법 3: in + index (2번 순회하므로 비효율)
def list_find_v3(lst, value):
    return lst.index(value) if value in lst else -1
```

## 내부 구현 원리

### CPython 구현 (간략화)

```python
# str.find() 내부 동작 (개념적)
def find(self, sub, start=0, end=None):
    if end is None:
        end = len(self)

    # Boyer-Moore 또는 단순 선형 탐색 사용
    for i in range(start, end - len(sub) + 1):
        if self[i:i+len(sub)] == sub:
            return i
    return -1

# str.index() 내부 동작 (개념적)
def index(self, sub, start=0, end=None):
    result = self.find(sub, start, end)
    if result == -1:
        raise ValueError("substring not found")
    return result
```

**핵심**: `index()`는 내부적으로 `find()`를 호출한 후 결과가 -1이면 예외를 발생시킵니다.

## 성능 비교

```python
import timeit

text = "a" * 10000 + "target" + "a" * 10000

# find() - 약간 더 빠름 (예외 처리 오버헤드 없음)
timeit.timeit(lambda: text.find("target"), number=10000)

# index() - 찾으면 거의 동일, 못 찾으면 예외 처리로 느림
timeit.timeit(lambda: text.index("target"), number=10000)
```

| 상황 | find() | index() |
|------|--------|---------|
| 찾는 경우 | 빠름 | 거의 동일 |
| 못 찾는 경우 | 빠름 (-1 반환) | 느림 (예외 발생) |

## 요약 정리

### 선택 기준
- **존재가 확실** → `index()` (없으면 버그이므로 에러 발생이 적절)
- **존재가 불확실** → `find()` (조건문으로 처리)
- **리스트/튜플** → `index()` + 예외처리 또는 enumerate

### 코딩테스트 팁
1. 문자열 검색은 `find()`가 더 안전하고 간결
2. `in` 체크 후 `find()`는 2번 순회하므로 비효율
3. 리스트는 `find()`가 없으므로 예외처리 필요

## 관련 노트

- [[set-operations]] - 집합에서의 멤버십 테스트
- [[python-slicing]] - 문자열 슬라이싱
- [[str-translate-maketrans]] - 문자열 변환 메서드

---

*관련 문제: #120904 숫자 찾기*
