from utils import log, choose, BLACKJACK
from playingcards import cards, Cards
from random import shuffle

# 카드 더미가 0이 되면 다시 섞어준다.


def shuffle_deck(verbose=False) -> Cards:
    if verbose:
        print("덱을 셔플합니다.")
    deck = cards.copy()
    shuffle(deck)
    return deck


Deck = shuffle_deck()


class Player:
    def __init__(self, name):
        self.name = name
        self.chips = 0
        self.prepare()

    def prepare(self):
        self.hand: list[str] = []
        self.card_sum = 0

    def cardcal(self, cardlast):
        if any(symbol in cardlast for symbol in "0JQK"):
            return 10
        return int(cardlast.split()[-1])

    def get_cards_from_deck(self, amount=1):
        global Deck

        result = [Deck.pop() for _ in range(amount)]
        if not len(Deck):
            Deck = shuffle_deck(verbose=True)

        return result

    def draw(self, amount=1):
        drawn_cards = self.get_cards_from_deck(amount)

        for card in drawn_cards:
            self.say(f"{card}을 뽑았습니다")
            self.hand.append(card)
            self.card_sum += self.cardcal(card)

        self.check_status()

    def check_status(self):
        if self.blackjack:
            self.say(f"블랙잭을 완성했습니다!")
        elif self.bust:
            self.say(f"버스트되었습니다.")

    @property
    def blackjack(self):
        return self.card_sum == BLACKJACK

    @property
    def bust(self):
        return self.card_sum > BLACKJACK

    def show_hands(self):
        self.say(f"{self.card_sum}점, 손패{self.hand}")

    def say(self, content):
        print(f"{self.name}: {content}")

    def win(self):
        print(f"{self.name}의 승리입니다")

    def play_turn(self):
        raise NotImplementedError


class HumanPlayer(Player):
    def __init__(self):
        super().__init__("사용자")
        self.wins = 0
        self.plays = 0
        self.bets = 0

    def set_chips(self):
        if self.chips == 0:
            log("기본칩 50개를 증정합니다.")
            self.chips = 50
        else:
            log("한 번 오신 적이 있으시군요.", f"남은 칩은 {self.chips}개 입니다.")
        log("게임을 시작합니다.")

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
        while not self.bust:
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
            f"남은 칩 : {self.chips}\n베팅 금액을 정해주십시오.\n",
            self.chips,
        )
        self.say(f"{self.bets}개 베팅하셨습니다.")
        self.chips -= self.bets


class DealerPlayer(Player):
    def __init__(self):
        super().__init__("딜러")

    def cardcal(self, cardlast):
        if "A" in cardlast:
            return [1, 11][self.card_sum > 10]
        return super().cardcal(cardlast)

    def play_turn(self):
        self.draw(2)
        while self.card_sum < 17:
            self.say("힛.")
            self.draw()
        self.say("스테이.")
