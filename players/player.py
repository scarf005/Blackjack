from .baseplayer import BasePlayer
from utils import log, choose, BLACKJACK


class Player(BasePlayer):
    def __init__(self):
        super().__init__("사용자", "cyan")
        self.wins = 0
        self.plays = 0
        self.bets = 0

    def set_chips(self):
        if self.chips == 0:
            result = ["기본칩 50개를 증정합니다."]
            self.chips = 50
        else:
            result = [
                "한 번 오신 적이 있으시군요.",
                f"남은 칩은 {self.chips}개 입니다.",
            ]
        result.append("게임을 시작합니다.")
        log(*result)

    def prepare(self):
        super().prepare()
        self.set_chips()
        self.bet_chips()
        self.plays += 1

    @property
    def win_rate(self):
        return int(self.wins / self.plays * 100)

    @property
    def info(self):
        return (
            f"게임 횟수 : {self.plays} / "
            f"승리 횟수 : {self.wins} / "
            f"승률 : {self.win_rate}%\n"
            f"남은 칩은 {self.chips}개입니다."
        )

    def cardcal(self, cardlast):
        if "A" in cardlast:
            print(f"{cardlast}는 1점 또는 11점으로 적용할 수 있습니다.")
            return int(choose("1", "11"))
        return super().cardcal(cardlast)

    def play_turn(self):
        self.draw(2)
        while not (self.blackjack or self.bust):
            self.show_hands()
            if choose("힛", "스테이") == "스테이":
                break
            self.draw()

    def win(self):
        super().win()
        self.wins += 1
        if self.card_sum == BLACKJACK:
            self.chips += self.bets * 2
        else:
            self.chips += int(self.bets * 1.5)

    def bet_chips(self):
        def get_int_input(ask: str, max: int):
            while True:
                try:
                    result = int(input(ask))
                    if 0 < result <= max:
                        return result
                    print("칩이 부족합니다.")
                except:
                    print("잘못 입력하셨습니다")

        self.bets = get_int_input(
            f"남은 칩 : {self.chips}\n베팅 금액을 정해주십시오. ",
            self.chips,
        )
        self.say(f"{self.bets}개 베팅하셨습니다.")
        self.chips -= self.bets
