from playingcards import Cards, cards
from utils import choose, log, how_to_play, farewell_greeting
from players import Player, Dealer


def check_winner(player: Player, rival: Dealer):
    player.say(player.card_sum)
    rival.say(rival.card_sum)
    if not player.bust and (rival.bust or player.card_sum >= rival.card_sum):
        return player.win()
    return rival.win()


def play_game(player: Player, dealer: Dealer):
    while True:
        player.prepare()
        dealer.prepare()

        if not dealer.bust:
            player.play_turn()

        if not player.bust:
            dealer.play_turn()

        check_winner(player, dealer)
        print(player.info)

        if player.chips == 0 or choose("다시 하기", "종료") == "종료":
            print("안녕히 가십시오.")
            break


def main():
    player = Player()
    dealer = Dealer()

    while True:
        log("블랙잭에 오신 것을 환영합니다.")
        result = choose("게임 시작", "나가기", "룰 설명")
        match result:
            case "게임 시작":
                play_game(player, dealer)
            case "나가기":
                break
            case _:
                how_to_play()

    farewell_greeting(player.chips)

if __name__ == "__main__":
    main()
