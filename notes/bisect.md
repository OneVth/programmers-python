# bisect - Python 이진 탐색 모듈

정렬된 리스트에서 **삽입 위치**를 찾는 모듈. O(log n) 탐색.

## 핵심 함수: bisect_left vs bisect_right

```python
from bisect import bisect_left, bisect_right

nums = [1, 3, 3, 3, 5, 7]
#       0  1  2  3  4  5

bisect_left(nums, 3)   # → 1 (3이 시작되는 위치)
bisect_right(nums, 3)  # → 4 (3이 끝나는 다음 위치)
```

### 시각화

```
nums = [1, 3, 3, 3, 5, 7]
            ↑        ↑
            │        └── bisect_right(nums, 3) = 4
            └── bisect_left(nums, 3) = 1

"3을 어디에 삽입해야 정렬 유지될까?"
- bisect_left: 같은 값들의 **왼쪽**에 삽입
- bisect_right: 같은 값들의 **오른쪽**에 삽입
```

### 값이 없을 때는?

```python
nums = [1, 3, 5, 7]
bisect_left(nums, 4)   # → 2 (4가 들어갈 위치)
bisect_right(nums, 4)  # → 2 (같은 결과!)

# 값이 없으면 left와 right 결과가 동일
```

## 기본 함수들

```python
from bisect import bisect_left, bisect_right, insort_left, insort_right

nums = [1, 3, 5, 7]

# 삽입 위치 찾기 (삽입은 안 함)
bisect_left(nums, 4)   # → 2
bisect_right(nums, 4)  # → 2

# 삽입까지 수행 (리스트 변경)
insort_left(nums, 4)   # nums = [1, 3, 4, 5, 7]
insort_right(nums, 6)  # nums = [1, 3, 4, 5, 6, 7]
```

## 자주 쓰는 패턴

### 1. 값이 존재하는지 확인

```python
def binary_search(nums, target):
    """target이 nums에 있으면 True"""
    i = bisect_left(nums, target)
    return i < len(nums) and nums[i] == target

nums = [1, 3, 5, 7]
binary_search(nums, 3)  # True
binary_search(nums, 4)  # False
```

### 2. 값의 개수 세기

```python
def count_value(nums, target):
    """정렬된 리스트에서 target 개수"""
    left = bisect_left(nums, target)
    right = bisect_right(nums, target)
    return right - left

nums = [1, 3, 3, 3, 5, 7]
count_value(nums, 3)  # → 3
```

### 3. 특정 값 이하/미만/이상/초과 개수

```python
nums = [1, 3, 3, 5, 7, 9]

# x 이하 개수 (x 포함)
def count_lte(nums, x):
    return bisect_right(nums, x)

# x 미만 개수 (x 미포함)
def count_lt(nums, x):
    return bisect_left(nums, x)

# x 이상 개수
def count_gte(nums, x):
    return len(nums) - bisect_left(nums, x)

# x 초과 개수
def count_gt(nums, x):
    return len(nums) - bisect_right(nums, x)

count_lte(nums, 5)  # 5 이하: 4개 [1,3,3,5]
count_lt(nums, 5)   # 5 미만: 3개 [1,3,3]
count_gte(nums, 5)  # 5 이상: 3개 [5,7,9]
count_gt(nums, 5)   # 5 초과: 2개 [7,9]
```

### 4. 범위 내 값 개수

```python
def count_range(nums, lo, hi):
    """lo 이상 hi 이하 개수"""
    return bisect_right(nums, hi) - bisect_left(nums, lo)

nums = [1, 3, 5, 7, 9]
count_range(nums, 3, 7)  # → 3 (3, 5, 7)
```

### 5. 가장 가까운 값 찾기

```python
def find_closest(nums, target):
    """target에 가장 가까운 값 반환"""
    if not nums:
        return None

    i = bisect_left(nums, target)

    if i == 0:
        return nums[0]
    if i == len(nums):
        return nums[-1]

    # 왼쪽과 오른쪽 중 더 가까운 것
    if target - nums[i-1] <= nums[i] - target:
        return nums[i-1]
    return nums[i]

nums = [1, 3, 8, 10]
find_closest(nums, 5)  # → 3 (거리 2 vs 3)
find_closest(nums, 6)  # → 8 (거리 3 vs 2)
```

## 코딩테스트 빈출 유형

### 유형 1: Lower/Upper Bound

```python
# C++의 lower_bound, upper_bound와 동일
lower_bound = bisect_left   # 이상인 첫 위치
upper_bound = bisect_right  # 초과인 첫 위치
```

### 유형 2: 팩토리얼 테이블 탐색 (현재 문제)

```python
factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

def find_max_factorial(n):
    """i! <= n인 가장 큰 i"""
    return bisect_right(factorials, n) - 1

find_max_factorial(7)  # → 3 (3! = 6 ≤ 7)
```

### 유형 3: 점수 순위 계산

```python
def get_rank(scores, my_score):
    """내 점수보다 높은 점수 개수 + 1 = 순위"""
    sorted_scores = sorted(scores, reverse=True)
    # 내 점수 초과인 개수 + 1
    return bisect_left(sorted_scores, my_score, key=lambda x: -x) + 1

# 또는 오름차순에서
def get_rank_v2(scores, my_score):
    sorted_scores = sorted(scores)
    return len(scores) - bisect_right(sorted_scores, my_score) + 1
```

### 유형 4: 이진 탐색 + 조건 만족

```python
def find_first_satisfying(nums, condition):
    """조건을 만족하는 첫 번째 인덱스"""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if condition(nums[mid]):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## bisect vs 직접 이진탐색

```python
# bisect 사용 (간결)
from bisect import bisect_left
idx = bisect_left(nums, target)

# 직접 구현 (동일 동작)
def my_bisect_left(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

## 요약: left vs right 선택 기준

| 상황 | 사용 함수 |
|------|----------|
| 값 **이상**인 첫 위치 | `bisect_left` |
| 값 **초과**인 첫 위치 | `bisect_right` |
| 값 **이하**인 개수 | `bisect_right` |
| 값 **미만**인 개수 | `bisect_left` |
| 같은 값들 중 **왼쪽**에 삽입 | `bisect_left` |
| 같은 값들 중 **오른쪽**에 삽입 | `bisect_right` |

```
기억법:
- left: "이 값이 시작되는 곳"
- right: "이 값이 끝나는 다음 곳"
```
