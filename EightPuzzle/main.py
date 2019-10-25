""" This code implements a path Finder with uninformed search,
    being able to use DFS or BFS for traversal, as well as A star search
    using Manhattan Distance or Ordered Pieces heuristics
"""
from __future__ import print_function
import search

def run():
    """ Function that runs the uninformed search and the A star search
    """
    initial_state = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
    final_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    algorithm = 0 # 0 for BFS / 1 for DFS
    print(search.uninformed_search(initial_state, final_state, algorithm))

    print("-----")

    heuristic = 0 # 0 for Manhattan Distance / 1 for Piece Count
    print(search.a_star_search(initial_state, final_state, heuristic))


if __name__ == "__main__":
    run()
