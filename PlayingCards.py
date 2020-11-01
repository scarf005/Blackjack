
cards = {}

# card[1 ~ 13] 스페이드 카드
number = 1
cards[1] = "Spade A"
for Spade in range(2, 11): 
    number += 1
    cards[Spade] = "Spade " + str(number)
cards[11] = "Spade J"
cards[12] = "Spade Q"
cards[13] = "Spade K"

# card[14 ~ 26] 다이아몬드 카드
number = 1
cards[14] = "Diamond A"
for Diamond in range(15, 24):
    number += 1
    cards[Diamond] = "Diamond " + str(number)
cards[24] = "Diamond J"
cards[25] = "Diamond Q"
cards[26] = "Diamond K"

# card[27 ~ 39] 하트 카드
number = 1
cards[27] = "Heart A"
for Heart in range(28, 37):
    number += 1
    cards[Heart] = "Heart " + str(number)
cards[37] = "Heart J"
cards[38] = "Heart Q"
cards[39] = "Heart K"

# card[40 ~ 52] 하트 카드
number = 1
cards[40] = "Club A"
for Club in range(41, 50):
    number += 1
    cards[Club] = "Club " + str(number)
cards[50] = "Club J"
cards[51] = "Club Q"
cards[52] = "Club K"
