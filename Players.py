import Card
import Pack
import Game


class Player:
    def __init__(self, player_id, parent_g):
        self.hand = []
        self.id = player_id
        self.game = parent_g

        # TODO Below
        """
        implement input as a function pointer to handle input getting from the user and also for bot
        """
        if game_type == 1:
            self.input = int()

    def __draw(self):
        self.hand.append(self.game.deck.draw_top())

    def __give_hint(self, player_choice: int, choice):
        if self.game.tokens > 0:
            self.game.tokens -= 1
            # TODO handle choice logic
        return None

    def __discard(self, hand_ind: int):
        if self.game.tokens < 8:
            self.game.tokens += 1
            self.__draw()
            return self.hand.pop(hand_ind)

        return None

    def __play(self, hand_ind: int):
        played_card = self.hand.pop(hand_ind)
        self.__draw()
        return played_card

    # TODO Adjust for Return types
    # COMMENT I think logic is better handled in Game - Vik
    # TODO adjust turn to work with the input object from game
    def turn(self, game_type: int, turn_type: int):
        if turn_type == 1:
            self.__give_hint()
        elif turn_type == 2:
            self.__discard(hand_ind)
        else:
            return self.__play(hand_ind)

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

