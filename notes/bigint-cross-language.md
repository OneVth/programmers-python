# 임의 정밀도 정수 (Big Integer) - 언어별 비교

> 관련 문제: [두 수의 합 #181846](../Lv0/181846/solution.py)

## 개요

일반적인 정수 타입은 고정된 비트 수로 표현되어 범위가 제한됩니다.
**임의 정밀도 정수(Arbitrary Precision Integer)**는 메모리가 허용하는 한 무한히 큰 정수를 다룰 수 있습니다.

### 고정 크기 정수의 한계

| 타입 | 비트 | 최대값 | 자릿수 |
|------|------|--------|--------|
| int32 | 32 | 2,147,483,647 | ~9자리 |
| int64 | 64 | 9,223,372,036,854,775,807 | ~19자리 |
| uint64 | 64 | 18,446,744,073,709,551,615 | ~20자리 |

10만 자리 숫자를 다루려면 **임의 정밀도 정수**가 필수입니다.

---

## 언어별 문법 비교

### Python - 내장 지원 (가장 간단)

```python
# Python 3의 int는 자동으로 임의 정밀도
a = 123456789012345678901234567890
b = 987654321098765432109876543210

# 일반 연산자 그대로 사용
result = a + b
result = a * b
result = a ** 100  # 거듭제곱도 OK

# 문자열 변환
s = str(a)
n = int("123456789012345678901234567890")

# 진법 변환
binary = bin(a)      # "0b..."
octal = oct(a)       # "0o..."
hexadec = hex(a)     # "0x..."
```

**특징**: 별도 임포트 없이 기본 `int`가 BigInteger입니다.

---

### JavaScript - BigInt (ES2020+)

```javascript
// 리터럴: 숫자 뒤에 n 접미사
const a = 123456789012345678901234567890n;
const b = BigInt("987654321098765432109876543210");

// 연산 (BigInt끼리만 가능)
const sum = a + b;
const product = a * b;
const power = a ** 100n;

// 일반 Number와 혼합 불가
const x = a + 10;   // ❌ TypeError
const y = a + 10n;  // ✅ OK

// 문자열 변환
const s = a.toString();
const hex = a.toString(16);

// 비교는 Number와 가능
console.log(10n > 5);  // true (암시적 변환)
console.log(10n === 10);  // false (타입 다름)
console.log(10n == 10);   // true (값만 비교)
```

**특징**: `n` 접미사 필수, Number와 연산 시 명시적 변환 필요

---

### Java - BigInteger 클래스

```java
import java.math.BigInteger;

// 생성
BigInteger a = new BigInteger("123456789012345678901234567890");
BigInteger b = BigInteger.valueOf(1000L);  // long에서 변환

// 상수
BigInteger zero = BigInteger.ZERO;
BigInteger one = BigInteger.ONE;
BigInteger ten = BigInteger.TEN;

// 사칙연산 (메서드 호출)
BigInteger sum = a.add(b);
BigInteger diff = a.subtract(b);
BigInteger prod = a.multiply(b);
BigInteger quot = a.divide(b);
BigInteger rem = a.mod(b);
BigInteger power = a.pow(100);

// 비교
int cmp = a.compareTo(b);  // -1, 0, 1
boolean isEqual = a.equals(b);

// 문자열 변환
String s = a.toString();
String hex = a.toString(16);

// BigInteger → long (범위 초과 시 예외)
long l = a.longValueExact();
```

**특징**: 연산자 오버로딩 없음, 모든 연산이 메서드 호출

---

### C++ - 직접 구현 또는 라이브러리

```cpp
// 방법 1: __int128 (GCC/Clang, 제한적)
__int128 a = 1;
for (int i = 0; i < 38; i++) a *= 10;  // 약 38자리까지

// 방법 2: Boost Multiprecision
#include <boost/multiprecision/cpp_int.hpp>
using namespace boost::multiprecision;

cpp_int a("123456789012345678901234567890");
cpp_int b("987654321098765432109876543210");

cpp_int sum = a + b;      // 연산자 오버로딩 지원
cpp_int prod = a * b;
cpp_int power = pow(a, 100);

std::string s = a.str();

// 방법 3: GMP (GNU Multiple Precision)
#include <gmpxx.h>

mpz_class x("123456789012345678901234567890");
mpz_class y = x + 1000;
```

**특징**: 표준 라이브러리에 없음, 외부 라이브러리 필요

---

### C# - BigInteger 구조체

```csharp
using System.Numerics;

// 생성
BigInteger a = BigInteger.Parse("123456789012345678901234567890");
BigInteger b = new BigInteger(1000);

// 연산자 오버로딩 지원
BigInteger sum = a + b;
BigInteger prod = a * b;
BigInteger power = BigInteger.Pow(a, 100);

// 비교
bool isGreater = a > b;
bool isEqual = a == b;

// 문자열 변환
string s = a.ToString();
string hex = a.ToString("X");

// 기타 유용한 메서드
BigInteger abs = BigInteger.Abs(a);
BigInteger gcd = BigInteger.GreatestCommonDivisor(a, b);
```

**특징**: .NET Framework 4.0+, 연산자 오버로딩 지원

---

### Go - math/big 패키지

```go
import "math/big"

// 생성
a := new(big.Int)
a.SetString("123456789012345678901234567890", 10)

b := big.NewInt(1000)

// 연산 (결과를 저장할 변수 필요)
sum := new(big.Int)
sum.Add(a, b)

prod := new(big.Int)
prod.Mul(a, b)

power := new(big.Int)
power.Exp(a, big.NewInt(100), nil)

// 비교
cmp := a.Cmp(b)  // -1, 0, 1

// 문자열 변환
s := a.String()
hex := a.Text(16)
```

**특징**: 연산자 오버로딩 없음, 메서드 체인 가능

---

### Rust - 외부 크레이트

```rust
// num-bigint 크레이트 사용
use num_bigint::BigInt;
use num_traits::{Zero, One};

// 생성
let a: BigInt = "123456789012345678901234567890".parse().unwrap();
let b: BigInt = BigInt::from(1000);

// 연산자 오버로딩 지원
let sum = &a + &b;
let prod = &a * &b;
let power = a.pow(100);

// 비교
let is_greater = a > b;

// 문자열 변환
let s = a.to_string();
```

**특징**: 표준 라이브러리에 없음, `num-bigint` 크레이트 권장

---

## 성능 비교

### 덧셈 시간복잡도: O(n)
### 곱셈 시간복잡도: O(n²) ~ O(n log n)

| 언어 | 곱셈 알고리즘 | 특징 |
|------|---------------|------|
| Python | Karatsuba | 큰 수에서 자동 최적화 |
| Java | Karatsuba + Toom-Cook | 크기에 따라 알고리즘 선택 |
| GMP (C/C++) | FFT 기반 | 가장 빠름 |

---

## 코딩 테스트 활용 팁

### Python 사용 시

```python
# 문자열로 주어진 큰 수의 덧셈
def solution(a: str, b: str) -> str:
    return str(int(a) + int(b))

# 팩토리얼 (매우 큰 수)
import math
factorial_1000 = math.factorial(1000)  # 2568자리 숫자

# 거듭제곱 + 나머지 (모듈러 연산)
pow(base, exp, mod)  # 효율적인 모듈러 거듭제곱
```

### 다른 언어 사용 시 주의점

1. **Java**: `BigInteger`는 불변(immutable)이므로 연산 결과는 새 객체
2. **JavaScript**: `BigInt`와 `Number` 혼합 연산 불가
3. **C++**: 표준 라이브러리에 없으므로 직접 구현하거나 문자열로 처리

---

## 면접 포인트

1. **왜 Python은 int가 무한 정밀도인가?**
   - 내부적으로 가변 길이 배열로 자릿수를 저장
   - 오버플로우 개념이 없음 (메모리만 충분하면 OK)

2. **BigInteger 연산의 시간복잡도는?**
   - 덧셈/뺄셈: O(n)
   - 곱셈: O(n²) 단순, O(n^1.585) Karatsuba, O(n log n) FFT
   - 나눗셈: O(n²)

3. **모듈러 거듭제곱이 중요한 이유는?**
   - `pow(a, b, m)`은 중간 결과를 작게 유지하며 O(log b) 시간에 계산
   - RSA 암호화 등에서 필수

---

## 요약 표

| 언어 | 타입/클래스 | 연산자 지원 | 표준 라이브러리 |
|------|-------------|-------------|-----------------|
| Python | `int` | ✅ | ✅ 내장 |
| JavaScript | `BigInt` | ✅ | ✅ ES2020+ |
| Java | `BigInteger` | ❌ 메서드 | ✅ java.math |
| C# | `BigInteger` | ✅ | ✅ System.Numerics |
| C++ | - | - | ❌ 외부 라이브러리 |
| Go | `big.Int` | ❌ 메서드 | ✅ math/big |
| Rust | `BigInt` | ✅ | ❌ num-bigint |

---

## 참고 자료

- [Python int 내부 구조](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [MDN BigInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
- [Java BigInteger Javadoc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/math/BigInteger.html)
