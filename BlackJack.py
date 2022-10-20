import random
from os import system
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4

def deal_card(hand):
    """takes a list and moves a random card from the deck to the hand,
    and turns 11 into 1 if hand goes over 21"""
    global deck
    if len(deck)  == 0:
        deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4    # To repopulate the deck when it is nearly empty
    card_to_add = random.choice(deck)
    deck.remove(card_to_add)
    hand.append(card_to_add)
    if sum(hand) > 21 and 11 in hand:    # To handle the case of aces being both 11 and 1
        hand[hand.index(11)] = 1

def display_table(dealers_hand, players_hand, player_is_standing):
    """clears screen then prints out the dealers and players hand,
    and if player is standing reveals the dealers second card."""
    system("cls")    # Clears screen
    if not player_is_standing:
        print(f"Dealer: {dealers_hand[0]} ?")    
    else:
        print("Dealer: " + " ".join(list(map(str, dealers_hand))))    # In case player stands, reveals dealer's hand
    print("You: " + " ".join(list(map(str, players_hand))))
    

while True:
    dealers_hand = []
    players_hand = []
    stand = False
    for _ in range(2):
        deal_card(dealers_hand)
        deal_card(players_hand)
    player_total = sum(players_hand)
    display_table(dealers_hand, players_hand, stand)
    if player_total == 21:
        print("You have BlackJack! You win!")
    else:
        while True:
            if input("Would you like to hit or stand?\n") in ["hit", "h"]:
                deal_card(players_hand)
                player_total = sum(players_hand)
                display_table(dealers_hand, players_hand, stand)
                if player_total == 21:
                    print("You have 21, you win!")
                    break
                elif player_total > 21:
                    print("You busted. The Dealer wins.")
                    break
            else:
                dealer_total = sum(dealers_hand)
                stand = True
                display_table(dealers_hand, players_hand, stand)
                while dealer_total < 17:
                    deal_card(dealers_hand)
                    dealer_total = sum(dealers_hand)
                    display_table(dealers_hand, players_hand, stand)
                if dealer_total > 21:
                    print("The Dealer busted. You win!")
                    break
                elif player_total == dealer_total:
                    print("The game is a push.")
                    break
                elif dealer_total > player_total:
                    print("The Dealer wins.")
                    break
                else:
                    print("You win!")
                    break
    if input("Would you like to play another?\n") not in ["yes", "y", "yeah", "ye"]:
        break
        
