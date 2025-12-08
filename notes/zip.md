# zip 함수

## 개요

`zip`은 **여러 iterable을 병렬로 묶어주는** Python 내장 함수입니다.

```python
zip(iterable1, iterable2, ...)
```

각 iterable에서 같은 위치의 요소들을 튜플로 묶어 반환합니다.

---

## 기본 사용법

### 두 리스트 묶기

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

list(zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

**시각화:**
```
names:  ['Alice',  'Bob',  'Charlie']
           ↓        ↓         ↓
ages:   [  25,      30,       35   ]
           ↓        ↓         ↓
result: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

### 세 개 이상도 가능

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [True, False, True]

list(zip(a, b, c))
# [(1, 'a', True), (2, 'b', False), (3, 'c', True)]
```

---

## 주요 특징

### 1. Lazy Evaluation (지연 평가)

`zip`은 iterator를 반환하므로, `list()`로 감싸야 리스트로 볼 수 있습니다.

```python
z = zip([1, 2], [3, 4])
print(z)        # <zip object at 0x...>
print(list(z))  # [(1, 3), (2, 4)]
```

### 2. 가장 짧은 iterable 기준

길이가 다르면 **가장 짧은 것에 맞춰** 잘립니다.

```python
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']

list(zip(a, b))
# [(1, 'a'), (2, 'b'), (3, 'c')]  # 4, 5는 버려짐
```

### 3. 빈 iterable이 있으면 빈 결과

```python
list(zip([1, 2, 3], []))
# []
```

---

## 자주 사용하는 패턴

### 패턴 1: 병렬 순회

```python
names = ['Alice', 'Bob']
scores = [95, 87]

for name, score in zip(names, scores):
    print(f"{name}: {score}점")
# Alice: 95점
# Bob: 87점
```

### 패턴 2: 딕셔너리 생성

```python
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Seoul']

dict(zip(keys, values))
# {'name': 'Alice', 'age': 25, 'city': 'Seoul'}
```

### 패턴 3: 인덱스와 함께 (enumerate + zip)

```python
names = ['Alice', 'Bob']
scores = [95, 87]

for i, (name, score) in enumerate(zip(names, scores)):
    print(f"{i+1}. {name}: {score}점")
# 1. Alice: 95점
# 2. Bob: 87점
```

### 패턴 4: 두 리스트 비교

```python
old = [1, 2, 3]
new = [1, 5, 3]

for o, n in zip(old, new):
    if o != n:
        print(f"변경: {o} → {n}")
# 변경: 2 → 5
```

---

## zip(*)로 언패킹 (전치, Transpose)

`*` 연산자와 함께 사용하면 **묶인 것을 다시 풀 수 있습니다**.

### 기본 언패킹

```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# *pairs는 개별 튜플로 풀어줌
nums, chars = zip(*pairs)
# nums = (1, 2, 3)
# chars = ('a', 'b', 'c')
```

### 행렬 전치 (Transpose)

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# 행과 열을 뒤집기
transposed = list(zip(*matrix))
# [(1, 4), (2, 5), (3, 6)]

# 시각화:
# 원본:          전치 후:
# 1  2  3        1  4
# 4  5  6   →    2  5
#                3  6
```

### 좌표 분리 (코딩테스트 필수!)

```python
points = [[1, 10], [2, 20], [3, 30]]

xs, ys = zip(*points)
# xs = (1, 2, 3)      # x좌표들
# ys = (10, 20, 30)   # y좌표들

# 활용: x, y 범위 구하기
x_range = max(xs) - min(xs)  # 2
y_range = max(ys) - min(ys)  # 20
```

---

## 코딩테스트 활용 예시

### 1. 직사각형 넓이 (좌표 분리)

```python
def solution(dots):
    xs, ys = zip(*dots)
    return (max(xs) - min(xs)) * (max(ys) - min(ys))
```

### 2. 두 배열 요소별 연산

```python
def add_arrays(a, b):
    return [x + y for x, y in zip(a, b)]

add_arrays([1, 2, 3], [10, 20, 30])
# [11, 22, 33]
```

### 3. 점수 순위 매기기

```python
scores = [85, 92, 78, 92, 88]
sorted_unique = sorted(set(scores), reverse=True)
rank_map = {score: i+1 for i, score in enumerate(sorted_unique)}
ranks = [rank_map[s] for s in scores]
# [3, 1, 4, 1, 2]
```

### 4. 문자열 비교 (같은 위치 문자)

```python
def count_same_position(s1, s2):
    return sum(c1 == c2 for c1, c2 in zip(s1, s2))

count_same_position("hello", "hallo")
# 4 ('h', 'l', 'l', 'o' 일치)
```

### 5. 연속 요소 쌍 만들기

```python
nums = [1, 2, 3, 4, 5]

# 현재와 다음 요소 쌍
pairs = list(zip(nums, nums[1:]))
# [(1, 2), (2, 3), (3, 4), (4, 5)]

# 활용: 차이 계산
diffs = [b - a for a, b in zip(nums, nums[1:])]
# [1, 1, 1, 1]
```

---

## itertools.zip_longest

길이가 다를 때 **긴 것에 맞추고** 싶다면:

```python
from itertools import zip_longest

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']

list(zip_longest(a, b, fillvalue='?'))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, '?'), (5, '?')]
```

---

## 요약

```python
# 기본: 병렬로 묶기
zip([1,2], ['a','b'])  →  [(1,'a'), (2,'b')]

# 순회
for a, b in zip(list1, list2):

# 딕셔너리
dict(zip(keys, values))

# 언패킹 (전치)
xs, ys = zip(*points)  # 좌표 분리

# 연속 쌍
zip(nums, nums[1:])  # 현재-다음 쌍

# 주의: 짧은 쪽 기준, 긴 쪽 필요시 zip_longest
```
