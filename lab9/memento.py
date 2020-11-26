import random
from cs1graphics import *
import itertools

img_path = 'images/'

suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
face_names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



bj_board = Canvas(600, 400, 'dark green', 'Black Jack 101')


"""
Define the Card class
"""
class Card:
    def __init__(self, suit, face, value, image, state):
        self.suit = suit
        self.value = value
        self.face = face
        self.image = image
        self.state = state


def create_deck(number = 1):
    """
    Create a list("deck") of all 52 cards, shuffle them and return the list.
    The list 'deck' have to include Card objects
    A Card is represented by a object with four attributes: the face, the suit, value, state, and the image object
    First, Have to define class 'Card'
    """
    deck = []
    for suit, face in itertools.product(suit_names, face_names):
        if face == "Ace":
            value = 11
        elif face in ['Jack', 'Queen', 'King']:
            value = 10
        else:
            value = int(face)
        img =  Image(img_path+suit+"_"+face + ".png")
        state = True
        card = Card(suit, face, value, img, state)
        deck.append(card)
    random.shuffle(deck)
    return deck


def hand_value(hand):
    """
    hand is a list including card objects
    Compute the value of the cards in the list "hand"
    """
    val = 0 
    for card in hand:
        val += card.value

    return val


def card_string(card):
    """
    Parameter "card" is a Card object
    Return a nice string to represent a card
    (sucn as "a King of Spades" or "an Ace of Diamonds")
    """
    article = ""
    if card.face == 'Ace':
        article = "an "
    elif card.face in ['Jack', 'Queen', 'King']:
        article = "a "
    return article + card.face + " of " + card.suit


def ask_yesno(prompt):
    """
    Display the text prompt and let's the user enter a string.
    If the user enters "y", the function returns "True",
    and if the user enters "n", the function returns "False".
    If the user enters anything else, the function prints "I beg your pardon!", and asks again,
	repreting this until the user has entered a correct string.
    """
    more = input(prompt)
    while more not in ["y", "n"]:
        print("I beg your pardon!")
        more = input(prompt)
    return more == 'y'


def draw_card(dealer,player):
    """
    This funuction add the cards of dealer and player to canvas, bj_board.
    If the state of each Card object is false, then you have to show the hidden card image(Back.png).
	The dealer's first card is hidden state.
    The parameter dealer and player are List objects including Card Objects.

    The start position of dealer's card is (100,100).
    The start position of player's card is (100,300).

    You can use the following methods for positioning images and text:
    Image() Object, Text() Object, moveTo() method, setDepth() method.

    You should use help function -
    help('cs1graphics.Image') -> about Image(), moveTo(), setDepth()
    help('cs1graphics.Text') -> about Text(),moveTo(), setDepth()
    """
    # hidden_img = Image(img_path+"back.png")
    depth = 100
    x0,y0 = 100,100
    x1,y1 = 100,300
    ix = 30

    bj_board.clear()
    for card in dealer:
        if card.state:
            card.image.moveTo(x0, y0)
            card.image.setDepth(depth)
            bj_board.add(card.image)
        else:
            img = Image(img_path+"Back.png")
            img.moveTo(x0, y0)
            img.setDepth(depth)
            bj_board.add(img)
        x0 += ix
    
    for card in player:
        if card.state:
            card.image.moveTo(x1, y1)
            card.image.setDepth(depth)
            bj_board.add(card.image)
        else:
            img = Image(img_path+"back.png")
            img.moveTo(x1, y1)
            img.setDepth(depth)
            bj_board.add(img)
        x1 += ix


def main():

    deck = []

    while True:
        # prompt for starting a new game and create a deck
        print ("Welcome to Black Jack 101!\n")
        if len(deck) < 12:
            deck = create_deck()

    # create two hands of dealer and player
        dealer = []
        player = []

    # initial two dealings
        card = deck.pop()
        print ("You are dealt " + card_string(card))
        player.append(card)

        card = deck.pop()
        print ("Dealer is dealt a hidden card")
        card.state=False
        dealer.append(card)

        card = deck.pop()
        print ("You are dealt " + card_string(card))
        player.append(card)

        card = deck.pop()
        print ("Dealer is dealt " + card_string(card))
        dealer.append(card)

        print ("Your total is", hand_value(player))
        draw_card(dealer,player)


    # player's turn to draw cards
        while hand_value(player) < 21 and ask_yesno("Would you like another card? (y/n) "):
        # draw a card for the player
            card = deck.pop()
            print ("You are dealt " + card_string(card))
            player.append(card)
            print ("Your total is", hand_value(player))

            draw_card(dealer,player)
    # if the player's score is over 21, the player loses immediately.
        if hand_value(player) > 21:
            print ("You went over 21! You lost.")
            dealer[0].state = True
            draw_card(dealer,player)
        else:
        # draw cards for the dealer while the dealer's score is less than 17
            print ("\nThe dealer's hidden card was " + card_string(dealer[0]))
            while hand_value(dealer) < 17:
                card = deck.pop()
                print ("Dealer is dealt " + card_string(card))
                dealer.append(card)
                print ("The dealer's total is", hand_value(dealer))

            dealer[0].state = True
            draw_card(dealer,player)
        # summary
            player_total = hand_value(player)
            dealer_total = hand_value(dealer)
            print ("\nYour total is", player_total)
            print ("The dealer's total is", dealer_total)

            if dealer_total > 21:
                print ("The dealer went over 21! You win!")
            else:
                if player_total > dealer_total:
                    print ("You win!")
                elif player_total < dealer_total:
                    print ("You lost!")
                else:
                    print ("You have a tie!")

        if not ask_yesno("\nPlay another round? (y/n) "):
            bj_board.close()
            break

main()
