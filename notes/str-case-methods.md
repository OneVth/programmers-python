# Python 문자열 대소문자 메서드

> `swapcase()` 등 코테에서 유용하지만 잊기 쉬운 메서드들

## 대소문자 변환 메서드

```python
s = "hELLo WoRLd"
```

| 메서드 | 결과 | 설명 |
|--------|------|------|
| `s.upper()` | `"HELLO WORLD"` | 전체 대문자 |
| `s.lower()` | `"hello world"` | 전체 소문자 |
| `s.swapcase()` | `"HellO wOrLd"` | 대↔소 토글 |
| `s.capitalize()` | `"Hello world"` | 첫 글자만 대문자, 나머지 소문자 |
| `s.title()` | `"Hello World"` | 각 단어 첫 글자 대문자 |
| `s.casefold()` | `"hello world"` | 더 강력한 소문자 (독일어 ß → ss) |

---

## 대소문자 판별 메서드

```python
"ABC".isupper()    # True - 모두 대문자
"abc".islower()    # True - 모두 소문자
"Abc".istitle()    # True - 타이틀 케이스
"A".isalpha()      # True - 알파벳만
```

---

## swapcase() 활용 예시

### 문제: 대소문자 토글
```python
# ❌ 직접 구현
"".join(c.upper() if c.islower() else c.lower() for c in s)

# ✅ 내장 메서드
s.swapcase()
```

### 문제: 대문자 개수 세기
```python
sum(1 for c in s if c.isupper())
# 또는
sum(c.isupper() for c in s)  # bool은 int로 자동 변환
```

---

## capitalize() vs title()

```python
s = "hello world"

s.capitalize()  # "Hello world" - 문자열 전체에서 첫 글자만
s.title()       # "Hello World" - 각 단어의 첫 글자
```

### title() 주의사항

```python
"it's a test".title()  # "It'S A Test" - 아포스트로피 후도 대문자!
"hello-world".title()  # "Hello-World" - 하이픈 후도 대문자
```

---

## casefold() vs lower()

```python
# 대부분의 경우 동일
"ABC".lower()     # "abc"
"ABC".casefold()  # "abc"

# 독일어 등 특수 케이스에서 차이
"ß".lower()       # "ß" (그대로)
"ß".casefold()    # "ss" (더 강력한 변환)
```

**용도**: 대소문자 구분 없는 문자열 비교 시 `casefold()` 권장

```python
# 대소문자 무시 비교
s1.casefold() == s2.casefold()
```

---

## 코테 빈출 패턴

### 1. 대소문자 토글
```python
my_string.swapcase()
```

### 2. 첫 글자만 대문자
```python
my_string.capitalize()
# 또는
my_string[0].upper() + my_string[1:]  # 원본이 소문자가 아닐 때
```

### 3. 대문자/소문자 개수
```python
upper_count = sum(c.isupper() for c in s)
lower_count = sum(c.islower() for c in s)
```

### 4. 알파벳만 추출
```python
"".join(c for c in s if c.isalpha())
```

### 5. 대소문자 무시 정렬
```python
sorted(words, key=str.lower)
# 또는
sorted(words, key=str.casefold)
```

---

## 핵심 정리

| 목적 | 메서드 |
|------|--------|
| 전체 대문자 | `upper()` |
| 전체 소문자 | `lower()` |
| **대↔소 토글** | `swapcase()` ⭐ |
| 첫 글자 대문자 | `capitalize()` |
| 단어별 대문자 | `title()` |
| 강력한 소문자 | `casefold()` |

---

*관련 문제: #120893 대문자와 소문자*
