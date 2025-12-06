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

## reduce(function, iterable)

요소들을 하나의 값으로 **누적** 계산합니다.

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
