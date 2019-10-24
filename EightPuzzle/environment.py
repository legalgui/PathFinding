""" Module that implements a Node and its Board for uninformed search

    The exported classes include a Board that serves as a reference for
    an 8 piece puzzle, using a Node to build an uninformed search tree
    and traverse through its action space.
"""
import copy
import helper

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
        """
        new_action = self.current_node.actions.pop(0)
        new_state = self.execute_action(new_action)
        return Node(self.current_node, new_state, new_action)
