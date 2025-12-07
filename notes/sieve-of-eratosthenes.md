# 에라토스테네스의 체 (Sieve of Eratosthenes)

n 이하의 **모든 소수를 한 번에** 찾는 가장 효율적인 알고리즘.

## 원리

1. 2부터 n까지 모든 수를 "소수 후보"로 표시
2. 가장 작은 소수(2)의 **배수들을 모두 제거**
3. 다음 소수(3)의 배수들을 모두 제거
4. √n까지 반복하면 남은 수가 모두 소수!

## 시각화 (n=30)

```
초기:     2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 ...
2의 배수: 2  3  ×  5  ×  7  ×  9  × 11  × 13  × 15  × 17  × 19  × ...
3의 배수: 2  3  ×  5  ×  7  ×  ×  × 11  × 13  ×  ×  × 17  × 19  × ...
5의 배수: 2  3  ×  5  ×  7  ×  ×  × 11  × 13  ×  ×  × 17  × 19  × ...

결과: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## 구현

```python
def sieve_of_eratosthenes(n: int) -> list[int]:
    """n 이하의 모든 소수 반환"""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0, 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:  # i가 소수면
            for j in range(i*i, n + 1, i):  # i의 배수들 제거
                is_prime[j] = False

    return [i for i, prime in enumerate(is_prime) if prime]
```

## 핵심 최적화: 왜 i*i부터 시작하나?

```python
for j in range(i*i, n + 1, i):  # i*2가 아니라 i*i부터!
```

- `i*2`는 이미 **2의 배수**로 제거됨
- `i*3`는 이미 **3의 배수**로 제거됨
- `i*(i-1)`까지는 **더 작은 소수의 배수로 이미 제거됨**
- 따라서 `i*i`부터 시작해도 됨!

예시 (i=5일 때):
```
5*2 = 10 → 2의 배수로 이미 제거됨
5*3 = 15 → 3의 배수로 이미 제거됨
5*4 = 20 → 2의 배수로 이미 제거됨
5*5 = 25 → 여기서부터 시작! ✅
```

## 시간복잡도 비교

| 방법 | 시간복잡도 | n=100 | n=10,000 | n=1,000,000 |
|------|-----------|-------|----------|-------------|
| 브루트포스 | O(n²) | 10,000 | 100,000,000 | 10¹² |
| √n 최적화 | O(n√n) | 1,000 | 1,000,000 | 10⁹ |
| **에라토스테네스** | O(n log log n) | ~460 | ~92,000 | ~13,800,000 |

## 언제 쓰나?

### 단일 소수 판별 → √n 방식

```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### n 이하 모든 소수 / 소수 개수 → 에라토스테네스의 체

```python
# 소수 개수
prime_count = sum(sieve_is_prime)

# 합성수 개수
composite_count = n - prime_count - 1  # 1은 소수도 합성수도 아님
```

## 응용: 소수 관련 문제 패턴

```python
# 1. n 이하 소수 리스트
primes = sieve_of_eratosthenes(n)

# 2. 소수 개수
prime_count = len(primes)

# 3. 합성수 개수
composite_count = n - prime_count - 1

# 4. 소수 판별 (여러 쿼리)
is_prime = [False, False] + [True] * (n - 1)
# ... 체 적용 후
if is_prime[x]:  # O(1) 판별!
    print(f"{x}는 소수")

# 5. 소인수분해 (최소 소인수 저장 변형)
min_factor = list(range(n + 1))
for i in range(2, int(n**0.5) + 1):
    if min_factor[i] == i:  # i가 소수
        for j in range(i*i, n + 1, i):
            if min_factor[j] == j:
                min_factor[j] = i
```

## 메모리 최적화 (비트 마스킹)

n이 매우 큰 경우 메모리 절약:

```python
import numpy as np

def sieve_numpy(n: int) -> list[int]:
    is_prime = np.ones(n + 1, dtype=bool)
    is_prime[0:2] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i::i] = False  # 슬라이싱으로 한 번에!

    return np.where(is_prime)[0].tolist()
```
