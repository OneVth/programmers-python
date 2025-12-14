# dict.fromkeys() - 순서 유지 중복 제거

> 삽입 순서를 보장하는 dict의 특성을 활용한 중복 제거 기법

## 기본 사용법

```python
# dict.fromkeys(iterable, value=None)
dict.fromkeys("abc")        # {'a': None, 'b': None, 'c': None}
dict.fromkeys("abc", 0)     # {'a': 0, 'b': 0, 'c': 0}
dict.fromkeys([1, 2, 3])    # {1: None, 2: None, 3: None}
```

---

## 중복 제거 + 순서 유지

```python
# 문자열에서 중복 문자 제거
s = "people"
"".join(dict.fromkeys(s))   # "peol"

# 리스트에서 중복 요소 제거
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
list(dict.fromkeys(nums))   # [3, 1, 4, 5, 9, 2, 6]
```

---

## set()과의 차이

```python
s = "banana"

# set() - 순서 보장 안 됨
set(s)                      # {'b', 'a', 'n'} (순서 불확정)

# dict.fromkeys() - 순서 보장
dict.fromkeys(s)            # {'b': None, 'a': None, 'n': None}
"".join(dict.fromkeys(s))   # "ban" (첫 등장 순서 유지)
```

| 방식 | 순서 유지 | 시간 복잡도 |
|------|----------|------------|
| `set()` | ❌ | O(n) |
| `dict.fromkeys()` | ✅ | O(n) |
| 리스트 + `in` 검사 | ✅ | O(n²) |

---

## 동작 원리

```python
# dict.fromkeys("aba") 내부 동작
{}                  # 시작
{'a': None}         # 'a' 삽입
{'a': None, 'b': None}  # 'b' 삽입
{'a': None, 'b': None}  # 'a' 중복 → 무시 (키가 이미 존재)
```

**핵심**: dict는 중복 키를 허용하지 않으므로, 첫 번째 등장만 남고 이후는 무시됨

---

## 활용 예시

### 1. 문자열 중복 제거

```python
def remove_duplicates(s: str) -> str:
    return "".join(dict.fromkeys(s))

remove_duplicates("programming")  # "progamin"
```

### 2. 리스트 중복 제거 (순서 유지)

```python
def unique_ordered(lst: list) -> list:
    return list(dict.fromkeys(lst))

unique_ordered([5, 3, 5, 2, 3, 1])  # [5, 3, 2, 1]
```

### 3. 첫 등장 인덱스 기록

```python
s = "abracadabra"
first_indices = {c: i for i, c in enumerate(s) if c not in dict.fromkeys(s[:i])}
# 더 간단하게:
{c: s.index(c) for c in dict.fromkeys(s)}  # {'a': 0, 'b': 1, 'r': 2, 'c': 4, 'd': 6}
```

---

## 대안: seen 집합 패턴

```python
def remove_duplicates_v2(s: str) -> str:
    seen = set()
    result = []
    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return "".join(result)
```

| 방식 | 장점 | 단점 |
|------|------|------|
| `dict.fromkeys()` | 한 줄, Pythonic | 덜 직관적 |
| `seen` 집합 | 로직 명확, 범용적 | 코드가 김 |

---

## 주의사항

### unhashable 타입은 불가

```python
# ❌ 리스트는 해시 불가 → dict 키로 사용 불가
dict.fromkeys([[1, 2], [3, 4]])  # TypeError

# ✅ 튜플로 변환
dict.fromkeys([(1, 2), (3, 4)])  # {(1, 2): None, (3, 4): None}
```

### Python 3.7+ 필요

```python
# Python 3.6 이하에서는 순서 보장 안 됨
# 코테 환경(프로그래머스, 백준 등)은 모두 3.7+ → OK
```

---

## 핵심 정리

1. **`dict.fromkeys(iterable)`**: iterable의 요소를 키로 하는 dict 생성
2. **중복 제거 + 순서 유지**: `"".join(dict.fromkeys(s))` 또는 `list(dict.fromkeys(lst))`
3. **O(n) 시간복잡도**: set과 동일, 리스트 `in` 검사(O(n²))보다 효율적
4. **Python 3.7+**: 삽입 순서 보장은 공식 스펙

---

*관련 노트: [dict-insertion-order.md](dict-insertion-order.md)*
*관련 문제: #120888 중복된 문자 제거*
