def arr_union(a, b, n, m):
    uni_arr = []
    for num in a:
        if num not in uni_arr:
            uni_arr.append(num)
    for num in b:
        if num not in uni_arr:
            uni_arr.append(num)
    print(len(uni_arr))

arr_union([1, 2, 3, 4, 5], [1, 2, 3], 5, 3)