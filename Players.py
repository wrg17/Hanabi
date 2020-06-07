import Card
import Pack


class Player:
    def __init__(self, player_id, player_type):
        self.hand = []
        self.id = player_id

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

    def __draw(self, deck: Pack):
        self.hand.append(deck.draw_top())

    def __give_hint(self):
        [player_choice, hint_type, hint] = self.get_input(1)
        h = ""
        if hint_type == 0:
            assert 0 <= hint < len(rank_list)
            h = rank_list[hint]
        elif hint_type == 1:
            assert 0 <= hint < len(suit_list)
            h = suit_list[hint]
        # TODO change once output function is implemented
        print("Player ", self.id, " tells player ",
              player_choice, " about all of their ", h, " cards.\n")

    def __discard(self):
        hand_ind = self.get_input(2)
        # TODO change once output function is implemented
        print("Player ", self.id, " has discarded a", self.hand[hand_ind].get_suit_str(),
              " ", self.hand[hand_ind].get_rank_str(), ".\n")
        return self.hand.pop(hand_ind)
        

    def __play(self):
        hand_ind = self.get_input(3)
        # TODO change once output function is implemented
        print("Player ", self.id, " has played a", self.hand[hand_ind].get_suit_str(),
              " ", self.hand[hand_ind].get_rank_str(), ".\n")
        return self.hand.pop(hand_ind)

    # TODO split discard_pile into safe and unsafe (pair of dictionaries)
    def turn(self, tokens: int, lives: int, deck, discard_pile, board):
        # TODO need to implement some try catch feature to check that turn choice is allowed
        turn_type = self.get_input(0, tokens)
        
        if turn_type == 1:
                self.__give_hint()
                tokens += 1
        elif turn_type == 2:
            # TODO change logic when we change the structure of discard_pile
            discard_pile[card.get_suit()].append(card)
            self.__draw(deck)
        else:
            card = self.__play(hand_ind)
            if card.is_playable(board):
                board[card.get_suit()] = card
                if card.get_rank() == 5:
                    tokens += 1
            else:
                discard_pile[card.get_suit()].append(card)
                lives -= 1
                
            self.__draw(deck)


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
