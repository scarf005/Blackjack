from utils import log, choose, BLACKJACK
from playingcards import cards, Cards
from random import shuffle
from termcolor import cprint


def shuffle_deck(verbose=False) -> Cards:
    if verbose:
        print("덱을 셔플합니다.")
    deck = cards.copy()
    shuffle(deck)
    return deck


Deck = shuffle_deck()


class BasePlayer:
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.chips = 0

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

    def win(self):
        self.say(f"승리했습니다!")

    def say(self, content):
        cprint(f"{self.name}: {content}", self.color)

    def play_turn(self):
        raise NotImplementedError
