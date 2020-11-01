import time, random
from PlayingCards import cards

# 1 ~ 53 리스트를 만들고 셔플, 키값을 셔플한 것과 동일
Deck = []
for i in range(1, 53):
    Deck.append(i)
random.shuffle(Deck) 

# 개요, 메뉴 화면
def introduction():
    while True:

        print ("=" * 100)
        print ("{0: >50}".format("블랙잭에 오신 것을 환영합니다."))
        print ("=" * 100)
        time.sleep(2)
        print ("1. 게임 시작")
        print ("2. 룰 설명")
        print ("3. 나가기")

        celect = input()
        celect = int(celect)

        if celect == 1:
            print ("=" * 100)
            print ("{0: >50}".format("게임을 시작합니다."))
            print ("=" * 100)
            time.sleep(2)
            Game()

        elif celect == 2:
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
            print ("{0: >50}".format("플레이어의 차례가 끝나면 딜러의 차례입니다."))
            print ("=" * 100)
            time.sleep(3)
            print ("{0: >50}".format("딜러는 숫자의 합이 17 이상이 될때까지 무조건 히트를 합니다."))
            print ("=" * 100)
            time.sleep(3)
            print ("{0: >50}".format("딜러보다 합이 높거나, 딜러가 Bust되면 플레이어의 승리입니다."))
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
    PlayerCardsum = 0
    while True:
        if PlayerCardsum > 21:
            print ("Bust!!!")
            time.sleep(1)
            print ("플레이어의 패배입니다.")
            time.sleep(1)
            retry = input("다시 하시겠습니까? Y/N")
            if retry == "Y" or retry == "y":
                Game()
            else:
                break
        # Deck[0]부터 하나씩 지워가며 카드를 뽑음, 변수에 cards에 덱의 키값를 넣고 문자열인 벨류를 변수에 할당
        print ("=" * 100)
        print ("{0: >50}".format("카드를 제공 합니다."))
        print ("=" * 100)
        time.sleep(3)
        
        # 문자열을 정수로 변환, 10/J/Q/K는 10으로 바꿔주는 작업
        
        Draw = cards[Deck[0]]
        print ("첫번째 카드 : {0}".format(Draw))
        PlayerCardsum += CardCal_Player(Draw[-1])
        del Deck[0]    
        time.sleep(1)

        Draw = cards[Deck[0]]
        print ("두번째 카드 : {0}".format(Draw))
        PlayerCardsum += CardCal_Player(Draw[-1])
        del Deck[0]
        time.sleep(1)    
        print ("합 : {0}".format(PlayerCardsum))
        
        if PlayerCardsum > 21:
            continue
        
        # 히트할 것인지 스테이 할 것인지 결정
        
        while True:
            if PlayerCardsum > 21:
                break
            
            choice = HitStay()

            if choice == "Hit":
                print ("=" * 100)
                print ("{0: >50}".format("카드를 뽑습니다."))
                print ("=" * 100)
                time.sleep(2)
                Draw = cards[Deck[0]]
                print ("뽑은 카드 : {0}".format(Draw))
                PlayerCardsum += CardCal_Player(Draw[-1])
                print ("합 : {0}".format(PlayerCardsum))
                del Deck[0]
                continue
            elif choice == "Stay":
                break
        if PlayerCardsum > 21:
            continue
        
        # 딜러의 턴으로 넘어간다
        Dealer_result = Dealer_turn()
        
        # 승자를 정한다
        Winner(PlayerCardsum, Dealer_result)

# 카드의 마지막 문자를 인덱싱해서 정수형으로 전환, 합산
def CardCal_Player(cardlast):
    if cardlast[-1] == "A":
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

# Hit할 것인지 Stay할 것인지 결정
def HitStay():
    while True:
        answer = input("Hit or Stay? ")
        if answer == "Hit" or answer == "hit" or answer == "H" or answer == "h":
            return "Hit"
        elif answer == "Stay" or answer == "stay" or answer == "S" or answer == "s":
            return "Stay"
        else:
            print ("잘못 입력하셨습니다. Hit 나 Stay 중 하나를 입력해주십시오.")
            continue

# 기능이 불필요하여 삭제
# def Bustcheck(PlayerCardsum):
#     if PlayerCardsum == 21:
#         print ("[Blackjack!!!]")
#         return PlayerCardsum
#     elif PlayerCardsum > 21:
#         print ("[Bust...]")
#         return "Bust"
#     else:
#         return PlayerCardsum

# 딜러의 차례, 정해진 규칙에 따르게끔, 숫자의 합을 리턴한다.
def Dealer_turn():
    
    print ("=" * 100)
    print ("{0: >50}".format("딜러의 차례입니다."))
    print ("=" * 100)
    time.sleep(3)
    print ("=" * 100)
    print ("{0: >50}".format("딜러가 카드를 뽑습니다."))
    print ("=" * 100)
    time.sleep(3)

    DealerCardsum = 0
    Draw = cards[Deck[0]]
    print ("첫번째 카드 : {0}".format(Draw))
    DealerCardsum += CardCal_Dealer(Draw[-1], DealerCardsum)
    del Deck[0]
    time.sleep(1)

    Draw = cards[Deck[0]]
    print ("두번째 카드 : {0}".format(Draw))
    DealerCardsum += CardCal_Dealer(Draw[-1], DealerCardsum)
    del Deck[0]
    time.sleep(1)

    print ("합 : {0}".format(DealerCardsum))
    time.sleep(1)
    while True:
        if DealerCardsum < 17:
            Draw = cards[Deck[0]]
            print ("=" * 100)
            print ("{0: >50}".format("[Hit.]"))
            print ("=" * 100)
            time.sleep(2)
            print ("뽑은 카드 : {0}".format(Draw))       
            DealerCardsum += CardCal_Dealer(Draw[-1], DealerCardsum)
            del Deck[0]
            time.sleep(2)
            print ("합 : {0}".format(DealerCardsum))
        elif DealerCardsum > 21:
            DealerCardsum = "Bust"
            break
        else:
            print ("=" * 100)
            print ("{0: >50}".format("[Stay.]"))
            print ("=" * 100)
            time.sleep(2)
            break
    return DealerCardsum

# 딜러의 합산은 따로 만들어준다.
def CardCal_Dealer(cardlast, DealerCardsum):
    if cardlast == "A":
        if DealerCardsum > 10:
            return 1
        else:
            return 11
    elif cardlast == "0" or cardlast == "J" or cardlast == "Q" or cardlast == "K":
        return 10
    else:
        return int(cardlast[-1])

# 값을 비교하여 승자를 결정한 후 다시 할 것인지 정한다.
def Winner(PlayerCardsum, Dealer_result):
    print (f"플레이어 : {PlayerCardsum}")
    print (f"딜러 : {Dealer_result}")
    if Dealer_result == "Bust":
        print ("플레이어의 승리입니다.")
    elif PlayerCardsum >= Dealer_result:
        print ("플레이어의 승리입니다.")
    else:
        print ("딜러의 승리입니다.")

    retry = input("다시 하시겠습니까? Y/N ")
    if retry == "Y" or retry == "y":
        Game()
    else:
        introduction()


introduction()
