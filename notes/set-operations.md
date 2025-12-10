# Python Set 완벽 가이드

## 개념

**Set(집합)**은 **중복 없는 요소들의 모음**으로, 해시 테이블 기반의 자료구조입니다.

```python
# 생성 방법
s = {1, 2, 3}           # 리터럴 (빈 set은 불가: {}는 dict)
s = set([1, 2, 2, 3])   # 리스트에서 생성 → {1, 2, 3}
s = set("hello")        # 문자열에서 → {'h', 'e', 'l', 'o'}
s = set()               # 빈 set
```

## 시간 복잡도

| 연산 | 시간 복잡도 | 설명 |
|------|-------------|------|
| `x in s` | **O(1)** | 멤버십 테스트 (리스트는 O(n)) |
| `s.add(x)` | O(1) | 요소 추가 |
| `s.remove(x)` | O(1) | 요소 제거 (없으면 KeyError) |
| `s.discard(x)` | O(1) | 요소 제거 (없어도 에러 없음) |
| `len(s)` | O(1) | 크기 |
| `s \| t` (합집합) | O(len(s) + len(t)) | |
| `s & t` (교집합) | O(min(len(s), len(t))) | |
| `s - t` (차집합) | O(len(s)) | |

## 핵심 패턴

### 1. 중복 제거

```python
# 리스트에서 중복 제거
nums = [1, 2, 2, 3, 3, 3]
unique = list(set(nums))  # [1, 2, 3] (순서 보장 안됨)

# 순서 유지하며 중복 제거 (Python 3.7+)
unique_ordered = list(dict.fromkeys(nums))  # [1, 2, 2, 3] → [1, 2, 3]
```

### 2. 빠른 멤버십 테스트

```python
# ❌ 느림: O(n) 매번 검색
forbidden = [1, 2, 3, 4, 5]
for x in data:
    if x in forbidden:  # O(n)
        pass

# ✅ 빠름: O(1) 검색
forbidden = {1, 2, 3, 4, 5}  # set으로 변환
for x in data:
    if x in forbidden:  # O(1)
        pass
```

### 3. 집합 연산

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 합집합 (Union)
a | b           # {1, 2, 3, 4, 5, 6}
a.union(b)      # 동일

# 교집합 (Intersection)
a & b           # {3, 4}
a.intersection(b)

# 차집합 (Difference)
a - b           # {1, 2} (a에만 있는 것)
a.difference(b)

# 대칭차집합 (Symmetric Difference)
a ^ b           # {1, 2, 5, 6} (한쪽에만 있는 것)
a.symmetric_difference(b)

# 부분집합/상위집합 확인
{1, 2} <= {1, 2, 3}  # True (부분집합)
{1, 2, 3} >= {1, 2}  # True (상위집합)
{1, 2}.issubset({1, 2, 3})
{1, 2, 3}.issuperset({1, 2})
```

### 4. 좌표/위치 추적 (2D 그리드)

```python
# 안전지대 문제에서 사용한 패턴
danger = set()
for i, row in enumerate(board):
    for j, x in enumerate(row):
        if x == 1:  # 지뢰 발견
            # 자신 + 8방향 좌표를 한 번에 추가
            danger.update(
                (i + di, j + dj)
                for di in [-1, 0, 1]
                for dj in [-1, 0, 1]
            )

# 경계 내 위험 좌표만 카운트
valid_danger = sum(0 <= i < n and 0 <= j < n for i, j in danger)
safe_count = n * n - valid_danger
```

### 5. 방문 체크 (BFS/DFS)

```python
def bfs(start, graph):
    visited = {start}  # set으로 방문 체크
    queue = [start]

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:  # O(1) 체크
                visited.add(neighbor)
                queue.append(neighbor)

    return visited
```

### 6. 두 리스트 비교

```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# 공통 요소
common = set(list1) & set(list2)  # {4, 5}

# list1에만 있는 요소
only_in_1 = set(list1) - set(list2)  # {1, 2, 3}

# 두 리스트가 같은 요소를 가지는지 (순서 무관)
set(list1) == set(list2)  # False
```

### 7. 문자열 공통 문자

```python
s1 = "hello"
s2 = "world"

# 공통 문자
common_chars = set(s1) & set(s2)  # {'l', 'o'}

# 모든 모음 포함 확인
vowels = set("aeiou")
text = "education"
has_all_vowels = vowels <= set(text)  # True
```

## set 메서드 정리

### 추가/제거

```python
s = {1, 2, 3}

s.add(4)           # {1, 2, 3, 4} - 단일 요소 추가
s.update([5, 6])   # {1, 2, 3, 4, 5, 6} - 여러 요소 추가
s.update({7}, [8]) # 여러 iterable 한 번에 추가 가능

s.remove(1)        # {2, 3, 4, 5, 6, 7, 8} - 없으면 KeyError
s.discard(100)     # 에러 없음 - 없어도 무시
s.pop()            # 임의의 요소 제거 및 반환
s.clear()          # 모든 요소 제거
```

### in-place 연산

```python
a = {1, 2, 3}
b = {3, 4, 5}

a |= b   # a.update(b)와 동일 - a = {1, 2, 3, 4, 5}
a &= b   # a.intersection_update(b)
a -= b   # a.difference_update(b)
a ^= b   # a.symmetric_difference_update(b)
```

## frozenset (불변 set)

```python
# dict의 key나 다른 set의 요소로 사용 가능
fs = frozenset([1, 2, 3])

# set의 set (일반 set은 불가능)
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}

# dict의 key로 사용
cache = {frozenset([1, 2]): "result"}
```

## 코딩테스트 실전 패턴

### 패턴 1: 유일한 값 개수

```python
# 배열에서 유일한 값의 개수
def count_unique(arr):
    return len(set(arr))
```

### 패턴 2: 중복 존재 여부

```python
# 중복이 있는지 확인
def has_duplicates(arr):
    return len(arr) != len(set(arr))
```

### 패턴 3: 누락된 숫자 찾기

```python
# 1~n 중 누락된 숫자들
def find_missing(arr, n):
    return set(range(1, n+1)) - set(arr)
```

### 패턴 4: 애너그램 확인

```python
# 같은 문자 구성인지 (빈도까지 확인하려면 Counter 사용)
def is_anagram_chars(s1, s2):
    return set(s1) == set(s2)  # 문자 종류만 비교
```

### 패턴 5: 연속 수열 길이

```python
# 가장 긴 연속 수열 (LeetCode 128)
def longest_consecutive(nums):
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        # 시퀀스 시작점에서만 카운트 (최적화)
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            max_len = max(max_len, length)

    return max_len
```

## 주의사항

1. **순서 보장 안됨**: Python 3.7+에서도 set은 순서를 보장하지 않음
2. **해시 가능한 요소만**: list, dict, set은 요소로 불가 (frozenset은 가능)
3. **빈 set 생성**: `{}` 아님! → `set()` 사용

```python
empty = {}      # ❌ 이건 빈 dict
empty = set()   # ✅ 빈 set

# 해시 불가능한 타입
{[1, 2]}        # ❌ TypeError: unhashable type: 'list'
{{1, 2}}        # ❌ TypeError: unhashable type: 'set'
{frozenset([1, 2])}  # ✅ OK
```

## 관련 노트

- [[collections-counter]] - 요소별 개수가 필요할 때
- [[dict-insertion-order]] - 순서 유지 자료구조
- [[time-complexity-guide]] - 시간 복잡도 비교
