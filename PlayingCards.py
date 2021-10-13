"""
1 ~ 13: 스페이드
14 ~ 26: 다이아몬드
27 ~ 39: 하트
40 ~ 52: 클럽
"""
Cards = list[str]
cards: Cards = []

values: list[str | int] = ["A", *range(2, 10 + 1), "J", "Q", "K"]

def append_symbol_set_to_cards(symbol: str):
    for value in values:
        cards.append(f"{symbol} {value}")


for symbol in ["Spade", "Diamond", "Heart", "Club"]:
    append_symbol_set_to_cards(symbol)


if __name__ == "__main__":
    from pprint import pprint

    pprint(cards)
