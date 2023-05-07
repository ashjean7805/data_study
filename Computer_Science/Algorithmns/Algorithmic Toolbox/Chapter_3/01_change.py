def change(money):
    # write your code here
    n = 0
    n += (money//10)
    money = money % 10
    n += (money//5)
    n += money % 5
    return n



if __name__ == '__main__':
    m = int(input())
    print(change(m))
