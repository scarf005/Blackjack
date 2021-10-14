Cards = list[str]
values: list[str | int] = ["A", *range(2, 10 + 1), "J", "Q", "K"]


def create_symbol_set(symbol: str):
    return [f"{symbol} {value}" for value in values]

cards: Cards = []
for symbol in ["스페이드", "다이아몬드", "하트", "클로버"]:
    cards.extend(create_symbol_set(symbol))
