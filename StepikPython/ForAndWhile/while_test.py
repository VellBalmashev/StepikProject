# This file test for Linux

# n = int(input())

# while n in range(10):
#     print(n)

# for i in range(n):
#     print(i)

# i = 0

# while i < 10:
#     print('Hello')
#     i += 1

# num = int(input())

# while num != -1:
#     print('The square of your number is:', num * num)
#     num = int(input())

# text = input()
# total = 0

# while text != 'stop':
#     total += int(text)
#     text = input()
# print('Sum of number is:', total)

# i = 5
# while i <= 11:
#     print('Python awesome!')
#     i += 1

# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2

# print(a)

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10

# print(product)

# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break
# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# n = 0
# while n < 10:
#     n += 2
#     if n == 8:
#         break
#     print(n)
# else:
#     print('Цикл завершен.')

# for i in range(4):
#     print(i, end='*')

for seconds in range(60):
    print(seconds)

    for minutes in range(60):
        for seconds in range(60):
            print(minutes, ':', seconds)