from baseplayer import BasePlayer

class Dealer(BasePlayer):
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