cards = [""]

# card[1 ~ 13] 스페이드 카드

cards.append("Spade A")
for i in range(2, 11):
    cards.append("Spade " + str(i))
cards.append("Spade J")
cards.append("Spade Q")
cards.append("Spade K")
# A, 2 ~ 10, J, Q, K

# card[14 ~ 26] 다이아몬드 카드
cards.append("Diamond A")
for i in range(2, 11):
    cards.append("Diamond " + str(i))
cards.append("Diamond J")
cards.append("Diamond Q")
cards.append("Diamond K")

# card[27 ~ 39] 하트 카드
cards.append("Heart A")
for i in range(2, 11):
    cards.append("Heart " + str(i))
cards.append("Heart J")
cards.append("Heart Q")
cards.append("Heart K")

# card[40 ~ 52] 하트 카드
cards.append("Club A")
for i in range(2, 11):
    cards.append("Club " + str(i))
cards.append("Club J")
cards.append("Club Q")
cards.append("Club K")

if __name__ == "__main__":
    from pprint import pprint

    pprint(cards)
