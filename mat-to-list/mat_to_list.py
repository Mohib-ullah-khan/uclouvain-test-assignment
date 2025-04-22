def mat_to_list(adj_mat):
    """Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """
    adj_list = []
    for i in range(len(adj_mat)):
        adj_list.append([])
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 1:
                adj_list[i].append(j)

    return adj_list
