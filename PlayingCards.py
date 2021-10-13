"""
1 ~ 13: 스페이드
14 ~ 26: 다이아몬드
27 ~ 39: 하트
40 ~ 52: 클럽
"""
Cards = list[str]
values: list[str | int] = ["A", *range(2, 10 + 1), "J", "Q", "K"]


def create_symbol_set(symbol: str):
    return [f"{symbol} {value}" for value in values]

cards: Cards = []
for symbol in ["Spade", "Diamond", "Heart", "Club"]:
    cards.extend(create_symbol_set(symbol))


if __name__ == "__main__":
    from pprint import pprint

    pprint(cards)
