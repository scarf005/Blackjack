cards = [""]

# card[1 ~ 13] 스페이드 카드
values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

for i in range(len(values)):
    cards.append("Spade " + str(values[i]))

# card[14 ~ 26] 다이아몬드 카드
for i in range(len(values)):
    cards.append("Diamond " + str(values[i]))

# card[27 ~ 39] 하트 카드
for i in range(len(values)):
    cards.append("Heart " + str(values[i]))

# card[40 ~ 52] 하트 카드
for i in range(len(values)):
    cards.append("Club " + str(values[i]))

if __name__ == "__main__":
    from pprint import pprint

    pprint(cards)
