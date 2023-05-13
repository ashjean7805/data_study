def majority_element_naive(elements):
    n = len(elements)/2
    ans = {}
    for e in elements:
        try:
            ans[e] += 1
        except:
            ans[e] = 1
    for answer in ans.values():
        if (answer > n):
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
