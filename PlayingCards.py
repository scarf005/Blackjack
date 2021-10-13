cards = [""]

values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


def append_symbol_set_to_cards(symbol: str):
    for i in range(len(values)):
        cards.append(symbol + " " + str(values[i]))


# card[1 ~ 13] 스페이드 카드
append_symbol_set_to_cards("Spade")
# card[14 ~ 26] 다이아몬드 카드
append_symbol_set_to_cards("Diamond")
# card[27 ~ 39] 하트 카드
append_symbol_set_to_cards("Heart")
# card[40 ~ 52] 하트 카드
append_symbol_set_to_cards("Club")


if __name__ == "__main__":
    from pprint import pprint

    pprint(cards)
