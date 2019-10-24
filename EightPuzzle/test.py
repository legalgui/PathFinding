""" Module that implements test functions for the path finding
"""
from __future__ import print_function
import copy
import environment

def test(initial_state, final_state, path):
    """ Tests the route got from search

        Arguments:
            initial_state: A list of lists describing the initial state
            final_state: A list of lists describing the final state
            path: A list of strings that indicate each step of the path
    """

    test_source_node = environment.Node(None, initial_state, "IGNORE")
    test_goal_node = environment.Node(None, final_state, "IGNORE")
    test_board = environment.Board(test_source_node, test_goal_node)
    test_board.current_node = test_source_node
    test_path = copy.deepcopy(path)

    while test_path:
        test_new_action = test_path.pop(0)
        test_new_state = test_board.execute_action(test_new_action)
        test_board.current_node.state = test_new_state
        if test_board.current_node == test_goal_node:
            print("PATH TEST PASSED")
            return True

    print("PATH TEST FAILED")
    return False
