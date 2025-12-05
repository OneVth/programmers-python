# Mutable vs Immutable

> Python 객체의 변경 가능 여부에 따른 분류

## 핵심 정의

| 구분 | 의미 | 예시 |
|------|------|------|
| **Mutable** | 생성 후 **값 변경 가능** | list, dict, set |
| **Immutable** | 생성 후 **값 변경 불가** | int, float, str, tuple |

---

## 눈으로 보는 차이

### Mutable (list)

```python
nums = [1, 2, 3]
print(id(nums))  # 140234567890  ← 메모리 주소

nums[0] = 100    # ✅ 값 변경 가능!
print(nums)      # [100, 2, 3]
print(id(nums))  # 140234567890  ← 같은 주소! 원본이 바뀜
```

### Immutable (str)

```python
s = "hello"
print(id(s))     # 140234512345  ← 메모리 주소

s[0] = "H"       # ❌ TypeError: 'str' does not support item assignment

# 변경하려면? → 새 객체 생성
s = "H" + s[1:]
print(s)         # "Hello"
print(id(s))     # 140234599999  ← 다른 주소! 새 객체가 생성됨
```

---

## 왜 이런 구분이 있을까?

### 1. 안전성 (Immutable의 장점)

```python
# 함수에 전달해도 원본이 안전
def process(text):
    text = text.upper()  # 새 객체 생성, 원본 무관
    return text

original = "hello"
result = process(original)
print(original)  # "hello" ← 원본 그대로!
```

### 2. 효율성 (Mutable의 장점)

```python
# 큰 리스트를 매번 복사하면 비효율
nums = [1, 2, 3, ..., 1000000]
nums.append(1000001)  # ✅ 원본에 바로 추가 (빠름)

# 만약 immutable이었다면?
# nums = nums + [1000001]  # ❌ 전체 복사 필요 (느림)
```

---

## 실전 주의사항

### 함수 인자로 mutable 전달 시

```python
def add_item(lst):
    lst.append(100)  # ⚠️ 원본이 바뀜!

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)  # [1, 2, 3, 100]  ← 원본이 변경됨!
```

### 기본 인자로 mutable 사용 금지

```python
# ❌ 위험한 패턴 (면접 단골 질문!)
def append_to(item, lst=[]):
    lst.append(item)
    return lst

print(append_to(1))  # [1]
print(append_to(2))  # [1, 2]  ← 이전 호출 결과가 남아있음!

# ✅ 올바른 패턴
def append_to(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

---

## 타입별 정리

| Immutable | Mutable |
|-----------|---------|
| `int`, `float`, `bool` | `list` |
| `str` | `dict` |
| `tuple` | `set` |
| `frozenset` | `bytearray` |

---

## dict key 제약

```python
# ✅ immutable은 dict key로 사용 가능
d = {
    "name": "Alice",      # str
    1: "one",             # int
    (1, 2): "tuple_key",  # tuple
}

# ❌ mutable은 dict key로 사용 불가
d = {
    [1, 2]: "list_key"    # TypeError: unhashable type: 'list'
}
```

**이유**: dict는 내부적으로 해시값을 사용하는데, mutable 객체는 값이 바뀌면 해시값도 바뀌어 문제가 됨.

---

## id() 함수로 확인하기

```python
# 같은 객체인지 확인
a = [1, 2, 3]
b = a           # 같은 객체 참조
c = a[:]        # 복사 (새 객체)

print(id(a) == id(b))  # True  ← 같은 객체
print(id(a) == id(c))  # False ← 다른 객체

# is 연산자도 동일
print(a is b)  # True
print(a is c)  # False
```

---

## 핵심 정리

1. **Mutable**: 원본 수정 가능, 메모리 효율적, 부작용 주의
2. **Immutable**: 원본 안전, 새 객체 생성 필요, 해시 가능
3. **함수 주의**: mutable 인자는 원본이 수정될 수 있음
4. **기본 인자**: mutable을 기본값으로 사용하지 말 것 (None 사용)
5. **dict key**: immutable만 사용 가능

---

*관련 문제: #120822 뒤집힌 문자열 (문자열은 immutable)*
