#import random for shuffling later and OS to clear screen/format
import random
import os
#Heading
print('Welcome to the game if WAR. Highcard wins. No ties. No prisoners!')
#Some lists and dicts for later
played = []
wins = {}
score = {}
#card vaues for the deck
value = list(range(2,15))
suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
face_cards = {
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A',
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
    }
#class to create the cards
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
#Function to generate a deck
def generate_cards(values, suits):
    cards = []
    for value in values:
        for suit in suits:
            if value in face_cards:
                card_value = face_cards[value]
                cards.append(Card(card_value, suit))
            else:
                cards.append(Card(value, suit))
    return cards
#Making calling the cards easier
cards = generate_cards(value, suits)

#Function to deal the cards
def deal(deck, players):
    x = 1
    n = 0
    round_scores = {}
    conti = input('Hit enter to deal cards or q to exit program')
    os.system('cls')
    while conti != 'q':
        while ((x <= players) and (len(deck) >= players)):
            name = names[n]
            played.append(deck[0])
            d = deck[0]
            deck.pop(0)
            print(f'{name} has the {d}')
            round_scores.update({name: d})
            x += 1
            n += 1
        score[max(round_scores, key=round_scores.get)] = score[max(round_scores, key=round_scores.get)] + 1 
        print(f'the winner of this round is {max(round_scores, key=round_scores.get)} with the {max(round_scores.values())}')
        print(f'The current score is {score}')
        break
    else:
        quit()
    
#Start of program
players = input('Enter number of players (2-3): ')
while isinstance(players, int) == False:
    try:
        players = int(players)
    except ValueError:
        players = input('Not a valid input. Enter number of players (2-3): ')
    
#Determining number of players and ensuring it is in the range. Then getting names.
while players > 3 or players <= 1:
    print('Must be less than 3 and more than 1 player')
    players = int(input('Enter number of players (2-3): '))
    
else:
    names = []
    for i in range(players):
        i = input('Enter name (no duplicate names):')
        names.append(i)
#Adding names to the 'wins' dicitionary to keep score        
for w in names:
        wins.update({w: 0})
        
#Start of program from user perspective
cont = 0
while (cont != 'q' and cont != 'Q'):
    #Shuffling cards
    shuffled = []
    for card in cards:
        deck = f'{card.value} of {card.suit}'
        shuffled.append(deck)
        random.shuffle(shuffled)
    #Adding names to the score dictionary      
    for j in names:
            score.update({j: 0})
    #Dealing cards as long as there are enough cards for number of players
    while len(shuffled) >= players:        
        deal(shuffled, players)
    #Getting rid of cards in deck so they cannot be reused. Then ending game when there are no more cards.    
    p = 0
    while p < len(played):
        try:
            shuffled.pop(p)
            p += 1
        except IndexError:
            print('No more cards. Game over!')
            print(f'{max(score, key=score.get)} wins the game with {max(score.values())} points! Congratulations {max(score, key=score.get)}!')
            break
    wins[max(score, key=score.get)] =  wins[max(score, key=score.get)] + 1
    print(f'Games Won: {wins}.')
    cont = input('Hit enter play again with same players or q to quit: ')
else:
    if cont == 'q' or cont == 'Q':
        print('Game over')
