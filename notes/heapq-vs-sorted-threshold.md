# heapq.nsmallest vs sorted() - 성능 임계점 분석

> 관련 노트: [heapq-nsmallest-nlargest.md](./heapq-nsmallest-nlargest.md)

## 핵심 질문

**"k가 n의 몇 %일 때 sorted()가 heapq보다 빠를까?"**

---

## 이론 vs 현실

### 이론적 시간복잡도

| 방법 | 시간복잡도 |
|------|-----------|
| `heapq.nsmallest(k, lst)` | O(n log k) |
| `sorted(lst)[:k]` | O(n log n) |

이론상 **항상** heapq가 유리해 보이지만, 현실은 다릅니다.

### 현실적 고려사항

1. **상수 계수 (constant factor)**: Big-O는 상수를 무시하지만, 실제 실행 시간에는 큰 영향
2. **Timsort 최적화**: Python의 sorted()는 실제 데이터 패턴에 최적화된 Timsort 사용
3. **캐시 친화성**: sorted()는 메모리를 순차적으로 접근, 힙은 불규칙적 접근
4. **C 구현**: sorted()는 완전히 C로 구현, heapq는 일부만 C

---

## 실제 벤치마크 결과

[CPython Issue #137095](https://github.com/python/cpython/issues/137095)의 벤치마크:

### n = 1,000 일 때

| k | heapq | sorted | 승자 |
|---|-------|--------|------|
| 100 (10%) | 0.084ms | 0.038ms | **sorted** (2.2배) |
| 500 (50%) | 0.201ms | 0.039ms | **sorted** (5.1배) |

### n = 100,000 일 때

| k | heapq | sorted | 승자 |
|---|-------|--------|------|
| 500 (0.5%) | 2.66ms | 15.9ms | **heapq** (6배) |
| 1,000 (1%) | 3.36ms | 15.8ms | **heapq** (4.7배) |

---

## 경험적 임계점

```
k / n 비율         권장 방법
─────────────────────────────
< 1%              heapq (압도적)
1% ~ 10%          heapq (우세)
10% ~ 35%         상황에 따라 다름 ⚠️
35% ~ 50%         sorted (우세)
> 50%             sorted (압도적, 1.5~5배)
```

### 왜 "약 35%"인가?

- **10%**: sorted()가 경쟁력을 갖기 시작하는 지점
- **35%**: 대부분의 경우 sorted()가 빠른 교차점
- **50%**: sorted()가 확실히 빠른 지점 (1.5~5배)

"35%"는 정확한 수치가 아니라 **경험적 중간값**입니다.

---

## CPython 내부 구현

```python
# Lib/heapq.py (간략화)
def nsmallest(n, iterable, key=None):
    # 최적화 1: n이 전체 크기 이상이면 sorted 사용
    try:
        size = len(iterable)
    except (TypeError, AttributeError):
        pass
    else:
        if n >= size:
            return sorted(iterable, key=key)[:n]

    # 최적화 2: n=1이면 min() 사용
    if n == 1:
        return [min(iterable, key=key)]

    # 일반적인 경우: 힙 사용
    # ...
```

**현재 CPython은 n >= size (100%)일 때만 sorted()로 전환합니다.**

---

## 왜 CPython은 35%에서 전환하지 않나?

[CPython Issue #137095](https://github.com/python/cpython/issues/137095)에서 논의됨:

1. **범용성**: 임계점은 데이터 크기, 타입, 하드웨어에 따라 다름
2. **예측 가능성**: 사용자가 함수의 동작을 예측하기 어려워짐
3. **len() 문제**: 제너레이터는 len()이 없어 임계점 계산 불가
4. **복잡성**: 이득 대비 구현 복잡도 증가

---

## 실전 가이드

### 언제 무엇을 쓸까?

```python
# ✅ heapq - k가 작을 때 (k << n)
import heapq
heapq.nsmallest(5, million_items)      # k=5, n=1,000,000

# ✅ sorted - k가 클 때 (k > n/3)
sorted(items)[:len(items)//2]          # 절반 가져오기

# ✅ min/max - k=1일 때
min(items)                             # 가장 작은 것 1개
max(items)                             # 가장 큰 것 1개

# ⚠️ 애매할 때 - 벤치마크
import timeit
# 둘 다 테스트해보고 결정
```

### 간단한 규칙

```
k ≤ n/10 (10% 이하)  →  heapq.nsmallest
k > n/3  (33% 이상)  →  sorted()[:k]
그 사이             →  프로파일링 또는 그냥 heapq
```

---

## 코딩테스트에서의 의미

프로그래머스 같은 코딩테스트에서:

1. **n ≤ 10,000**: 둘 다 빠름, 가독성 우선 (sorted 추천)
2. **n ≤ 100,000, k ≤ 100**: heapq가 안전
3. **n > 100,000**: 시간복잡도 신중히 고려

```python
# 실제로는 이 정도 규모에서 차이가 체감됨
n = 100_000
k = 100  # 0.1%

# heapq: O(100,000 * log(100)) ≈ 700,000 연산
# sorted: O(100,000 * log(100,000)) ≈ 1,700,000 연산
```

---

## 요약

| 질문 | 답변 |
|------|------|
| 이론적 교차점 | k = n일 때 (같은 O(n log n)) |
| 실제 교차점 | **k ≈ n/10 ~ n/3** (10%~35%) |
| CPython 내부 임계값 | n >= size (100%)만 sorted 전환 |
| 실전 규칙 | k ≤ 10% → heapq, k > 33% → sorted |

**결론**: "35%"는 정확한 수치가 아니라, "k가 n의 상당 부분을 차지하면 sorted()가 빠르다"는 경험칙의 대략적 표현입니다.

---

## 참고 자료

- [CPython heapq.py 소스 코드](https://github.com/python/cpython/blob/main/Lib/heapq.py)
- [CPython Issue #137095 - 성능 최적화 논의](https://github.com/python/cpython/issues/137095)
- [Python 공식 문서 - heapq](https://docs.python.org/3/library/heapq.html)
- [John Lekberg - Python's heapq module](https://johnlekberg.com/blog/2020-11-01-stdlib-heapq.html)
