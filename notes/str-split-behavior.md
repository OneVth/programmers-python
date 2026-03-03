# Python split() vs split(' ') 동작 차이

## 핵심 차이점

| 특성 | `split()` | `split(' ')` |
|------|-----------|--------------|
| **앞뒤 공백** | 자동 제거 | 빈 문자열 생성 |
| **연속 공백** | 하나의 구분자로 취급 | 공백마다 분리 |
| **결과에 `''`** | 절대 포함 안 됨 | 포함될 수 있음 |
| **대상 공백** | 모든 whitespace (`\t`, `\n` 등) | 정확히 `' '`만 |

## 동작 비교

```python
s = "  i   love  you  "

s.split()      # ['i', 'love', 'you']
s.split(' ')   # ['', '', 'i', '', '', 'love', '', 'you', '', '']
```

### split() — 인자 없음

1. 앞뒤 공백 제거 (strip과 동일)
2. 연속된 공백을 하나의 구분자로 취급
3. 빈 문자열이 결과에 절대 포함되지 않음

```
"  i   love  you  "
 ^^                ^^ → 앞뒤 공백 무시
     ^^^   ^^         → 연속 공백을 하나로 취급
→ ['i', 'love', 'you']
```

### split(' ') — 구분자 지정

1. 앞뒤 공백을 특별 취급하지 않음
2. 공백 한 개마다 정확히 한 번 분리
3. 연속 공백 사이에 빈 문자열 `''`이 생김

```
"  i   love  you  "
^^ → '' '' 'i'
   ^^^ → '' '' 'love'
      ^^ → '' 'you'
        ^^ → '' ''
→ ['', '', 'i', '', '', 'love', '', 'you', '', '']
```

## whitespace 종류별 동작

```python
mixed = "hello\tworld\nfoo  bar"

# split() - 모든 whitespace를 구분자로 처리
mixed.split()      # ['hello', 'world', 'foo', 'bar']

# split(' ') - 공백(' ')만 구분자로 사용
mixed.split(' ')   # ['hello\tworld\nfoo', '', 'bar']

# split('\t') - 탭만 구분자로 사용
mixed.split('\t')  # ['hello', 'world\nfoo  bar']
```

## split(' ')로 같은 결과를 얻으려면

```python
s = "  i   love  you  "

# ❌ split(' ')만으로는 부족
s.split(' ')  # ['', '', 'i', '', '', 'love', '', 'you', '', '']

# 🔺 strip + split + 필터 (비효율)
[x for x in s.strip().split(' ') if x]  # ['i', 'love', 'you']

# ✅ split()이 가장 간결하고 빠름
s.split()  # ['i', 'love', 'you']
```

## 코딩테스트 실전 패턴

### 패턴 1: 공백 구분 단어 추출

```python
# 가장 흔한 패턴 — split() 사용
def solution(my_string):
    return my_string.split()

# " i love you"  → ['i', 'love', 'you']
# " programmers " → ['programmers']
```

### 패턴 2: CSV처럼 정확한 구분자가 있을 때

```python
# 구분자가 명확할 때는 split(구분자) 사용
"1,2,3".split(",")     # ['1', '2', '3']
"a-b-c".split("-")     # ['a', 'b', 'c']
```

### 패턴 3: maxsplit으로 분리 횟수 제한

```python
s = "name age city country"

s.split(maxsplit=1)    # ['name', 'age city country']
s.split(maxsplit=2)    # ['name', 'age', 'city country']

# 구분자 지정 + maxsplit
"a::b::c".split("::", 1)  # ['a', 'b::c']
```

### 패턴 4: join과 조합하여 공백 정규화

```python
# 연속 공백을 단일 공백으로 변환
s = "  hello   world  "
" ".join(s.split())  # "hello world"
```

## 내부 구현 원리

Python 공식 문서 (str.split):

> If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace.

즉, `split()`은 인자가 없으면 **별도의 알고리즘**을 사용합니다.
CPython 내부적으로 `STRINGLIB(split_whitespace)`와 `STRINGLIB(split_char)` 두 가지 C 함수로 나뉘어 구현됩니다.

## 요약 정리

### 선택 기준
- **공백으로 단어 분리** → `split()` (인자 없이)
- **특정 구분자로 분리** → `split(구분자)`
- **공백 정규화** → `" ".join(s.split())`

### 코딩테스트 팁
1. 공백 관련 문자열 문제에서는 `split()`이 거의 항상 정답
2. `split(' ')`은 빈 문자열이 포함되므로 주의
3. `split()`은 `\t`, `\n` 등 모든 whitespace를 처리

## 관련 노트

- [[str-index-vs-find]] - 문자열 검색 메서드
- [[str-translate-maketrans]] - 문자열 변환 메서드
- [[python-slicing]] - 문자열 슬라이싱

---

*관련 문제: #181868 공백으로 구분하기 2*
