# 정규표현식 (Regular Expression)

## 정규표현식이란?

문자열에서 특정 **패턴**을 찾거나, 바꾸거나, 검증할 때 사용하는 표현 언어입니다.

```python
import re

# 문자열에서 숫자만 찾기
re.findall(r'\d', "hello123")  # ['1', '2', '3']

# 이메일 형식 검증
re.match(r'\w+@\w+\.\w+', "test@email.com")  # Match!
```

---

## Python re 모듈 핵심 함수

| 함수 | 용도 | 반환값 |
|------|------|--------|
| `re.findall(pattern, string)` | 모든 매칭 찾기 | `list` |
| `re.search(pattern, string)` | 첫 번째 매칭 찾기 | `Match` 객체 or `None` |
| `re.match(pattern, string)` | **문자열 시작부터** 매칭 | `Match` 객체 or `None` |
| `re.sub(pattern, repl, string)` | 패턴을 다른 문자로 치환 | `str` |
| `re.split(pattern, string)` | 패턴으로 문자열 분리 | `list` |

### 사용 예시

```python
import re

text = "My phone: 010-1234-5678, Office: 02-999-8888"

# findall: 모든 매칭을 리스트로
re.findall(r'\d+', text)  # ['010', '1234', '5678', '02', '999', '8888']

# search: 첫 번째 매칭만 (Match 객체 반환)
match = re.search(r'\d{3}-\d{4}-\d{4}', text)
match.group()  # '010-1234-5678'

# match: 문자열 시작부터 매칭해야 함
re.match(r'My', text)    # Match!
re.match(r'phone', text) # None (시작이 아님)

# sub: 치환
re.sub(r'\d', '*', text)  # 'My phone: ***-****-****, Office: **-***-****'

# split: 분리
re.split(r'[-,]', "a-b,c-d")  # ['a', 'b', 'c', 'd']
```

---

## 메타 문자 (특수 문자)

### 문자 클래스

| 패턴 | 의미 | 동등 표현 |
|------|------|----------|
| `\d` | 숫자 | `[0-9]` |
| `\D` | 숫자가 아닌 것 | `[^0-9]` |
| `\w` | 단어 문자 (영문, 숫자, _) | `[a-zA-Z0-9_]` |
| `\W` | 단어 문자가 아닌 것 | `[^a-zA-Z0-9_]` |
| `\s` | 공백 문자 (스페이스, 탭, 줄바꿈) | `[ \t\n\r\f\v]` |
| `\S` | 공백이 아닌 것 | `[^ \t\n\r\f\v]` |
| `.` | 아무 문자 (줄바꿈 제외) | - |

```python
re.findall(r'\d', "a1b2c3")     # ['1', '2', '3']
re.findall(r'\w', "Hi! 안녕")   # ['H', 'i', '안', '녕']
re.findall(r'\s', "a b\tc")     # [' ', '\t']
re.findall(r'.', "ab\nc")       # ['a', 'b', 'c'] (줄바꿈 제외)
```

### 위치 지정

| 패턴 | 의미 |
|------|------|
| `^` | 문자열의 시작 |
| `$` | 문자열의 끝 |
| `\b` | 단어 경계 (word boundary) |

```python
re.findall(r'^Hello', "Hello World")  # ['Hello']
re.findall(r'World$', "Hello World")  # ['World']
re.findall(r'\bcat\b', "cat catalog") # ['cat'] (catalog의 cat은 매칭 안됨)
```

---

## 수량자 (반복)

| 패턴 | 의미 | 예시 |
|------|------|------|
| `*` | 0회 이상 | `a*` → "", "a", "aa", "aaa" |
| `+` | 1회 이상 | `a+` → "a", "aa", "aaa" |
| `?` | 0회 또는 1회 | `a?` → "", "a" |
| `{n}` | 정확히 n회 | `a{3}` → "aaa" |
| `{n,}` | n회 이상 | `a{2,}` → "aa", "aaa", ... |
| `{n,m}` | n회 이상 m회 이하 | `a{2,4}` → "aa", "aaa", "aaaa" |

```python
re.findall(r'\d+', "a1bb22ccc333")   # ['1', '22', '333']
re.findall(r'\d{2}', "a1bb22ccc333") # ['22', '33']
re.findall(r'\d{2,}', "1 22 333")    # ['22', '333']
```

### Greedy vs Non-Greedy

기본적으로 수량자는 **탐욕적(greedy)** - 최대한 많이 매칭

```python
text = "<div>Hello</div>"

# Greedy (기본): 최대한 많이
re.findall(r'<.*>', text)   # ['<div>Hello</div>']

# Non-Greedy (?): 최소한으로
re.findall(r'<.*?>', text)  # ['<div>', '</div>']
```

---

## 문자 집합 `[]`

| 패턴 | 의미 |
|------|------|
| `[abc]` | a, b, c 중 하나 |
| `[a-z]` | a부터 z까지 소문자 |
| `[A-Z]` | 대문자 |
| `[0-9]` | 숫자 (= `\d`) |
| `[^abc]` | a, b, c가 아닌 것 |
| `[a-zA-Z]` | 모든 영문자 |

```python
re.findall(r'[aeiou]', "hello")     # ['e', 'o'] (모음만)
re.findall(r'[^aeiou]', "hello")    # ['h', 'l', 'l'] (모음 제외)
re.findall(r'[a-z]+', "Hello123")   # ['ello']
re.findall(r'[a-zA-Z]+', "Hello123") # ['Hello']
```

---

## 그룹화 `()`

### 기본 그룹화

```python
# 전화번호에서 지역번호와 나머지 분리
text = "010-1234-5678"
match = re.match(r'(\d{3})-(\d{4})-(\d{4})', text)

match.group(0)  # '010-1234-5678' (전체)
match.group(1)  # '010' (첫 번째 그룹)
match.group(2)  # '1234' (두 번째 그룹)
match.groups()  # ('010', '1234', '5678')
```

### findall과 그룹

```python
# 그룹이 있으면 그룹만 반환
re.findall(r'(\d{3})-(\d{4})', "010-1234, 02-5678")
# [('010', '1234'), ('02', '5678')]

# 전체 매칭을 원하면 non-capturing group 사용
re.findall(r'(?:\d{3})-(?:\d{4})', "010-1234, 02-5678")
# ['010-1234', '02-5678']
```

### OR 연산 `|`

```python
re.findall(r'cat|dog', "I have a cat and a dog")  # ['cat', 'dog']
re.findall(r'(Mr|Mrs|Ms)\.', "Mr. Kim, Mrs. Lee") # ['Mr', 'Mrs']
```

---

## 자주 사용하는 패턴

### 숫자 관련

```python
# 정수
r'-?\d+'                    # -123, 456

# 소수점 포함
r'-?\d+\.?\d*'              # -123, 45.67

# 콤마 포함 숫자
r'\d{1,3}(,\d{3})*'         # 1,000,000
```

### 문자열 관련

```python
# 영문자만
r'[a-zA-Z]+'

# 한글만
r'[가-힣]+'

# 영문+숫자 (알파벳과 숫자)
r'[a-zA-Z0-9]+'

# 공백으로 구분된 단어
r'\S+'
```

### 검증 패턴

```python
# 이메일 (간단 버전)
r'[\w.-]+@[\w.-]+\.\w+'

# 전화번호 (한국)
r'0\d{1,2}-\d{3,4}-\d{4}'

# URL (간단 버전)
r'https?://[\w./%-]+'

# 날짜 (YYYY-MM-DD)
r'\d{4}-\d{2}-\d{2}'
```

---

## 코딩 테스트 활용 예시

### 1. 특정 문자 제거

```python
# 모음 제거
re.sub(r'[aeiou]', '', "hello")  # 'hll'

# 숫자만 남기기
re.sub(r'[^0-9]', '', "a1b2c3")  # '123'

# 영문자만 남기기
re.sub(r'[^a-zA-Z]', '', "Hi! 123")  # 'Hi'
```

### 2. 숫자 추출

```python
# 모든 숫자 추출
re.findall(r'\d', "a1b2c3")       # ['1', '2', '3']

# 연속된 숫자 추출
re.findall(r'\d+', "a12b345c6")   # ['12', '345', '6']

# 숫자를 정수로 변환
[int(x) for x in re.findall(r'\d+', "12 apples, 5 oranges")]  # [12, 5]
```

### 3. 문자열 분리

```python
# 여러 구분자로 분리
re.split(r'[,;:\s]+', "a,b;c:d e")  # ['a', 'b', 'c', 'd', 'e']

# 숫자와 문자 분리
re.split(r'(\d+)', "abc123def456")  # ['abc', '123', 'def', '456', '']
```

### 4. 패턴 치환

```python
# 연속 공백을 하나로
re.sub(r'\s+', ' ', "a   b    c")  # 'a b c'

# 민감정보 마스킹
re.sub(r'\d{4}', '****', "010-1234-5678")  # '010-****-****'
```

---

## Raw String `r''`

정규표현식에서는 항상 **raw string** (`r''`)을 사용하세요!

```python
# 백슬래시 문제
'\\d'   # 일반 문자열: 실제로는 '\d' (2글자)
r'\d'   # raw string: 그대로 '\d' (2글자, 정규식으로 해석)

# 실제 차이
print('\\n')   # 줄바꿈 아닌 '\n' 출력
print(r'\n')   # '\n' 그대로 출력

# 정규표현식에서
re.findall('\\d+', '123')   # 동작하지만 가독성 떨어짐
re.findall(r'\d+', '123')   # 권장!
```

---

## 요약 치트시트

```
문자 클래스:  \d(숫자) \w(단어) \s(공백)  대문자는 반대
수량자:       *(0+) +(1+) ?(0-1) {n} {n,m}
위치:         ^(시작) $(끝) \b(단어경계)
집합:         [abc] [a-z] [^abc]
그룹:         () (?:) |
Non-greedy:   *? +? ??

주요 함수:
  findall  → 모든 매칭 리스트
  search   → 첫 매칭 (어디서든)
  match    → 첫 매칭 (시작부터)
  sub      → 치환
  split    → 분리
```
