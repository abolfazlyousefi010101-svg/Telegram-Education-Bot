# -----------------------تعیین سطح----------------------------
# 1
# x = int(input("enter the number: "))
#
# if x % 3 == 0 and x % 5 == 0:
#     print("fizzbuzz")
# elif x % 3 == 0:
#     print("fizz")
# elif x % 5 == 0:
#     print("buzz")
# else:
#     print("wrong")
# from numpy.f2py.symbolic import number_types
from itertools import count

# ---------------------------------------------------
# 2
# نمونه کوچکتر
# y = [54]
# x = [23]
# if x < y:
#     print("as")
# else:
#     print("wrong")
# نمونه بزرکتر

# largest = [5,12,7,20,3,18,1]
# x = 0
# while True:
#     if x >= 0:
#         print("max:", x)
#     break
# x += 1
#
# ----------------------------------------------
# 4
# number = [5,12,7,20,3,18,1]
# largest = number[0]
# for i in number:
#     if i > largest:
#         largest = i
#         print(largest)
#------------------------------------------
# 5
# numbers = [5,12,7,20,3,18,1]
# largest = numbers[0]
# for i in numbers:
#     if i > largest:
#         largest = i
#print(largest)

# ----------------------------------------
# 3

# x = "hello"
# for i in reversed(x):
#     print(i, end="")
#     i = ""
#     if i == x:
#         print("True")
#     else:
#         print("false")
#     i += 1
# ----------------------------------------
# 4
# x = []
# for i in range(1,21):
#     x.append(i ** 2)
# print(x)
# روش دوم
# با استفاده از لیست کامپرهنشن
# abl = [i ** 2 for i in range(1,21)]
# print(abl)

#----------------------------------------------
# 5

# students = {"ali": 18, "sara": 20, "amir": 15}
# x = sum(students.values())
# print(x/3)
# ------------------**********************************************************---------------------------
# -----------------------***********************************************-----------------------
# -----------------------------**********************************------------------------------------------
# ----------------------------------**********************---------------------------------------
# ---------------------------------------**********----------------------------------------------
#----------------------شروع سوالات 1 تا 100-------------------------
# 1

# x = "abolfazl yousefi"
# count = 0
# for i in x:
#     count += 1
#     print(count, end=",")

# ----------------------------------------------
# 2

# x = [1,2,3,43,48,59,60,57,58,90,95,85,69]
# count = 0
# for i in x:
#     if i % 2 == 0:
#         count += 1
# print(count)
#------------------------------------------------------
# 3

# number_lest = [43,48,59,60,57,58,90,95,85,69]
# count = number_lest[0]
# for number in number_lest:
#     if number < count:
#         count = number
# print(count)
#----------------------------------------------------------
# 1

# name_f_l = "reza dolali 01"
# number = 0
# for name in name_f_l:
#     number += 1
#     print(number)
# ------------------------------------------
# 2

# number_z = [1,2,3,43,48,59,60,57,58,90,95,85,69]
# sh = 0
# for num in number_z:
#     if num % 2 == 0:
#         sh += 1
#         print(num,":",sh)
# print("*" * 50)
# print(sh)
# -----------------------------------------------------
# 4

# number_lest = [43,48,59,60,57,19,58,90,95,85,69]
# motghaer_s = number_lest[0]
# for num in number_lest:
#     if num < motghaer_s:
#         motghaer_s = num
# print(motghaer_s)
#
# number_lest = [43,48,59,60,57,19,58,90,95,85,69]
# motghaer_l = number_lest[0]
# for num in number_lest:
#     if num > motghaer_l:
#         motghaer_l = num
# print(motghaer_l)
# --------------------------------------------------------
# 5

# number_lest = [17,23,45,68,98,34,22,21]
# count = 0
# for num in number_lest:
#     if num % 2 != 0:
#         count += num
#         print(count)
# --------------------------------------------------
# 6
# name = "abas ahmade"
# count_m = 0
# for i in name:
#     if i == "a":
#         count_m += 1
# print(count_m,"\n",name)
# -------------------------------------------------
# 7
# name = "Abolfazl"
# new_name = ""
# for i in name:
#     new_name = i + new_name
# print(new_name)

# ---------------------------------------------------
# 8
# number_list = [23,21,49,78,56,60,69]
# largest = number_list[0]
# second = number_list[0]
# for number in number_list:
#     if number > largest:
#         second = largest
#         largest = number
#     elif number > second:
#         second = number
# print(second)
#-----------------------------------------------------
# 9
# numbers = [21,2,32,43,-9]
# for num in numbers:
#     if num > 0:
#         print("True")
#     else:
#         print("False")

# حالت دوم

# numbers = [21,2,32,43]
# all_positive = True
# for num in numbers:
#     if num <= 0:
#         all_positive = False
# print(all_positive)
#-------------------------------------------------------
# مرور تمرین9
# numbers = [98,54,21,2,32,43]
#
# for i in numbers:
#     if i > 0:
#         print("True")
#     else:
#         print("False")

# حالت دوم

# numbers = [-98,54,-21,-2,-32,-43]
# All_nigiteve = True
# for num in numbers:
#     if num >= 0:
#         All_nigiteve = False
# print(All_nigiteve)

#---------------------------------------------------
# 10
# mint = "hello my mother very very love how are you and my father"
# cou = 0
# for soup in mint:
#     if " " == soup:
#         cou += 1
# print(cou+1)

# --------------------------------------------------
# 11
# dish = {"abas":16, "fate":13, "ali":18, "ahmad":15, "negar":12}
# max_score = max(dish.values())
# for name,score in dish.items():
#     if score == max_score:
#         print(name, ":" ,score ,"\n" "(score more)")
#-------------------------------------------------------------
# 12
# کته قابل توجه اینه که ما چرا از دیکشنریها استفاده کردیم ؟ زیرا آن ها مانند مجموعه ها یک عبارت را دوبار نشان نمیدهند
# name = "abolfazl"
# dic = {}
# for n in name:
#     dic[n] = name.count(n)
# print(dic)

# ---------------------------------------شروع سطح 2 سوالات---------------------------
# 13
# عداد اعداد منفی یک لیست را حساب کنید
# list_number =[1,2,-4,54,0,-14,-23,-6,-9]
# counter = 0
# for num in list_number:
#     if num < 0:
#         counter += 1
#         print(counter,":",num)
# print(50 * "*")
# print(counter)
# -------------------------------------------------
# 14

# abl_list = [10,89,69,34,22,43,98]
# counter = abl_list[0]
# for num in abl_list:
#     if num > counter and num % 2 == 0:
#         counter = num
# print(counter)
# -------------------------------------------------
# 15
# sum_list = [10,80,30,90]
# x = 0
# for i in sum_list:
#     if i > 50:
#         x += i
# print(x)

# --------------------------------------------------
# 16
# text = "hello abolfazl my accopation polic and studense"
# word = text.split()
# large_word = text[0]
# for able in word:
#     if len(able) > len(large_word):
#         large_word = able
# print(large_word)



import requests

print(requests.get("https://api.telegram.org").status_code)




























