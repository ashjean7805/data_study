def edit_distance(first_string, second_string):
    n_first = len(first_string) 
    n_second = len(second_string)
    dp_matrix = [[0 for x in range(n_second+1)] for x in range(n_first+1)]
    for i in range(1, n_first + 1):
        dp_matrix[i][0] = i

    for j in range(1, n_second + 1):
        dp_matrix[0][j] = j

    for i in range(1,n_first+1):
        for j in range(1,n_second+1):
            if first_string[i-1] == second_string[j-1]:
                dp_matrix[i][j] = dp_matrix[i-1][j-1]
            else:
                dp_matrix[i][j] = min(dp_matrix[i][j-1],dp_matrix[i-1][j],dp_matrix[i-1][j-1])+1
    return dp_matrix[n_first][n_second]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
