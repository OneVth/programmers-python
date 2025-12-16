# 정규표현식 기초 완벽 정리

## 핵심 패턴 해부

```python
re.compile(r'^(aya|ye|woo|ma)+$')
```

이 패턴을 하나씩 분해해보자:

```
^        (       aya | ye | woo | ma       )        +        $
│        │       └───────┬───────┘         │        │        │
시작     그룹      OR 연산자              그룹끝   1회이상   끝
```

---

## 메타문자 완전 정복

### 위치 지정자 (Anchors)

| 기호 | 의미 | 예시 |
|------|------|------|
| `^` | 문자열 **시작** | `^hello` → "hello world" ✅, "say hello" ❌ |
| `$` | 문자열 **끝** | `world$` → "hello world" ✅, "world war" ❌ |

```python
import re

re.match(r'^hello', 'hello world')  # ✅ Match
re.match(r'^hello', 'say hello')    # ❌ None

re.search(r'world$', 'hello world')  # ✅ Match
re.search(r'world$', 'world war')    # ❌ None
```

### 수량자 (Quantifiers)

| 기호 | 의미 | 예시 |
|------|------|------|
| `+` | **1회 이상** 반복 | `a+` → "a", "aa", "aaa" ✅, "" ❌ |
| `*` | **0회 이상** 반복 | `a*` → "", "a", "aa" 모두 ✅ |
| `?` | **0회 또는 1회** | `a?` → "", "a" ✅, "aa" (첫 a만) |
| `{n}` | **정확히 n회** | `a{3}` → "aaa" ✅, "aa" ❌ |
| `{n,m}` | **n회 ~ m회** | `a{2,4}` → "aa", "aaa", "aaaa" ✅ |

```python
# + vs *의 차이
re.match(r'a+', '')    # ❌ None (1회 이상 필요)
re.match(r'a*', '')    # ✅ Match (0회도 OK)

# 실전 예: 숫자 1개 이상
re.match(r'\d+', '123')   # ✅ Match
re.match(r'\d+', 'abc')   # ❌ None
```

### 그룹과 OR (Groups & Alternation)

| 기호 | 의미 | 예시 |
|------|------|------|
| `(...)` | **그룹화** | `(ab)+` → "ab", "abab" ✅ |
| `\|` | **OR 연산** | `a\|b` → "a" 또는 "b" |
| `(?:...)` | **비캡처 그룹** | 그룹화만, 캡처 안 함 |

```python
# 그룹 없이
re.match(r'ab+', 'abbb')    # "abbb" (b만 반복)

# 그룹으로 묶으면
re.match(r'(ab)+', 'abab')  # "abab" (ab가 반복)

# OR 연산
re.match(r'cat|dog', 'cat')  # ✅ Match
re.match(r'cat|dog', 'dog')  # ✅ Match
```

---

## 옹알이 패턴 완전 분석

```python
pattern = r'^(aya|ye|woo|ma)+$'
```

### 단계별 매칭 과정

```
문자열: "ayaye"
패턴:   ^(aya|ye|woo|ma)+$

Step 1: ^ → 문자열 시작 확인 ✅
Step 2: (aya|ye|woo|ma) → "aya" 매칭 시도
        - "aya" ✅ 매칭! 남은 문자열: "ye"
Step 3: + → 1회 이상이므로 계속 시도
Step 4: (aya|ye|woo|ma) → "ye" 매칭 시도
        - "ye" ✅ 매칭! 남은 문자열: ""
Step 5: $ → 문자열 끝 확인 ✅

결과: 전체 매칭 성공!
```

### 실패 케이스 분석

```
문자열: "wyeoo"
패턴:   ^(aya|ye|woo|ma)+$

Step 1: ^ → 문자열 시작 확인 ✅
Step 2: (aya|ye|woo|ma) → "w"로 시작하는 패턴 없음!
        - "aya" ❌ (w ≠ a)
        - "ye" ❌ (w ≠ y)
        - "woo" ❌ (wye... ≠ woo)
        - "ma" ❌ (w ≠ m)

결과: 매칭 실패! (시작부터 맞는 패턴 없음)
```

---

## re 모듈 주요 함수

### match vs search vs fullmatch

```python
import re

text = "hello world"

# match: 시작부터 매칭
re.match(r'hello', text)   # ✅ Match
re.match(r'world', text)   # ❌ None (시작이 아님)

# search: 어디서든 매칭
re.search(r'hello', text)  # ✅ Match
re.search(r'world', text)  # ✅ Match (중간에서 찾음)

# fullmatch: 전체가 정확히 매칭 (Python 3.4+)
re.fullmatch(r'hello', text)        # ❌ None
re.fullmatch(r'hello world', text)  # ✅ Match
```

### 정리 표

| 함수 | 매칭 범위 | `^$` 필요 |
|------|----------|----------|
| `match` | 시작부터 | `$`만 필요 |
| `search` | 어디서든 | `^$` 둘 다 필요 |
| `fullmatch` | 전체 | 불필요 |

```python
# 옹알이 문제에서 동일한 결과
re.match(r'^(aya|ye)+$', word)      # ^$ 필요
re.fullmatch(r'(aya|ye)+', word)    # ^$ 불필요
```

### compile의 장점

```python
# 매번 컴파일 (비효율)
for word in words:
    if re.match(r'^(aya|ye)+$', word):
        count += 1

# 미리 컴파일 (효율적) ✅
pattern = re.compile(r'^(aya|ye)+$')
for word in words:
    if pattern.match(word):
        count += 1
```

---

## 자주 쓰는 문자 클래스

| 패턴 | 의미 | 동등 표현 |
|------|------|----------|
| `\d` | 숫자 | `[0-9]` |
| `\D` | 숫자 아닌 것 | `[^0-9]` |
| `\w` | 단어 문자 | `[a-zA-Z0-9_]` |
| `\W` | 단어 문자 아닌 것 | `[^a-zA-Z0-9_]` |
| `\s` | 공백 문자 | `[ \t\n\r\f\v]` |
| `\S` | 공백 아닌 것 | `[^ \t\n\r\f\v]` |
| `.` | 아무 문자 (줄바꿈 제외) | |

```python
re.match(r'\d+', '123abc')   # '123' 매칭
re.match(r'\w+', 'hello_1')  # 'hello_1' 매칭
re.match(r'\s+', '   ')      # '   ' 매칭
```

---

## 실전 패턴 모음

### 1. 특정 단어들로만 구성

```python
# 옹알이 패턴
r'^(aya|ye|woo|ma)+$'

# 사용법
words = ["ayaye", "yemawoo", "hello"]
pattern = re.compile(r'^(aya|ye|woo|ma)+$')
valid = [w for w in words if pattern.match(w)]
# ['ayaye', 'yemawoo']
```

### 2. 숫자만

```python
r'^\d+$'

re.match(r'^\d+$', '12345')  # ✅
re.match(r'^\d+$', '123a5')  # ❌
```

### 3. 영문자만

```python
r'^[a-zA-Z]+$'

re.match(r'^[a-zA-Z]+$', 'Hello')  # ✅
re.match(r'^[a-zA-Z]+$', 'Hello1') # ❌
```

### 4. 이메일 (간단 버전)

```python
r'^[\w.+-]+@[\w-]+\.[\w.-]+$'

re.match(r'^[\w.+-]+@[\w-]+\.[\w.-]+$', 'test@example.com')  # ✅
```

### 5. 전화번호

```python
r'^\d{3}-\d{4}-\d{4}$'

re.match(r'^\d{3}-\d{4}-\d{4}$', '010-1234-5678')  # ✅
```

---

## 흔한 실수와 해결

### 실수 1: `^$` 누락

```python
# ❌ 부분 매칭 허용
re.match(r'(aya)+', 'ayaXXX')  # 'aya' 매칭됨!

# ✅ 전체 매칭 강제
re.match(r'^(aya)+$', 'ayaXXX')  # None
```

### 실수 2: 특수문자 이스케이프 누락

```python
# ❌ .은 "아무 문자"를 의미
re.match(r'a.b', 'aXb')  # 매칭됨!

# ✅ 실제 점을 찾으려면
re.match(r'a\.b', 'a.b')  # 매칭됨
```

### 실수 3: 그룹 없이 OR 사용

```python
# ❌ ab 또는 c (의도와 다름)
r'ab|c+'  # "ab" 또는 "c+"

# ✅ a 다음에 b 또는 c
r'a(b|c)+'  # "ab", "ac", "abc", "acb" 등
```

---

## Raw String (r'...')의 의미

```python
# 일반 문자열: 백슬래시가 이스케이프
'\n'     # 줄바꿈 문자
'\\n'    # 백슬래시 + n

# Raw 문자열: 백슬래시 그대로
r'\n'    # 백슬래시 + n (정규표현식용)
```

```python
# 정규표현식에서 \d를 쓰려면
re.match('\\d+', '123')   # 일반 문자열 (\\로 이스케이프)
re.match(r'\d+', '123')   # Raw 문자열 (권장) ✅
```

---

## 요약 - 시험 전 복습용

```
┌─────────────────────────────────────────────────┐
│  정규표현식 핵심 요약                            │
├─────────────────────────────────────────────────┤
│                                                 │
│  ^  시작     $  끝      .  아무문자             │
│  +  1회이상  *  0회이상  ?  0또는1회            │
│  |  OR      ()  그룹    []  문자클래스          │
│                                                 │
│  \d 숫자    \w 단어문자  \s 공백                │
│                                                 │
│  ─────────────────────────────────────────      │
│  옹알이 패턴 분석:                               │
│  ^(aya|ye|woo|ma)+$                             │
│  │ └─────┬─────┘ │                              │
│  │   4개 중 하나  │                              │
│  시작    1회이상   끝                            │
│                                                 │
│  match: 시작부터   fullmatch: 전체              │
│  search: 어디서든  compile: 미리 컴파일         │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 관련 노트

- [[string-pattern-comparison]] - Replace vs 정규표현식 비교

---

*관련 문제: #120956 옹알이*
