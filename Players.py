import Card
import Pack
import Game


class Player:
    def __init__(self, player_id):
        self.hand = []
        self.id = player_id

    def add_to_hand(self, c: Card):
        self.hand.append(c)

    def from_hand(self, hand_ind):
        return self.hand.pop(hand_ind)

    def receive_hint(self, hint_type, hint):
        pass


class Human(Player):
    def __init__(self, player_id):
        super().__init__(player_id)

        # TODO Below
        """
        - implement input as a function pointer to handle input getting from the user and also for bot
        - get_input(type: int) is its name
            - type == 0 --> get turn_type (1,2, or 3)
            - type == 1 --> get input for hint
            - type == 2 --> get input for discard
            - type == 3 --> get input for play
        - implement output as a function point to handle giving output to different types of players
            - encode various outputs like above
        """
        self.decider = IOpy(game_type)


    def __console_input(self):
        super().game
        turn_type, player_ind, hint_type, hand_ind = 0, 0, 0, 0
        return [turn_type, player_ind, hint_type, hand_ind]

    def __console_output(self):
        pass

    def __web_input(self):
        pass

    def __web_output(self):
        pass


class Simple(Player):
    def __init__(self, player_id, player_type):
        super().__init__(player_id)

        # TODO Below
        """
        - implement input as a function pointer to handle input getting from the user and also for bot
        - get_input(type: int) is its name
            - type == 0 --> get turn_type (1,2, or 3)
            - type == 1 --> get input for hint
            - type == 2 --> get input for discard
            - type == 3 --> get input for play
        - implement output as a function point to handle giving output to different types of players
            - encode various outputs like above
        """
        if game_type == 1:
            self.input = int()

    def recieve_hint(self):
        pass