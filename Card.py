# Card.py
# Represents a single playing card
# by William George, Vikram Mathew, Grace Miller

import random

"""
Globals Related to Card
"""
RANK_ONE = "One"
RANK_TWO = "Two"
RANK_THREE = "Three"
RANK_FOUR = "Four"
RANK_FIVE = "Five"

SUIT_BLUE = "Blue"
SUIT_GREEN = "Green"
SUIT_YELLOW = "Yellow"
SUIT_RED = "Red"
SUIT_WHITE = "White"
SUIT_RAINBOW = "Rainbow"

class Card:
    # rank and suit names
    """
    REQUIRES 
    _Rank is one of "One", "Two", "Three", "Four", "Five"
    _Suit is one of "Blue", "Green", "Yellow", "Red", "White", and "Rainbow"
    EFFECTS Initializes Card to specified rank and suit
    """
    def __init__(self, rank_in: str, suit_in: str):
        self.__rank = rank_in
        self.__suit = suit_in

    def get_rank(self):
        return self.__rank

    def get_suit(self):
        return self.__suit

# TODO setup a data structure for card rank and suit for faster comparison and storage
rank_list = [RANK_ONE, RANK_TWO, RANK_THREE, RANK_FOUR, RANK_FIVE]
suit_list = [SUIT_BLUE, SUIT_GREEN, SUIT_YELLOW, SUIT_RED, SUIT_WHITE, SUIT_RAINBOW]


class Pack:
    # TODO Implement variants
    def __init__(self, variant: int):
        self.deck = []
        self.card_quantity = {}
        if variant == 0:
            for rank, quantity in zip(rank_list, [3, 2, 2, 2, 1]):
                for suit in suit_list:
                    # TODO is a card object or pair the better key
                    self.card_quantity[Card(rank, suit)] = quantity

                    for i in range(quantity):
                        self.deck.append(Card(rank, suit))

    def shuffle(self):
        # TODO Implement
        return None

    # COMMENT if we have a a __draw function in player, is this needed - Vik
    """
    def draw(self):
        drawn = self.deck.pop()
        self.card_quantity[drawn] -= 1
        assert self.card_quantity[drawn] >= 0
        return drawn
    """


class Player:
    def __init__(self, player_id, parent_g):
        self.hand = []
        self.id = player_id
        self.game = parent_g

    def __draw(self):
        self.hand.append(self.game.deck.pop(0))
        # TODO confirm index should be 0
        return None

    def __give_hint(self, player_choice: int, choice):
        if self.game.tokens > 0:
            self.game.tokens -= 1
            # TODO handle choice logic
        return None

    def __discard(self, hand_ind: int):
        if self.game.tokens < 8:
            self.game.tokens += 1
            self.__draw()
            return hand.pop(hand_ind)
        
        return None

    def __play(self, hand_ind: int):
        played_card = self.hand.pop(hand_ind)
        self.__draw()
        return played_card

    # TODO Adjust for Return types
    # COMMENT I think logic is better handled in Game - Vik
    """
    def turn(self, turn_type: int, hand_ind = None):
        if turn_type == 1:
            self.__give_hint()
        elif turn_type == 2:
            self.__discard(hand_ind)
        else:
            return self.__play(hand_ind)
    """

class Game:
    def __init__(self, num_players):
        self.deck = Pack()
        self.lives = 3
        self.tokens = 8
        self.players = [Player(self) for i in num_players]
        self.board = []


    def deal(self):
        for i in range(5):
            for player in self.players:
                player.__draw()
        return None

    def run(self):
        self.deck.shuffle()
        self.deal()

        num_players = len(self.players)
        turn = 0
        while self.lives > 0 and len(self.deck) > 0:

            turn_choice = int(input("Choose something to do: \n 1) Give hint\n 2) Discard\n 3) Play\n"))
            if turn_choice == 1:
                player_ind = int(input("Which player would you like to give a hint to?"))
                choice_type = int(input("1) Rank\n 2) Suit\n"))
                choice = ""
                if choice_type == 1:
                    choice = int(input("Which rank would you like to inform player ", player_ind, " about?"))
                elif choice_type == 2:
                    choice = int(input("Which rank would you like to inform player ", player_ind, " about?"))
                self.players[turn].__give_hint(player_ind, choice)
            elif turn_choice == 2:
                hand_ind = int(input"Which card would you like to discard (1-5)?")
                assert 1 <= hand_ind <= 5
                self.players[turn].__discard(hand_ind)
            elif turn_choice == 3:
                hand_ind = int(input"Which card would you like to play (1-5)?")
                assert 1 <= hand_ind <= 5
                self.players[turn].__play(hand_ind)
                
            turn = (turn + 1) % num_players



















