# Card.py
# Represents a single playing card
# by William George, Vikram Mathew, Grace Miller

from random import shuffle

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

# TODO consider benifits of dictionary over list
rank_list = [RANK_ONE, RANK_TWO, RANK_THREE, RANK_FOUR, RANK_FIVE]
suit_list = [SUIT_BLUE, SUIT_GREEN, SUIT_YELLOW, SUIT_RED, SUIT_WHITE, SUIT_RAINBOW]

class Card:
    # rank and suit names
    """
    REQUIRES 
    _Rank is one of "One", "Two", "Three", "Four", "Five"
    _Suit is one of "Blue", "Green", "Yellow", "Red", "White", and "Rainbow"
    EFFECTS Initializes Card to specified rank and suit
    """
    def __init__(self, rank_in: int, suit_in: int):
        self.__rank = rank_in
        self.__suit = suit_in

    def get_rank(self):
        return self.__rank

    def get_rank_str(self):
        return rank_list[self.__rank]

    def get_suit(self):
        return self.__suit

    def get_suit_str(self):
        return suit_list[self.__suit]













