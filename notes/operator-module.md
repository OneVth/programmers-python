# Python `operator` 모듈

> 연산자를 함수로 사용할 수 있게 해주는 표준 라이브러리

## 왜 필요한가?

Python에서 `+`, `-`, `*` 같은 연산자는 그 자체로 함수가 아니라서 변수에 담거나 인자로 전달할 수 없습니다.

```python
# ❌ 불가능
op = +
result = op(3, 5)

# ✅ operator 모듈 사용
import operator
op = operator.add
result = op(3, 5)  # 8
```

## 주요 함수들

### 산술 연산자

| 연산자 | operator 함수 | 동작 |
|--------|---------------|------|
| `a + b` | `operator.add(a, b)` | 덧셈 |
| `a - b` | `operator.sub(a, b)` | 뺄셈 |
| `a * b` | `operator.mul(a, b)` | 곱셈 |
| `a / b` | `operator.truediv(a, b)` | 나눗셈 (실수) |
| `a // b` | `operator.floordiv(a, b)` | 나눗셈 (정수) |
| `a % b` | `operator.mod(a, b)` | 나머지 |
| `a ** b` | `operator.pow(a, b)` | 거듭제곱 |
| `-a` | `operator.neg(a)` | 부호 반전 |

### 비교 연산자

| 연산자 | operator 함수 | 동작 |
|--------|---------------|------|
| `a == b` | `operator.eq(a, b)` | 같음 |
| `a != b` | `operator.ne(a, b)` | 다름 |
| `a < b` | `operator.lt(a, b)` | 작음 |
| `a <= b` | `operator.le(a, b)` | 작거나 같음 |
| `a > b` | `operator.gt(a, b)` | 큼 |
| `a >= b` | `operator.ge(a, b)` | 크거나 같음 |

### 논리 연산자

| 연산자 | operator 함수 | 동작 |
|--------|---------------|------|
| `not a` | `operator.not_(a)` | 논리 부정 |
| `a and b` | `operator.and_(a, b)` | 비트 AND |
| `a or b` | `operator.or_(a, b)` | 비트 OR |

> ⚠️ `and_`, `or_`, `not_`는 **비트 연산**입니다. 논리 연산 `and`, `or`와 다릅니다!

### 아이템/속성 접근

| 표현식 | operator 함수 | 동작 |
|--------|---------------|------|
| `obj[k]` | `operator.getitem(obj, k)` | 인덱싱 |
| `obj[k] = v` | `operator.setitem(obj, k, v)` | 아이템 설정 |
| `obj.attr` | `operator.attrgetter('attr')` | 속성 접근 (함수 반환) |

## 실전 활용 패턴

### 1. 딕셔너리 디스패치 (조건문 대체)

```python
import operator

def calculate(a: int, op: str, b: int) -> int:
    """조건문 없이 연산자 매핑으로 계산"""
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    return ops[op](a, b)

calculate(10, '+', 5)  # 15
calculate(10, '*', 5)  # 50
```

**장점:**
- 조건문보다 깔끔하고 확장성 좋음
- Open-Closed Principle 준수 (새 연산자는 딕셔너리에 추가만)

### 2. 고차 함수와 함께 사용

```python
from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]

# 모든 요소의 곱
product = reduce(operator.mul, numbers)  # 120

# 모든 요소의 합 (sum과 동일)
total = reduce(operator.add, numbers)  # 15
```

### 3. 정렬 키 함수로 활용

```python
import operator

# 튜플 리스트를 특정 인덱스로 정렬
data = [('Alice', 25), ('Bob', 30), ('Charlie', 20)]

# 나이(인덱스 1)로 정렬
sorted(data, key=operator.itemgetter(1))
# [('Charlie', 20), ('Alice', 25), ('Bob', 30)]

# 객체 속성으로 정렬
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person('Alice', 25), Person('Bob', 30)]
sorted(people, key=operator.attrgetter('age'))
```

### 4. `itemgetter`로 다중 키 정렬

```python
import operator

data = [
    {'name': 'Alice', 'age': 25, 'score': 90},
    {'name': 'Bob', 'age': 25, 'score': 85},
    {'name': 'Charlie', 'age': 30, 'score': 90},
]

# 나이 오름차순, 점수 내림차순 정렬
sorted(data, key=lambda x: (x['age'], -x['score']))

# itemgetter 사용 (단일 키만 가능, 다중 키는 lambda가 더 유연)
sorted(data, key=operator.itemgetter('age', 'score'))
```

## lambda vs operator

```python
# lambda 방식
sorted(data, key=lambda x: x[1])
reduce(lambda a, b: a + b, numbers)

# operator 방식
sorted(data, key=operator.itemgetter(1))
reduce(operator.add, numbers)
```

| 비교 | lambda | operator |
|------|--------|----------|
| 가독성 | 의도가 명확할 때 좋음 | 연산자 의미가 직관적 |
| 성능 | 약간 느림 (함수 생성) | 약간 빠름 (C 구현) |
| 유연성 | 복잡한 로직 가능 | 단순 연산에 적합 |

## 실전 예제: 간단한 식 계산하기

```python
# 프로그래머스 #181865
import operator

def solution(binomial: str) -> int:
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    a, op, b = binomial.split()
    return ops[op](int(a), int(b))
```

## 요약

1. **operator 모듈**은 연산자를 함수로 사용할 수 있게 해줌
2. **딕셔너리 디스패치** 패턴으로 조건문 대체 가능
3. **reduce**, **sorted** 등 고차 함수와 조합하면 강력함
4. **itemgetter**, **attrgetter**로 정렬 키 함수 간결하게 작성
5. 단순 연산은 operator가 lambda보다 약간 빠르고 명확함

## 참고

- [Python 공식 문서 - operator](https://docs.python.org/3/library/operator.html)
- 관련 노트: `filter-map-reduce.md`, `multi-key-sorting.md`
