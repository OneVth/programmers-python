# 대칭 행렬과 루프 최적화

## 관련 문제
- [181830 - 정사각형으로 만들기](../Lv0/181830/solution.py)
- [181831 - 특별한 이차원 배열 2](../Lv0/181831/solution.py)

---

## 1. 대칭 행렬 (Symmetric Matrix)

`arr[i][j] == arr[j][i]`를 만족하는 정사각 행렬

```
    j=0  j=1  j=2
i=0 [ 5, 192,  33]
i=1 [192,  72,  95]  ← arr[0][1] == arr[1][0] == 192
i=2 [ 33,  95, 999]
```

### 판별 방법 3가지

```python
# v1: 모든 쌍 비교 (중복 비교 있음)
def is_symmetric_v1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):  # n² 번
            if arr[i][j] != arr[j][i]:
                return False
    return True

# v2: 전치행렬과 비교 (Pythonic but 메모리 사용)
def is_symmetric_v2(arr):
    return arr == list(map(list, zip(*arr)))  # O(n²) 공간

# v3: 상삼각만 비교 (최적)
def is_symmetric_v3(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):  # n(n-1)/2 번
            if arr[i][j] != arr[j][i]:
                return False
    return True
```

---

## 2. 가짜 최적화 vs 진짜 최적화

### 가짜 최적화 (루프 횟수 동일)

```python
for i in range(n):
    for j in range(n):      # 여전히 n² 번 반복!
        if i >= j:
            continue        # 조건 검사만 추가됨
        if arr[i][j] != arr[j][i]:
            return 0
```

- 루프: n² 번
- `i >= j` 검사: n² 번 (오버헤드)
- 실제 비교: n(n-1)/2 번

### 진짜 최적화 (루프 범위 조정)

```python
for i in range(n):
    for j in range(i + 1, n):  # 루프 자체가 n(n-1)/2 번!
        if arr[i][j] != arr[j][i]:
            return 0
```

- 루프: n(n-1)/2 번
- 조건 검사 오버헤드: 없음
- 실제 비교: n(n-1)/2 번

---

## 3. 성능 측정 스크립트

```python
import timeit

def solution_v1(arr):
    """모든 쌍 비교"""
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

def solution_v3_fake(arr):
    """가짜 최적화: continue 사용"""
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i >= j:
                continue
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

def solution_v3_real(arr):
    """진짜 최적화: 루프 범위 조정"""
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

# 대칭 행렬 생성 (최악의 경우: 전부 검사해야 함)
n = 100
arr = [[i + j for j in range(n)] for i in range(n)]

print('=== 루프 횟수 비교 (n=100) ===')
print(f'v1:        {n*n} = {n*n} 번')
print(f'v3_fake:   {n*n} 루프 + {n*n} 번 i>=j 검사')
print(f'v3_real:   {n*(n-1)//2} = {n*(n-1)//2} 번')

print()
print('=== 실제 성능 측정 ===')
t1 = timeit.timeit(lambda: solution_v1(arr), number=1000)
t3_fake = timeit.timeit(lambda: solution_v3_fake(arr), number=1000)
t3_real = timeit.timeit(lambda: solution_v3_real(arr), number=1000)

print(f'v1:        {t1:.4f}s')
print(f'v3_fake:   {t3_fake:.4f}s')
print(f'v3_real:   {t3_real:.4f}s')
```

### 실행 결과 예시

```
=== 루프 횟수 비교 (n=100) ===
v1:        10000 = 10000 번
v3_fake:   10000 루프 + 10000 번 i>=j 검사
v3_real:   4950 = 4950 번

=== 실제 성능 측정 ===
v1:        0.3218s
v3_fake:   0.2792s
v3_real:   0.1522s  ← 약 2배 빠름!
```

---

## 4. 핵심 교훈

| 방식 | 루프 횟수 | 비고 |
|------|----------|------|
| 전체 비교 | n² | 중복 비교 있음 |
| continue 사용 | n² | 조건 검사 오버헤드 |
| **range(i+1, n)** | **n(n-1)/2** | **진짜 최적화** |

> **불필요한 반복을 `continue`로 건너뛰지 말고, 루프 범위 자체를 줄여라!**

---

## 5. 응용: 2차원 배열 정사각형 만들기

```python
# In-place 수정 (원본 변경)
def make_square_inplace(arr):
    rows, cols = len(arr), len(arr[0])
    if rows > cols:
        for row in arr:
            row.extend([0] * (rows - cols))
    elif cols > rows:
        arr.extend([[0] * cols for _ in range(cols - rows)])
    return arr

# 새 배열 생성 (원본 보존, 더 깔끔)
def make_square_new(arr):
    rows, cols = len(arr), len(arr[0])
    m = max(rows, cols)
    result = [[0] * m for _ in range(m)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = arr[i][j]
    return result
```

### Trade-off

| | In-place | 새 배열 |
|---|---|---|
| Space | O(1) 추가 | O(m²) |
| 원본 보존 | ❌ | ✅ |
| 코딩 테스트 | 부작용 주의 | 안전하고 권장 |
