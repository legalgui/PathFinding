""" Module that implements a Node and its Board for uninformed search, as well
    as a Priority Queue for an ordered insertion of nodes depending their
    state

    The exported classes include a Board that serves as a reference for
    an 8 piece puzzle, using a Node to build an uninformed search tree
    and traverse through its action space.
"""
from __future__ import print_function
from itertools import product
import copy
import helper

class PriorityQueue(object):
    """ Class Priority Queue that constitutes a queue with special insertion

        Attributes:
            priority_list: A node from which this node was created.
    """
    def __init__(self):
        """ Inits PriorityQueue class with an empty list
        """
        self.priority_list = []

    def enqueue(self, node):
        """ Enqueues the Node in a position that depends on its weight
            Arguments:
                node: A node that will be appended in order
        """
        if not self.priority_list:
            self.priority_list.append(node)
        else:
            for i in range(0, len(self.priority_list)):
                if self.priority_list[i].weight >= node.weight:
                    self.priority_list.insert(i, node)
                    return
            self.priority_list.append(node)

    def dequeue(self):
        """ Dequeues the first node
        """
        return self.priority_list.pop(0)

class Node(object):
    """ Class Node to constitute a Tree for searching.

        Attributes:
            parent: A node from which this node was created.
            state: A list of strings with a path i.e ["UP", "UP", "DOWN"]
            state_size: An integer length of the state
            actions: A list of strings i.e ["UP", "DOWN", "LEFT", "RIGHT"]
            arrival_action: A string i.e "UP", "DOWN", "LEFT", "RIGHT"
            cost: An integer of the step's cost
            heuristic: An integer of the heuristic's value
            weight: An integer of the sum of the cost and heuristic
    """

    def __init__(self, parent, state, action):
        """ Inits Node Class with a Parent Node (Origin node), a State
            (description of its configuration), the size of the State,
            Actions (the list of possible actions), the Action (state changer),
            the Heuristic (the value of the heuristic), the Cost (the cost value),
            the Weight (the weighted score of the heuristic and the cost)
        """
        self.parent = parent
        self.state = state
        self.state_size = len(state)
        self.actions = []
        self.arrival_action = action
        self.cost = 0
        self.heuristic = 0
        self.weight = 0

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.state == other.state

    def count_ordered_pieces(self, final_state):
        """ Counts the number of pieces that are on their correct location

            Arguments:
                final_state: A list of lists that specifies the target state
            Returns:
                count: An integer specifying the number of correct pieces
        """
        count = 0
        for i, j in product(range(self.state_size), range(self.state_size)):
            if self.state[i][j] == final_state[i][j]:
                count += 1
        return count

    def calculate_manhattan_distance(self, final_state):
        """ Calculates the manhattan distance between two states

            Arguments:
                final_state: A list of lists that specifies the target state
            Returns:
                distance: An integer specifying the distance from the final
                          state
        """
        distance = 0
        for i, j in product(range(self.state_size), range(self.state_size)):
            row, col = helper.index_2d(self.state[i][j], final_state)
            distance += abs(row - i) + abs(col - j)
        return distance

    def calculate_cost(self):
        """ Calculates the cost of traversal

            Returns:
                count: An integer specifying the cost of the traversal
        """
        count = 0
        parent = self.parent
        while parent != None:
            parent = parent.parent
            count += 1
        return count


    def update_search_values(self, heuristic_type, final_state):
        """ Updates the cost via the heuristic and updates the weight

            Arguments:
                final_state: A list of lists that specifies the target state
                heuristic_type: An integer that specifies which heuristic the
                                search must use
        """
        if heuristic_type == 1:
            self.heuristic = self.calculate_manhattan_distance(final_state)
        else:
            self.heuristic = self.count_ordered_pieces(final_state)
        self.cost = self.calculate_cost()
        self.weight = self.cost + self.heuristic

class Board(object):
    """ Class Board that abstracts the 8 piece puzzle

        Attributes:
            source_node: A node that specifies the origin
            goal_node: A node that specifies the destination
            current_node: A node that specifies the actual node
            visited_states: A list of strings that specify past states
            rows: An integer with the number of rows
            columns: An integer with the number of columns
    """

    def __init__(self, source_node, goal_node):
        """ Inits Board Class with a Source Node (position of white piece),
            Goal Node (goal position of white piece), Current Node (current
            position of white piece), Visited States (description of the path)
            and Rows and Columns (the dimensions of the board)
        """
        self.source_node = source_node
        self.goal_node = goal_node
        self.current_node = source_node
        self.visited_states = []
        self.rows = len(source_node.state)
        self.columns = len(source_node.state[0])

    def visited(self, node):
        """ Checks if the state has been visited

            Arguments:
                node: A Node object with its state
            Returns:
                True if visited,
                False if not visited
        """
        if node.state not in self.visited_states:
            self.visited_states.append(node.state)
            return False
        return True

    def is_goal(self, node):
        """ Checks if the node's state is the goal

            Arguments:
                node: A Node object with its state
            Returns:
                True if node's state is the goal,
                False if it's not the goal
        """
        return node == self.goal_node

    def define_actions_current_node(self):
        """ Defines the legal actions for the current node
        """
        current_state = self.current_node.state
        row, col = helper.index_2d(0, current_state)

        # Prevent Loop, create Action List
        if row > 0 and self.current_node.arrival_action != "DOWN":
            self.current_node.actions.append("UP")
        if row < self.rows - 1 and self.current_node.arrival_action != "UP":
            self.current_node.actions.append("DOWN")
        if col > 0 and self.current_node.arrival_action != "RIGHT":
            self.current_node.actions.append("LEFT")
        if col < self.columns - 1 and self.current_node.arrival_action != "LEFT":
            self.current_node.actions.append("RIGHT")

    def execute_action(self, action):
        """ Swaps two matrix values

            Arguments:
                action: A string defining a direction for action
            Returns:
                current_state: A list of lists that describes the current state
        """
        current_state = copy.deepcopy(self.current_node.state)
        row, col = helper.index_2d(0, current_state)

        if action == "UP":
            helper.swap(current_state, row, col, row - 1, col)
        elif action == "DOWN":
            helper.swap(current_state, row, col, row + 1, col)
        elif action == "RIGHT":
            helper.swap(current_state, row, col, row, col + 1)
        elif action == "LEFT":
            helper.swap(current_state, row, col, row, col - 1)
        return current_state

    def create_child_current_node(self):
        """ Creates a child for the current node

            Returns:
                anonymous node: A fully constructed instance of a Node
        """
        new_action = self.current_node.actions.pop(0)
        new_state = self.execute_action(new_action)
        return Node(self.current_node, new_state, new_action)
