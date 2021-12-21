import copy
import time


class Game:
    def __init__(self, chips: int):
        self.initialize_game()
        self.current_state = [chips]

    def initialize_game(self):
        self.current_state = []

        # Possible Players are Max or Min
        # Max is the computer
        # Min is the human player
        # Player Max always plays first
        self.player_turn = 'Max'

    def draw_board(self):
        print(self.current_state)
        print()

    def is_valid(self, index: int, new_stack: list):
        # index is an integer of the list to explode
        # newList is the result of the exploded list only
        # newList must be appended then to the state
        if self.current_state[index] <= 2:
            return False
        elif len(new_stack) != 2 or new_stack[0] + new_stack[1] != self.current_state[index]:
            return False
        else:
            return True

    def explode_stack(self, index: int, new_stack: list):
        del self.current_state[index]
        i = index
        for chip in new_stack:
            self.current_state.insert(i, chip)
            i = i + 1

    def possible_sum(self, x: int):
        possibles: list[list]
        possibles = []

        for i in range(1, x // 2):
            possibles.append([x - i, i])
        if x % 2 != 0:
            possibles.append([x // 2 + 1, x - (x // 2 + 1)])
        return possibles

    def is_end(self):
        # checks if all the chips are 1 or 2 then the game is finished and the blocked player has lost
        # we verify if there is a chips >2 then the game is not ended yet =>we return None
        for stack in self.current_state:
            if stack > 2:
                return None
        # if all the chips are under or equal to 2 then the game is ended and the player that have the turn has lost
        return self.player_turn

    def max(self):

        # Possible values for maxv are:
        # -1 - loss
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = float('-inf')

        index = None
        sum_result = None
        self.player_turn = 'Max'
        result = self.is_end()

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 1  - win
        if result == 'Min':
            return (1, 0, 0, 1)
        elif result == 'Max':
            return (-1, 0, 0, 1)
        # we will loop on the current stack chips
        stack_before = copy.deepcopy(self.current_state)
        visited_nodes = 0
        for i in range(0, len(self.current_state)):
            # test if the chips is greater than two then we can still devid it
            if self.current_state[i] > 2:
                sum_list = self.possible_sum(self.current_state[i])
                for sum in sum_list:
                    # here sum is a list composed of the two numbers in the sum of current number for exple 7 => [6,1]
                    self.explode_stack(i, sum)
                    (m, min_i, min_j, child_visited_nodes) = self.min()
                    visited_nodes = visited_nodes + child_visited_nodes + 1
                    if m > maxv:
                        maxv = m
                        index = i
                        sum_result = sum
                    self.current_state = stack_before[:]
        return (maxv, index, sum_result, visited_nodes)

    def min(self):

        # Possible values for maxv are:
        # -1 - loss
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        minv = float('inf')

        index = None
        sum_result = None
        self.player_turn = 'Min'
        result = self.is_end()

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 1  - win
        if result == 'Min':
            return (1, 0, 0, 1)
        elif result == 'Max':
            return (-1, 0, 0, 1)
        self.player_turn = 'Min'
        # we will loop on the current stack chips
        stack_before = copy.deepcopy(self.current_state)
        visited_nodes = 0
        for i in range(0, len(self.current_state)):
            # test if the chips is greater than two then we can still divide it
            if self.current_state[i] > 2:
                sum_list = self.possible_sum(self.current_state[i])
                for sum in sum_list:
                    # here sum is a list composed of the two numbers in the sum of current number for exple 7 => [6,1]
                    self.explode_stack(i, sum)
                    (m, max_index, max_sum, child_visited_nodes) = self.max()
                    visited_nodes = visited_nodes + child_visited_nodes + 1
                    if m < minv:
                        minv = m
                        index = i
                        sum_result = sum
                    self.current_state = stack_before[:]
        return (minv, index, sum_result, visited_nodes)

    def max_alpha_beta_pruning(self, alpha, beta):

        # Possible values for maxv are:
        # -1 - loss
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = float('-inf')

        index = None
        sum_result = None
        self.player_turn = 'Max'
        result = self.is_end()

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 1  - win
        if result == 'Min':
            return (1, 0, 0, 1)
        elif result == 'Max':
            return (-1, 0, 0, 1)
        # we will loop on the current stack chips
        stack_before = copy.deepcopy(self.current_state)
        visited_nodes = 0
        for i in range(0, len(self.current_state)):
            # test if the chips is greater than two then we can still devid it
            if self.current_state[i] > 2:
                sum_list = self.possible_sum(self.current_state[i])
                for sum in sum_list:
                    # here sum is a list composed of the two numbers in the sum of current number for exple 7 => [6,1]
                    self.explode_stack(i, sum)
                    (m, min_i, min_j, child_visied_nodes) = self.min_alpha_beta_pruning(alpha, beta)
                    visited_nodes = visited_nodes + child_visied_nodes + 1
                    if m > maxv:
                        maxv = m
                        index = i
                        sum_result = sum
                    self.current_state = stack_before[:]
                    # the only diff with the normal max
                    if maxv >= beta:
                        return (maxv, index, sum_result, visited_nodes)

                    if maxv > alpha:
                        alpha = maxv
        return (maxv, index, sum_result, visited_nodes)

    def min_alpha_beta_pruning(self, alpha, beta):

        # Possible values for maxv are:
        # -1 - loss
        # 1  - win

        # We're initially setting it to +inf as worse than the worst case:
        minv = float('inf')

        index = None
        sum_result = None
        self.player_turn = 'Min'
        result = self.is_end()

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 1  - win
        if result == 'Min':
            return (1, -1, [], 1)
        elif result == 'Max':
            return (-1, -1, [], 1)
        self.player_turn = 'Min'
        # we will loop on the current stack chips
        stack_before = copy.deepcopy(self.current_state)
        visited_nodes = 0
        for i in range(0, len(self.current_state)):
            # test if the chips is greater than two then we can still divide it
            if self.current_state[i] > 2:
                sum_list = self.possible_sum(self.current_state[i])
                for sum in sum_list:
                    # here sum is a list composed of the two numbers in the sum of current number for exple 7 => [6,1]
                    self.explode_stack(i, sum)
                    (m, max_index, max_sum, child_visited_nodes) = self.max_alpha_beta_pruning(alpha, beta)
                    visited_nodes = visited_nodes + child_visited_nodes + 1
                    if m < minv:
                        minv = m
                        index = i
                        sum_result = sum
                    self.current_state = stack_before[:]
                    # The only diff with normal min
                    if minv <= alpha:
                        return (minv, index, sum_result, visited_nodes)

                    if minv < beta:
                        beta = minv
        return (minv, index, sum_result, visited_nodes)

    def play(self):
        while True:
            self.draw_board()
            self.result = self.is_end()

            # Printing the appropriate message if the game has ended
            if self.result != None:
                if self.result == 'Min':
                    print('The winner is IA!')
                elif self.result == 'Max':
                    print('The winner is Human!')

                self.initialize_game()
                return

            # If it's player's turn
            if self.player_turn == 'Min':

                while True:

                    start = time.time()
                    (m, index, sum, visited_nodes) = self.min()
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: Stack Index = {}, Sum = {}'.format(index, sum))

                    player_index = int(input('Insert the index of the stack to explode: '))
                    player_sum_1st_member = int(input('Insert the sum 1st member: '))
                    player_sum_2nd_member = int(input('Insert the sum 2nd member: '))
                    player_sum = [player_sum_1st_member, player_sum_2nd_member]
                    (index, sum) = (player_index, player_index)

                    if self.is_valid(player_index, player_sum):
                        self.explode_stack(player_index, player_sum)
                        self.player_turn = 'Max'
                        break
                    else:
                        print('The move is not valid! Try again.')

            # If it's AI's turn
            else:
                (m, index, sum, visited_nodes) = self.max()
                self.explode_stack(index, sum)
                self.result = self.is_end()
                self.player_turn = 'Min'

    def play_with_pruning(self):
        while True:
            self.draw_board()
            self.result = self.is_end()

            # Printing the appropriate message if the game has ended
            if self.result != None:
                if self.result == 'Min':
                    print('The winner is IA!')
                elif self.result == 'Max':
                    print('The winner is Human!')

                self.initialize_game()
                return

            # If it's player's turn
            if self.player_turn == 'Min':

                while True:

                    start = time.time()
                    (m, index, sum, visited_nodes) = self.min_alpha_beta_pruning(-2, 2)
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: Stack Index = {}, Sum = {}'.format(index, sum))

                    player_index = int(input('Insert the index of the stack to explode: '))
                    player_sum_1st_member = int(input('Insert the sum 1st member: '))
                    player_sum_2nd_member = int(input('Insert the sum 2nd member: '))
                    player_sum = [player_sum_1st_member, player_sum_2nd_member]
                    (index, sum) = (player_index, player_index)

                    if self.is_valid(player_index, player_sum):
                        self.explode_stack(player_index, player_sum)
                        self.player_turn = 'Max'
                        break
                    else:
                        print('The move is not valid! Try again.')

            # If it's AI's turn
            else:
                (m, index, sum, visited_nodes) = self.max_alpha_beta_pruning(-2, 2)
                self.explode_stack(index, sum)
                self.result = self.is_end()
                self.player_turn = 'Min'

    def play_simulation(self, pruning):
        while True:
            self.draw_board()
            self.result = self.is_end()

            # Printing the appropriate message if the game has ended
            if self.result != None:
                if self.result == 'Min':
                    print('The winner is IA!')
                elif self.result == 'Max':
                    print('The winner is Human!')

                self.initialize_game()
                return

            # If it's player's turn
            if self.player_turn == 'Min':
                start = time.time()
                if pruning:
                    (m, index, sum, visited_nodes) = self.min_alpha_beta_pruning(-2, 2)
                else:
                    (m, index, sum, visited_nodes) = self.min()
                end = time.time()
                self.explode_stack(index, sum)
                self.player_turn = 'Max'
            # If it's AI's turn
            else:
                if pruning:
                    (m, index, sum, visited_nodes) = self.max_alpha_beta_pruning(-2, 2)
                else:
                    (m, index, sum, visited_nodes) = self.max()
                self.explode_stack(index, sum)
                self.result = self.is_end()
                self.player_turn = 'Min'

    def max_visited_nodes(self, pruning):
        if (pruning):
            (max, index, sum, visited_nodes) = self.max_alpha_beta_pruning(-2, 2)
        else:
            (max, index, sum, visited_nodes) = self.max()
        return visited_nodes
