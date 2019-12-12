#-*- coding: utf-8 -*-
import string
import random

dict_name = {}
S = 0
def tsk_0 ():
    with open ("input.txt", "r", encoding='utf-8') as f:
        print("STEP 1: ")
        for line in f:
            line = line.strip()
            line = line.split('.')
            dict_name[line[0]] = int (line[1].strip())
            print (line, end='\n')
        print ()

    print("STEP 2: SET LIST")
    for second_name, value in dict_name.items():
        print ("{:15} {}".format (second_name, value))
    print()

    print("STEP 2: Список студентов обучающиеся на оц. <= 3")
    for second_name, value in dict_name.items():
        S += value
        if value <= 3:
            print ("{:15} {}".format (second_name, value))
    print()


    print ("------")
    mean = sum(dict_name.values()) / len(dict_name)
    print ("Средний бал {:.2f}".format(mean))
    print ("Средний бал {:.2%}".format(mean))

def tsk_1():
    split_value = ['!', '?', '...', '.']
    count_sentense = 0
    with open ("input_two.txt", "r", encoding='utf-8') as f:
        print("STEP 1: ")
        text = f.read()
        for char in split_value:
            text = text.replace(char, ".")

        sentense = text.split(".")
        print('STEP 2', sentense)
        print()

        for i in sentense:
            count_sentense += 1
        print("STEP 2: КОЛ_ВО ПРЕДЛОЖЕНИЙ: ", count_sentense)
        print()

        count_word = 0
        for s in sentense:
            count_word += len(s.split(" "))
            print("{:120} {}".format (s, count_word))
        print("STEP 3: КОЛ_ВО СЛОВ: ", count_word)
        print()

        count_let = 0
        no__ = text.replace('.', '')
        no__ = no__.replace(' ', '')
        no__ = no__.replace("’", '')
        no__ = no__.replace(",", '')
        print(no__)
        print()
        len_ = len(no__)
        print("Всего букв в тексте: = ", len_)
        print()

       # for i in range(len_)


        # print(string.punctuation)
        # ll = len(string.punctuation)
        # print(ll)
        # for i in string.punctuation:
        #     print(i)




def tsk_w ():

    row = 5
    col = 5
    table = []
    with open("input_num.txt", "w", encoding='utf-8')  as f:

        for _ in range(row):
            table.append([random.randint(-3, 3) for _ in range(col)])
        print("step 1: ", table)
        print()

        print("step 2: вывод в виде таблицы")
        for i in range(row):
            print("<---------------------->")
            for j in range(col):
                f.write("{:{width}}".fotmat(i*j, width))
                print(table[i][j], end=" ")
            f.write ("\n")
            print("<-ln.down->")





