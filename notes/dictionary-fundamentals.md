# Python Dictionary 완벽 가이드

딕셔너리는 코딩 테스트에서 가장 자주 사용되는 자료구조 중 하나입니다.
해시 테이블 기반으로 O(1) 조회/삽입/삭제가 가능합니다.

## 1. 기본 개념

### 딕셔너리란?
- **Key-Value 쌍**으로 데이터를 저장하는 자료구조
- Key는 **고유**해야 함 (중복 불가)
- Key는 **불변(immutable)** 타입만 가능 (str, int, tuple 등)

```python
# 생성 방법
dic = {}                          # 빈 딕셔너리
dic = dict()                      # 빈 딕셔너리
dic = {"a": 1, "b": 2}            # 초기값과 함께 생성
dic = dict(a=1, b=2)              # 키워드 인자로 생성
dic = dict([("a", 1), ("b", 2)])  # 리스트로 생성 ⭐
```

## 2. 핵심 메서드

### 2.1 값 조회: `get()` vs `[]`

```python
dic = {"apple": 3, "banana": 5}

# [] 접근 - 키가 없으면 KeyError 발생!
dic["apple"]   # 3
dic["grape"]   # ❌ KeyError: 'grape'

# get() 접근 - 키가 없으면 None 또는 기본값 반환
dic.get("apple")        # 3
dic.get("grape")        # None (에러 없음)
dic.get("grape", 0)     # 0 (기본값 지정) ⭐
```

**🎯 코딩 테스트 팁:** 빈도수 카운팅할 때 `get(key, 0)` 필수!
```python
# ❌ 번거로운 방식
if c not in dic:
    dic[c] = 0
dic[c] += 1

# ✅ get() 활용
dic[c] = dic.get(c, 0) + 1
```

### 2.2 키/값 존재 확인

```python
dic = {"apple": 3, "banana": 5}

# 키 존재 확인
"apple" in dic           # True
"grape" in dic           # False
"apple" in dic.keys()    # True (동일하지만 불필요)

# 값 존재 확인
3 in dic.values()        # True
10 in dic.values()       # False
```

**🎯 주의:** `in dic`과 `in dic.keys()`는 동일하므로 간결하게 `in dic` 사용

### 2.3 키/값/아이템 순회

```python
dic = {"apple": 3, "banana": 5}

# 키만 순회
for key in dic:
    print(key)  # "apple", "banana"

# 값만 순회
for value in dic.values():
    print(value)  # 3, 5

# 키-값 함께 순회 ⭐
for key, value in dic.items():
    print(f"{key}: {value}")
```

### 2.4 삭제 메서드

```python
dic = {"a": 1, "b": 2, "c": 3}

# pop() - 키로 삭제하고 값 반환
val = dic.pop("a")       # val = 1, dic = {"b": 2, "c": 3}
val = dic.pop("z", -1)   # val = -1 (기본값), 에러 없음

# del - 키로 삭제
del dic["b"]             # dic = {"c": 3}

# clear() - 전체 삭제
dic.clear()              # dic = {}
```

### 2.5 기본값 설정: `setdefault()`

```python
dic = {"a": 1}

# 키가 없으면 기본값 설정하고 반환
dic.setdefault("b", 2)   # dic = {"a": 1, "b": 2}, 반환: 2
dic.setdefault("a", 99)  # dic 변경 없음 (이미 존재), 반환: 1
```

**🎯 활용:** 그룹핑할 때 유용
```python
# 첫 글자별로 단어 그룹핑
words = ["apple", "ant", "banana", "bear"]
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
# {'a': ['apple', 'ant'], 'b': ['banana', 'bear']}
```

## 3. 딕셔너리 변환 패턴 ⭐

### 3.1 2차원 배열 → 딕셔너리

```python
# [["key", "value"], ...] 형태의 2차원 배열
db = [["id1", "pw1"], ["id2", "pw2"], ["id3", "pw3"]]

# dict()로 한 번에 변환! ⭐
dic = dict(db)
# {"id1": "pw1", "id2": "pw2", "id3": "pw3"}

# 활용: 로그인 검증 (120883번 문제)
def check_login(id_pw, db):
    db_dict = dict(db)
    if id_pw[0] not in db_dict:
        return "fail"
    return "login" if db_dict[id_pw[0]] == id_pw[1] else "wrong pw"
```

### 3.2 리스트 → 빈도수 딕셔너리

```python
items = ["a", "b", "a", "c", "a", "b"]

# 방법 1: 수동 카운팅
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1
# {"a": 3, "b": 2, "c": 1}

# 방법 2: Counter 사용 (권장)
from collections import Counter
freq = Counter(items)
# Counter({"a": 3, "b": 2, "c": 1})
```

### 3.3 두 리스트 → 딕셔너리 (zip)

```python
keys = ["name", "age", "city"]
values = ["Alice", 25, "Seoul"]

dic = dict(zip(keys, values))
# {"name": "Alice", "age": 25, "city": "Seoul"}
```

## 4. 딕셔너리 비교 ⭐

### 4.1 `==` 연산자

```python
dic1 = {"a": 1, "b": 2}
dic2 = {"b": 2, "a": 1}  # 순서 다름
dic3 = {"a": 1, "b": 3}  # 값 다름

dic1 == dic2  # True  (순서 무관, 키-값 쌍이 모두 같으면 True)
dic1 == dic3  # False (값이 다름)
```

**🎯 비교 원리:**
1. 두 딕셔너리의 키 집합이 같은지 확인
2. 각 키에 대해 값이 같은지 확인
3. 모두 같으면 True

### 4.2 애너그램 판별 (120886번 문제)

```python
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

is_anagram("listen", "silent")  # True
is_anagram("hello", "world")    # False
```

## 5. 자주 쓰는 패턴 템플릿

### 5.1 빈도수 카운팅

```python
def count_frequency(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq
```

### 5.2 그룹핑

```python
def group_by(items, key_func):
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

# 사용 예: 길이별 그룹핑
words = ["a", "bb", "ccc", "dd", "e"]
group_by(words, len)  # {1: ["a", "e"], 2: ["bb", "dd"], 3: ["ccc"]}
```

### 5.3 인덱스 매핑

```python
def create_index_map(items):
    """각 아이템의 첫 등장 인덱스 저장"""
    index_map = {}
    for i, item in enumerate(items):
        if item not in index_map:
            index_map[item] = i
    return index_map

# 사용 예: 등수 매기기 (120882번 문제)
scores = [90, 85, 90, 80]
sorted_scores = sorted(scores, reverse=True)  # [90, 90, 85, 80]
rank_map = create_index_map(sorted_scores)    # {90: 0, 85: 2, 80: 3}
ranks = [rank_map[s] + 1 for s in scores]     # [1, 3, 1, 4]
```

### 5.4 Two Sum 패턴

```python
def two_sum(nums, target):
    """target을 만드는 두 수의 인덱스 반환"""
    seen = {}  # 값 → 인덱스 매핑
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

## 6. 관련 collections 모듈

### 6.1 Counter

```python
from collections import Counter

c = Counter("hello")      # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
c.most_common(2)          # [('l', 2), ('h', 1)] - 빈도 상위 2개
c["l"]                    # 2
c["z"]                    # 0 (없는 키도 에러 없이 0 반환!)
```

### 6.2 defaultdict

```python
from collections import defaultdict

# 기본값이 자동 설정되는 딕셔너리
dd = defaultdict(int)     # 기본값 0
dd["a"] += 1              # {"a": 1} - KeyError 없음!

dd = defaultdict(list)    # 기본값 []
dd["fruits"].append("apple")  # {"fruits": ["apple"]}
```

## 7. 시간복잡도 정리

| 연산 | 시간복잡도 | 비고 |
|------|:----------:|------|
| `dic[key]` | O(1) | 조회 |
| `dic[key] = value` | O(1) | 삽입/수정 |
| `del dic[key]` | O(1) | 삭제 |
| `key in dic` | O(1) | 존재 확인 |
| `dic.get(key)` | O(1) | 안전한 조회 |
| `len(dic)` | O(1) | 크기 |
| `dic.keys()` | O(1) | 뷰 반환 |
| `for k in dic` | O(N) | 순회 |
| `dic1 == dic2` | O(N) | 비교 |

## 8. 흔한 실수와 해결

### 실수 1: KeyError
```python
# ❌ 없는 키 직접 접근
value = dic["없는키"]  # KeyError!

# ✅ get() 사용
value = dic.get("없는키", 기본값)
```

### 실수 2: 순회 중 수정
```python
# ❌ 순회하면서 삭제
for key in dic:
    if some_condition:
        del dic[key]  # RuntimeError!

# ✅ 복사본으로 순회
for key in list(dic.keys()):
    if some_condition:
        del dic[key]
```

### 실수 3: 빈도수 카운팅에서 count() 남용
```python
# ❌ O(N²) - 매번 전체 순회
for c in string:
    dic[c] = string.count(c)

# ✅ O(N) - 누적 카운팅
for c in string:
    dic[c] = dic.get(c, 0) + 1
```

---

## 핵심 요약

1. **조회는 `get(key, default)`** - KeyError 방지
2. **존재 확인은 `key in dic`** - `.keys()` 불필요
3. **2차원 배열 변환은 `dict(list)`** - 한 줄로 끝
4. **딕셔너리 비교는 `==`** - 순서 무관, 키-값 쌍 비교
5. **빈도수는 `Counter` 또는 `get(k, 0) + 1`** - count() 반복 금지
