# filter, map, reduce - Python 함수형 프로그래밍

## filter(function, iterable)

조건을 만족하는 요소만 **필터링**해서 반환합니다.

```python
# 기본 구조
filter(조건_함수, 반복가능한_객체)

# 예시: 짝수만 필터링
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4, 6]

# 약수 필터링
n = 20
divisors = filter(lambda i: n % i == 0, range(1, n + 1))
print(list(divisors))  # [1, 2, 4, 5, 10, 20]
```

### 주의: iterator 반환
```python
result = filter(lambda x: x > 0, [1, -2, 3])
print(result)        # <filter object at 0x...>  ← 객체!
print(list(result))  # [1, 3]  ← list()로 변환 필요
```

## map(function, iterable)

모든 요소에 함수를 **적용**해서 반환합니다.

```python
# 기본 구조
map(변환_함수, 반복가능한_객체)

# 예시: 제곱
numbers = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))  # [1, 4, 9, 16]

# 문자열 → 정수 변환
strings = ["1", "2", "3"]
ints = list(map(int, strings))  # [1, 2, 3]
```

## reduce(function, iterable) - Python의 Aggregate

요소들을 하나의 값으로 **누적** 계산합니다.
다른 언어의 `aggregate`, `fold`와 동일한 개념입니다.

```python
from functools import reduce

# 기본 구조
reduce(누적_함수, 반복가능한_객체, 초기값)

# 예시: 합계
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15

# 예시: 최댓값
max_val = reduce(lambda a, b: a if a > b else b, numbers)
print(max_val)  # 5

# 예시: 곱
product = reduce(lambda acc, x: acc * x, numbers, 1)
print(product)  # 120
```

### 다른 언어와 비교

| 언어 | 함수명 | 예시 |
|------|--------|------|
| Python | `reduce` | `reduce(lambda a,b: a+b, lst)` |
| JavaScript | `reduce` | `arr.reduce((a,b) => a+b)` |
| C# | `Aggregate` | `list.Aggregate((a,b) => a+b)` |
| Kotlin | `fold/reduce` | `list.fold(0) { a,b -> a+b }` |
| Java | `reduce` | `stream.reduce(0, (a,b) -> a+b)` |

### reduce vs 전용 함수

**전용 함수가 있으면 그걸 쓰자!**

```python
from functools import reduce
from math import prod

# ❌ reduce 사용 (불필요하게 복잡)
reduce(lambda a, b: a + b, lst)      # 합계
reduce(lambda a, b: a * b, lst)      # 곱
reduce(lambda a, b: a if a > b else b, lst)  # 최대

# ✅ 전용 함수 사용 (간결하고 빠름)
sum(lst)       # 합계
prod(lst)      # 곱 (Python 3.8+)
max(lst)       # 최대
min(lst)       # 최소
```

### reduce를 써야 할 때

**커스텀 누적 연산**이 필요할 때만 사용:

```python
# 1. 복합 객체 누적
data = [{"name": "A", "score": 80}, {"name": "B", "score": 90}]
total_score = reduce(lambda acc, x: acc + x["score"], data, 0)

# 2. 조건부 누적
numbers = [1, -2, 3, -4, 5]
positive_sum = reduce(lambda acc, x: acc + x if x > 0 else acc, numbers, 0)

# 3. 중첩 구조 평탄화
nested = [[1, 2], [3, 4], [5]]
flat = reduce(lambda acc, x: acc + x, nested, [])  # [1, 2, 3, 4, 5]

# 4. 파이프라인 함수 합성
funcs = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
pipeline = reduce(lambda f, g: lambda x: g(f(x)), funcs)
print(pipeline(3))  # ((3+1)*2)^2 = 64
```

### Python 3에서 functools로 옮겨진 이유

> "명시적인 것이 암시적인 것보다 낫다" - Zen of Python

- `reduce`는 가독성이 떨어지고 남용되기 쉬움
- 대부분의 경우 `sum()`, `max()`, comprehension으로 대체 가능
- 정말 필요할 때만 명시적으로 import해서 사용하도록 유도

## 함수형 vs Comprehension 비교

| 방식 | filter | map |
|------|--------|-----|
| 함수형 | `list(filter(lambda x: x>0, lst))` | `list(map(lambda x: x*2, lst))` |
| Comprehension | `[x for x in lst if x>0]` | `[x*2 for x in lst]` |

### Python에서는 Comprehension 선호!
```python
# ❌ 함수형 (덜 Pythonic)
list(filter(lambda x: x % 2 == 0, range(10)))

# ✅ List Comprehension (Pythonic)
[x for x in range(10) if x % 2 == 0]

# ✅ Generator Expression (메모리 효율)
sum(x for x in range(10) if x % 2 == 0)
```

### 언제 filter/map을 쓸까?
- 이미 정의된 함수가 있을 때: `list(map(int, strings))`
- 함수형 프로그래밍 스타일이 필요할 때
- 다른 언어(JavaScript, Java Stream)와 일관성이 필요할 때

## 실전 예시

```python
# 문자열 리스트 → 정수 변환 후 양수만 필터링
data = ["1", "-2", "3", "-4", "5"]

# 함수형
result = list(filter(lambda x: x > 0, map(int, data)))

# Comprehension (더 읽기 쉬움)
result = [int(x) for x in data if int(x) > 0]

# 결과: [1, 3, 5]
```
