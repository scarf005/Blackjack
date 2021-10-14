# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: youkim < youkim@student.42seoul.kr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/10/14 13:24:13 by youkim            #+#    #+#              #
#    Updated: 2021/10/14 13:24:13 by youkim           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from playingcards import Cards, cards
from utils import choose, log, how_to_play, farewell_greeting
from players import HumanPlayer, DealerPlayer, Deck


def check_winner(player: HumanPlayer, rival: DealerPlayer):
    player.say(player.card_sum)
    rival.say(rival.card_sum)
    if not player.bust and (rival.bust or player.card_sum >= rival.card_sum):
        return player.win()
    return rival.win()


def play_game(player: HumanPlayer, dealer: DealerPlayer):
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
    player = HumanPlayer()
    dealer = DealerPlayer()

    while True:
        log("블랙잭에 오신 것을 환영합니다.")
        match choose("게임 시작", "룰 설명", "나가기"):
            case "게임 시작":
                play_game(player, dealer)
            case "룰 설명":
                how_to_play()
            case _:
                break

    farewell_greeting(player.chips)

if __name__ == "__main__":
    main()
