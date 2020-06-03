import Card


class Pack:
    # TODO Implement variants
    def __init__(self, variant: int):
        self.deck = []
        self.card_quantity = {}

        # Deck Related variant
        card_quantity = []
        card_quantity_rainbow = []
        if variant == 0:
            card_quantity = [3, 2, 2, 2, 1]
            card_quantity_rainbow = [0, 0, 0, 0, 0]

        # The loop that actual builds the deck
        for suit_ind, suit in enumerate(suit_list):
            suit_quantity = []
            if suit == SUIT_RAINBOW:
                suit_quantity = card_quantity_rainbow
            else:
                suit_quantity = card_quantity

            for rank_ind, quantity in zip(range(len(rank_list)), suit_quantity):
                self.card_quantity[Card(rank_ind, suit_ind)] = quantity
                for i in range(quantity):
                    self.deck.append(Card(rank_ind, suit_ind))

    def shuffle(self):
        shuffle(self.deck)

    def draw_top(self):
        drawn = self.deck.pop()
        self.card_quantity[drawn] -= 1
        assert self.card_quantity[drawn] >= 0
        return drawn

