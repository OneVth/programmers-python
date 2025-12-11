# LCM과 GCD의 관계

> 최소공배수(LCM)를 최대공약수(GCD)로 구하는 방법

## 핵심 공식

```
LCM(a, b) = (a × b) / GCD(a, b)
```

---

## 왜 이게 성립할까?

두 수 a, b를 소인수분해 했을 때:

```
a = 2² × 3¹ × 5⁰ = 12
b = 2¹ × 3² × 5¹ = 90
```

| | 2 | 3 | 5 | 결과 |
|---|---|---|---|------|
| a=12 | 2² | 3¹ | 5⁰ | |
| b=90 | 2¹ | 3² | 5¹ | |
| **GCD** (min) | 2¹ | 3¹ | 5⁰ | **6** |
| **LCM** (max) | 2² | 3² | 5¹ | **180** |

- **GCD**: 각 소인수의 **최솟값** 선택
- **LCM**: 각 소인수의 **최댓값** 선택

---

## 증명

```
a × b = (각 소인수의 지수 합)
GCD × LCM = (min + max) = (지수 합)

∴ a × b = GCD × LCM
∴ LCM = (a × b) / GCD
```

검증: `12 × 90 = 1080`, `6 × 180 = 1080` ✅

---

## Python 구현

### 유클리드 호제법 (GCD 직접 구현)

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

gcd(12, 90)  # 6
```

#### 💡 max/min이 필요 없는 이유

흔한 실수: `gcd(max(a,b), min(a,b))`처럼 큰 수를 앞에 넣어야 한다고 생각

```python
gcd(3, 12)  # a=3, b=12 (작은 수가 앞에 있음)
# 1회차: a, b = 12, 3 % 12 → (12, 3)  ← 자동으로 swap됨!
# 2회차: a, b = 3, 12 % 3 → (3, 0)
# 결과: 3 ✅
```

**원리**: `a < b`일 때 `a % b = a`가 되어 첫 반복에서 **자동으로 큰 수가 앞으로** 이동한다.

```
gcd(3, 12)
→ (12, 3)   # a % b = 3 % 12 = 3, 자동 swap
→ (3, 0)   # 12 % 3 = 0
→ 3
```

### 내장 함수 사용

```python
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

lcm(12, 90)  # 180
```

### 내장 함수 (Python 3.9+)

```python
from math import lcm

lcm(12, 90)  # 180
lcm(4, 6, 8)  # 24 (여러 수도 가능)
```

---

## 주의사항

### 정수 오버플로 방지

```python
# ❌ a * b가 먼저 계산되어 오버플로 가능
a * b // gcd(a, b)

# ✅ 나눗셈을 먼저 해서 오버플로 방지
a // gcd(a, b) * b
```

### 여러 수의 LCM

```python
from functools import reduce
from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

def lcm_multiple(*args):
    return reduce(lcm, args)

lcm_multiple(4, 6, 8)  # 24
```

---

## 활용 예시

### 피자 나눠 먹기 (#120815)

n명이 6조각 피자를 **남김없이** 나눠먹으려면?

```python
from math import lcm

def solution(n):
    # 총 조각 수가 n의 배수이면서 6의 배수여야 함
    # → LCM(n, 6) 조각 필요
    # → LCM(n, 6) / 6 판 필요
    return lcm(n, 6) // 6
```

---

*관련 문제: #120815 피자 나눠 먹기 (2)*
