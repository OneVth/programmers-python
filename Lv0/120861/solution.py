"""
문제: 캐릭터의 좌표
난이도: Lv0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/120861

설명:
머쓱이는 RPG게임을 하고 있습니다. 게임에는 up, down, left, right 방향키가 있으며
각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다.
예를 들어 [0,0]에서 up을 누르면 [0, 1], down을 누르면 [0, -1],
left를 누르면 [-1, 0], right를 누르면 [1, 0]입니다.

머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board가 매개변수로 주어집니다.
캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를
return하도록 solution 함수를 완성해주세요.

- [0, 0]은 board의 정 중앙에 위치합니다.
- 예를 들어 board의 가로 크기가 9라면 캐릭터는 왼쪽으로 최대 [-4, 0]까지
  오른쪽으로 최대 [4, 0]까지 이동할 수 있습니다.

제한사항:
- board은 [가로 크기, 세로 크기] 형태로 주어집니다.
- board의 가로 크기와 세로 크기는 홀수입니다.
- board의 크기를 벗어난 방향키 입력은 무시합니다.
- 0 ≤ keyinput의 길이 ≤ 50
- 1 ≤ board[0] ≤ 99
- 1 ≤ board[1] ≤ 99
- keyinput은 항상 up, down, left, right만 주어집니다.
"""


def solution_v1(keyinput: list[str], board: list[int]) -> list[int]:
    """
    [Approach] if-else 분기 - 이동 전 경계 체크
    [Time] O(n) - keyinput 순회
    [Space] O(1) - 상수 공간
    """
    answer = [0, 0]
    for s in keyinput:
        if s == "left":
            if answer[0] > -(board[0] // 2):
                answer[0] -= 1
        elif s == "right":
            if answer[0] < board[0] // 2:
                answer[0] += 1
        elif s == "up":
            if answer[1] < board[1] // 2:
                answer[1] += 1
        elif s == "down":
            if answer[1] > -(board[1] // 2):
                answer[1] -= 1

    return answer


def solution_v2(keyinput: list[str], board: list[int]) -> list[int]:
    """
    [Approach] 딕셔너리 매핑 + 클램핑 - 이동 후 범위 제한
    [Time] O(n) - keyinput 순회
    [Space] O(1) - 상수 공간 (moves 딕셔너리는 고정 크기)
    """
    moves = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}

    max_x = board[0] // 2
    max_y = board[1] // 2

    x = y = 0
    for key in keyinput:
        x += moves[key][0]
        y += moves[key][1]

        if x > max_x:
            x = max_x
        if x < -max_x:
            x = -max_x
        if y > max_y:
            y = max_y
        if y < -max_y:
            y = -max_y

    return [x, y]


def solution_v3(keyinput: list[str], board: list[int]) -> list[int]:
    """
    [Approach] min/max 클램핑 - 이동과 범위 제한을 한 줄로 처리
    [Time] O(n) - keyinput 순회
    [Space] O(1) - 상수 공간
    """
    lim_x = board[0] // 2
    lim_y = board[1] // 2
    answer = [0, 0]

    for key in keyinput:
        if key == "left":
            answer[0] = max(answer[0] - 1, -lim_x)
        elif key == "right":
            answer[0] = min(answer[0] + 1, lim_x)
        elif key == "up":
            answer[1] = min(answer[1] + 1, lim_y)
        elif key == "down":
            answer[1] = max(answer[1] - 1, -lim_y)

    return answer


solution = solution_v3
