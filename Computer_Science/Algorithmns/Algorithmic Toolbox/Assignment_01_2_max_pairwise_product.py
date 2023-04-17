def max_pairwise_product(numbers):
    x = max(numbers)
    numbers.remove(x)
    return x * max(numbers)

if __name__ == '__main__':
    _ = input()
    print(max_pairwise_product(list(map(int, input().split()))))

