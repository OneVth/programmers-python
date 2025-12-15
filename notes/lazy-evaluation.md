# Python Lazy Evaluation 완벽 가이드

## 개념

**Lazy Evaluation(지연 평가)**은 **값이 실제로 필요할 때까지 계산을 미루는** 평가 전략입니다.

```python
# Eager (즉시 평가) - 모든 값을 미리 계산
numbers = [x * 2 for x in range(1000000)]  # 즉시 100만개 생성, 메모리 점유

# Lazy (지연 평가) - 요청할 때만 계산
numbers = (x * 2 for x in range(1000000))  # 아직 아무것도 계산 안 함!
```

## Eager vs Lazy 비교

| 특성 | Eager (즉시 평가) | Lazy (지연 평가) |
|------|-------------------|------------------|
| **계산 시점** | 정의 즉시 | 값 요청 시 |
| **메모리** | 전체 결과 저장 | 하나씩만 저장 |
| **재사용** | 여러 번 순회 가능 | 한 번만 순회 가능 |
| **무한 시퀀스** | 불가능 | 가능 |
| **대표 타입** | `list`, `dict`, `set` | `generator`, `iterator` |

## Python에서 Lazy한 것들

### 1. Generator Expression (제너레이터 표현식)

```python
# 리스트 컴프리헨션 - Eager (대괄호)
eager = [x ** 2 for x in range(10)]
print(type(eager))  # <class 'list'>
print(eager)        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 제너레이터 표현식 - Lazy (소괄호)
lazy = (x ** 2 for x in range(10))
print(type(lazy))   # <class 'generator'>
print(lazy)         # <generator object <genexpr> at 0x...>

# 값을 요청해야 계산됨
print(next(lazy))   # 0 (이제야 첫 번째 값 계산)
print(next(lazy))   # 1 (두 번째 값 계산)
print(list(lazy))   # [4, 9, 16, 25, 36, 49, 64, 81] (나머지 전부 계산)
```

### 2. Generator Function (yield)

```python
def count_up(n):
    """n까지 카운트하는 제너레이터"""
    print("시작!")
    i = 0
    while i <= n:
        print(f"yield 직전: {i}")
        yield i  # 여기서 멈추고 값 반환, 다음 호출까지 대기
        print(f"yield 이후: {i}")
        i += 1

gen = count_up(3)
print("제너레이터 생성 완료")  # "시작!" 출력 안 됨 - 아직 실행 안 함!

print(next(gen))  # "시작!" → "yield 직전: 0" → 0 반환
print(next(gen))  # "yield 이후: 0" → "yield 직전: 1" → 1 반환
print(next(gen))  # "yield 이후: 1" → "yield 직전: 2" → 2 반환
```

### 3. 내장 함수들

```python
# filter() - Lazy
nums = [1, 2, 3, 4, 5, 6]
filtered = filter(lambda x: x % 2 == 0, nums)
print(filtered)       # <filter object at 0x...>
print(list(filtered)) # [2, 4, 6] (이제야 계산)

# map() - Lazy
mapped = map(lambda x: x * 2, nums)
print(mapped)         # <map object at 0x...>
print(list(mapped))   # [2, 4, 6, 8, 10, 12]

# range() - Lazy (엄밀히는 sequence지만 lazy하게 동작)
r = range(1000000000)  # 10억! 하지만 메모리 거의 안 씀
print(r[999999999])    # 999999999 (즉시 접근 가능)

# zip() - Lazy
zipped = zip([1, 2, 3], ['a', 'b', 'c'])
print(zipped)         # <zip object at 0x...>
print(list(zipped))   # [(1, 'a'), (2, 'b'), (3, 'c')]

# enumerate() - Lazy
enum = enumerate(['a', 'b', 'c'])
print(enum)           # <enumerate object at 0x...>
```

### 4. itertools 모듈 (전부 Lazy)

```python
from itertools import count, islice, takewhile, chain

# count() - 무한 시퀀스 (Lazy라서 가능!)
counter = count(start=1)  # 1, 2, 3, 4, ... 무한
print(next(counter))  # 1
print(next(counter))  # 2

# islice() - 슬라이싱 (Lazy)
first_five = islice(count(1), 5)  # 무한에서 5개만
print(list(first_five))  # [1, 2, 3, 4, 5]

# takewhile() - 조건 만족하는 동안만
nums = takewhile(lambda x: x < 5, count(1))
print(list(nums))  # [1, 2, 3, 4]

# chain() - 여러 iterable 연결 (Lazy)
chained = chain([1, 2], [3, 4], [5, 6])
print(list(chained))  # [1, 2, 3, 4, 5, 6]
```

## 메모리 비교 실험

```python
import sys

# Eager - 리스트
eager_list = [x for x in range(1000000)]
print(f"리스트 크기: {sys.getsizeof(eager_list):,} bytes")  # ~8,000,000 bytes

# Lazy - 제너레이터
lazy_gen = (x for x in range(1000000))
print(f"제너레이터 크기: {sys.getsizeof(lazy_gen):,} bytes")  # ~200 bytes

# 약 40,000배 차이!
```

## Lazy Evaluation의 장점

### 1. 메모리 효율

```python
# ❌ 메모리 폭발 - 1억 개의 제곱수를 메모리에 저장
squares = [x ** 2 for x in range(100000000)]  # MemoryError 위험!

# ✅ 메모리 효율 - 하나씩만 처리
squares = (x ** 2 for x in range(100000000))
for sq in squares:
    if sq > 1000:
        print(sq)
        break  # 1024 출력 후 종료, 메모리 거의 안 씀
```

### 2. 불필요한 계산 방지

```python
def expensive_operation(x):
    print(f"비싼 연산 수행: {x}")
    return x * 100

# Eager - 모든 연산 수행
eager = [expensive_operation(x) for x in range(10)]
# "비싼 연산 수행: 0" ~ "비싼 연산 수행: 9" 전부 출력

# Lazy - 필요한 것만 수행
lazy = (expensive_operation(x) for x in range(10))
first = next(lazy)  # "비싼 연산 수행: 0"만 출력
# 나머지 9개는 계산 안 함!
```

### 3. 무한 시퀀스 처리

```python
def fibonacci():
    """무한 피보나치 수열"""
    a, b = 0, 1
    while True:  # 무한 루프지만 OK!
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")  # 0 1 1 2 3 5 8 13 21 34
```

### 4. 파이프라인 구성

```python
# 데이터 처리 파이프라인 - 메모리 효율적
def read_large_file(path):
    with open(path) as f:
        for line in f:  # 한 줄씩 읽기 (Lazy)
            yield line.strip()

def filter_lines(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line

def process_line(line):
    return line.upper()

# 파이프라인 구성 (아직 아무것도 실행 안 됨!)
lines = read_large_file("huge_file.txt")
filtered = filter_lines(lines, "error")
processed = (process_line(line) for line in filtered)

# 이제야 한 줄씩 처리 시작
for result in processed:
    print(result)
```

## Lazy Evaluation의 주의점

### 1. 일회성 (한 번만 순회 가능)

```python
gen = (x for x in range(5))

print(list(gen))  # [0, 1, 2, 3, 4]
print(list(gen))  # [] - 이미 소진됨!

# 여러 번 사용하려면 리스트로 변환하거나
data = list(x for x in range(5))  # 리스트로 저장

# 또는 매번 새로 생성
def get_gen():
    return (x for x in range(5))

print(list(get_gen()))  # [0, 1, 2, 3, 4]
print(list(get_gen()))  # [0, 1, 2, 3, 4]
```

### 2. 길이 확인 불가

```python
gen = (x for x in range(5))

# len(gen)  # TypeError: object of type 'generator' has no len()

# 길이가 필요하면 리스트로 변환 (Lazy의 이점 상실)
data = list(gen)
print(len(data))  # 5
```

### 3. 인덱싱 불가

```python
gen = (x for x in range(5))

# gen[0]  # TypeError: 'generator' object is not subscriptable

# 특정 인덱스가 필요하면
from itertools import islice
gen = (x for x in range(5))
third = next(islice(gen, 2, 3))  # 인덱스 2의 값
print(third)  # 2
```

### 4. 디버깅 어려움

```python
gen = (x ** 2 for x in range(5))
print(gen)  # <generator object <genexpr> at 0x...>
# 내용을 보려면 list()로 변환해야 함 (소진됨)

# 디버깅 팁: 작은 데이터로 리스트 버전 먼저 테스트
debug_list = [x ** 2 for x in range(5)]
print(debug_list)  # [0, 1, 4, 9, 16]
```

## 코딩테스트 실전 패턴

### 패턴 1: filter() vs 리스트 컴프리헨션

```python
# 문제: n의 배수 고르기

# 방법 1: 리스트 컴프리헨션 (Eager, 권장)
def solution_v1(n, numlist):
    return [x for x in numlist if x % n == 0]

# 방법 2: filter() (Lazy → list로 변환)
def solution_v2(n, numlist):
    return list(filter(lambda v: v % n == 0, numlist))

# 코딩테스트에서는 v1이 더 빠름 (lambda 오버헤드 없음)
```

### 패턴 2: 대용량 데이터에서 조건 만족하는 첫 값

```python
# ❌ 전부 계산 후 첫 번째 선택
def find_first_eager(data):
    processed = [expensive(x) for x in data]  # 전부 계산
    for item in processed:
        if condition(item):
            return item

# ✅ Lazy하게 필요한 것만 계산
def find_first_lazy(data):
    processed = (expensive(x) for x in data)  # Lazy
    for item in processed:
        if condition(item):
            return item  # 찾으면 즉시 종료, 나머지 계산 안 함
```

### 패턴 3: any() / all() 과 함께 (Short-circuit)

```python
nums = range(1000000)

# any() - 하나라도 True면 즉시 반환 (Lazy하게 동작)
result = any(x > 100 for x in nums)  # 101에서 True, 나머지 검사 안 함

# all() - 하나라도 False면 즉시 반환
result = all(x >= 0 for x in nums)  # 전부 검사해야 함 (모두 True)
result = all(x < 500000 for x in nums)  # 500000에서 False, 나머지 검사 안 함
```

### 패턴 4: sum(), max(), min() 과 함께

```python
# 리스트 만들지 않고 바로 집계
total = sum(x ** 2 for x in range(1000))  # 제너레이터 직접 전달
maximum = max(x ** 2 for x in range(1000))
```

## 언제 Lazy를 쓸까?

### ✅ Lazy가 좋은 경우
- 대용량 데이터 처리
- 무한 시퀀스 필요
- 파이프라인 구성
- 조건 만족하는 첫 값만 필요
- 메모리가 제한적인 환경

### ❌ Eager가 좋은 경우
- 여러 번 순회해야 할 때
- 길이나 인덱스 접근이 필요할 때
- 디버깅이 필요할 때
- 데이터가 작을 때 (오버헤드 > 이점)
- 코딩테스트에서 간단한 필터링

## 요약 정리

```
Lazy Evaluation = "필요할 때까지 계산 미루기"

장점: 메모리 효율, 무한 시퀀스, 불필요한 계산 방지
단점: 일회성, len/index 불가, 디버깅 어려움

Python Lazy 타입:
- generator expression: (x for x in ...)
- generator function: yield 사용
- 내장 함수: filter(), map(), zip(), enumerate(), range()
- itertools: count(), islice(), chain(), ...

코딩테스트 팁:
- 단순 필터링 → 리스트 컴프리헨션 (Eager)
- 대용량/첫 값만 필요 → 제너레이터 (Lazy)
- sum/any/all과 함께 → 제너레이터 직접 전달
```

## 관련 노트

- [[generator-expression]] - 제너레이터 표현식 상세
- [[filter-map-reduce]] - 함수형 프로그래밍 도구
- [[time-complexity-guide]] - 시간/공간 복잡도

---

*관련 문제: #120905 n의 배수 고르기 (filter vs list comprehension)*
