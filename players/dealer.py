from .baseplayer import BasePlayer


class Dealer(BasePlayer):
    def __init__(self):
        super().__init__("딜러", "magenta")

    def cardcal(self, cardlast):
        if "A" in cardlast:
            return [1, 11][self.card_sum > 10]
        return super().cardcal(cardlast)

    def play_turn(self):
        self.draw(2)
        while self.card_sum < 17:
            self.show_hands()
            self.say("힛.")
            self.draw()
        if not any((self.bust, self.blackjack)):
            self.say("스테이.")
