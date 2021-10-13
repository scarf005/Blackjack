import random

from playingcards import Cards, cards
from utils import log, how_to_play, farewell_greeting

# 카드 더미가 0이 되면 다시 섞어준다.
def shuffle_deck() -> Cards:
    deck = cards.copy()
    random.shuffle(deck)
    return deck


Deck = shuffle_deck()

# 클래스로 플레이어와 딜러의 클래스 변수와 메소드를 할당
# 메소드에는 카드를 뽑고, A를 계산하고, bust를 체크하고, 히트나 스테이를 결정하는 기능을 할당
class Player:
    def __init__(self, name, type, chips, hand, card_sum, card_number):
        self.name = name
        self.type = type
        self.chips = chips
        self.hand = hand
        self.card_sum: int = card_sum
        self.card_number = card_number

    # 시작할 때마다 손패를 초기화한다.
    def basic_setting(self):
        del self.hand[:]
        self.card_sum = 0
        self.card_number = 0

    def cardcal(self, cardlast):
        raise NotImplementedError

    def draw(self, *, say_drawn=False):
        global Deck
        self.card_number += 1
        draw = Deck.pop()
        if say_drawn:
            print(f"뽑은 카드 : {draw}")
        print(f"{self.name}의 {self.card_number}번째 카드 : {draw}")
        self.hand.append(draw)
        self.card_sum += self.cardcal(draw[-1])
        print(f"{self.name}의 현재 카드 : {self.hand}")
        print(f"{self.name}의 현재 합 : {self.card_sum}")
        if self.card_sum == 21:
            print(f"{self.name}님이 [Blackjack]을 완성했습니다.")
        elif self.card_sum > 21:
            print(f"{self.name}님이 [Bust]되었습니다.")
            self.card_sum = "Bust"
        if not len(Deck):
            print("덱을 셔플합니다.")
            Deck = shuffle_deck()


class UserPlayer(Player):
    def __init__(self):
        Player.__init__(self, "사용자", "User", 0, [], 0, 0)

    def cardcal(self, cardlast):
        if cardlast == "A":
            while True:
                try:
                    A = int(input("1과 11중 무엇으로 하시겠습니까?"))
                    if A == 1 or A == 11:
                        return A
                except:
                    print("잘못된 값을 입력하셨습니다.")
                    continue
        elif cardlast in "0JQK":
            return 10

        return int(cardlast[-1])

    def hit_or_stay(self):
        while True:
            choice = input("Hit or Stay? ").lower()
            if choice in ["hit", "h"]:
                return "Hit"
            elif choice in ["stay", "s"]:
                return "Stay"
            else:
                print("잘못 입력하셨습니다. Hit 나 Stay 중 하나를 입력해주십시오.")
                continue


class DealerPlayer(Player):
    def __init__(self):
        Player.__init__(self, "딜러", "Dealer", 0, [], 0, 0)

    def draw(self):
        super().draw(say_drawn=True)

    def cardcal(self, cardlast):
        if cardlast == "A":
            if self.card_sum > 10:
                return 1
            else:
                return 11
        elif cardlast in "0JQK":
            return 10
        else:
            return int(cardlast[-1])

    def hit_or_stay(self):
        if self.card_sum < 17:
            return "Hit"
        else:
            return "Stay"


user = UserPlayer()
dealer = DealerPlayer()

# 덱은 52의 범위를 가진 리스트를 섞어서 만든다. 0부터 지워가면서 묘듈에서부터 해당 위치와 동일한 위치의 카드를 뽑아낸다.


# 게임 횟수, 승리횟수는 함수에서 global로 전역함수를 만든다.
wanna_play = True
played_game = 0
win_game = 0
winning_rate = 0


def introduction():
    global wanna_play
    global played_game
    global win_game

    while True:
        if wanna_play == False:
            break
        log("블랙잭에 오신 것을 환영합니다.")
        print("1. 게임 시작")
        print("2. 룰 설명")
        print("3. 나가기")

        try:
            select = int(input())
        except:
            select = 3

        if select == 1:
            set_user_chips()
            game()
        elif select == 2:
            how_to_play()
        else:
            break


def set_user_chips():
    if user.chips == 0:
        log("기본칩 50개를 증정합니다.")
        user.chips = 50
    else:
        log("한 번 오신 적이 있으시군요.")
        log(f"남은 칩은 {user.chips}개 입니다.")
    log("게임을 시작합니다.")

# 카드의 합을 파라미터로 받아 승패를 계산하고 칩을 처리한다.
def winner(player, rival, prize):
    global played_game
    global win_game
    global winning_rate
    winning_prize = prize * 2
    blackjack_prize = int(prize * 1.5)
    print(f"사용자 : {player}")
    print(f"딜러 : {rival}")
    if rival == "Bust":
        print("사용자의 승리입니다.")
        win_game += 1
        if player == 21:
            user.chips += blackjack_prize
        else:
            user.chips += winning_prize
    elif player == "Bust":
        print("딜러의 승리입니다.")
    elif player >= rival:
        print("사용자의 승리입니다.")
        win_game += 1
        if player == 21:
            user.chips += blackjack_prize
        else:
            user.chips += winning_prize
    else:
        print("딜러의 승리입니다.")
    winning_rate = int(win_game / played_game * 100)
    print(f"게임 횟수 : {played_game} / 승리 횟수 : {win_game} / 승률 : {winning_rate}%")
    print(f"남은 칩은 {user.chips}개입니다.")
    if user.chips == 0:
        print("안녕히 가십시오.")
        introduction()

# 게임 진행
def game():
    global played_game
    global win_game
    user.basic_setting()
    dealer.basic_setting()
    played_game += 1

    bet_chips = 1
    while True:
        print(f"{len(Deck)=}")  # DEBUG
        print(f"남은 칩 : {user.chips}")
        try:
            bet_chips = int(input("베팅 금액을 정해주십시오.\n"))
            if 0 < bet_chips <= user.chips:
                print(f"{bet_chips}개 베팅하셨습니다.")
                user.chips -= bet_chips
            else:
                print("칩이 부족합니다.")
        except:
            print("잘못 입력하셨습니다")
        break

    user.draw()
    user.draw()

    while (
        user.card_sum != "Bust"
        and dealer.card_sum != "Bust"
        and user.card_sum != 21
    ):
        choice = user.hit_or_stay()
        if choice == "Hit":
            user.draw()
            continue
        else:
            break
    if user.card_sum != "Bust":
        dealer.draw()
        dealer.draw()
        while dealer.card_sum != "Bust":
            choice = dealer.hit_or_stay()
            if choice == "Hit":
                print("Hit.")
                dealer.draw()
                continue
            else:
                print("Stay.")
                break
    winner(user.card_sum, dealer.card_sum, bet_chips)

    # 값을 비교하여 승자를 결정한 후 다시 할 것인지 정한다.
    if wanna_play:
        retry = input("다시 하시려면 Y를 입력해주세요. ").lower()
        if "y" in retry:
            game()
        introduction()


introduction()
farewell_greeting(user.chips)
log("안녕히 가십시오.")
