cards = [""]

# card[1 ~ 13] 스페이드 카드
cards.append("Spade A")
for Spade in range(2, 11):
    cards.append("Spade " + str(Spade))
cards.append("Spade J")
cards.append("Spade Q")
cards.append("Spade K")
# A, 2 ~ 10, J, Q, K

# card[14 ~ 26] 다이아몬드 카드
number = 1
cards.append("Diamond A")
for Diamond in range(15, 24):
    number += 1
    cards.append("Diamond " + str(number))
cards.append("Diamond J")
cards.append("Diamond Q")
cards.append("Diamond K")

# card[27 ~ 39] 하트 카드
number = 1
cards.append("Heart A")
for Heart in range(28, 37):
    number += 1
    cards.append("Heart " + str(number))
cards.append("Heart J")
cards.append("Heart Q")
cards.append("Heart K")

# card[40 ~ 52] 하트 카드
number = 1
cards.append("Club A")
for Club in range(41, 50):
    number += 1
    cards.append("Club " + str(number))
cards.append("Club J")
cards.append("Club Q")
cards.append("Club K")

if __name__ == "__main__":
    from pprint import pprint

    pprint(cards)
