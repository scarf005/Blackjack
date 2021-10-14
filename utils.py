from typing import Optional
import sys


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
        return ch

    getch = _getch


def choose(action_1: str, action_2: str, other: Optional[str] = None):
    def choose_two_or(action_1: str, action_2: str, other: str):
        try:
            return [action_1, action_2][int(getch()) - 1]
        except:
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
    print("=" * 60)

    for line in [line, *lines]:
        pad_print(line)

    print("=" * 60)


def pad_print(string: str):
    print(f"{string:>30}")


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


def farewell_greeting(chips):
    if chips > 2000:
        log(
            "이런 얘기를 꺼내게 되서 안타깝습니다만",
            "앞으로 더 이상 저희 카지노에 입장하실 수 없습니다.",
            "무슨 뜻인지 충분히 이해하셨을 거라 생각합니다.",
        )
    elif chips > 1000:
        log(
            "제 눈을 믿을 수가 없군요.",
            "손님이 세우신 업적으로 카지노가 들썩거리고 있습니다.",
            "멋진 플레이를 보여주신 것에 대한 보답입니다.",
            "빠른 시일 내에 다시 방문해주시기를 간절히 기도하겠습니다.",
        )
    elif chips > 500:
        log(
            "정말 놀랍군요.",
            "행운의 여신의 사랑을 받고 계신 것 같습니다.",
            "저희 카지노 측에서 준비한 소정의 선물입니다.",
            "다음 번에도 또 찾아와주십시오.",
        )
    log("즐거운 시간이 되셨기를 바랍니다.", "안녕히 가십시오.")
