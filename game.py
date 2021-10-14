from playingcards import Cards, cards
from utils import choose, log, how_to_play, farewell_greeting
from players import UserPlayer, DealerPlayer, Deck

user = UserPlayer()
dealer = DealerPlayer()

# 게임 횟수, 승리횟수는 함수에서 global로 전역함수를 만든다.
played_game = 0
win_game = 0
winning_rate = 0


def introduction():
    global played_game
    global win_game

    log("블랙잭에 오신 것을 환영합니다.")
    choice = choose("게임 시작", "룰 설명", "나가기")
    if choice == "게임 시작":
        game()
    elif choice == "룰 설명":
        how_to_play()


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
    user.set_chips()
    user.basic_setting()
    dealer.basic_setting()
    played_game += 1

    bets = user.bet_chips()

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
    winner(user.card_sum, dealer.card_sum, bets)

    # 값을 비교하여 승자를 결정한 후 다시 할 것인지 정한다.
    if choose("다시 하기", "종료") == "다시 하기":
        game()
    else:
        introduction()

introduction()
farewell_greeting(user.chips)
