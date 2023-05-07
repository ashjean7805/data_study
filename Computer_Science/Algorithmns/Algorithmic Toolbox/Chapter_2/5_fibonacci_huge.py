def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%m

    return current 

# def fibonacci_huge_naive(n,m):
#     damn = []
#     for i in range(n+1):
#         if i <= 1:
#             damn.append(i)
#         else:
#             damn.append((damn[i-1]+damn[i-2])%m)
#     return damn.pop()


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
