# bare except를 사용하지 말아야 하는 이유

> `except:` 대신 항상 구체적인 예외 타입을 명시하라

## 핵심 요약

```python
# ❌ bare except
try:
    result = arr.index(1, idx)
except:
    return -1

# ✅ 구체적 예외 명시
try:
    result = arr.index(1, idx)
except ValueError:
    return -1
```

---

## bare except란?

예외 타입을 지정하지 않고 `except:`만 쓰는 구문이다.

```python
try:
    something()
except:        # ← bare except: 모든 예외를 잡음
    handle()
```

`except Exception:`과도 다르다 — bare except는 **BaseException**까지 잡는다.

---

## 사용하면 안 되는 이유

### 1. 중단 불가능한 프로그램

```python
import time

while True:
    try:
        time.sleep(1)
    except:  # KeyboardInterrupt까지 잡힘
        pass  # Ctrl+C로 종료 불가!
```

bare except는 `KeyboardInterrupt`(Ctrl+C)와 `SystemExit`(`sys.exit()`)까지 잡아버린다. 프로그램을 정상적으로 종료할 수 없게 된다.

### 2. 버그가 숨겨짐

```python
def get_user_name(users, user_id):
    try:
        return users[user_id]["name"]
    except:
        return "Unknown"
```

이 코드에서 발생할 수 있는 예외들:
- `KeyError` — user_id가 없음 (의도한 처리)
- `TypeError` — users가 None임 (버그!)
- `IndexError` — users가 list인데 dict로 착각 (버그!)

bare except는 **의도한 예외와 버그를 구분하지 못한다**.

### 3. 디버깅 지옥

```python
def process_data(data):
    try:
        # 100줄의 복잡한 로직
        parsed = json.loads(data)
        result = transform(parsed)
        save_to_db(result)
    except:
        print("에러 발생")  # 어디서? 무슨 에러?
```

에러의 종류와 위치를 알 수 없어 디버깅이 극도로 어려워진다.

---

## Python 예외 계층 구조

bare except가 왜 위험한지 이해하려면 예외 계층을 알아야 한다.

```
BaseException           ← bare except가 잡는 범위
├── KeyboardInterrupt   ← Ctrl+C (잡으면 안 됨)
├── SystemExit          ← sys.exit() (잡으면 안 됨)
├── GeneratorExit       ← 제너레이터 종료 (잡으면 안 됨)
└── Exception           ← except Exception:이 잡는 범위
    ├── ValueError
    ├── TypeError
    ├── KeyError
    ├── IndexError
    ├── FileNotFoundError
    └── ...
```

**`except Exception:`은 일반적인 에러만 잡고**, 시스템 종료 관련 예외는 통과시킨다. bare except보다 훨씬 안전하다.

---

## 올바른 예외 처리 패턴

### 패턴 1: 구체적 예외 타입 명시 (권장)

```python
try:
    return arr.index(1, idx)
except ValueError:
    return -1
```

발생할 수 있는 예외가 정확히 무엇인지 파악하고 명시한다.

### 패턴 2: 여러 예외 처리

```python
try:
    value = int(data[key])
except KeyError:
    print(f"키 '{key}'가 존재하지 않습니다")
except ValueError:
    print(f"'{data[key]}'는 숫자가 아닙니다")
```

### 패턴 3: 여러 예외를 동일하게 처리

```python
try:
    value = mapping[key]
except (KeyError, IndexError, TypeError):
    value = default
```

### 패턴 4: 정말 모든 예외를 잡아야 할 때

```python
try:
    risky_operation()
except Exception as e:  # BaseException이 아닌 Exception
    logger.error(f"예상치 못한 에러: {e}")
    raise  # 반드시 다시 raise하거나 로깅
```

`except Exception:`을 쓰되, **로깅 후 재발생(raise)** 시키는 것이 일반적이다.

---

## 린터 경고

| 린터 | 규칙 | 메시지 |
|------|------|--------|
| flake8 | E722 | `do not use bare 'except'` |
| ruff | E722 | `Do not use bare except` |
| pylint | W0702 | `No exception type(s) specified` |
| mypy | — | 타입 체크 시 경고 |

모든 주요 린터가 bare except를 경고한다.

---

## 자주 쓰는 내장 함수별 예외 정리

| 함수/연산 | 발생 예외 | 예시 |
|-----------|----------|------|
| `list.index()` | `ValueError` | 값이 없을 때 |
| `dict[key]` | `KeyError` | 키가 없을 때 |
| `list[i]` | `IndexError` | 인덱스 범위 초과 |
| `int("abc")` | `ValueError` | 변환 불가 |
| `1 / 0` | `ZeroDivisionError` | 0으로 나눗셈 |
| `open("x.txt")` | `FileNotFoundError` | 파일 없음 |
| `None.attr` | `AttributeError` | 속성 없음 |

이 표를 참고하면 어떤 예외를 잡아야 하는지 바로 알 수 있다.

---

## 요약

1. **bare except는 모든 예외를 잡는다** — `KeyboardInterrupt`, `SystemExit` 포함
2. **버그가 숨겨진다** — 의도한 예외와 실제 버그를 구분할 수 없다
3. **항상 구체적 예외를 명시하라** — `except ValueError:`, `except (KeyError, TypeError):`
4. **넓은 범위가 필요하면** `except Exception:`을 쓰되, 로깅 + raise를 함께 사용
5. **모든 주요 린터가 경고한다** — E722 규칙

---

*관련 문제: #181898 가까운 1 찾기 — `list.index()`의 `ValueError` 처리*
