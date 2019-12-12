
def tsk4 ():
    num = int (input("COUNT FROM - NUM: "))
    max = int (input("DO IN TILL - MAX: "))

    while num <= max:
        if num % 2 == 0:
            print (num)
            num += 1
        else:
            num += 1
            continue


def tsk5_bank (account, percent, needs):
    N = 0 # количесство лет
    am_ = 0
    while am_ <= needs:
        print("Amount ", am_, "YEAR(s) = ", N)
        am_ = am_ + ((account * percent) / 100)
        account = account + am_  ### Ваш код
        N += 1

    print(account)
    return N

#return_ = tsk5_bank(int(input("Сумма вклада = ")), float (input("Процентная ставка = ")), int (input("Желаемая сумма = ")))
#print(return_)


def tsk6 ():
    values= [1, 2, 4, 8, 16, 32, 64]
    dict_ = {v: 0 for v in values}
    N = 100221
    for v in reversed(list(dict_)):
        dict_[v] = N // v
        N = N % v
        print (v, dict_[v])

tsk6()