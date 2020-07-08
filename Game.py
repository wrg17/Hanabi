import Card
import Pack
import Players


def variant(var_num: int):
    if var_num == 1:
        return Game()


class Game:
    def __init__(self, game_type: int, num_players):
        # TODO split discard pile into safe and unsare (pair of dictionaries)
        self.deck = Pack()
        self.lives = 3
        self.tokens = 8
        self.players = [Players.Human(i) for i in num_players]
        self.discard_pile = ({}, {})
        self.board = {}

    # TODO work with main to end the program and declare a loss
    def zero_lives(self):
        return None

    def deal(self):
        for i in range(5):
            for player in self.players:
                player.add_to_hand(self.deck.draw_top())

    # TODO split discard_pile into safe and unsafe (pair of dictionaries)
    def turn(self, player):
        # TODO need to implement some try catch feature to check that turn choice is allowed

        turn_type, other_player, hint_type, hand_info = player.decider(self)

        # If give hint
        if turn_type == 1:
            other_player.receive_hint(hint_type, hand_info)
            self.tokens -= 1
        else:
            popped_card = player.from_hand(hand_info)
            # If playing
            if turn_type == 2:
                if popped_card.is_playable(self.board):
                    self.board[popped_card.get_suit()] = popped_card
                    if popped_card.get_rank() == 5:
                        self.tokens += 1
                else:
                    self.lives -= 1
                    # TODO change logic when we change the structure of discard_pile
                    self.discard_pile[0][popped_card.get_suit()].append(popped_card)
                    player.add_to_hand(self.deck.draw_top())
            else:
                # TODO change logic when we change the structure of discard_pile
                self.discard_pile[0][popped_card.get_suit()].append(popped_card)
                player.add_to_hand(self.deck.draw_top())

        """
        turn_choice = int(input("Choose something to do: \n1) Give hint\n2) Discard\n3) Play\n"))
        if turn_choice == 1:
            player_ind = int(input("Which player would you like to give a hint to?"))
            choice_type = int(input("1) Rank\n2) Suit\n"))
            choice = ""
            if choice_type == 1:
                choice = int(input("Which rank would you like to inform player ", player_ind, " about?"))
            elif choice_type == 2:
                choice = int(input("Which rank would you like to inform player ", player_ind, " about?"))
            self.__give_hint(player_ind, choice)
        elif turn_choice == 2:
            hand_ind = int(input("Which card would you like to discard (1-5)?"))
            assert 1 <= hand_ind <= 5
            self.__discard(hand_ind)
        elif turn_choice == 3:
            hand_ind = int(input("Which card would you like to play (1-5)?"))
            assert 1 <= hand_ind <= 5
            self.__play(hand_ind)
        """

    def run(self):
        self.deck.shuffle()
        self.deal()

        num_players = len(self.players)
        player_ind = 0

        while len(self.deck) > 0:
            # If out of lives
            if self.lives < 1:
                self.zero_lives()

            # TODO switch to a container object ?
            self.turn(self.players[player_ind])

            player_ind = (player_ind + 1) % num_players

        for t in range(num_players):
            if self.lives < 1:
                self.zero_lives()
            self.turn(player_ind)
