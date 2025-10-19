# #과제15
# a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = map(int, input().split())
# b = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
# min = min(b)
# max = max(b)
# print(min, max)


# #과제16
# a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = map(int, input().split())
# b = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
# min = min(b)
# max = max(b)
# sum = 0

# for i in range(len(b)):
#     if b[i] == min or b[i] == max:
#         continue
#     sum += b[i]

# print(sum)


# #과제17
# a = [10, 20, 30, 40, 30, 20, 10]
# b = a.copy()
# for i in range(len(b)):
#     if b[i] == 20:
#         a.remove(20)
# print(a)


# #과제18
# a = list(i for i in range(1, 6))
# print(a)


# #과제19
# a = list(i for i in range(1, 21)if i % 2 == 1)
# print(a)


# #과제20
# a = int(input("첫번째값(1 ~ 20) : "))
# b = int(input("첫번째값(10 ~ 30) : "))
# c = []

# for i in range(a, b+1):
#     c.append(2 ** i)

# del c[1]
# del c[-2]

# print(c)


# #과제21
# a = input("Hello, world! 입력 : ")
# print(a.replace("Hello", "Hi"))


# #과제22
# a = input("첫번째 :")
# b = input("두번째 :")
# c = input("세번째 : ")
# d = input("네번째 : ")

# abcd = [a, b, c, d]
# abcd = " ".join(abcd)
# print(abcd)


# #과제23
# a = input("성을 영어로 입력 : ")
# a = a.lower()
# a = a.rjust(10)
# print(a)


#과제24
a = list(map(int, input().split(";")))
a.sort(reverse = True)

for i in a:
    print(str(i).rjust(9))

