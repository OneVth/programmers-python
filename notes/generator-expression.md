# 제너레이터 표현식과 Space O(1)

## 리스트 컴프리헨션 vs 제너레이터 표현식

```python
# 리스트 컴프리헨션 - 대괄호 []
[x for x in range(1000000)]   # Space O(n) - 100만개 메모리에 저장

# 제너레이터 표현식 - 소괄호 ()
(x for x in range(1000000))   # Space O(1) - 하나씩 생성
```

---

## 왜 Space O(1)인가?

### 리스트 컴프리헨션의 동작

```python
numbers = [int(c) for c in "12345"]
# 1. 메모리에 리스트 공간 할당
# 2. 모든 요소를 한번에 생성하여 저장
# 3. [1, 2, 3, 4, 5] 전체가 메모리에 존재
# → Space O(n)
```

### 제너레이터 표현식의 동작

```python
numbers = (int(c) for c in "12345")
# 1. 제너레이터 객체만 생성 (아직 값은 없음)
# 2. next() 호출될 때마다 하나씩 계산
# 3. 이전 값은 버리고 현재 값만 메모리에 존재
# → Space O(1)
```

---

## Lazy Evaluation (지연 평가)

제너레이터는 **값이 필요할 때만** 계산합니다.

```python
gen = (x**2 for x in range(1000000))
# 이 시점에서는 아무것도 계산하지 않음!

next(gen)  # 0 - 첫 번째 값만 계산
next(gen)  # 1 - 두 번째 값만 계산
next(gen)  # 4 - 세 번째 값만 계산
```

### 메모리 비교

```python
import sys

# 리스트: n개 요소 전체 저장
lst = [x for x in range(1000)]
sys.getsizeof(lst)  # 약 8,856 bytes

# 제너레이터: 객체 크기만 (요소 개수와 무관!)
gen = (x for x in range(1000))
sys.getsizeof(gen)  # 약 200 bytes (고정)

gen = (x for x in range(1000000))
sys.getsizeof(gen)  # 여전히 약 200 bytes!
```

---

## sum()과 제너레이터

```python
# ❌ 비효율적 - 리스트 먼저 생성
sum([int(c) for c in "12345"])
# 1. [1, 2, 3, 4, 5] 리스트 생성 (O(n) 공간)
# 2. sum()이 리스트 순회하며 합산
# 3. 결과: 15

# ✅ 효율적 - 제너레이터 직접 전달
sum(int(c) for c in "12345")
# 1. 제너레이터 객체 생성 (O(1) 공간)
# 2. sum()이 하나씩 꺼내며 합산
# 3. 결과: 15
```

### 동작 과정 시각화

```
sum(int(c) for c in "12345")

Step 1: gen 생성 (메모리: 제너레이터 객체만)
Step 2: next(gen) → 1, total = 1   (메모리: 1만 존재)
Step 3: next(gen) → 2, total = 3   (메모리: 2만 존재, 1은 버림)
Step 4: next(gen) → 3, total = 6   (메모리: 3만 존재)
Step 5: next(gen) → 4, total = 10  (메모리: 4만 존재)
Step 6: next(gen) → 5, total = 15  (메모리: 5만 존재)
Step 7: StopIteration → return 15
```

---

## 언제 무엇을 쓸까?

### 리스트 컴프리헨션 사용

```python
# 1. 결과를 여러 번 사용할 때
nums = [x**2 for x in range(10)]
print(sum(nums))   # 285
print(max(nums))   # 81
print(nums[5])     # 25 (인덱싱 필요)

# 2. 결과 길이를 알아야 할 때
len(nums)  # 10
```

### 제너레이터 표현식 사용

```python
# 1. 한 번만 순회할 때
sum(x**2 for x in range(10))

# 2. 데이터가 매우 클 때
sum(x for x in range(10000000))  # 메모리 효율적

# 3. 함수에 바로 전달할 때
max(x**2 for x in range(10))
min(x**2 for x in range(10))
any(x > 5 for x in range(10))
all(x > 0 for x in range(1, 10))
```

---

## 주의: sorted()는 O(n)

```python
# sorted()는 내부적으로 리스트를 만들어야 함
sorted(int(c) for c in "54321")  # Space O(n)

# 왜? 정렬하려면 모든 요소를 알아야 하니까!
```

| 함수 | 제너레이터 Space | 이유 |
|------|------------------|------|
| `sum()` | O(1) | 누적만 하면 됨 |
| `max()` | O(1) | 최댓값만 기억 |
| `min()` | O(1) | 최솟값만 기억 |
| `any()` | O(1) | True 나오면 즉시 종료 |
| `all()` | O(1) | False 나오면 즉시 종료 |
| `sorted()` | O(n) | 전체 필요 |
| `list()` | O(n) | 전체 저장 |
| `len()` | ❌ 불가 | 길이 모름 |

---

## 요약

```
리스트 컴프리헨션  [...]  →  즉시 평가, Space O(n)
제너레이터 표현식  (...)  →  지연 평가, Space O(1)

sum/max/min/any/all + 제너레이터 = 메모리 효율적!
sorted/list + 제너레이터 = 어차피 O(n)
```
