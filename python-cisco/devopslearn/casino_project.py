# Las Vegas Casino have approached you to create a new online game. They would like you to produce a version of the popular Casino game! 
#
# The application should take into account the following game play: 
#
# 1. A standard deck of playing cards is required to play 21
#   - Create a deck of standard playing cards
#   - Shuffle the deck in a random order
# 2. Allow players of the game to bet using chips
#   - Aks the player how much they would like to bet
#   - Check to see if the player has enough chips to continue
# 3. Deal two cards to the dealer and two cards to the Player
#   - Show only one of the dealer's cards. The other should remain hidden
#   - Show both of the player's cards. 
# 4. Aks the player if they wish to 'Hit' or 'Stand'
#   - If the player's hand remains under 21, ask if they would like to Hit again
#   - If a player sticks, play the dealer's hand. The Dealer will always Hit unit the dealer's value is at least 17 or more
# 5. Determine the winner and adjust the player's chips accordingly
# 6. Aks the player if they'd like to play again
# 7. The ace value can be either 1 or 11. This depends if the total value of the player's hand exceeds 21. 


import random

# Global variables. Used to setup card decks. 

suites = ('Diamonds', 'Hearts', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Logic to create standard playing cards. 
# A class in Python is a blueprint for creating objects. An object is an instance of a class - it holds data (attributes) and can have behavior (methods). 
# init is a special method called a constructor. It gets called automatically when you create a new object of the class. 

class Card:
    ''' User defined object to represent an card with a chosen suit and value'''
    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    ''' User defined object to create a deck of cards'''
    def __init__(self):
        '''Double for loop utilizing the global variables and the Card class for the instantiation the deck of cards.'''
        self.deck = []
        for suit in suites:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        '''Utalizing the __str__ method of a card object'''
        deck_check = ''
        for card in self.deck:
            deck_check += '\n ' + card.__str__()
        return 'The deck you are using has: ' + deck_check

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        '''Pop the last card of the deck utalizing the pop method'''
        single_card = self.deck.pop()
        return single_card
    
class Hand:
    '''User defined object for the instantiation of the player's and dealers hand of cards.'''
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        '''Adjust for the ace value if the total value of the player's hand exceeds 21.'''
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
# Chip Account and beting

class ChipAccount:
    '''Set the initial chips. Adjust the chips with the methods win_bet and lose_bet accordingly after the creation of a ChipAccount object.'''
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):
    '''Set the number of chips the player wants to play. Break out of the while loop if the chips total is greater of equal to the number of chips that are
    being played. The argument of this function is an object of the class ChipAccount. Hence we can call the methods 'total' and 'bet' of a ChipAccount class.
    The first else statement is always evaluated to true. 
    '''
    while True:
        try:
            chips.bet = int(input("Place your bet! How many chips?"))

        except ValueError:
            print("You must enter an integer!")

        else:
            if chips.bet > chips.total:
                print("You don't have enough chips. You only have", chips.total)
            else:
                break
# Implement the 'Hit' or 'Stand logic

def hit(deck, hand):
    '''The arguments of the function are an instantiation of an Deck object. Hence we can call the 'deal' method to pop the last card of the deck.
    The 'add_card' method has an argument of a card. This is the return value of the method 'deal' of a deck object. The 'adjust_for_ace' method speaks for itself.
    '''
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck, hand):
    '''If the player 'stands' the playing variable will be set to false. The value of playing is used within the game logic underneath.'''
    global playing

    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's': ")

        if x[0].lower() == 'h':
            hit(deck, hand)
            
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue

        break
    
# Showing the cards logic

def show_partial_cards(player, dealer):
    '''Printing the first card of the dealer's hand and showing all cards of the player's hand.
    The cards method can be called after a Hand object is created.'''
    print("\nDealer's hand:")
    print(" *** ")
    print('', dealer.cards[1])
    print("\nPlayer's hand:", *player.cards, sep= '\n ')

def show_all_cards(player, dealer):
    '''Printing all the card's of the dealer's hand and showing all card's of the player's hand.
    The cards method can be called after a Hand object is created.'''
    print("\nDealer's hand:", *dealer.cards, sep= '\n ')
    print("Dealer's hand =", dealer.value)
    print("\nPlayer's hand:", *player.cards, sep= '\n ')
    print("Player's hand =", player.value)
    
# Implement logic for game outcomes

def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()
def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()
def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.lose_bet()
def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.win_bet()
def tie(player, dealer):
    print("Dealer and Player tie!")
    
# Implement Game Play logic

playing = True
# See the playing value being set in the 'hit_or_stand' function. 

player_chips = ChipAccount()

while True:

    print('''
    Welcome to 21! The aim of the game is to get as close to 21 as you can without going over! The Dealer will keep hitting until they reach 17. 
    Aces count as 1 or 11.
    ''')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    take_bet(player_chips)

    show_partial_cards(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_partial_cards(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all_cards(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            tie(player_hand, dealer_hand)

    print("\nPlayer's winnings stand at", player_chips.total)

    new_game = input("Would you like to play another hand? Enter 'y' or 'n': ")

    if new_game[0].lower() == 'y':
        playing = True
        continue

    else: 
        print("Thanks for playing!")
        break