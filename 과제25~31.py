# #과제25
# a = list(map(str, input().split()))
# b = list(map(int, input().split()))
# x = dict(zip(a, b))
# print(x)

# #과제26
# park = {"korean" : 94, "english" : 91, "mathematics" : 89 , "science": 83}
# print(park.get("english"), park.get("science"))

# #과제27
# kim = {"korean" : 94, "english" : 91, "mathematics" : 89 , "science": 83}
# print(dict.fromkeys(kim, 100))

# #과제28
# lee = {"korean" : 94, "english" : 91, "mathematics" : 89 , "science": 83}
# if lee.get("english") != "None":
#     a = lee.pop("english")
#     print(a)

# #과제29
# lim = {"korean" : 94, "english" : 91, "mathematics" : 89 , "science": 83}
# print(lim.items())

# #과제30
# choi = {"korean" : 94, "english" : 91, "mathematics" : 89 , "science": 83}
# for i, j in  choi.items():
#     if j >= 90 :
#         print(i)

# #과제31
# sum = 0
# avg = 0
# yoo = {"korean" : 94, "english" : 91, "mathematics" : 89 , "science": 83}
# for i in yoo.values():
#     sum += i
# avg = sum/len(yoo)
# print("평균점수 : ", avg)