""" Module that implements a Node and its Board for uninformed search

    The exported classes include a Board that serves as a reference for
    an 8 piece puzzle, using a Node to build an uninformed search tree
    and traverse through its action space.
"""
import copy

class Node(object):
    """ Class Node to constitute a Tree for searching.

        Attributes:
            parent: A node from which this node was created.
            state: A list of strings with a path i.e ["UP", "UP", "DOWN"]
            actions: A list of strings i.e ["UP", "DOWN", "LEFT", "RIGHT"]
            arrival_action: A string i.e "UP", "DOWN", "LEFT", "RIGHT"
    """

    def __init__(self, parent, state, action):
        """ Inits Node Class with a Parent Node (Origin node), a State
            (description of its configuration), Actions (the list of
            possible actions) and the Action (state changer)
        """
        self.parent = parent
        self.state = state
        self.actions = []
        self.arrival_action = action

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.state == other.state

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

    def index_2d(self, value, state_list):
        """ Gets the 2D index of the white piece

            Arguments:
                value: An integer to represent the white piece
                state_list: A list of lists of integers that represent the
                            board pieces i.e [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
            Returns:
                Two integers, one for the y coordinate and another for the
                x coordinate of the value in the map. If the value is not found
                it returns -1
        """
        for y_coordinate, row in enumerate(state_list):
            if value in row:
                x_coordinate = row.index(value)
                return (y_coordinate, x_coordinate)
        return -1
