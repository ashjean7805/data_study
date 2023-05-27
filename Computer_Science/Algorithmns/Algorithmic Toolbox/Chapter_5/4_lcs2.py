def lcs2(first_sequence, second_sequence):
    n_first = len(first_sequence) 
    n_second = len(second_sequence)
    dp_matrix = [[0 for x in range(n_second+1)] for x in range(n_first+1)]
    for i in range(1,n_first+1):
        for j in range(1,n_second+1):
            if first_sequence[i-1] == second_sequence[j-1]:
                dp_matrix[i][j] = dp_matrix[i-1][j-1] + 1
            else:
                dp_matrix[i][j] = max(dp_matrix[i][j-1],dp_matrix[i-1][j])
    return dp_matrix[n_first][n_second] 


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))