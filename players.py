from utils import log, choose
from playingcards import cards, Cards
from random import shuffle

# 카드 더미가 0이 되면 다시 섞어준다.


def shuffle_deck() -> Cards:
    deck = cards.copy()
    shuffle(deck)
    return deck


Deck = shuffle_deck()


class Player:
    def __init__(self, name):
        self.name = name
        self.chips = 0
        self.reset_hands()

    def reset_hands(self):
        self.hand: list[str] = []
        self.card_sum = 0
        self.bust = False

    def cardcal(self, cardlast):
        if any(symbol in cardlast for symbol in "0JQK"):
            return 10
        return int(cardlast.split()[-1])

    def draw(self, amount=1):
        global Deck
        for _ in range(amount):
            drawn_card = Deck.pop()
            self.say(f"{drawn_card}을 뽑았습니다")
            self.hand.append(drawn_card)
            self.card_sum += self.cardcal(drawn_card)

        self.say(f"{self.card_sum}점, 손패{self.hand}")

        self.check_bust()
        if not len(Deck):
            print("덱을 셔플합니다.")
            Deck = shuffle_deck()

    def check_bust(self):
        if self.card_sum == 21:
            self.say(f"블랙잭을 완성했습니다!")
        elif self.card_sum > 21:
            self.say(f"버스트되었습니다.")
            self.bust = True

    def say(self, string:str):
        print(f"{self.name}: {string}")

class UserPlayer(Player):
    def __init__(self):
        super().__init__("사용자")
        self.wins = 0
        self.plays = 0

    def set_chips(self):
        if self.chips == 0:
            log("기본칩 50개를 증정합니다.")
            self.chips = 50
        else:
            log("한 번 오신 적이 있으시군요.", f"남은 칩은 {self.chips}개 입니다.")
        log("게임을 시작합니다.")

    @property
    def win_rate(self):
        return int(self.wins / self.plays * 100)

    def __str__(self):
        return (
            f"게임 횟수 : {self.plays} / "
            f"승리 횟수 : {self.wins} / "
            f"승률 : {self.win_rate}%\n"
            f"남은 칩은 {self.chips}개입니다."
        )

    def cardcal(self, cardlast):
        if "A" in cardlast:
            return int(choose("1", "11"))
        return super().cardcal(cardlast)

    def hit_or_stay(self):
        return choose("Hit", "Stay")

    def give_prize(self, prize: int):
        print("사용자의 승리입니다.")
        self.wins += 1
        if self.card_sum == 21:
            self.chips += prize * 2
        else:
            self.chips += int(prize * 1.5)

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

        result = get_int_input(
            f"남은 칩 : {self.chips}\n베팅 금액을 정해주십시오.\n",
            self.chips,
        )
        self.say(f"{result}개 베팅하셨습니다.")
        self.chips -= result
        return result


class DealerPlayer(Player):
    def __init__(self):
        super().__init__("딜러")

    def cardcal(self, cardlast):
        if "A" in cardlast:
            return [1, 11][self.card_sum > 10]
        return super().cardcal(cardlast)

    def hit_or_stay(self):
        while self.card_sum < 17:
            self.say("힛.")
            self.draw()
        self.say("스테이.")