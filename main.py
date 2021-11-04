# def enter_num():
#     number = int(input('Enter number: '))
#     return number

#
# def func(number):
#     i = 0
#     while number != 1:
#         if number % 2 == 1:
#             number = 3 * number + 1
#         else:
#             number /= 2
#         i += 1
#         print(number, "->")
#     return number, i
#
#
# print(func(enter_num()))


def func(num, index):
    # if num == 1:
    #     return index
    while num != 1:
        if num % 2 == 1:
            num = 3 * num + 1
        elif num % 2 == 0:
            num = num / 2
        index += 1
        print(num)
    return index


for i in range(3, 1000000):
    a = func(i, 1)
    buf = 0
    if a > buf:
        buf = a

print(buf)





# print(func(837799, 1))
