# str.translate() & str.maketrans()

Python의 문자열 일괄 치환을 위한 내장 메서드.

## 기본 사용법

### `str.maketrans(x, y)` — 변환 테이블 생성

```python
table = str.maketrans("abc", "xyz")
# 결과: {97: 120, 98: 121, 99: 122}
# ord('a')→ord('x'), ord('b')→ord('y'), ord('c')→ord('z')
```

### `str.translate(table)` — 변환 테이블 적용

```python
"abc".translate(table)  # → "xyz"
"cab".translate(table)  # → "zxy"
```

## maketrans 시그니처

```python
# 형태 1: 두 문자열 (1:1 매핑)
str.maketrans("abc", "xyz")

# 형태 2: 딕셔너리
str.maketrans({"a": "x", "b": "y", "c": "z"})

# 형태 3: 삭제할 문자 지정 (3번째 인자)
str.maketrans("", "", "aeiou")  # 모음 삭제용 테이블
```

## 활용 예시

### 1. 숫자 → 알파벳 변환
```python
"123".translate(str.maketrans("0123456789", "abcdefghij"))
# → "bcd"
```

### 2. 특정 문자 삭제
```python
"hello world".translate(str.maketrans("", "", "aeiou"))
# → "hll wrld" (모음 삭제)
```

### 3. 시저 암호 (ROT13)
```python
import string
rot13 = str.maketrans(
    string.ascii_lowercase + string.ascii_uppercase,
    string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
    string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
)
"hello".translate(rot13)  # → "uryyb"
```

### 4. 구두점 제거
```python
import string
"Hello, World!".translate(str.maketrans("", "", string.punctuation))
# → "Hello World"
```

## 성능 비교

| 방법 | 코드 | 시간복잡도 | 비고 |
|------|------|-----------|------|
| for 루프 | `"".join(d[c] for c in s)` | O(n) | Python 레벨 |
| replace 체인 | `s.replace('a','x').replace(...)` | O(n*k) | k번 순회 |
| **translate** | `s.translate(table)` | O(n) | C 레벨, 최적화 |

## 왜 translate가 빠른가?

1. **C 레벨 구현**: CPython 인터프리터 내부에서 최적화
2. **단일 순회**: 문자열을 한 번만 순회
3. **해시 테이블**: O(1) 조회로 각 문자 변환
4. **메모리 효율**: 중간 문자열 생성 최소화

## 주의사항

- `maketrans`의 두 문자열은 **길이가 같아야** 함
- 유니코드 문자도 지원
- 테이블에 없는 문자는 그대로 유지됨

## 코딩테스트 활용

- 문자 치환/인코딩 문제
- 암호화/복호화 문제
- 문자열 정제 (특수문자 제거)
- 대소문자 변환 커스터마이징
