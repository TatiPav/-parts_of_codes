from random import shufe

class Card:
    suits = ["пикей", "червей",
             "бубей", "треф"]


    values = [None, None, "2", "3", "4", "5", "6", "7",
            "8", "9", "10","валета", "даму",
            "короля", "туза"]

    def __init__(self, v, s):
    """suit  value — Y 
"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
        return True


19
if self.value == c2.value:
    20
    if self.suit < c2.suit:
        21
    return True
22 else:
23
return False
24
return False
25


def __gt__(self, c2):

    if self.value > c2.value:

    return True



if self.value == c2.value:

    if self.suit > c2.suit:

    return True
 else:

return False

return False



def __repr__(self):

    v = self.values[self.value] + " " \
 + self.suits[self.suit]

return v

class Deck:

    def __init__(self):

    self.cards = []

for i in range(2, 15):

    for j in range(4):

    self.cards.append(Card(i, j))
shufe(self.cards)

def rm_card(self):

    if len(self.cards) == 0:

    return

return self.cards.pop()


class Player:
    def __init__(self, name):
    self.wins = 0

self.card = None
54
self.name = name
55


class Game:
    56

    def __init__(self):

        57
    name1 = input("

    1: ")

    58
    name2 = input("

    2: ")

    59
    self.deck = Deck()
    60
    self.p1 = Player(name1)
    61
    self.p2 = Player(name2)
    62


def wins(self, winner):
    63
    w = "{} B


"
64
w = w.format(winner)
65
print(w)
66


def draw(self, p1n, p1c, p2n, p2c):
    67
    d = "{}


{},
{}
{}
"
68
d = d.format(p1n, p1c, p2n, p2c)
69
print(d)
70


def play_game(self):
    71
    cards = self.deck.cards


72
print("
G
!")
73
while len(cards) >= 2:
    74
    m = "$

& G

.$
& WW
W

*

."
75
response = input(m)
76
if response == '':
    77
    break
78
p1c = self.deck.rm_card()
79
p2c = self.deck.rm_card()
80
p1n = self.p1.name
81
p2n = self.p2.name
82
self.draw(p1n, p1c, p2n, p2c)
83
if p1c > p2c:
    84
    self.p1.wins += 1

85
self.wins(self.p1.name)
86 else:
87
self.p2.wins += 1
88
self.wins(self.p2.name)
89
win = self.winner(self.p1, self.p2)
90
print("R

      .
{}

!".format(win))

91


def winner(self, p1, p2):

    if p1.wins > p2.wins:

    return p1.name

if p1.wins < p2.wins:

    return p2.name

return "$!"

game = Game()
game.play_game()