from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0
    # write your code here
    # f_values = [values[i] / weights[i]  for i in range(len(weights))]
    f_values = [values[i] / weights[i]  for i in range(n)]
    flag = True

    while(flag):
        try:
            max_index = f_values.index(max(f_values))
        except:
            break
        if(weights[max_index] <= capacity):
            capacity -= weights[max_index]
            value += values[max_index]
            values.pop(max_index)
            f_values.pop(max_index)
            weights.pop(max_index)
        else:
            value += f_values[max_index]*capacity
            flag = False
            break

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
