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
suit_list = []


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

    def draw(self):
        drawn = self.deck.pop()
        self.card_quantity[drawn] -= 1
        assert self.card_quantity[drawn] >= 0
        return drawn


class Player:
    def __init__(self):
        self.hand = []
        self.game =

    def __draw(self):
        # TODO Implement
        return None

    def __give_hint(self):
        # TODO Implement
        return None

    def __discard(self, hand_ind: int):
        # TODO Implement
        return None

    def __play(self, hand_ind: int):
        played_card = self.hand.pop(hand_ind)
        self.__draw()
        return played_card

    # TODO Adjust for Return types
    def turn(self, turn_type: int, hand_ind = None):
        if turn_type == 1:
            self.__give_hint()
        elif turn_type == 2:
            self.__discard(hand_ind)
        else:
            return self.__play(hand_ind)

class Game:
    self.deck = Pack()
    self.lives = 3
    self.tokens = 8

    def __init__(self, num_players):
        self.players = [Player() for i in num_players]
        self.board = []


    def deal(self):
        # TODO Implement
        return None

    def play(self, ):

    def run(self):
        self.deck.shuffle()
        self.deal()



















