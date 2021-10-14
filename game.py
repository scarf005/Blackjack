from playingcards import Cards, cards
from utils import choose, log, how_to_play, farewell_greeting
from players import UserPlayer, DealerPlayer, Deck

user = UserPlayer()
dealer = DealerPlayer()


def check_winner(player: UserPlayer, rival: DealerPlayer, prize):
    player.say(player.card_sum)
    rival.say(rival.card_sum)
    if not player.bust and (rival.bust or player.card_sum >= rival.card_sum):
        return user.win(prize)
    return rival.win()


def game():
    user.set_chips()
    user.reset_hands()
    dealer.reset_hands()
    user.plays += 1

    bets = user.bet_chips()

    if not dealer.bust:
        user.play_turn()

    if not user.bust:
        dealer.play_turn()

    check_winner(user, dealer, bets)
    print(user)

    if user.chips == 0:
        print("안녕히 가십시오.")
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
