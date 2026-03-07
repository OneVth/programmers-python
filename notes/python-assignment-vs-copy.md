# Python 할당(=) vs 복사(copy)

> C의 포인터 대입과 비교하며 이해하는 Python 참조 할당

## 핵심: `=`는 복사가 아니라 참조

```python
arr = [1, 2, 3]
prev = arr          # 같은 객체를 가리킴 (복사 X)

prev[0] = 99
print(arr)          # [99, 2, 3] ← arr도 바뀜!
print(prev is arr)  # True
```

C 언어로 비유하면 **포인터 대입**과 같다:

```c
int arr[] = {1, 2, 3};
int *prev = arr;     // 같은 메모리 주소
prev[0] = 99;        // arr[0]도 99가 됨
```

---

## 복사하는 방법

### Shallow Copy (1차원 리스트에 충분)

```python
prev = arr[:]         # 슬라이싱
prev = arr.copy()     # 메서드
prev = list(arr)      # 생성자

prev[0] = 99
print(arr)            # [1, 2, 3] ← 원본 유지
```

### Deep Copy (중첩 리스트일 때)

```python
import copy

matrix = [[1, 2], [3, 4]]
shallow = matrix[:]           # 외부 리스트만 복사
deep = copy.deepcopy(matrix)  # 내부 리스트까지 복사

shallow[0][0] = 99
print(matrix)    # [[99, 2], [3, 4]] ← shallow copy는 내부 객체 공유!

deep[0][0] = 0
print(matrix)    # [[99, 2], [3, 4]] ← deep copy는 완전히 독립
```

---

## 실전 패턴: 변환 루프에서의 활용

### 패턴 1: 새 리스트 생성 후 비교

```python
prev = arr
while True:
    curr = [transform(x) for x in prev]  # 매번 새 리스트 생성
    if prev == curr:                      # O(n) 비교
        break
    prev = curr  # prev가 새 리스트(curr)를 가리킴, 원본 arr는 무관
```

- `prev = arr`는 복사가 아니지만, `curr`가 매번 새 리스트이므로 원본 `arr`에 영향 없음
- Space: O(n) (curr 리스트)

### 패턴 2: in-place 변환 + changed 플래그

```python
while True:
    changed = False
    for i in range(len(arr)):
        new_val = transform(arr[i])
        if arr[i] != new_val:
            arr[i] = new_val
            changed = True
    if not changed:
        break
```

- 새 리스트 생성 없음, 비교 연산 없음
- Space: O(1)
- 주의: **원본 배열이 수정됨** (side effect)

---

## C vs Python 비교 정리

| 동작 | C | Python |
|------|---|--------|
| 참조 할당 | `int *p = arr;` | `p = arr` |
| 값 복사 | `memcpy(dst, src, n)` | `dst = src[:]` or `src.copy()` |
| 깊은 복사 | 직접 재귀 구현 | `copy.deepcopy(src)` |
| 동일 객체 확인 | `p == arr` (주소 비교) | `p is arr` |
| 값 동등 확인 | `memcmp(a, b, n)` | `a == b` |

---

*관련 노트: [mutable-vs-immutable.md](mutable-vs-immutable.md)*
*관련 문제: #181881 조건에 맞게 수열 변환하기 2*
