import random

# initial values
# List = real value, suits, card
player_cards = []
dealer_cards = []

MINIMUM = 17

# poker card as a dictionary
poker_card = {
    1: "Ace",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "King",
    12: "Queen",
    13: "Jack"
}

suits_card = {
    0: "Clubs",
    1: "Diamonds",
    2: "Hearts",
    3: "Spades"
}


# assign cards at the start of the game
def start():
    for i in range(2):
        add_card(player_cards)
        add_card(dealer_cards)


# adding another card to the card holder
def add_card(cards):
    num = random.randint(1, 13)
    s = random.randint(0, 3)
    suit = suits_card[s]
    if num >= 10:
        card = [10, suit, poker_card[num]]
    elif num == 1:
        card = [11, suit, poker_card[num]]
    else:
        card = [num, suit, poker_card[num]]
    cards.append(card)


def display_cards(cards):
    for i in range(len(cards)):
        print(cards[i][2] + " of " + cards[i][1])
    print()


# get the total points from given set of cards

def evaluate_total_points(cards):
    total_point = 0
    for i in range(len(cards)):
        total_point += cards[i][0]
    return total_point


def check_blackjack(playerPoints, dealerPoints):
    pPoint = playerPoints
    dPoint = dealerPoints
    if pPoint == 21 and dPoint == 21:
        print("Both player and dealer got blackjack.\nIt's a Tie.")
        return True
    elif pPoint == 21:
        print("Player got a BLACKJACK!!!\nPlayer wins!!")
        return True
    elif dPoint == 21:
        print("Dealer got a BLACKJACK!!!\nDealer wins!!")
        return True

    return False


# check who got more points
def evaluate_winner(ppoint, dpoint):
    if ppoint > 21 and dpoint > 21:
        print("It's a draw.")
    elif ppoint > dpoint:
        if ppoint <= 21:
            print("Player wins!!")
        elif ppoint > 21 and dpoint <= 21:
            print("Dealer wins!!")

    elif ppoint < dpoint:
        if dpoint <= 21:
            print("Dealer wins!!")
        elif dpoint > 21 and ppoint <= 21:
            print("Player wins!!")
    else:
        print("It's a draw.")

    # print the values
    print("Player points:: " + str(playerPoints))
    print("Dealer points:: " + str(dealerPoints))


# check if the cards has any ace in them
# return the index of the ace card
def check_ace(cards):
    for i in range(len(cards)):
        if cards[i][2] == "Ace":
            return i
        else:
            return -1


# Dealers picking cards

# If the total is 17 or more, it must stand.
# If the total is 16 or under, they must take a card.
# The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand.
# return True if the dealer is picking, False if the dealer is not
def dealer_pick(totalPoint):
    if totalPoint >= MINIMUM:
        return False
    else:
        return True


# If the dealer has an ace, and counting it as 11 would bring the total to 17 or more
# (but not over 21), the dealer must count the ace
# as 11 and stand. The dealer's decisions, then, are automatic on all plays
# return 11 if the total is less or equal to 21, 1 if it is more than 21
def dealer_ace(totalpoint, indexoface, cards):
    if (totalpoint - 1) + 11 <= 21:
        cards[indexoface][0] = 11
    else:
        cards[indexoface][0] = 1


# program start
start()
print("Your cards::")
display_cards(player_cards)

# for testing purpose
# print("Dealer::")
# display_cards(dealer_cards)

playerPoints = evaluate_total_points(player_cards)
dealerPoints = evaluate_total_points(dealer_cards)

# for testing purpose
# print("Start player point: " + str(playerPoints))
# print("Start dealer point: " + str(dealerPoints))

if check_ace(dealer_cards) > -1:
    placeOfAce = check_ace(dealer_cards)
    dealer_ace(dealerPoints, placeOfAce, dealer_cards)

if not check_blackjack(playerPoints, dealerPoints):

    while dealer_pick(dealerPoints):

        add_card(dealer_cards)
        dealerPoints = evaluate_total_points(dealer_cards)

        # for testing purpose
        # print("current dealer points: " + str(dealerPoints))

    choice = input("Do you want to hit or stand? ")
    while choice != 'hit' and choice != 'stand':
        print("Enter a valid choice.")
        choice = input("Do you want to hit or stand? ")

    while choice == 'hit':
        add_card(player_cards)
        print("Player::")
        display_cards(player_cards)
        choice = input("Do you want to hit or stand? ")
        while choice != 'hit' and choice != 'stand':
            print("Enter a valid choice.")
            choice = input("Do you want to hit or stand? ")
    if check_ace(player_cards) > -1:
        aceValue = int(input("Do you want to use your Ace as (1 or 11):: "))

        # Change ace value to 1
        if aceValue == 11:
            player_cards[check_ace(player_cards)][0] = 1

    playerPoints = evaluate_total_points(player_cards)
    dealerPoints = evaluate_total_points(dealer_cards)

    evaluate_winner(playerPoints, dealerPoints)
