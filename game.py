from playingcards import Cards, cards
from utils import choose, log, how_to_play, farewell_greeting
from players import UserPlayer, DealerPlayer, Deck

user = UserPlayer()
dealer = DealerPlayer()

def winner(player, rival, prize):
    print(f"사용자 : {player}")
    print(f"딜러 : {rival}")
    if rival == "Bust":
        user.give_prize(prize)
    elif player == "Bust":
        print("딜러의 승리입니다.")
    elif player >= rival:
        user.give_prize(prize)
    else:
        print("딜러의 승리입니다.")

# 게임 진행
def game():
    user.set_chips()
    user.basic_setting()
    dealer.basic_setting()
    user.plays += 1

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
    print(user)

    if user.chips == 0:
        print("안녕히 가십시오.")
    # 값을 비교하여 승자를 결정한 후 다시 할 것인지 정한다.
    elif choose("다시 하기", "종료") == "다시 하기":
        game()
    introduction()


def introduction():
    log("블랙잭에 오신 것을 환영합니다.")
    choice = choose("게임 시작", "룰 설명", "나가기")
    if choice == "게임 시작":
        game()
    elif choice == "룰 설명":
        how_to_play()


if __name__ == "__main__":
    introduction()
    farewell_greeting(user.chips)
