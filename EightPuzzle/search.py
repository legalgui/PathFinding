""" Module that implements the uninformed search, the depth first search and
    the breadth first search methods for game traversal.
"""
from __future__ import print_function
import test
import environment

def depth_first_search(board, nodes, route_queue, initial_state, final_state):
    """ Implements the depth first search algorithm

        Arguments:
            board: A board object that abstracts the 8 piece puzzle
            nodes: A Node objects list specifying each game step
            route_queue: A list of actions that describes the route
            initial_state: A list of lists describing the initial state
            final_state: A list of lists describing the final state
    """
    while nodes:
        board.current_node = nodes[-1]
        if not board.visited(board.current_node):
            if board.is_goal(board.current_node):
                nodes.append(board.current_node)
                while nodes:
                    route_queue.append(nodes.pop(0).arrival_action)
                route_queue.pop(0)
                if test.test(initial_state, final_state, route_queue):
                    return route_queue
                return []

            board.define_actions_current_node()

            # This is always true, left for heuristics
            if board.current_node.actions:
                new_node = board.create_child_current_node()
                nodes.append(new_node)
            else:
                print(1)
                nodes.pop(-1)

        else:
            if board.current_node.actions:
                new_node = board.create_child_current_node()
                nodes.append(new_node)
            else:
                nodes.pop(-1)


    return []

def breadth_first_search(board, nodes, route_queue, initial_state, final_state):
    """ Implements the breadth first search algorithm

        Arguments:
            board: A board object that abstracts the 8 piece puzzle
            nodes: A Node objects list specifying each game step
            route_queue: A list of actions that describes the route
            initial_state: A list of lists describing the initial state
            final_state: A list of lists describing the final state
    """
    while nodes:
        board.current_node = nodes.pop(0)
        board.define_actions_current_node()
        number_of_actions = len(board.current_node.actions)
        for i in range(0, number_of_actions):
            new_node = board.create_child_current_node()
            if not board.visited(new_node):
                if not board.is_goal(new_node):
                    nodes.append(new_node)
                else:
                    while new_node.parent != None:
                        route_queue.append(new_node.arrival_action)
                        new_node = new_node.parent

                    route_queue.reverse()
                    if test.test(initial_state, final_state, route_queue):
                        return route_queue
                    return []
    return []

def uninformed_search(initial_state, final_state, algorithm):
    """ Implements the uninformed search

        Arguments:
            initial_state: A list of lists describing the initial state
            final_state: A list of lists describing the final state
            algorithm: Integer for algorithm selection
    """
    if algorithm != 0 and algorithm != 1:
        print("Wrong Option")
        exit()

    source_node = environment.Node(None, initial_state, "IGNORE")
    goal_node = environment.Node(None, final_state, "IGNORE")

    board = environment.Board(source_node, goal_node)
    nodes = []
    nodes.append(source_node)

    route_queue = []

    if algorithm == 1:
        print("DFS SOLVER SELECTED")
        return depth_first_search(board, nodes, route_queue, initial_state, final_state)

    elif algorithm == 0:
        print("BFS SOLVER SELECTED")
        return breadth_first_search(board, nodes, route_queue, initial_state, final_state)

    else:
        print("Error")


def a_star_search(initial_state, final_state, heuristic):
    """ Implements the a star search

        Arguments:
            initial_state: A list of lists describing the initial state
            final_state: A list of lists describing the final state
            heuristic: Integer for heuristic selection
    """
    if heuristic != 0 and heuristic != 1:
        print("Wrong Option")
        exit()

    if heuristic:
        print("MANHATTAN DISTANCE HEURISTIC")
    else:
        print("ORDERED PIECES HEURISTIC")
        
    source_node = environment.Node(None, initial_state, "IGNORE")
    goal_node = environment.Node(None, final_state, "IGNORE")

    board = environment.Board(source_node, goal_node)
    node_list = environment.PriorityQueue()
    node_list.enqueue(source_node)
    route_queue = []

    while node_list:
        board.current_node = node_list.dequeue()
        board.define_actions_current_node()
        number_of_actions = len(board.current_node.actions)
        for i in range(0, number_of_actions):
            new_node = board.create_child_current_node()
            if not board.visited(new_node):
                if not board.is_goal(new_node):
                    new_node.update_search_values(heuristic, goal_node.state)
                    node_list.enqueue(new_node)
                else:
                    while new_node.parent != None:
                        route_queue.append(new_node.arrival_action)
                        new_node = new_node.parent

                    route_queue.reverse()
                    if test.test(initial_state, final_state, route_queue):
                        return route_queue
                    return []
    return []
