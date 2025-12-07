# heapq - Python 힙(Heap) 자료구조

## 힙(Heap)이란?

**완전 이진 트리** 기반의 자료구조로, 부모 노드가 자식 노드보다 항상 작거나(min-heap) 큼(max-heap).

```
       1          ← 루트가 항상 최솟값 (min-heap)
      / \
     3   2
    / \
   7   4
```

Python의 `heapq`는 **min-heap**만 지원합니다.

## 기본 연산

```python
import heapq

# 리스트를 힙으로 변환 - O(n)
nums = [5, 3, 8, 1, 2]
heapq.heapify(nums)  # [1, 2, 8, 5, 3] - 내부 구조 변경

# 힙에 원소 추가 - O(log n)
heapq.heappush(nums, 0)  # 0 추가

# 최솟값 제거 및 반환 - O(log n)
smallest = heapq.heappop(nums)  # 0 반환

# 최솟값 확인 (제거 안 함) - O(1)
peek = nums[0]

# push와 pop을 한 번에 - O(log n)
heapq.heappushpop(nums, 4)  # push 후 pop (더 효율적)
heapq.heapreplace(nums, 4)  # pop 후 push
```

## 핵심 함수

### nlargest / nsmallest - 상위/하위 k개 추출

```python
from heapq import nlargest, nsmallest

nums = [5, 3, 8, 1, 2, 9, 7]

# 상위 3개
top3 = nlargest(3, nums)      # [9, 8, 7]

# 하위 3개
bottom3 = nsmallest(3, nums)  # [1, 2, 3]

# key 함수 지정 가능
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
top2 = nlargest(2, students, key=lambda x: x[1])
# [('Bob', 92), ('Alice', 85)]
```

### 시간복잡도 비교

| 방법 | 시간복잡도 | k=3, n=1000 |
|------|-----------|-------------|
| `sorted(lst)[:k]` | O(n log n) | ~9,966 |
| `nsmallest(k, lst)` | O(n + k log n) | ~1,030 |
| 전체 힙 구성 후 k번 pop | O(n + k log n) | ~1,030 |

**k가 n보다 훨씬 작을 때** `nlargest`/`nsmallest`가 유리!

## 자주 쓰는 패턴

### 1. 우선순위 큐 (Priority Queue)

```python
import heapq

# 작업 스케줄링 - 우선순위가 낮은 것부터 처리
tasks = []
heapq.heappush(tasks, (1, "긴급 작업"))
heapq.heappush(tasks, (3, "일반 작업"))
heapq.heappush(tasks, (2, "중요 작업"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"처리: {task} (우선순위: {priority})")
# 처리: 긴급 작업 (우선순위: 1)
# 처리: 중요 작업 (우선순위: 2)
# 처리: 일반 작업 (우선순위: 3)
```

### 2. Top K 문제

```python
from heapq import nlargest, nsmallest

# 가장 큰 k개
def top_k_largest(nums, k):
    return nlargest(k, nums)

# 가장 작은 k개
def top_k_smallest(nums, k):
    return nsmallest(k, nums)

# k번째로 큰 수
def kth_largest(nums, k):
    return nlargest(k, nums)[-1]
```

### 3. 스트리밍 데이터에서 Top K 유지

```python
import heapq

def maintain_top_k(stream, k):
    """스트림에서 상위 k개만 유지"""
    heap = []
    for num in stream:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:  # 현재 최솟값보다 크면
            heapq.heapreplace(heap, num)  # 교체
    return sorted(heap, reverse=True)

# 예: 실시간으로 들어오는 점수 중 상위 3개 유지
scores = [85, 92, 78, 95, 88, 76, 99]
top3 = maintain_top_k(scores, 3)  # [99, 95, 92]
```

### 4. Max-Heap 구현 (음수 트릭)

```python
import heapq

# Python heapq는 min-heap만 지원
# max-heap이 필요하면 음수로 변환!

nums = [5, 3, 8, 1, 2]
max_heap = [-x for x in nums]
heapq.heapify(max_heap)

# 최댓값 추출
largest = -heapq.heappop(max_heap)  # 8

# 값 추가
heapq.heappush(max_heap, -10)  # 10 추가
```

### 5. 힙 병합 (여러 정렬된 리스트 합치기)

```python
from heapq import merge

list1 = [1, 4, 7]
list2 = [2, 5, 8]
list3 = [3, 6, 9]

# 정렬된 상태로 병합
merged = list(merge(list1, list2, list3))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 코딩테스트 빈출 유형

### 유형 1: K번째 큰/작은 수

```python
def find_kth_largest(nums, k):
    return nlargest(k, nums)[-1]

def find_kth_smallest(nums, k):
    return nsmallest(k, nums)[-1]
```

### 유형 2: 중앙값 찾기 (두 힙 활용)

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # 작은 절반 (음수로 저장)
        self.min_heap = []  # 큰 절반

    def add_num(self, num):
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2
```

### 유형 3: 다익스트라 최단 경로

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)

        if dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances
```

## heapq vs 다른 자료구조

| 연산 | list | sorted list | heapq |
|------|------|-------------|-------|
| 최솟값 찾기 | O(n) | O(1) | O(1) |
| 최솟값 제거 | O(n) | O(n) | O(log n) |
| 삽입 | O(1) | O(n) | O(log n) |
| 정렬 유지 | X | O(n) 삽입마다 | 자동 |

**언제 heapq를 쓰나?**
- 최솟값/최댓값을 **반복적으로** 추출해야 할 때
- 데이터가 **동적으로 추가/삭제**될 때
- **Top K** 문제
- **우선순위 큐**가 필요할 때

## 주의사항

```python
import heapq

# ❌ 잘못된 사용: 힙이 아닌 리스트에서 heappop
nums = [5, 3, 8, 1, 2]
heapq.heappop(nums)  # 5가 나옴 (최솟값 아님!)

# ✅ 올바른 사용: heapify 먼저
nums = [5, 3, 8, 1, 2]
heapq.heapify(nums)  # 힙으로 변환
heapq.heappop(nums)  # 1이 나옴 (최솟값)
```
