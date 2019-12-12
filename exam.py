def task_8(end):
    # YOUR CODE HERE
    n_list = [2]
    n = 0

    list_ = (2, 3, 4, 5, 6, 7, 8, 9)
    len_ = len(n_list)
    print(list_, len_)

    while len(n_list) < end:
        for i in list_:
            n += 1
            if n != 1 and n % i != 0:
                print(n)


assert task_8(1) == [2]
assert task_8(2) == [2, 3]
assert task_8(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]