""" Module that implements helper functions
"""
def swap(two_list, i_a, j_a, i_b, j_b):
    """ Swaps two matrix values

        Arguments:
            two_list: A list of lists, matrix or object indexable by [][]
            i1, j1, i2, j2: The indexes for value retrieval
    """
    temp = two_list[i_a][j_a]
    two_list[i_a][j_a] = two_list[i_b][j_b]
    two_list[i_b][j_b] = temp


def index_2d(value, two_list):
    """ Gets the 2D index of a value within a list of lists

        Arguments:
            value: An integer to represent the white piece
            two_list: A list of lists of integers that represent the
                        board pieces i.e [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
        Returns:
            Two integers, one for the y coordinate and another for the
            x coordinate of the value in the map. If the value is not found
            it returns -1
    """
    for y_coordinate, row in enumerate(two_list):
        if value in row:
            x_coordinate = row.index(value)
            return (y_coordinate, x_coordinate)
    return -1
