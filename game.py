import time, random
from PlayingCards import cards


# 클래스로 플레이어와 딜러의 클래스 변수와 메소드를 할당
# 메소드에는 카드를 뽑고, A를 계산하고, bust를 체크하고, 히트나 스테이를 결정하는 기능을 할당
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
        Player.__init__(self, "사용자", "User", 0,[], 0, 0)

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
            time.sleep(1)
            print (f"{self.name}님이 [Blackjack]을 완성했습니다.")
        elif self.card_sum > 21:
            time.sleep(1)
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
        Player.__init__(self, "딜러", "Dealer", 0,[], 0, 0)
    
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
        time.sleep(1.5)
        if self.card_sum == 21:
            time.sleep(1)
            print (f"{self.name}님이 [Blackjack]을 완성했습니다.")
        elif self.card_sum > 21:
            time.sleep(1)
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

user = UserPlayer()
dealer = DealerPlayer()

# 덱은 52의 범위를 가진 리스트를 섞어서 만든다. 0부터 지워가면서 묘듈에서부터 해당 위치와 동일한 위치의 카드를 뽑아낸다.   

Deck = []
for i in range(1, 53):
    Deck.append(i)
    random.shuffle(Deck)

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
            if user.chips == 0:
                time.sleep(1)
                print ("=" * 100)
                print ("{0: >50}".format("기본칩 50개를 증정합니다."))
                print ("=" * 100)
                user.chips = 50
            else:
                time.sleep(1)
                print ("=" * 100)
                print ("{0: >50}".format("한 번 오신 적이 있으시군요."))
                print ("=" * 100)
                time.sleep(1)
                print ("=" * 100)
                print ("{0: >50}".format(f"남은 칩은 {user.chips}개 입니다."))
                print ("=" * 100)
            time.sleep(1)
            print ("=" * 100)
            print ("{0: >50}".format("게임을 시작합니다."))
            print ("=" * 100)

            Game()
            

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
            wanna_play = False
            break

# 시작할 때마다 손패를 초기화한다.

def basic_setting():
    del user.hand[:]
    user.card_sum = 0
    user.card_number = 0
    del dealer.hand[:]
    dealer.card_sum = 0
    dealer.card_number = 0

# 카드 더미가 0이 되면 다시 섞어준다.

def deck_check():
    if len(Deck) == 0:
        time.sleep(1)
        print ("덱을 셔플합니다.")
        time.sleep(1)
        for i in range(1, 53):
            Deck.append(i)
        random.shuffle(Deck)

# 카드의 합을 파라미터로 받아 승패를 계산하고 칩을 처리한다.

def Winner(player, rival, prize):
    global played_game
    global win_game
    global winning_rate
    winning_prize = prize * 2
    blackjack_prize = int(prize*1.5)
    print (f"사용자 : {player}")
    print (f"딜러 : {rival}")
    if rival == "Bust":
        time.sleep(1)
        print ("사용자의 승리입니다.")
        win_game += 1
        if player == 21:
            user.chips += blackjack_prize
        else:
            user.chips += winning_prize
    elif player == "Bust":
        time.sleep(1)
        print ("딜러의 승리입니다.")
    elif player >= rival:
        time.sleep(1)
        print ("사용자의 승리입니다.")
        win_game += 1
        if player == 21:
            user.chips += blackjack_prize
        else:
            user.chips += winning_prize
    else:
        time.sleep(1)
        print ("딜러의 승리입니다.")
    time.sleep(1)
    winning_rate = int(win_game/played_game*100)
    print (f"게임 횟수 : {played_game} / 승리 횟수 : {win_game} / 승률 : {winning_rate}%")
    print (f"남은 칩은 {user.chips}개입니다.")
    if user.chips == 0:
        time.sleep(1)
        print ("안녕히 가십시오.")
        introduction()

# 칩에 따라 다른 반응이 나온다.

def farewell_greeting(chips, winning_rate):
    if chips > 2000:
        time.sleep(1)
        print ("=" * 100)
        print ("{0: >50}".format("이런 얘기를 꺼내게 되서 안타깝습니다만"))
        print ("=" * 100)
        time.sleep(1)
        print ("=" * 100)
        print ("{0: >50}".format("앞으로 더 이상 저희 카지노에 입장하실 수 없습니다."))
        print ("=" * 100)
        time.sleep(1)
        print ("=" * 100)
        print ("{0: >50}".format("무슨 뜻인지 충분히 이해하셨을 거라 생각합니다."))
        print ("=" * 100)

    elif chips > 1000:
        time.sleep(1)
        print ("=" * 100)
        print ("{0: >50}".format("제 눈을 믿을 수가 없군요."))
        print ("=" * 100)
        time.sleep(1)
        print ("=" * 100)
        print ("{0: >50}".format("손님이 세우신 업적으로 카지노가 들썩거리고 있습니다."))
        print ("=" * 100)
        time.sleep(1)
        print ("=" * 100)
        print ("{0: >50}".format("멋진 플레이를 보여주신 것에 대한 보답입니다."))
        print ("=" * 100)
        time.sleep(1)
        print ("=" * 100)
        print ("{0: >50}".format("빠른 시일 내에 다시 방문해주시기를 간절히 기도하겠습니다."))
        print ("=" * 100)
    elif chips > 500:
        time.sleep(1)
        print ("=" * 100)
        print ("{0: >50}".format("정말 놀랍군요."))
        print ("=" * 100)
        time.sleep(1)
        print ("=" * 100)
        print ("{0: >50}".format("행운의 여신의 사랑을 받고 계신 것 같습니다."))
        print ("=" * 100)
        time.sleep(1)
        print ("=" * 100)
        print ("{0: >50}".format("저희 카지노 측에서 준비한 소정의 선물입니다."))
        print ("=" * 100)
        time.sleep(1)
        print ("=" * 100)
        print ("{0: >50}".format("다음 번에도 또 찾아와주십시오."))
        print ("=" * 100)

    time.sleep(1)
    print ("=" * 100)
    print ("{0: >50}".format("즐거운 시간이 되셨기를 바랍니다."))
    print ("=" * 100)

# 게임 진행
def Game():
    global played_game
    global win_game
    basic_setting()
    played_game += 1

    while True:
        print (f"남은 칩 : {user.chips}")
        bet_chips = 0
        bet_chips = int(input("베팅 금액을 정해주십시오.\n"))
        if bet_chips <= user.chips and bet_chips != 0:
            pass
        else:
            print ("칩이 부족하거나 잘못 입력하셨습니다.")
            continue
        print (f"{bet_chips}개 베팅하셨습니다.")
        user.chips -= bet_chips
        break
            
    user.draw()
    deck_check()
    user.draw()
    deck_check()

    while user.card_sum != "Bust" and dealer.card_sum != "Bust" and user.card_sum != 21:
        choice = user.hit_or_stay()
        if choice == "Hit":
            user.draw()
            deck_check()
            continue
        else:
            break
    if user.card_sum != "Bust":
        dealer.draw()
        deck_check()
        dealer.draw()
        deck_check()
        while dealer.card_sum != "Bust":
            choice = dealer.hit_or_stay()
            if choice == "Hit":
                print ("Hit.")
                time.sleep(1)
                
                dealer.draw()
                deck_check()
                continue
            else:
                print ("Stay.")
                time.sleep(1)
                break

    Winner(user.card_sum, dealer.card_sum, bet_chips)
    if wanna_play != False:
        retry = input("다시 하시려면 Y를 입력해주세요. ")
        time.sleep(1)
        if "Y" in retry:
            Game()
        elif "y" in retry:
            Game()
        else:
            introduction()
    # 값을 비교하여 승자를 결정한 후 다시 할 것인지 정한다.


introduction()
farewell_greeting(user.chips, winning_rate)
print ("=" * 100)
print ("{0: >50}".format("안녕히 가십시오."))
print ("=" * 100)
