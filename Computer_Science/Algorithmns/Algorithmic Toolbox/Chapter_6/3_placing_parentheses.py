def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(dataset):
    n = len(dataset) // 2
    min_vals = [[float('inf')] * (n+1) for _ in range(n+1)]
    max_vals = [[-float('inf')] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        min_vals[i][i] = int(dataset[2*i])
        max_vals[i][i] = int(dataset[2*i])

    for length in range(1, n+1):
        for i in range(n-length+1):
            j = i + length
            min_val = float('inf')
            max_val = -float('inf')
            for k in range(i, j):
                op = dataset[2*k+1]
                a = evaluate(min_vals[i][k], min_vals[k+1][j], op)
                b = evaluate(min_vals[i][k], max_vals[k+1][j], op)
                c = evaluate(max_vals[i][k], min_vals[k+1][j], op)
                d = evaluate(max_vals[i][k], max_vals[k+1][j], op)
                min_val = min(min_val, a, b, c, d)
                max_val = max(max_val, a, b, c, d)
            min_vals[i][j] = min_val
            max_vals[i][j] = max_val

    return max_vals[0][n]



if __name__ == "__main__":
    print(maximum_value(input()))
