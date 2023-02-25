def bubbleSort(list1):
    for i in range(len(list1)):
        for j in range(0, len(list1) - i - 1):
            if list1[j] > list1[j + 1]:
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp


Pos = [4, 76, 30, 10, 5, 7]
bubbleSort(Pos)

print('Отсортированные числа:')
print(Pos)


def binary_search(A, Val):
    N = len(A)
    ResultOk = False
    First = 0
    Last = N - 1

    while First <= Last:
        Middle = (First + Last) // 2
        if A[Middle] == Val:
            ResultOk = True
            Pos = Middle
            break
        elif A[Middle] > Val:
            Last = Middle - 1
        else:
            First = Middle + 1

    if ResultOk:
        print(f"Число {Val} найденo\nИндекс: {Pos}")
    else:
        print(f"Число {Val} не найдено")


Val = int(input("Введите число: "))
binary_search(Pos, Val)
