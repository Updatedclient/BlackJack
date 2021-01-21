import random


#----------------------------------------------------------------------------------------------------Innit----------------------------------------------------------------------------------------------------#
Deck = []
PlayerList = []
PlayerCards = []
Suits = ("Hearts", "Diamonds", "Clubs", "Spades")
Cards = (("King", 10), ("Queen", 10), ("Jack", 10), ("Ten", 10), ("Nine", 9), ("Eight", 8), ("Seven", 7), ("Six", 6), ("Five", 5), ("Four", 4), ("Three", 3), ("Two", 2), ("Ace", 1))

#How many players
while True:
    NumPlayers = int(input("How many hands should be dealt? 5 Max"))
    if NumPlayers <= 5 and NumPlayers > 0:
        for x in range(1, NumPlayers + 1):
            PlayerCards.append(f"Player {x}")
        break
    print("There is a maximum of 5 players at once and a minimum of 1 player")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------Deck_Creation--------------------------------------------------------------------------------------------#
for x in range(6):
    for suit in (Suits):
        for card in (Cards):
            Card = {'suit':suit, 'name':card[0], 'value':card[1]}
            #print("the", Card['name'], "of", Card['suit'], "is worth", Card['value'])
            Deck.append(Card)
def Shuffle():
    ShuffledDeck = random.sample(Deck, len(Deck))
    return(ShuffledDeck)

DealDeck = Shuffle()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Initial Count of cards
for x in range(0, NumPlayers):
    PlayerInfo = {'player':f'{PlayerCards[x]}', 'hand':[DealDeck[x]['name'], DealDeck[NumPlayers + 1 + x]['name']], 'handvalue':DealDeck[x]['value'] + DealDeck[NumPlayers + 1 + x]['value']}
    PlayerList.append(PlayerInfo)

