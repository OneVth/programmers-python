"""
프로그래머스 문제 테스트 러너

사용법:
    python runner.py Lv0/120583
    python runner.py Lv0/120583 -f review_1.py
"""
import sys
import json
import argparse
import importlib.util
from pathlib import Path

# Windows 콘솔 UTF-8 출력 설정
sys.stdout.reconfigure(encoding='utf-8')


def load_solution(problem_path: Path, filename: str = "solution.py"):
    """solution 파일에서 solution 함수를 동적으로 로드"""
    solution_file = problem_path / filename
    if not solution_file.exists():
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {solution_file}")
    spec = importlib.util.spec_from_file_location("solution", solution_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.solution


def load_testcases(problem_path: Path) -> dict:
    """testcases.json 로드"""
    testcase_file = problem_path / "testcases.json"
    with open(testcase_file, "r", encoding="utf-8") as f:
        return json.load(f)


def run_single_test(solution_fn, inputs: list, expected):
    """단일 테스트 케이스 실행"""
    try:
        result = solution_fn(*inputs)
        passed = result == expected
        return {"passed": passed, "result": result, "expected": expected, "error": None}
    except Exception as e:
        return {"passed": False, "result": None, "expected": expected, "error": str(e)}


def run_all_tests(problem_path: Path, filename: str = "solution.py"):
    """모든 테스트 케이스 실행"""
    solution_fn = load_solution(problem_path, filename)
    data = load_testcases(problem_path)

    print(f"\n{'='*50}")
    print(f"📝 {data.get('title', '제목 없음')} (#{data['problem_id']})")
    if filename != "solution.py":
        print(f"📄 파일: {filename}")
    print(f"{'='*50}\n")

    passed = 0
    total = len(data["testcases"])

    for i, tc in enumerate(data["testcases"], 1):
        result = run_single_test(solution_fn, tc["inputs"], tc["expected"])

        status = "✅ PASS" if result["passed"] else "❌ FAIL"
        print(f"  Test {i}: {status}")
        print(f"     입력: {tc['inputs']}")
        print(f"     기대: {result['expected']}")
        print(f"     결과: {result['result']}")
        if result.get("error"):
            print(f"     에러: {result['error']}")
        print()

        if result["passed"]:
            passed += 1

    print(f"\n{'─'*50}")
    print(f"  결과: {passed}/{total} 통과", end="")
    print(" 🎉" if passed == total else " 💪")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="프로그래머스 문제 테스트 러너")
    parser.add_argument("problem_path", help="문제 경로 (예: Lv0/120583)")
    parser.add_argument("-f", "--file", default="solution.py",
                        help="실행할 솔루션 파일 (기본: solution.py)")
    args = parser.parse_args()

    problem_path = Path(args.problem_path)

    if not problem_path.exists():
        print(f"❌ 경로를 찾을 수 없습니다: {problem_path}")
        sys.exit(1)

    run_all_tests(problem_path, args.file)
