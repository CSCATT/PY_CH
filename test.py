import random

def random_table(rows, columns):
    table = []
    for _ in range(rows):
        table.append([random.randint(-9, 9) for _ in range(columns)])
    return table

def task_2():
    for i in range(1, 10):
        for j in range(1, 10):
            print (i * j, end = " ")
        print (end="\n")

def task_3():
    rows = 5
    columns = 6
    tab = random_table(rows, columns)

    mean_col = []
    min_row = []
    max_row = []

    count_ = 0

    print()
    print ("таблица рандом", tab)
    print()

    #среднее арифметическое каждого столбца
    def mean_(n):
        print()
        for col in range(columns):
            s = 0

            n += 1
            print(n, "STEP:", "MEAN ------> ", mean_col)

            for row in range(rows):
                s += tab[row][col]
            mean_col.append(s / rows)


    #максимум и минимум каждой строки
    for r in range(rows):
        min_row.append(min(tab[r]))
        max_row.append(max(tab[r]))

        count_ += 1
        print(count_, "STEP:", "MIN ------> ", min_row, "    MAX ------> ", max_row)


    mean_(count_)

def task_7():
    rows = 7
    columns = 7
    tab = random_table(rows, columns)

    print()
    print("таблица рандом", tab)
    print()

    max_col = []
    count_ = 0

    print(max(tab))


    for col in range(columns):
        m_ = 0
        for row in range(rows):
            m_ = tab[row][col]
            if tab[row][col] > m_:
                print("Число {} больше найденного прежде минимального элемента {}".format(tab[row][col], m_))
                m_ = tab[row][col]  # новый минимум
            else:
                print("Число {} меньше найденного прежде минимального элемента {}".format(tab[row][col], m_))
            print("---")
        print("Конец цикла")
        print()
        print("Ответ: максимальный элемента списка = ", m_)
        print()

        #count_ += 1
        #print(count_, "STEP:", "MAX ------> ", max_col)

def hw1 ():
    rows = 3
    columns = 4
    tab = random_table(rows, columns)

    print()
    print("таблица рандом", tab)
    print()

    sum_ = 0

    for col in range(-1):
        for row in range(rows):
            sum_ += tab[row][col]
    print(sum_)



if __name__ == "__main__":
   # task_2()
   #task_3()
   #task_7()
   hw1()
   # print()
   # print(random_table(5, 6))



