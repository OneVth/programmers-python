# Walrus Operator (`:=`)

## 개요

Python 3.8에서 도입된 **Assignment Expression** (할당 표현식)입니다.
바다코끼리(walrus)의 눈과 이빨을 닮아서 "Walrus Operator"라고 부릅니다.

```
:=  ←  바다코끼리 얼굴처럼 생김 🦭
```

## 기본 문법

```python
# 표현식 내에서 변수에 값을 할당하면서 동시에 그 값을 사용
(variable := expression)
```

**핵심**: 값을 **할당하면서 동시에 반환**

---

## 기존 방식 vs Walrus Operator

### 예시 1: 조건문에서 사용

```python
# ❌ 기존 방식 - 두 줄 필요
data = get_data()
if data:
    process(data)

# ✅ walrus operator - 한 줄로
if (data := get_data()):
    process(data)
```

### 예시 2: while 루프

```python
# ❌ 기존 방식
line = input()
while line != "quit":
    process(line)
    line = input()

# ✅ walrus operator
while (line := input()) != "quit":
    process(line)
```

### 예시 3: 리스트 컴프리헨션

```python
# ❌ 기존 방식 - 함수를 두 번 호출
results = [func(x) for x in items if func(x) > 0]

# ✅ walrus operator - 함수를 한 번만 호출
results = [y for x in items if (y := func(x)) > 0]
```

---

## 실전 활용 예시

### 1. 파일 읽기

```python
# ❌ 기존 방식
while True:
    chunk = file.read(1024)
    if not chunk:
        break
    process(chunk)

# ✅ walrus operator
while (chunk := file.read(1024)):
    process(chunk)
```

### 2. 정규표현식 매칭

```python
import re

# ❌ 기존 방식
match = re.search(r'\d+', text)
if match:
    print(match.group())

# ✅ walrus operator
if (match := re.search(r'\d+', text)):
    print(match.group())
```

### 3. len()과 함께 사용

```python
# ❌ 기존 방식
tokens = s.split()
for i in range(len(tokens)):
    print(tokens[i])

# ✅ walrus operator
for i in range(len(tokens := s.split())):
    print(tokens[i])
```

### 4. 딕셔너리 get()과 함께

```python
# ❌ 기존 방식
value = data.get("key")
if value is not None:
    process(value)

# ✅ walrus operator
if (value := data.get("key")) is not None:
    process(value)
```

---

## 코딩 테스트 활용

### 패턴 1: 조건부 처리

```python
# 리스트에서 조건 만족하는 첫 요소 찾아서 처리
if (found := next((x for x in items if x > 10), None)):
    print(f"Found: {found}")
```

### 패턴 2: 중복 계산 방지

```python
# 비용이 큰 연산 결과를 재사용
filtered = [
    (n, sqrt)
    for n in numbers
    if (sqrt := n ** 0.5) == int(sqrt)  # 제곱수만 필터링
]
```

### 패턴 3: 누적 계산

```python
# running total 계산
total = 0
running_totals = [(total := total + x) for x in [1, 2, 3, 4, 5]]
# [1, 3, 6, 10, 15]
```

---

## 주의사항

### 1. 괄호 필요한 경우가 많음

```python
# ❌ 에러
if x := get_value() > 0:  # 우선순위 문제

# ✅ 괄호로 명확하게
if (x := get_value()) > 0:
```

### 2. 일반 할당(`=`)과 다름

```python
# = 는 문(statement), 표현식 내에서 사용 불가
# := 는 표현식(expression), 표현식 내에서 사용 가능

x = 5        # 할당문 (statement)
print(x)     # 5

print(y := 10)  # 할당 표현식 - 할당하면서 값 반환
# 10
```

### 3. 람다에서는 사용 불가

```python
# ❌ 람다 내에서 walrus operator 사용 불가
f = lambda: (x := 10)  # SyntaxError
```

### 4. 컴프리헨션 스코프 주의

```python
# 컴프리헨션 내 walrus는 바깥 스코프에 변수 생성
[y := x * 2 for x in range(3)]
print(y)  # 4 (마지막 값이 바깥에 남음)
```

---

## 언제 사용할까?

### ✅ 사용하면 좋은 경우

1. **중복 계산 방지**: 비용이 큰 함수를 한 번만 호출하고 싶을 때
2. **조건문 + 할당**: if/while에서 값을 검사하면서 저장할 때
3. **코드 간결화**: 임시 변수 줄이고 싶을 때

### ❌ 피해야 하는 경우

1. **가독성 저하**: 복잡해지면 오히려 읽기 어려움
2. **남용**: 모든 곳에 쓰면 코드가 cryptic해짐
3. **팀 규칙**: 팀에서 사용 금지하는 경우

---

## 요약

```python
# Walrus Operator := (Python 3.8+)
# 표현식 내에서 할당 + 값 반환을 동시에

# 기본 패턴
if (x := expensive_func()):
    use(x)

while (data := get_data()):
    process(data)

[y for x in items if (y := func(x)) > 0]

# 핵심: 중복 계산 방지, 코드 간결화
# 주의: 가독성 > 간결함, 남용 금지
```
