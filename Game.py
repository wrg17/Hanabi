import Card
import Pack
import Players


class Game:
    def __init__(self, game_type: int, num_players):
        self.deck = Pack()
        self.lives = 3
        self.tokens = 8
        self.players = [Player(i, self) for i in num_players]
        self.discard_pile = []
        self.board = []

    # TODO work with main to end the program and declare a loss
    def zero_lives(self):
        return None

    def deal(self):
        for i in range(5):
            for player in self.players:
                player.__draw()

    def run(self):
        self.deck.shuffle()
        self.deal()

        num_players = len(self.players)
        turn = 0

        while len(self.deck) > 0:
            # If out of lives
            if self.lives < 1:
                self.zero_lives()

            self.players[turn].turn(self.tokens, self.lives, self.deck,
                                    self.discard_pile, self.board)

            turn = (turn + 1) % num_players

        for t in range(num_players):
            if self.lives < 1:
                self.zero_lives()
            self.players[(turn + t) % num_players].turn(self.tokens, self.lives, self.deck,
                                    self.discard_pile, self.board)
