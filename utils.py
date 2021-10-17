from typing import Optional
from termcolor import cprint
import sys

BLACKJACK = 21
_LINE_WIDTH = 60
_CTRL_C = "\x03"
_LOG_COLOR = "green"

if sys.platform == "win32":
    import msvcrt

    getch = lambda: msvcrt.getch()

else:
    import tty, termios

    def _getch():
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        if ch == _CTRL_C:
            sys.tracebacklimit = 0
            raise KeyboardInterrupt
        return ch

    getch = _getch


def choose(action_1: str, action_2: str, other: Optional[str] = None):
    def choose_two_or(action_1: str, action_2: str, other: str):
        try:
            return [action_1, action_2][int(getch()) - 1]
        except ValueError:
            return other

    def choose_two(action_1: str, action_2: str):
        while True:
            result = choose_two_or(action_1, action_2, "retry")
            if result != "retry":
                return result
            print("잘못 입력하셨습니다. 1과 2 중 하나를 선택해주십시오.")

    print(f"1: {action_1}, 2: {action_2}")
    if other:
        print(f"다른 키: {other}")
        return choose_two_or(action_1, action_2, other)

    return choose_two(action_1, action_2)


def log(line: str, *lines: str):
    cprint("=" * _LINE_WIDTH, _LOG_COLOR)

    for line in [line, *lines]:
        cprint(f"{line:>30}", _LOG_COLOR)

    cprint("=" * _LINE_WIDTH, _LOG_COLOR)


def how_to_play():
    log(
        "블랙잭은 21에 가까운 수를 만들면 이기는 게임입니다.",
        "J, Q, K는 10으로, A는 1과 11 어느쪽으로든 계산할 수 있습니다.",
        "시작하며 카드 두장을 기본으로 지급받습니다.",
        "카드를 더 뽑으면 Hit, 뽑지 않고 차례를 마치면 Stay.",
        "숫자의 합이 21을 넘어가면 Bust로 즉시 패배합니다.",
        "플레이어의 차례가 끝나면 상대의 차례입니다.",
        "딜러는 숫자의 합이 17 이상이 될때까지 무조건 히트를 합니다.",
        "상대보다 합이 높거나, 상대가 Bust되면 플레이어의 승리입니다.",
    )
