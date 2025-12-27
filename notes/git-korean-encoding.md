# Git 한글 인코딩 설정

## 문제 상황

Windows Git Bash에서 한글이 깨지는 현상:
```
[main 8908fe3] feat: Lv0 8臾몄젣 ???諛??쒗??鍮꾧탳 ?숈뒿 ?명듃 異붽?
```

## 해결 방법

### 필수 설정

```bash
# 한글 파일명 이스케이프 비활성화
git config --global core.quotepath false

# 커밋 메시지 인코딩
git config --global i18n.commitencoding utf-8

# 로그 출력 인코딩
git config --global i18n.logoutputencoding utf-8

# pager 유니코드 지원
git config --global core.pager "less -R"
```

### 한 줄로 실행

```bash
git config --global core.quotepath false && git config --global i18n.commitencoding utf-8 && git config --global i18n.logoutputencoding utf-8 && git config --global core.pager "less -R"
```

### 설정 확인

```bash
git config --global --list | grep -E "(encoding|quotepath|pager)"
```

예상 출력:
```
core.quotepath=false
core.pager=less -R
i18n.commitencoding=utf-8
i18n.logoutputencoding=utf-8
```

## 각 설정 설명

| 설정 | 값 | 설명 |
|------|-----|------|
| `core.quotepath` | `false` | 한글 파일명을 `\xxx` 형태로 이스케이프하지 않음 |
| `i18n.commitencoding` | `utf-8` | 커밋 메시지를 UTF-8로 저장 |
| `i18n.logoutputencoding` | `utf-8` | `git log` 출력을 UTF-8로 표시 |
| `core.pager` | `less -R` | 색상 코드와 유니코드를 제대로 처리하는 pager |

## 추가 문제: `fatal: unknown write failure on standard output`

### 원인
- Git Bash와 Windows 콘솔 간 파이프 통신 문제
- 한글 출력 시 버퍼 오버플로우

### 해결책
1. **무시해도 됨** - 커밋 자체는 성공
2. **Windows Terminal 사용** - Git Bash를 Windows Terminal에서 실행하면 더 안정적
3. **환경 변수 설정** (Git Bash ~/.bashrc에 추가):
   ```bash
   export LANG=ko_KR.UTF-8
   export LC_ALL=ko_KR.UTF-8
   ```

## Windows Terminal에서 Git Bash 실행

1. Windows Terminal 설정 열기
2. 새 프로필 추가
3. 명령줄: `C:\Program Files\Git\bin\bash.exe --login -i`
4. 시작 디렉터리: 원하는 경로

## 참고

- Git Bash 기본 LANG: `en_US.UTF-8`
- Windows 콘솔 기본 코드 페이지: CP949 (한글 Windows)
- `chcp 65001` 명령으로 콘솔을 UTF-8로 변경 가능
