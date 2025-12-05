# Dict 삽입 순서 보장

> Python 3.7부터 dict는 삽입 순서를 보장한다

## 버전별 동작

| 버전 | dict 순서 | 비고 |
|------|-----------|------|
| Python 3.5 이하 | ❌ 보장 안 됨 | 해시값 기반 저장 |
| Python 3.6 | ⚠️ CPython만 | 구현 세부사항 |
| **Python 3.7+** | ✅ **공식 스펙** | 모든 구현체에서 보장 |

---

## 왜 순서가 없었을까?

dict는 **해시 테이블**로 구현됨:

```
키 → 해시 함수 → 해시값 → 내부 배열 인덱스
```

해시값에 따라 저장 위치가 결정되므로, 삽입 순서와 저장 순서가 달랐음.

```python
# Python 3.5 이하
d = {'a': 1, 'b': 2, 'c': 3}
print(list(d.keys()))
# 출력: ['b', 'a', 'c']  # 순서 뒤죽박죽!
```

---

## Python 3.7+ 동작

```python
# Python 3.7+
d = {'a': 1, 'b': 2, 'c': 3}
print(list(d.keys()))
# 출력: ['a', 'b', 'c']  # 항상 삽입 순서!

# 중간 삽입/삭제 후에도 순서 유지
d['d'] = 4
del d['b']
print(list(d.keys()))
# 출력: ['a', 'c', 'd']
```

---

## 순서 의존 코드의 위험성

```python
# ⚠️ 순서에 의존하는 로직
discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95}

for threshold, rate in discount_rates.items():
    if price >= threshold:
        return int(price * rate)  # 큰 값부터 검사해야 함!
```

**문제점**: Python 3.6 이하에서는 `100000`이 먼저 검사될 수 있음

---

## 안전한 대안

### 1. list of tuples (권장)

```python
# ✅ 순서가 명시적으로 보장됨
discount_rates = [
    (500000, 0.8),
    (300000, 0.9),
    (100000, 0.95),
]
for threshold, rate in discount_rates:
    if price >= threshold:
        return int(price * rate)
```

### 2. OrderedDict (3.6 이하 호환 필요시)

```python
from collections import OrderedDict

# Python 2.7+ 에서도 순서 보장
discount_rates = OrderedDict([
    (500000, 0.8),
    (300000, 0.9),
    (100000, 0.95),
])
```

### 3. 정렬 후 사용

```python
# 순서가 중요하면 명시적으로 정렬
for threshold in sorted(discount_rates.keys(), reverse=True):
    if price >= threshold:
        return int(price * discount_rates[threshold])
```

---

## 코딩테스트 환경

| 플랫폼 | Python 버전 | dict 순서 |
|--------|-------------|-----------|
| 프로그래머스 | 3.8+ | ✅ 보장 |
| 백준 | 3.11+ | ✅ 보장 |
| LeetCode | 3.10+ | ✅ 보장 |

→ **코테에서는 dict 순서 걱정 없음!**

---

## 언제 뭘 쓸까?

```python
# ✅ dict 사용 OK
config = {'host': 'localhost', 'port': 8080}  # 순서 무관

# ✅ list of tuples 권장
priority_queue = [(1, 'high'), (2, 'medium'), (3, 'low')]  # 순서가 의미 있음

# ✅ OrderedDict (레거시 호환)
# Python 3.6 이하 지원이 필요한 경우만
```

---

## 핵심 정리

1. **Python 3.7+**: dict 삽입 순서 = 공식 스펙
2. **코테 환경**: 모두 3.7+ → 걱정 없음
3. **실무 습관**: 순서가 중요하면 list/tuple이 의도가 더 명확
4. **코드 가독성**: "이 순서가 중요한가?"를 읽는 사람이 바로 알 수 있게

---

*관련 문제: #120818 옷가게 할인 받기*
