# 문자열 회전 트릭 완벽 정리

## 핵심 공식 (외우세요!)

```python
# 🔑 S를 회전해서 T가 될 수 있는가?
T in (S + S)  # True면 가능, False면 불가능

# 🔑 몇 번 회전해야 하는가?
(S + S).find(T)  # 회전 횟수 (오른쪽 회전 기준)
```

## 왜 이게 되는가?

### 직관적 이해

문자열 `S = "hello"`를 생각해보자.

```
오른쪽 회전 (마지막 → 맨앞):
0번: hello
1번: ohell  (o가 맨앞으로)
2번: lohel
3번: llohe
4번: elloh
5번: hello  (원래대로)
```

이제 `S + S = "hellohello"`를 보면:

```
h e l l o h e l l o
^^^^^         hello (0번 회전)
  ^^^^^       elloh (4번 회전)
    ^^^^^     llohe (3번 회전)
      ^^^^^   lohel (2번 회전)
        ^^^^^ ohell (1번 회전)
```

**놀라운 사실**: `S + S` 안에 **모든 회전 상태**가 부분 문자열로 존재한다!

### 수학적 증명

- 길이 n인 문자열 S의 i번 오른쪽 회전: `S[n-i:] + S[:n-i]`
- `S + S`에서 인덱스 i부터 n글자: `(S + S)[i:i+n]` = `S[i:] + S[:i]`
- 따라서 `(S + S)[n-i:n-i+n]` = i번 회전한 결과

## 실전 패턴

### 패턴 1: 회전 가능 여부 확인

```python
def can_rotate_to(S: str, T: str) -> bool:
    """S를 회전해서 T가 될 수 있는가?"""
    if len(S) != len(T):
        return False
    return T in (S + S)

# 예시
can_rotate_to("hello", "ohell")  # True
can_rotate_to("apple", "elppa")  # False (회전이 아니라 뒤집기)
```

### 패턴 2: 최소 회전 횟수 찾기 (오른쪽 회전)

```python
def min_rotation_right(A: str, B: str) -> int:
    """A를 오른쪽으로 밀어서 B가 되는 최소 횟수 (-1: 불가능)"""
    if len(A) != len(B):
        return -1
    return (B + B).find(A)  # ⚠️ B를 2배! (A가 아님)

# 예시: "hello" → "ohell"
(B + B).find(A)  # "ohellohell".find("hello") = 1
```

### 패턴 3: 최소 회전 횟수 찾기 (왼쪽 회전)

```python
def min_rotation_left(A: str, B: str) -> int:
    """A를 왼쪽으로 밀어서 B가 되는 최소 횟수 (-1: 불가능)"""
    if len(A) != len(B):
        return -1
    return (A + A).find(B)  # ⚠️ A를 2배! (B가 아님)

# 예시: "hello" → "elloh"
(A + A).find(B)  # "hellohello".find("elloh") = 1
```

### 헷갈림 방지 - 방향별 정리

| 회전 방향 | 동작 | 공식 |
|----------|------|------|
| **오른쪽** (→) | 마지막 문자가 맨앞으로 | `(B + B).find(A)` |
| **왼쪽** (←) | 첫 문자가 맨뒤로 | `(A + A).find(B)` |

**기억법**: "결과(B)를 2배로 만들고 원본(A)을 찾으면 오른쪽 회전 횟수"

## 자주 하는 실수

### 실수 1: A와 B를 바꿔서 사용

```python
# ❌ 틀림: 오른쪽 회전인데 A를 2배
(A + A).find(B)  # 이건 왼쪽 회전 횟수!

# ✅ 맞음: 오른쪽 회전
(B + B).find(A)
```

### 실수 2: 길이 체크 누락

```python
# ❌ 길이가 다르면 항상 False인데 체크 안 함
def can_rotate(S, T):
    return T in (S + S)  # len("abc") != len("ab") 인데도 True 반환 가능

# ✅ 길이 체크 필수
def can_rotate(S, T):
    return len(S) == len(T) and T in (S + S)
```

### 실수 3: 동일 문자열 처리

```python
A = "abc"
B = "abc"

# A == B일 때 회전 횟수는 0
(B + B).find(A)  # "abcabc".find("abc") = 0 ✅ 정상 작동
```

## 직접 회전 vs 트릭 비교

```python
# 방법 1: 직접 회전 - O(n²)
def rotate_direct(A: str, B: str) -> int:
    for i in range(len(A)):
        rotated = A[-i:] + A[:-i] if i else A
        if rotated == B:
            return i
    return -1

# 방법 2: 트릭 - O(n)
def rotate_trick(A: str, B: str) -> int:
    return (B + B).find(A)
```

| 방법 | 시간 | 공간 | 코드 |
|------|------|------|------|
| 직접 회전 | O(n²) | O(n) | 5줄+ |
| 트릭 | O(n) | O(n) | 1줄 |

## 응용 문제

### 1. 순환 문자열 동등성

```python
def are_rotations(s1: str, s2: str) -> bool:
    """두 문자열이 서로의 회전인가?"""
    return len(s1) == len(s2) and s1 in (s2 + s2)
```

### 2. 모든 회전 상태 생성

```python
def all_rotations(s: str) -> list[str]:
    """문자열의 모든 회전 상태"""
    doubled = s + s
    return [doubled[i:i+len(s)] for i in range(len(s))]

all_rotations("abc")  # ['abc', 'bca', 'cab']
```

### 3. 사전순 최소 회전

```python
def min_rotation(s: str) -> str:
    """사전순으로 가장 작은 회전 상태"""
    doubled = s + s
    return min(doubled[i:i+len(s)] for i in range(len(s)))

min_rotation("cba")  # "acb"
```

### 4. 회전해서 같아지는 위치 모두 찾기

```python
def all_rotation_positions(A: str, B: str) -> list[int]:
    """A를 오른쪽으로 밀어 B가 되는 모든 횟수"""
    if len(A) != len(B):
        return []

    doubled = B + B
    positions = []
    start = 0
    while True:
        idx = doubled.find(A, start)
        if idx == -1 or idx >= len(A):
            break
        positions.append(idx)
        start = idx + 1
    return positions

# "atat" → "tata": 1번 또는 3번
all_rotation_positions("atat", "tata")  # [1, 3]
```

## 관련 자료구조

### deque.rotate() - 직접 회전할 때

```python
from collections import deque

d = deque("hello")
d.rotate(1)   # 오른쪽 회전: deque(['o', 'h', 'e', 'l', 'l'])
d.rotate(-1)  # 왼쪽 회전: deque(['h', 'e', 'l', 'l', 'o'])
```

### 슬라이싱으로 회전

```python
s = "hello"
s[-1:] + s[:-1]  # "ohell" (오른쪽 1칸)
s[1:] + s[:1]    # "elloh" (왼쪽 1칸)
s[-k:] + s[:-k]  # 오른쪽 k칸
s[k:] + s[:k]    # 왼쪽 k칸
```

## 요약 - 시험 전 복습용

```
┌─────────────────────────────────────────────┐
│  문자열 회전 트릭 핵심 공식                   │
├─────────────────────────────────────────────┤
│  ✓ 회전 가능?: T in (S + S)                 │
│  ✓ 오른쪽 회전 횟수: (B + B).find(A)        │
│  ✓ 왼쪽 회전 횟수: (A + A).find(B)          │
│                                             │
│  핵심 원리: S+S에 모든 회전 상태가 포함됨    │
└─────────────────────────────────────────────┘
```

## 관련 노트

- [[python-slicing]] - 슬라이싱으로 회전 구현
- [[str-index-vs-find]] - find() 메서드 상세

---

*관련 문제: #120921 문자열 밀기*
