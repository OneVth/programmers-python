# 다중 키 정렬 (Multi-Key Sorting)

Python `sorted()`와 `list.sort()`에서 **여러 기준**으로 정렬하는 방법.

## 핵심 개념: 튜플 비교

Python에서 튜플은 **사전순(lexicographic)** 비교됩니다:

```python
(1, 5) < (1, 10)  # True  (첫 번째 같으면 두 번째 비교)
(1, 5) < (2, 1)   # True  (첫 번째가 다르면 첫 번째로 결정)
(2, 5) < (1, 10)  # False (2 > 1)
```

이 특성을 `key` 함수에 활용하면 다중 기준 정렬이 가능합니다.

## 기본 문법

```python
# key에 튜플을 반환하는 함수 전달
sorted(data, key=lambda x: (기준1, 기준2, 기준3, ...))

# 각 기준은 순서대로 우선순위
# 기준1로 정렬 → 같으면 기준2로 → 같으면 기준3으로 ...
```

## 실전 예제

### 예제 1: 학생 성적 정렬

```python
students = [
    ("Alice", 85, 22),
    ("Bob", 90, 20),
    ("Charlie", 85, 21),
    ("David", 90, 20),
]

# 성적 내림차순 → 나이 오름차순 → 이름 오름차순
sorted(students, key=lambda x: (-x[1], x[2], x[0]))
# [('Bob', 90, 20), ('David', 90, 20), ('Charlie', 85, 21), ('Alice', 85, 22)]
```

### 예제 2: 좌표 정렬

```python
points = [(3, 5), (1, 2), (3, 1), (1, 5)]

# x 오름차순 → y 내림차순
sorted(points, key=lambda p: (p[0], -p[1]))
# [(1, 5), (1, 2), (3, 5), (3, 1)]
```

### 예제 3: 특이한 정렬 (문제 120880)

```python
def solution(numlist, n):
    # n과의 거리 오름차순 → 값 내림차순
    return sorted(numlist, key=lambda x: (abs(x - n), -x))

# n=4, numlist=[1,2,3,4,5,6]
# 각 원소의 키 값:
# 1: (3, -1)   4: (0, -4)
# 2: (2, -2)   5: (1, -5)
# 3: (1, -3)   6: (2, -6)
#
# 정렬 결과: [4, 5, 3, 6, 2, 1]
```

## 정렬 방향 제어

### 숫자: 부호 반전

```python
nums = [3, 1, 4, 1, 5]

sorted(nums)                    # [1, 1, 3, 4, 5] 오름차순
sorted(nums, key=lambda x: -x)  # [5, 4, 3, 1, 1] 내림차순
```

### 문자열: 부호 반전 불가 → reverse 또는 다른 방법

```python
words = ["apple", "banana", "cherry"]

# 방법 1: reverse=True (단일 키일 때)
sorted(words, reverse=True)  # ['cherry', 'banana', 'apple']

# 방법 2: 다중 키에서 문자열 내림차순이 필요하면?
# → 별도 정렬 후 결합 또는 클래스 활용
```

### 다중 키에서 일부만 역순

```python
data = [("a", 3), ("b", 1), ("a", 1)]

# 첫 번째 오름차순, 두 번째 내림차순
sorted(data, key=lambda x: (x[0], -x[1]))
# [('a', 3), ('a', 1), ('b', 1)]
```

## 문자열 역순 정렬 트릭

문자열에는 `-`를 붙일 수 없으므로 다른 방법 필요:

### 방법 1: 두 번 정렬 (안정 정렬 활용)

```python
data = [("apple", 3), ("banana", 1), ("apple", 2)]

# Python sort는 안정 정렬(stable sort)
# → 같은 키 값이면 원래 순서 유지

# 1. 먼저 보조 기준(문자열)으로 내림차순 정렬
temp = sorted(data, key=lambda x: x[0], reverse=True)
# 2. 그 다음 주 기준(숫자)으로 오름차순 정렬
result = sorted(temp, key=lambda x: x[1])
```

### 방법 2: functools.cmp_to_key

```python
from functools import cmp_to_key

def compare(a, b):
    # 숫자 오름차순
    if a[1] != b[1]:
        return a[1] - b[1]
    # 문자열 내림차순
    if a[0] > b[0]:
        return -1
    elif a[0] < b[0]:
        return 1
    return 0

sorted(data, key=cmp_to_key(compare))
```

### 방법 3: 클래스로 비교 연산 정의

```python
class ReverseStr:
    def __init__(self, s):
        self.s = s
    def __lt__(self, other):
        return self.s > other.s  # 역순

data = [("apple", 3), ("banana", 1), ("cherry", 1)]
sorted(data, key=lambda x: (x[1], ReverseStr(x[0])))
# [('cherry', 1), ('banana', 1), ('apple', 3)]
```

## 자주 쓰는 패턴

### 패턴 1: 절대값 기준 정렬

```python
nums = [-5, 2, -1, 4, -3]
sorted(nums, key=abs)  # [-1, 2, -3, 4, -5]
```

### 패턴 2: 거리 기준 정렬 (특정 점에서)

```python
target = 3
nums = [1, 5, 2, 4, 6]
sorted(nums, key=lambda x: abs(x - target))  # [2, 4, 1, 5, 6]
```

### 패턴 3: 문자열 길이 → 사전순

```python
words = ["ab", "a", "abc", "b"]
sorted(words, key=lambda w: (len(w), w))
# ['a', 'b', 'ab', 'abc']
```

### 패턴 4: None 값 처리 (끝으로 보내기)

```python
data = [3, None, 1, None, 2]
sorted(data, key=lambda x: (x is None, x or 0))
# [1, 2, 3, None, None]

# x is None → True(1) / False(0)
# None은 1로 계산되어 뒤로 감
```

### 패턴 5: 딕셔너리 정렬

```python
scores = {"Alice": 85, "Bob": 90, "Charlie": 85}

# 값 내림차순 → 키 오름차순
sorted(scores.items(), key=lambda x: (-x[1], x[0]))
# [('Bob', 90), ('Alice', 85), ('Charlie', 85)]
```

## operator.itemgetter 활용

```python
from operator import itemgetter

data = [("a", 3, 1), ("b", 1, 2), ("c", 3, 0)]

# 인덱스 1 기준 정렬
sorted(data, key=itemgetter(1))
# [('b', 1, 2), ('a', 3, 1), ('c', 3, 0)]

# 인덱스 1, 2 다중 기준
sorted(data, key=itemgetter(1, 2))
# [('b', 1, 2), ('c', 3, 0), ('a', 3, 1)]
```

**장점**: lambda보다 약간 빠름, 가독성 좋음
**단점**: 역순 정렬이나 변환 적용 불가

## 요약: key 함수 작성 패턴

| 요구사항 | key 함수 |
|----------|----------|
| 오름차순 | `lambda x: x` |
| 내림차순 (숫자) | `lambda x: -x` |
| 내림차순 (전체) | `reverse=True` |
| 다중 기준 | `lambda x: (기준1, 기준2)` |
| 절대값 기준 | `lambda x: abs(x)` |
| 거리 기준 | `lambda x: abs(x - target)` |
| 길이 → 값 | `lambda x: (len(x), x)` |
| 값 → 역순키 | `lambda x: (x[0], -x[1])` |

```
기억법:
- 튜플 = 우선순위 순서
- 숫자 역순 = 마이너스
- 문자열 역순 = 별도 처리 필요
```
