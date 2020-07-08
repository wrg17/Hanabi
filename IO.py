from Game import Game


class IOpy:
    def __init__(self, game_type: bool):
        if game_type == 1:
            pass
        elif game_type == 2:
            pass


class Output:
    # TODO pass a function that either sends to web or to console
    def __init__(self, f, g: Game):
        self.out_func = f

    def hint_output(self):
        pass

    def discard_output(self):
        pass

    def play_output(self):
        pass


class Console(Output):
    def hint_output(self):
        if hint_type == 0:
            assert 0 <= hint < len(rank_list)
            h = rank_list[hint]
        elif hint_type == 1:
            assert 0 <= hint < len(suit_list)
            h = suit_list[hint]
        # TODO change once output function is implemented
        print("Player ", self.id, " tells player ",
              player_choice, " about all of their ", h, " cards.\n")

    def discard_output(self):
        pass

    def play_output(self):
        pass


class Web(Output):
    def hint_output(self):
        pass

    def discard_output(self):
        pass

    def play_output(self):
        pass
