# collections.Counter 가이드

> 요소의 개수를 세는 딕셔너리 서브클래스

## 기본 정보

```python
from collections import Counter
```

- **모듈**: `collections` (표준 라이브러리, 설치 불필요)
- **타입**: `dict`의 서브클래스
- **용도**: 해시 가능한 객체의 개수를 셀 때

---

## 기본 사용법

### 생성

```python
# 리스트에서 생성
Counter([1, 2, 2, 3, 3, 3])
# Counter({3: 3, 2: 2, 1: 1})

# 문자열에서 생성
Counter("hello")
# Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# 딕셔너리에서 생성
Counter({'a': 4, 'b': 2})

# 키워드 인자로 생성
Counter(a=4, b=2)
```

### 개수 접근

```python
c = Counter([1, 2, 2, 3, 3, 3])

c[3]      # 3 (3이 3번 등장)
c[999]    # 0 (없는 키는 KeyError 대신 0 반환!)
```

---

## 주요 메서드

### most_common(n)

가장 흔한 n개 요소를 `(요소, 개수)` 튜플 리스트로 반환

```python
c = Counter("abracadabra")
c.most_common(3)
# [('a', 5), ('b', 2), ('r', 2)]

c.most_common()  # 전체를 빈도순으로
```

### elements()

개수만큼 요소를 반복하는 이터레이터

```python
c = Counter(a=3, b=1)
list(c.elements())
# ['a', 'a', 'a', 'b']
```

### update() / subtract()

```python
c = Counter(a=3, b=1)
c.update({'a': 1, 'c': 2})  # 더하기
# Counter({'a': 4, 'c': 2, 'b': 1})

c.subtract({'a': 2})  # 빼기
# Counter({'a': 2, 'c': 2, 'b': 1})
```

---

## 연산자 지원

```python
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

c1 + c2  # Counter({'a': 4, 'b': 3})  합집합
c1 - c2  # Counter({'a': 2})          차집합 (음수는 제거)
c1 & c2  # Counter({'a': 1, 'b': 1})  교집합 (min)
c1 | c2  # Counter({'a': 3, 'b': 2})  합집합 (max)
```

---

## 코딩 테스트 활용 패턴

### 1. 최빈값 구하기

```python
def get_mode(arr):
    return Counter(arr).most_common(1)[0][0]
```

### 2. 빈도수 비교 (애너그램 판별)

```python
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

is_anagram("listen", "silent")  # True
```

### 3. 특정 개수 이상인 요소 필터링

```python
c = Counter([1, 1, 1, 2, 2, 3])
[x for x, count in c.items() if count >= 2]
# [1, 2]
```

### 4. 문자열에서 문자 빈도

```python
Counter("hello world")
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

### 5. 두 리스트의 공통 요소 개수

```python
c1 = Counter([1, 1, 2, 3])
c2 = Counter([1, 2, 2, 4])
(c1 & c2).total()  # 2 (Python 3.10+)
sum((c1 & c2).values())  # 2 (이전 버전)
```

---

## 시간복잡도

| 연산 | 복잡도 |
|------|--------|
| 생성 `Counter(iterable)` | O(n) |
| 접근 `c[key]` | O(1) |
| `most_common(k)` | O(n log k) |
| `update()` | O(n) |
| `+`, `-`, `&`, `\|` | O(n) |

---

## 주의사항

1. **없는 키는 0 반환**: `KeyError`가 아닌 `0` 반환
   ```python
   c = Counter()
   c['없는키']  # 0 (에러 아님!)
   ```

2. **음수 개수 허용**: 연산 결과 음수가 될 수 있음
   ```python
   c = Counter(a=1)
   c.subtract({'a': 5})
   c['a']  # -4
   ```

3. **`most_common()` 반환 형태**: `[(요소, 개수), ...]`
   ```python
   mc = Counter([1,1,2]).most_common(1)
   mc[0][0]  # 1 (요소)
   mc[0][1]  # 2 (개수) ← 혼동 주의!
   ```

---

## dict와의 차이점

| 특징 | dict | Counter |
|------|------|---------|
| 없는 키 접근 | KeyError | 0 반환 |
| `most_common()` | ❌ | ✅ |
| `elements()` | ❌ | ✅ |
| 산술 연산 (`+`, `-`) | ❌ | ✅ |
| 용도 | 범용 | 빈도 계산 특화 |

---

*관련 문제: #120812 최빈값 구하기*
