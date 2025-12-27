# heapq.nsmallest / nlargest - 상위/하위 k개 추출

> 관련 문제: [뒤에서 5등까지 #181853](../Lv0/181853/solution.py), [뒤에서 5등 위로 #181852](../Lv0/181852/solution.py)

## 개요

리스트에서 가장 작은/큰 k개의 원소를 추출할 때 사용하는 효율적인 방법입니다.

```python
import heapq

# 가장 작은 k개
heapq.nsmallest(k, iterable)

# 가장 큰 k개
heapq.nlargest(k, iterable)
```

---

## 기본 사용법

```python
import heapq

nums = [12, 4, 15, 46, 38, 1, 14]

# 가장 작은 5개
heapq.nsmallest(5, nums)  # [1, 4, 12, 14, 15]

# 가장 큰 5개
heapq.nlargest(5, nums)   # [46, 38, 15, 14, 12]
```

---

## sorted vs heapq 비교

### 시간복잡도

| 방법 | 시간복잡도 | k=5, n=1,000,000 |
|------|-----------|------------------|
| `sorted(lst)[:k]` | O(n log n) | O(n log n) ≈ 20n |
| `heapq.nsmallest(k, lst)` | O(n log k) | O(n log 5) ≈ 2.3n |

### 선택 기준

```python
# ✅ heapq가 유리한 경우: k << n
heapq.nsmallest(5, million_items)   # O(n log 5) ≈ O(n)
sorted(million_items)[:5]            # O(n log n) - 훨씬 느림

# ✅ sorted가 유리한 경우: k ≈ n
heapq.nsmallest(n//2, items)  # O(n log(n/2)) ≈ O(n log n)
sorted(items)[:n//2]          # O(n log n), 내부 최적화로 더 빠름

# ✅ 둘 다 비슷한 경우: n이 작을 때
# n ≤ 100이면 성능 차이 무의미, sorted가 더 직관적
```

### 실전 가이드

| n 크기 | k 크기 | 추천 |
|--------|--------|------|
| n ≤ 100 | any | `sorted()` (간결함) |
| n > 1000 | k ≤ log(n) | `heapq.nsmallest/nlargest` |
| n > 1000 | k > n/2 | `sorted()` |

---

## heapq 주요 함수

### Top-k 추출

```python
import heapq

# 가장 작은 k개
heapq.nsmallest(k, iterable)
heapq.nsmallest(k, iterable, key=func)  # key 함수 지원

# 가장 큰 k개
heapq.nlargest(k, iterable)
heapq.nlargest(k, iterable, key=func)
```

### 힙 연산

```python
import heapq

heap = []

# 원소 추가 - O(log n)
heapq.heappush(heap, item)

# 최솟값 추출 - O(log n)
smallest = heapq.heappop(heap)

# 최솟값 확인 (추출 없이) - O(1)
smallest = heap[0]

# 리스트를 힙으로 변환 - O(n)
heapq.heapify(list)

# push + pop 한 번에 - O(log n)
heapq.heapreplace(heap, item)  # pop 먼저, push
heapq.heappushpop(heap, item)  # push 먼저, pop
```

---

## key 함수 활용

```python
import heapq

# 튜플 리스트에서 두 번째 값 기준으로 정렬
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# 점수가 가장 낮은 2명
heapq.nsmallest(2, students, key=lambda x: x[1])
# [('Charlie', 78), ('Alice', 85)]

# 점수가 가장 높은 2명
heapq.nlargest(2, students, key=lambda x: x[1])
# [('Bob', 92), ('Alice', 85)]
```

---

## 내부 동작 원리

### nsmallest 알고리즘 (개념적)

```python
def nsmallest_concept(k, iterable):
    """
    max-heap을 사용하여 k개의 최솟값 유지
    - 힙에 k개 미만이면 추가
    - 새 원소가 힙의 최댓값보다 작으면 교체
    """
    # Python의 heapq는 min-heap이므로 음수로 변환하여 max-heap 시뮬레이션
    max_heap = []

    for item in iterable:
        if len(max_heap) < k:
            heapq.heappush(max_heap, -item)
        elif -item > max_heap[0]:  # item < -max_heap[0]
            heapq.heapreplace(max_heap, -item)

    return sorted(-x for x in max_heap)
```

### 시간복잡도 분석

- 각 원소마다 힙 연산: O(log k)
- 총 n개 원소: O(n log k)
- 최종 정렬: O(k log k) (무시 가능)

---

## 실전 예제

### 예제 1: 상위 3개 점수

```python
import heapq

scores = [72, 85, 91, 68, 77, 95, 88, 62]

# 상위 3개
top_3 = heapq.nlargest(3, scores)  # [95, 91, 88]

# 하위 3개
bottom_3 = heapq.nsmallest(3, scores)  # [62, 68, 72]
```

### 예제 2: 가장 비싼 상품 5개

```python
import heapq

products = [
    {"name": "A", "price": 1000},
    {"name": "B", "price": 500},
    {"name": "C", "price": 1500},
    {"name": "D", "price": 800},
]

expensive = heapq.nlargest(2, products, key=lambda x: x["price"])
# [{'name': 'C', 'price': 1500}, {'name': 'A', 'price': 1000}]
```

### 예제 3: 스트리밍 데이터에서 Top-k 유지

```python
import heapq

def streaming_top_k(stream, k):
    """스트리밍 데이터에서 실시간으로 상위 k개 유지"""
    min_heap = []  # 상위 k개 중 최솟값을 빠르게 찾기 위해 min-heap 사용

    for num in stream:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:  # 현재 top-k의 최솟값보다 크면
            heapq.heapreplace(min_heap, num)

    return sorted(min_heap, reverse=True)  # 내림차순 정렬

# 예시: 무한 스트림에서 상위 3개
stream = iter([5, 2, 8, 1, 9, 3, 7, 4, 6])
print(streaming_top_k(stream, 3))  # [9, 8, 7]
```

---

## 주의사항

### Python heapq는 min-heap만 지원

```python
import heapq

# max-heap이 필요하면 음수로 변환
nums = [3, 1, 4, 1, 5, 9]

max_heap = [-x for x in nums]
heapq.heapify(max_heap)

# 최댓값 추출
largest = -heapq.heappop(max_heap)  # 9
```

### nsmallest/nlargest는 새 리스트 반환

```python
import heapq

nums = [3, 1, 4, 1, 5]
result = heapq.nsmallest(3, nums)

# 원본 변경 없음
print(nums)    # [3, 1, 4, 1, 5]
print(result)  # [1, 1, 3]
```

---

## 요약

| 상황 | 코드 | 시간복잡도 |
|------|------|-----------|
| 가장 작은 k개 | `heapq.nsmallest(k, lst)` | O(n log k) |
| 가장 큰 k개 | `heapq.nlargest(k, lst)` | O(n log k) |
| 전체 정렬 후 슬라이싱 | `sorted(lst)[:k]` | O(n log n) |
| 스트리밍 top-k | 힙 직접 관리 | O(n log k) |

**결론**: k가 n보다 훨씬 작을 때 `heapq.nsmallest/nlargest`가 효율적!
