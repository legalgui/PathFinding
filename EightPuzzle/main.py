""" This code implements a path Finder with uninformed search,
    being able to use DFS or BFS for traversal
"""
from __future__ import print_function
import search

def run():
    """ Function that runs the uninformed search
    """
    initial_state = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
    final_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    algorithm = 0 # 0 for BFS / 1 for DFS
    print(search.uninformed_search(initial_state, final_state, algorithm))


if __name__ == "__main__":
    run()
