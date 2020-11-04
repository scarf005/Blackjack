import time, random
from PlayingCards import cards

# 베팅 시스템
# 처음부터 다시 짜야 겠는데
#
#

# 1 ~ 53 리스트를 만들고 셔플, 키값을 셔플한 것과 동일
class Player:
    def __init__(self, name, type, chips, hand, card_sum, card_number):
        self.name = name
        self.type = type
        self.chips = chips
        self.hand = hand
        self.card_sum = card_sum
        self.card_number = card_number
    
class UserPlayer(Player):
    def __init__(self):
        Player.__init__(self, "사용자", "User", 50,[], 0, 0)

    def draw(self):
        self.card_number += 1
        draw = cards[Deck[0]]
        print (f"{self.name}의 {self.card_number}번째 카드 : {draw}")
        self.hand.append(draw)
        self.card_sum += UserPlayer.cardcal_user(self, draw[-1])
        print (f"{self.name}의 현재 카드 : {self.hand}")
        print (f"{self.name}의 현재 합 : {self.card_sum}")
        del Deck[0]    
        time.sleep(1)
        if self.card_sum == 21:
            print (f"{self.name}님이 [Blackjack]을 완성했습니다.")
        elif self.card_sum > 21:
            print (f"{self.name}님이 [Bust]되었습니다.")
            self.card_sum = "Bust"

    def cardcal_user(self, cardlast):
        if cardlast == "A":
            while True:
                A = int(input("1과 11중 무엇으로 하시겠습니까?"))
                if A == 1 or A == 11:
                    return int(A)
                else:
                    print ("잘못된 값을 입력하셨습니다.")
                    continue
        elif cardlast == "0" or cardlast == "J" or cardlast == "Q" or cardlast == "K":
            return 10
        else:
            return int(cardlast[-1])

    def hit_or_stay(self):
        while True:
            choice = input("Hit or Stay? ")
            if choice == "Hit" or choice == "hit" or choice == "H" or choice == "h":
                return "Hit"
            elif choice == "Stay" or choice == "stay" or choice == "S" or choice == "s":
                return "Stay"
            else:
                print ("잘못 입력하셨습니다. Hit 나 Stay 중 하나를 입력해주십시오.")
                continue

class DealerPlayer(Player):
    def __init__(self):
        Player.__init__(self, "딜러", "Dealer", 50,[], 0, 0)
    
    def draw(self):
        self.card_number += 1
        draw = cards[Deck[0]]
        print (f"뽑은 카드 : {draw}")
        print (f"{self.name}의 {self.card_number}번째 카드 : {draw}")
        self.hand.append(draw)
        self.card_sum += DealerPlayer.cardcal_dealer(self, draw[-1])
        print (f"{self.name}의 현재 카드 : {self.hand}")
        print (f"{self.name}의 현재 합 : {self.card_sum}")
        del Deck[0]    
        time.sleep(3)
        if self.card_sum == 21:
            print (f"{self.name}님이 [Blackjack]을 완성했습니다.")
        elif self.card_sum > 21:
            print (f"{self.name}님이 [Bust]되었습니다.")
            self.card_sum = "Bust"

    def cardcal_dealer(self, cardlast):
        if cardlast == "A":
            if self.card_sum > 10:
                return 1
            else:
                return 11
        elif cardlast == "0" or cardlast == "J" or cardlast == "Q" or cardlast == "K":
            return 10
        else:
            return int(cardlast[-1])
    
    def hit_or_stay(self):
        if self.card_sum < 17:
            return "Hit"
        else:
            return "Stay"

def introduction():

    while True:

        print ("=" * 100)
        print ("{0: >50}".format("블랙잭에 오신 것을 환영합니다."))
        print ("=" * 100)
        time.sleep(2)
        print ("1. 게임 시작")
        print ("2. 룰 설명")
        print ("3. 나가기")

        select = input()
        select = int(select)

        if select == 1:
            # print ("=" * 100)
            # print ("{0: >50}".format("어떤 게임을 하시겠습니까?"))
            # print ("=" * 100)
            time.sleep(2)
            print ("=" * 100)
            print ("{0: >50}".format("게임을 시작합니다."))
            print ("=" * 100)
            Game()
            # print ("=" * 100)
            # print ("{0: >50}".format("1. 기본"))
            # print ("{0: >50}".format("2. 1대1"))
            # print ("=" * 100)
            # while True:
            #     select = input()
            #     select = int(select)
            #     if select == 1:
            #         print ("=" * 100)
            #         print ("{0: >50}".format("게임을 시작합니다."))
            #         print ("=" * 100)
            #         Game()
            #     elif select == 2:
            #         print ("=" * 100)
            #         print ("{0: >50}".format("게임을 시작합니다."))
            #         print ("=" * 100)
            #         Game()
            #     else:
            #         print ("다시 입력해주십시오.")
            #         continue

        elif select == 2:
            print ("=" * 100)
            print ("{0: >50}".format("블랙잭은 21에 가까운 수를 만들면 이기는 게임입니다."))
            print ("=" * 100)
            time.sleep(3)
            print ("{0: >50}".format("J, Q, K는 10으로, A는 1과 11 어느쪽으로든 계산할 수 있습니다."))
            print ("=" * 100)
            time.sleep(3)
            print ("{0: >50}".format("시작하며 카드 두장을 기본으로 지급받습니다."))
            print ("=" * 100)
            time.sleep(3)
            print ("{0: >50}".format("카드를 더 뽑으면 Hit, 뽑지 않고 차례를 마치면 Stay."))
            print ("=" * 100)
            time.sleep(3)
            print ("{0: >50}".format("숫자의 합이 21을 넘어가면 Bust로 즉시 패배합니다."))
            print ("=" * 100)
            time.sleep(3)
            print ("{0: >50}".format("플레이어의 차례가 끝나면 상대의 차례입니다."))
            print ("=" * 100)
            time.sleep(3)
            print ("{0: >50}".format("딜러는 숫자의 합이 17 이상이 될때까지 무조건 히트를 합니다."))
            print ("=" * 100)
            time.sleep(3)
            print ("{0: >50}".format("상대보다 합이 높거나, 상대가 Bust되면 플레이어의 승리입니다."))
            print ("=" * 100)
            time.sleep(3)              
            continue

        else:
            print ("=" * 100)
            print ("{0: >50}".format("다음에 또 찾아주십시오."))
            print ("=" * 100)
            time.sleep(3)
            break

# 게임 진행
def Game():

    user = UserPlayer()
    dealer = DealerPlayer()

    global Deck
    Deck = []
    for i in range(1, 53):
        Deck.append(i)
    random.shuffle(Deck)

    user.draw()
    user.draw()
    while user.card_sum != "Bust" and dealer.card_sum != "Bust":
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
                print ("Hit.")
                dealer.draw()
                continue
            else:
                print ("Stay.")
                break

    Winner(user.card_sum, dealer.card_sum)

    retry = input("다시 하시겠습니까? Y/N ")
    if retry == "Y" or retry == "y":
        Game()
    else:
        introduction()
# 값을 비교하여 승자를 결정한 후 다시 할 것인지 정한다.
def Winner(user, rival):
    print (f"사용자 : {user}")
    print (f"상대방 : {rival}")
    if rival == "Bust":
        print ("사용자의 승리입니다.")
    elif user == "Bust":
        print ("상대방의 승리입니다.")
    elif user >= rival:
        print ("사용자의 승리입니다.")
    else:
        print ("상대방의 승리입니다.")

# def basic_hand(self):
#     print ("=" * 100)
#     print ("{0: >50}".format("카드를 제공 합니다."))
#     print ("=" * 100)
#     self.Draw()
#     time.sleep(3)

introduction()

