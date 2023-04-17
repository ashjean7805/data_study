def sum_of_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    A,B = map(int, input().split())
    print(sum_of_digits(A,B))