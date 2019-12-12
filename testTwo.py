


def tsk2 (N):
    fl = True
    while True:
        if N % 3 == 0:
            N = N // 3
            if N == 1 or N == 2:
                break
            else:
                continue
        else:
            fl = False
            break
    return fl


def tsk1 ():
    i = 0
    N = 20
    S = 0
    max_ = 500
    control = 0

    while i <= N:
        i += 1
        if i % 2 == 0:
            S += i ** 2
            print ("i = ", i, "S = ", S, 'control = ', control)

        else:
            continue

        if S > max_:
            print()
            print("Активированна функция BREAK так как S>", max_, " CONTROL = ", control)
            break

if __name__ == "__main__":
    print (22//3)
    num = int (input("Введите число: "))
    result = tsk2(num)
    if result:
        print("+")

    else:
        print("-")
