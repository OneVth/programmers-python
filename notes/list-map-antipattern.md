# list(map(...))은 안티패턴

> 문제 풀이 중 배운 점: `list(map(...))`을 쓰지 말아야 하는 이유

## 핵심 요약

`map()`의 장점(지연 평가)이 `list()`로 감싸는 순간 사라진다.

## map()의 장점: 지연 평가 (Lazy Evaluation)

```python
# map은 즉시 계산하지 않고, 필요할 때 하나씩 계산
result = map(lambda x: x * 2, range(1_000_000))  # 메모리: 거의 0
# 아직 아무것도 계산 안 됨!

for item in result:  # 이때 하나씩 계산
    if item > 10:
        break  # 6개만 계산하고 끝!
```

## list(map(...))의 문제

```python
# list()로 감싸면 전부 즉시 계산 → 지연 평가 장점 사라짐
result = list(map(lambda x: x * 2, range(1_000_000)))
# 메모리: 100만 개 전부 저장
```

## 비교표

| 방식 | 메모리 | 속도 | 가독성 |
|------|--------|------|--------|
| `list(map(...))` | O(n) | 느림 | ❌ 복잡함 |
| `[... for ...]` | O(n) | 빠름 | ✅ 명확함 |
| `map(...)` (단독) | O(1) | 빠름 | 함수형 |

## 권장 패턴

```python
# ❌ 안티패턴
list(map(lambda x: x * 2, numbers))

# ✅ 리스트 컴프리헨션 사용
[x * 2 for x in numbers]

# ✅ 순회만 할 거면 map 단독 사용
for item in map(lambda x: x * 2, numbers):
    print(item)

# ✅ 다른 함수에 바로 전달
sum(map(int, string_numbers))  # list 없이 바로 sum에 전달
```

## map 단독 사용이 적합한 경우

1. **대용량 데이터를 한 번만 순회**할 때
2. **다른 함수에 바로 전달**할 때 (`sum()`, `max()`, `join()` 등)
3. **메모리가 제한적**일 때

## 결론

- 리스트가 필요하면 → **리스트 컴프리헨션**
- 순회만 필요하면 → **map 단독** 또는 **제너레이터 표현식**
- `list(map(...))` → **사용하지 않기**

---

*관련 문제: #120809 배열 두 배 만들기*
