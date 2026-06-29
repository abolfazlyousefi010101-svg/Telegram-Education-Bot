# n = int(input("enter rows: "))
# while row <= n:
#     print("*" * row)
#     row += 1
#---------------------------------------------------------؟
# y = 3
# x = 7
# print(x)
# print(y)
# --------------------------------------------------
import copy
import numbers
import time
from enum import nonmember
# from collections.abc import list_iterator
from idlelib.debugger_r import start_debugger
from idlelib.outwin import file_line_pats
# from multiprocessing.pool import job_counter
from operator import truediv
from os import remove
from os.path import sep
from selectors import SelectSelector
from threading import main_thread
from tkinter.font import names
from turtledemo.penrose import start

# print(2 ,4 , 6 ,  end = "-00" , sep = "-")
# -------------------------------------------------
# x = 2
# y = 3
# print(x>1 and y<2)
# -------------------------------------------------
# x = [1,2,3,4]
# y = [1,2,3,4]
# print(id(x))
# print(id(y))
# print(x is not y)
# --------------------------------------------------
# x = 0b01
# print(x)
# -------------------------------------------------
# f = 2e+400
# print(f)
# -------------------------------------------------
# a = 123.1362323423
# print(round(a,3))
# -------------------------------------------------
# kg = int(input("enter kg:"))
# g = kg * 1000
# print(g, "g")
# -------------------------------------------------
# x = int(input("enter x:"))
# y = int(input("enter y:"))
# s = 1/2 * x * y
# print("s :",s)
#--------------------------------------------------
# x = int(input("enter temp:"))
# temp = x % 10
# print(temp)
# -------------------------------------------------
# x = int(input("enter:"))
# temp = x % 10
# print(temp)
# x = x // 10
# temp = x % 10
# print(temp)
# x = x // 10
# temp = x % 10
# print(temp)
# -----------------------------------------------------
# x = "a\nb\no\nl\nf\na\nz\nl\ny\no\nu\ns\ne\nf\ni "
# print(x)
# -----------------------------------------------------
# x = "abol\tfazl"
# print(x)
# ------------------------------------------------------
# x = "abolfazl"
# print(x[-2])
# ------------------------------------------------------
# x = "abolfazl yousefi"
# print(x[2:12])
#-------------------------------------------------------
# x = "abolfazl yousefi"
# print(x[2:12:2])
# -------------------------------------------------------
# x = "ip1iws@#$%"
# print(x[4:len(x)])
# --------------------------------------------------------
# s = "abolfazl"
# s = s.upper()
# print(s)
# print(s.lower())
# -------------------------------------------------------
# x = "abolfazl"
# x = x.count("l")
# print(x)
#--------------------------------------------------------
# x = "abolfazl"
# x = x.endswith("z")
# print(x)
#--------------------------------------------------------
# s = "abolfazl"
# print(s.find("z"), s)
#--------------------------------------------------------
# x = "abolfazl"
# print(x[2])
#--------------------------------------------------------
# s = "abolfazla youseafi"
# print(s.rfind("a "))
#---------------------------------------------------------
# x = "abolfazl"
# y = ("01")
# print(y.join(x))
#---------------------------------------------------------
# x = "abolfazl"
# y = ("12")
# print(y.join(x))
# -------------------------------------------------------
# x = "uhopijoioiuo808i9uo\rabolfazl\nyousef\tiw\b\t0\t1"
# print(x)
#----------------------------------------------------------
# print("abolfazl: %s%i" % ("abbas" , 84))
#----------------------------------------------------------
# x = str(input("enter x:"))
# y = int(input("enter y:"))
# z = ("ceo: %s%i" % (str(x), int(y)))
# print(z)
#-----------------------------------------------------------
# x = float(input("enter x:"))
# z = ("%2.f" % x)
# print(z)
# ----------------------------------------------------------
# x = float(input("enter x:"))
# z = ("%52.f" % x)
# print(z)
#-----------------------------------------------------------
# x = 3.45355334
# y = int(input("enter y:"))
# z = int(input("enter z:"))
# w = ("%0*.*f" % (y, z , x))
# print(w)
#------------------------------------------------------------
# x = 5
# y = 10
# z = ("x is {}\ny is {}\nz is {}\nc is {}".format(x, y ,20+5, 3+5))
# print(z)
#---------------------------------------------------------------------------
# x = 5
# y = 10
# z = ("x is \ny is \nz is \nc is ".format(x, y ,20+5, 3+5))
# print(z)
# ----------------------------------------------------------------
# x = 9
# y = 5.33544565
# d = ('%032.3f % (y)')میخوام این خط رو اعمال کنم ولی فعلا نمیدونم چیکار کنم
# z = {"x:9, y:8, z:10"}
# print("x is {}\ny is {}\nz is {}".format(x,y,z,d))
# ----------------------------------------------------------------------------------
# x = ("abolfazl")
# y = (x[0: 5: 2])
# print(y)
# -------------------------------------------------------------
# x = "abolfazl"
# print(x.find("a"))
#--------------------------------------------------------------
# print("x is {0:#b}".format(12345))
#--------------------------------------------------------------
# print("x is {0:<30}".format(25) , "*" ,sep="(-=")
#--------------------------------------------------------------
# x = ("x is {0:+^40}".format(12), '*' )
# print(x)
#--------------------------------------------------------------
# x = 2.345678
# x = 1.234
# y = 2.345567
# print("x is {}\ny is {}\nd is {}".format(x,y,5**3))
#--------------------------------------------------------------
# x = 6.67899
# y = 8.89
# print(F"x is {x}\ny is {y}")
# ---------------------------------------------------
# x = [1, 2, 3, "abolfazl yousefi"]
# print(type(x), "\n" ,len(x), "\n", type(x[0]), "\n", type(x[3]), sep="***" )
# -----------------------------------------------------------------------------
# x = [1 , 0 , "abolfazl"]
# x[2] = 20
# print(x)
#--------------------------
# x = [1,2,3,4,5,"qwaszx12"]
# x[5] = 6
# print(x)
#--------------------------------------
# e1 = 2
# a1 = e1
# print(id(e1))
# print(id(a1))
#---------------------------------
# x1 = [3,4,5,6]
# x2 = x1
# x3 = x2
# print(id(x1))
# print(id(x2))
# print(id(x3))
# x3[2] = 12
# print(x1)
# print(x2)
# print(x3)
# -------------------------------
# x1 = [1,2,3]
# x2 = x1.copy()
# یا
# x1 = [1,2,3]
# x2 = copy.copy(1)
# و
# x1 = [1,2,3]
# x2 = copy.deepcopy(x1)
#----------------------------------
# x = [1,2,345678345678,4,5]
# x.append(6)
# print(x)
# ---------------------------------
# abolfazl = [1,2,3,4,5]
# abolfazl[1:3] = ["a","b"]
# print(abolfazl)
#----------------------------------
# a , b , *c = [1 , 233 , 421 , 12345 , 244323]
# print(b)
# برسر هر متغیری که بخواهیم میتوانیم ستاره بگذاریم
# ------------------------------------------------
# x = ({"a":1 , "b":2})
# print(x["b"])
# ---------------------------------------------------
# x = {"a": 123,"b":122,"c":121}
# print(x["a"])
# x["a"] = 124
# print(x["a"])
# print(x)
# --------------------------------------------------
# x = {"a": 123,"b":122,"c":121}
# print(x["w"])
# --------------------------------------------------
# x = {"a": 123,"b":122,"c":121}
# print(x.get("w"))
# print(x.keys())
# print(x.values())
# print(x.items())
#----------------------------------------------------
# x = [123412,123232,47837648,67273983,67,12,34]
# x = sorted(x)
# print(x)
# --------------------------------------------------
# x = {1,2,3,4,"abolfazl"}
# x.remove(2)
# print(x)
#---------------------------------------------------
# x = input("enter name:")
# z = 'abolfazl yuosefi'
# print("z")z.split(-)
#---------------------------------------------------
# x = "a,b,o,l,f a z l".split(",")
# print(x)
#---------------------------------------------------
# x = input("enter a list:").split(",")
# print(60*"-")
# print(type(x))
# print(x)
# --------------------------------------------------
# if False:
#     print("abolfazl")
# print("end")
#---------------------------------------------------
# x = float(input("enter number:"))
# if x > 7 and x >= 18:
#     print("abolfazl level up")
#     print("abolfazl vere good")
# --------------------------------------------------
# namber = float(input("enter number:"))
# if namber >= 7:
#     print("Accepted")
# else:
#     print("Rrejected")
#--------------------------------------------------
# z = (1,2,3,4,5,-3)
# print(min(z))
# print(max(z))
# print(sum(z))
# ------------------------------------------------
# print(min("abolfazl","ali"))
# -------------------------------------------------
# print(sum((1,2,4,5),start=12))
#---------------------------------
# x = 0
# while x <= 12:
#     print("abolfazl")
# print("-"*80)
# --------------------------------
# z = 0
# while z < 10:
#     print("abolfazl")
#     z += 1
# print("aaaaaaaaa")
# --------------------------------
# m = int(input("enter:"))
# while m < 100:
#     if m % 2 == 0:
#         print(m)
#     m += 1
# ----------------------------------------
# m = int(input("enter:"))
# while m < 200:
#     if (m % 5 == 0) and (m % 3 == 0):
#         print(m)
#     m += 1
# -----------------------------------------
# x = float(input("enter:"))
# while x < 1000:
#     if x % 5 == 0:
#         print(x)
#     x += 2
#------------------------------------------
# حالت اول بینهایت بار تکرار میشود
# x = 1
# while x <= 5:
#     print("*")
# -----------------------------------------
# حالت دوم فقظ یکی به حاصل ما اضافه میشود که مشتقاتی هم دارد که مهم نیست
# x = 1
# while x <= 5:
#     print(x)
#     x += 1
# هم میتوانیم از حالت ستاره یا عدد و یا هر چیز دیگری استفاده کنیم برای پرینت کردن
# -------------------------------------------
# حالت سوم برای ستاره ای هایی هست که شکل مثلث باضلع نود درجه را میسازند که خود دو بخش دارد
# بخش 1 عددی
# x = 1
# while x <= 5:
#     print(x * 3)
#     x += 1
#بخش2 ستاره ای
# x = 1
# while x <= 5:
#   print("*" * 3)
#     x += 1
#------------------------------------------------------------
# حالت چهارم ساخت مثلث به صورت کامپیوتری
# x = 1
# while x <= 5:
#     y = ("*" * x)
#     print(y)
#     x += 1
# نکته : در پرینت باشد یا یک متغیر دیگر فرقی ندارد
# ---------------------------------------------
# حالا تعداد و اندازه مثلث را کار بر انتخاب میکند
# x = 1
# a = int(input("enter x:"))
# while x <= a:
#     print("*" * x)
#     x += 1
# ------------------------------------------------
# x = 1
# n = int(input("enter the number: "))
# while x <= n:
#     print(x * "*")
#     x += 1
# ------------------------------------------------
# برعکس
# x = int(input("enter number:"))
# while x >= 1:
#     print(x * "*")
#     x -= 1
#-------------------------------------------------
#  چون شمارنده ما x هست پس ما آن را در پرینت قرار میدهیم
# n = 12
# x = 1
# while x <= n:
#     if n % x ==0:
#         print(x)
#     x += 1
# =======================================================
# n = int(input("enter:"))
# x = 1
# while x <= n:
#     if n % x == 0:
#         print(x , end="," , sep="")
#     x += 1
# -------------------------------------------------------
# x = int(input("enter namber:"))
# y = 1
# z = []
# while y <= x:
#     if x % y == 0:
#         print(y)
#     y += 1
# ---------------------------------------------------------
# (((((((((((((((((((((((مهم و کاربردی))))))))))))))))))))))
# n = int(input("enter number:"))
# x = 1
# z = []
# while x <= n:
#     if n % x == 0:
#         z.append(x)
#     x += 1
# print(z)
# if sum(z)-n == n:
#     print("complete","sum all manber:",sum(z))
# else:
#     print("no","sum mumber:", sum(z))
# ---------------------------------------------------------
# x = int(input("enter:"))
# y = 1
# z = 0
# while y < x:
#     if x % y == 0:
#         z += y
#     y += 1
# if z == x:
#     print("complete")
# else:
#     print("not complete")
# -----------------------------------------------------
# قاعده فیبو نانچی
# x = 1
# a , b = 0 , 1
# while x <= 30:
#     print(a)
#     a , b = b , a+b
#     x += 1
#------------------------------------------------------
# x = int(input("enter:"))
# y = 1
# while y <= x:
#     print(y)
#     if y == 20:
#         break
#     y += 1
#-----------------------------------------------------
# x = float (input("x:"))
# m = x
# while True:
#     z = input("do you continue?:")
#     if z.lower() == ("no"):
#         break
# print(m , "end")
# ------------------------------------------------
# x = float (input("x:"))
# m = x
# while True:
#     z = input("do you continue?:")
#     if z.lower() == ("no"):
#         break
#     x = float(input("n:"))
#     if x < m:
#         m = x
# print(m , "end")
# -----------------------------------------------
# در این مثال خالت ماکسیمم را در نظر گزفتیم و x1 , x2 جدا کردیم و فقظ با تغییر یک علامت در خط455 حالت مینیمم به ماکسیمم عوض شد
# x1 =float(input("x:"))
# m = x1
# while True:
#     z = input("do you contenew:")
#     if z.lower() == ("no"):
#         break
#     x2 = float(input("x:"))
#     if x2 > x1:
#         m = x2
# print(m , "king")
#----------------------------------------------------------
# x = 0
# while x < 10:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x)
#     print("end")
#--------------------------------------------------------
# x = 0
# while x < 10 :
#     x += 1
#     if x % 2 == 0 :
#         continue
#     print(x)
# else:
#     print("ok")
# print("end")
# --------------------------------------------------------
# همراه با ویدیو
# n = int(input("n:"))
# x = 2
# if n > 1:
#     while x < n:
#         if n % x == 0:
#             print(n, "is not a prime number")
#             break
#         x += 1
#     else:
#         print(n , "is a prime number")
# else:
#     print(n , "is not prime number")
# -------------------------------------------------
# بدون ویدیو در این مثال 3 نوع عدد داریم اعداداول مرکب و اعداد واحد این مثال کامل تر و قشنگ تر از بالایی است
# a = int(input("n:"))
# n = 2
# if a > 1:
#     while n < a:
#         if a % n == 0:
#             print(n , "is not a prime number, it is composite number")
#             break
#         n += 1
#     else:
#         print(n , "is a prime number")
# else:
#     print(n , "is not a prim number, it is a single number")
# -----------------------------------------------------------------
# l = ["abolfazl","ali","abbas","mohamad","hossine" ]
# n = 0
# while n < len(l):
#     print(l[n])
#     n += 1
# ---------------------------------------------------------------
# مثالی درباره تورفتگی ها بسیار مهممممممممممممممممممممممممممممممممممممممممممممممم
# l = ["abolfazl","ali","abbas","mohamad","hossine" ]
# n = 0
# while n < len(l):
#     x = l[n]
#     z = 0
#     while z < len(x):
#         if z % 2 == 0:
#             print(x[z].upper(), end="")
#         else:
#             print(x[z], end="")
#         z += 1
#     print()
#     n += 1
#-------------------------------------------------------------------
# مرور
# x = input("name:").split("-")
# print(x)
# x1 = 0
# while x1 < len(x):
#     z = x[x1]
#     n = 0
#     while n < len(z):
#         if n % 2 == 0:
#             print(z[n].upper(), end="")
#         else:
#             print(z[n], end="")
#         n += 1
#     print()
#     x1 += 1
# else:
#     print("finesh")
#----------------------------------------------------------
# مثال جدول ضرب
# i = 1
# while i<= 10:
#     j = 1
#     while j <= 10:
#         print(i*j , end="\t")
#         j += 1
#     print()
#     i += 1
#------------------------------------------------------
# i = 1
# while i <= 10:
#     print(i * "*")
#     i += 1
#فکر کن نمیتونیم همچین کاری بکنیم
# i = 11
# while i <= 10:
#     j = 1
#     while j <= i:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1
#--------------------------------
# for
# l = [12,11,23,1234,87,885,69]
# for s in l:
#     print(chr(s))
#-----------------------------------
# l1 = [1,2,3,4,5,6,69,85,7,8]
# l2 = [1,2,85,69,9,87,67,45]
# for i in l1:
#     for j in l2:
#         if i == j:
#             print(i)
# یا
# l1 = [1,2,3,4,5,6,69,85,7,8]
# l2 = [1,2,85,69,9,87,67,45]
# for i in l1:
#     if i in l2:
#         print(i)
#------------------------------------
# l1 =[1,2,3,4,23,12,34,5,32]
# l2 = [1,2,3,4,5,98,76,98,687]
# for a in l1:
#     for b in l2:
#         if a == b:
#             print(a)
# ------------------------------------------------------
# for a , b , *c in [[1,2,3,0],[4,5,6,85],[7,8,9,69]]:
#     print(a , b , c)
# ------------------------------------------------------
# d = {"a":1, "b":2, "c":3}
# for k in d:
    # print(k ,":", d[k],",", end="\t")
#یا
# d = {"a":1, "b":2, "c":3}
# for k in d:
#     print(k ,":", d[k])
#
# یا
#
# d = {"a":1, "b":2, "c":3}
# for key , value in d.items():
#     print(key ,":",value)
# ------------------------------------------------
# مثالی که صفر در ان وجود ندارد و با رنج و فور و عملگر نات مساوی ساخته شده است
# x = list(range(11))
# for z in x:
#     if z != 0:
#         print(z)
# یا ی جور دیگه که راحت تره ولی توش صفر هم داره
# for a in range(10):
#     print(a)
#--------------------------------------------------------
# for a in range(1 , 18 , 3):
#     print(a)
#--------------------------------------------------------
# سه حالت جدید که کار بر وارد میکند
# 1
# x = input("name: ").split("-")
# print(x)
# for i in x:
#     print(i)
# 2
# x = input("names:").split("-")
# print(x)
# for i in range(0 , len(x)):
#     print(i)
# --------------------------------------
# x = input("names: ")
# print(x)
# for i in range(0 , len(x)):
#     print(i,x[i])
#----------------------------------------
# یک عدد از کاربر بگیریم و فکتور یل ان را پیدا کنیم
# اشتباه
# x = int(input("enter number n:"))
# for a in range(1 , x * x-1):
#     print(a)
#یا
# n = int(input("n:"))
# x = 1
# for i in range(x , n+1):
#     x *= i
# print("f:",x)
#--------------------------------------------------
# n = input("number:").split("-")
# for i in range(len(n)-1, -1 ,-1):
#         print(n[i],end=",")
# ------------------------------------------------
# n = input("n:")
# x = ""
# for i in range(len(n)-1, -1 , -1):
#     x += n[i]
# z = int(x)
# print(type(z))
# print(x)
#-------------------------------------------------
# مرور ستاره هرمی با وایل
# x = int(input("enter number star:"))
# y = 1
# while y <= x:
#     print(y * "*")
#     y += 1
#--------------------------------------------------
# ستاره هرمی با فور و بر عکس هن مهم و زیبا
# n = int(input("n:"))
# for i in range(1 , n+1):
#     for j in range(1 , i+1):
#         print(j, end="")
#     print()
# for i in range(n-1 , 0 ,-1):
#     for j in range(1 , i+1):
#         print(j , end="")
#     print()
# ---------------------------------------------------
# مرور جدول ضرب
# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i * j , end="\t")
#         j += 1
#     print()
#     i += 1
# ----------------------------------------------------
# l = ['a','b','c','d']
# for i in (l):
#     print(i)
# یا
# l = ['a','b','c','d']
# for i in range(0 , len(l)):
#     print(i, ":" , l[i])
#یا
# l = input("l:").split(",")
# print(l)
# for i in range(0 , len(l)):
#     print(i, ":" , l[i])
#----------------------------------------------------
# تابع enumerate
# l = ['a','b','c','d']
# for i , j in enumerate(l):
#     print(i,":",j , end="\t")
#---------------------------------------------------
# x = ["abolfazl","sara","zahra","ahmad"]
# for z , y in enumerate(x):
    # print(z, ":" , y)
# --------------------------------------------------
# x = ["abolfazl","sara","zahra","ahmad"]
# y = [12,32,21,20]
# for i in range(0 , len(x)):
#         print("name:",x[i] ,"-", "age:",y[i])
# -----------------------------------------------------یاااااااااااااااااااااااااااااااااااااااااااااااااااا
# x = ["abolfazl","sara","zahra","ahmad"]
# y = [12, 32, 21, 20]
# for i , j in zip(x , y):
#     print("name:", i , "-" , "age:", j)
# -----------------------------------------------------------
# x = ["abolfazl", "sara", "zahra","ahmad"]
# y = [12, 32, 21, 20]
# for i in reversed(range(10)):
#     print(i+1)
# -------------------------------------------------------
# x = ["abolfazl", "sara", "zahra","mohamad"]
# y = [12, 32, 21, 20]
# for i in sorted(x):
#     print(i)
# --------------------------------------------------
# x = ["abolfazl", "sara", "zahra","mohamad"]
# y = [12, 32, 21, 20]
# for i in reversed(sorted(x)):
#     print(i)
# ------------------------------------------------------
# from random import random
# print(random())
# -----------------------------------------------------
# min + (random * (max - min))
#فرمول برای اینکه در یک بازه اعداد رندم چاپ شود مثلا بازه 5 تا 10
# from random import random , seed
# for _ in range(5):
#     print(int(5 + (random() * (10 - 5))))
#----------------------------------------------------------
# ترفند جدید
# from random import random , uniform
# for _ in range(10):
#     print(uniform(10 , 25))
# ----------------------------------------------------
# from random import random , uniform
# for _ in range(150):
#     if int(uniform(10, 100)) == 98:
#         print("abolfazl")
# یااااااااااااااااااااااااااااااااااااااااااااااا
# from random import random , randint , seed
# seed(9)
# for _ in range(10):
#     if randint(10, 100) == 98:
#         print("abolfazl")
#     else:
#         print("9")
# -----------------------------------------------
#-----------------------------------------------------
# مرور
# p = [98, 99 , 100]
# for i in p:
#     print(p)
# -----------------------------------------------
# در این دستور دیکه نیازی به نوشتن ایتیجر هم نیست
# from random import random , randint
# for _ in range(15):
#     print(randint(80 , 800))
# ------------------------------------------
# from random import randrange
# for _ in range(10):
#     print(randrange(14,22,2))
#---------------------------------------------
# from random import choice
# x = ["a","b","c""d""e","f","g"]
# for _ in range(10):
#     print(choice(x))
#---------------------------------------------
# from random import sample
# x = ["a","b","c""d""e","f","g","p"]
# for _ in range(10):
#     print(sample(x , 3))
# -----------------------------------------
# from random import shuffle
# x = ["a","b","c""d""e","f","g","p"]
# for _ in range(10):
#     shuffle(x)
#     print(x)
#------------------------------------------
# x = ['a' , 'b' , 'c' , 'd']
# y = [1,2,3,4]
# for i , j in range(x , y):
#         print(i,":",j)
#--------------------------------------------------
# x = ["abolfazl", "sara", "zahra","mohamad"]
# y = [12, 32, 21, 20]
# for i in reversed(sorted(x)):
#     print(i)
#--------------------------------------------------
# from random import random
# for _ in range(10):
#     print(random())
# -------------------------------------------------
# from random import randint
# for _ in range(100):
#     if randint(5 , 50) == 12:
#         print("abolfazl")
# ------------------------------------------------
# from random import randi
# for _ in range(100):
#     print(randint(13,110))
# -----------------------------------------
# from random import randrange
# for _ in range(100):
#     if randrange(0 , 100 , 5) == 55:
#         print("hello")
#     else:
#         print("goodbye")
# ------------------------------------
# from random import choice
# x = ['l','k','j','h','m','n']
# for _ in range(200):
#     print(choice(x), end=",")
# ---------------------------------
# from random import sample
# x = ['l','k','j','h','m','n']
# for _ in range(10):
#     print(sample(x , 2))
# ----------------------------------
# from random import shuffle
# x = ['l','k','j','h','m','n']
# for _ in range(10):
#     shuffle(x)
#     print(x)
# ------------------------------------
# میخواهیم شیر یاخط بازی کنیم
# from random import choice
# x = ["sher" , "khat"]
# sh = 0
# kh = 0
# for _ in range(100):
#     y = choice(x)
#     if y == "sher":
#         sh += 1
#     else:
#         kh += 1
# print("sher:",sh)
# print("khat:",kh)
#یاااااااااااااااااااااااااااااااااااااااااااااااااااااااااا
# یک تاس داریم و میخواهیم ببینیم هر یک از وجه های ان چند بار می اید

# from random import randint
# tas = {1:0,2:0,3:0,4:0,5:0,6:0}
# for _ in range(10000):
#     tas[randint(1,6)] += 1
# print(tas)
#------------------------------------------------------
# x = ['a','b','c','d']
# for i in reversed(x):
#     print(i)
#------------------------------------------
# from random import randint
# for _ in range(100):
#     print(randint(0 , 21))
#choice - sample - shuffle
# ----------------------------------------
# مروررررررررررررررررررررررررررررررررررررر
# from random import choice
# x = ["sher","khat"]
# sh = 0
# kh = 0
# for _ in range(1000):
#     z = choice(x)
#     if z == "sher":
#         sh += 1
#     else:
#         kh += 1
# print("sher:", sh)
# print("khat:", kh)
# ----------------------------------------------
# مرور
# from random import randint
# tas = {1:0,2:0,3:0,4:0,5:0,6:0}
# for _ in range(100):
#     tas[randint(1,6)] += 1
# print(tas)
# --------------------------------------------------
from random import randint, choice

# x = list(input("enter two number:").strip(","))
# for i in (x, 2):

# -------------------------------------------
#11111111111111 دوعدد کاربر وارد کرده که مابین انهاچاپ میشود
# x = int(input("enter number:"))
# y = int(input("enter number:"))
# for i in range(x+1 , y):
#     print(i)
# 33333333333333333333333333---------------------------------
# x = int(input("enter number:"))
# y = int(input("enter number:"))
# max1 = max(x , y)
# min1 = min(x , y)
# for i in range(1,x+1):
#      if x % i == 0 and y % i == 0 and x % i == 0 and y % i == 0:
#         print(i, end=" ")
#---111111111111111111111111111-------------------
# x = int(input("x:"))
# y = int(input("y:"))
# max1 = max(x , y)
# min1 = min(x , y)
# while min1 <= max1:
#     print(min1)
#     min1 += 1
# یاااااااااااااااااااااااااااااااااا
# x = int(input("x:"))
# y = int(input("y:"))
# max1 = max(x , y)
# min1 = min(x , y)
# for i in range(min1, max1+1):
#     print(i)
# ---------3333333333333333333333333
# x = int(input("x:"))
# y = int(input("y:"))
# z = min(x,y)
# v = 1
# for i in range(y , 0 , -1):
#     if x % i == 0 and y % i == 0:
#         print(i)
#         break
#--44444444444444444444444444444444
# x = int(input("x:"))
# y = int(input("y:"))
# min1 = min(x,y)
# max1 = max(x,y)
# for i in range(1, min1+1):
#     if max1 * i % min1 == 0:
#         print(max1 * i)
#         break
#-----555555555555555555555555555555
# x = int(input("x:"))
# y = 1
# while x >= y:
#     print(y)
#      y += 1
# and
# x = int(input("x:"))
# y = 0
# while x > 0:
#     x //= 10
#     y += 1
# print(y)
#66666666666666126666666666666666666666666666
# x = int(input("x:"))
# y = int(input("y:"))
# min1 = min(x , y)
# z = 1
# while z < min1:
#     if min1 * z % min1 == 0:
#         print(min1 * z)
#         z += 1
#---------------------
# مرور
# x = int( input("x:"))
# y = -1
# while :
#     print(y * "*")
#     y -= 1
# and
# x = int(input("x:"))
# y = int(input("y:"))
# min1 = min(x,y)
# max1 = max(x,y)
# for i in range(1 , min1+1):
#     if max1 * i % min1 == 0:
#         print(max1 * i)
#         break
# ----------------------------------------------
# x = int(input("x:"))
# y = 1
# while x > y:
#     x//=10
#     y += 1
# print(y)
# 6666666666666666666666666666666666666666666666
# x = int(input("x:"))
# for i in range(1 , x+1):
#     print(" " * (x - i), end="" )
#     print("*" * i)
# ORRRRRRRRRRRRRRRRRRRRRRRRR
# x = int(input("x:"))
# for i in range(1, x+1):
#     for j in range(0, x-i):
#         print(" " ,end="")
#     for z in range(0, i):
#         print("*", end="")
#     print()
#777777777777777777777777777
# from random import sample
# x = ["a","b","c"]
# for i in sample(x):
#     if i is "a":
#         y = int(input("yes or no:"))
#         if y is "no":
#             if i is "b":
#                 z = int(input("yes or no:"))
#                 if z is "yes":
#                     print("trou")
#                 else:
#                     print("finish")
#----------------------7777777------------------------
# تمرین بسیااااار زیبا
# from random import choice
# names = ["a","b","c","d","e","f","g","h","i","j"]
# names_cp = names.copy()
# while True:
#     if len(names_cp) == 0:
#         break
#     cmp_choice = choice(names_cp)
#     ans = input(f"is your choice: {cmp_choice} ? (y/n): ")
#     if "y" in ans.lower():
#         print("you win!")
#         break
#     names_cp.remove(cmp_choice)
# ------------------------------------------------------
# from random import choice
# x = ["a","b","c","d","e","f","g","h","i","j","k"]
# cp_copy = x.copy()
# while True:
#     if len(x) == 0:
#         break
#     v = choice(cp_choice)
#     z = input(f"is your choice: {cp_choice} ? (y/n):")
#     if "y" in z.lower():
#         print("you win")
#         break
#     cp_choice.remove(v)
#-------------------------------------------------------------






#------------------------------------------------------------
# ولین مینی پرو پایتون رمز نگاری کردن نوشته ها و رمز کشایی کردن ان ها
# while True:
#     print("choose your option:\n\t1)encrypt\n\t2)decrypt\n\t3)exit")
#     choice = input("your choice: ")
#     if choice == "1":
#         plain_text = input("text: ")
#         encrypted_text = ""
#         for c in plain_text:
#             x = ord(c) * 2 + 5
#             encrypted_text += chr(x)
#         print("encrypted_text: ", encrypted_text)
#         print("*" * 40 + "\n")
#     elif choice == "2":
#         encrypted_text = input("encrypted text: ")
#         plain_text = ""
#         for c in encrypted_text:
#             x = (ord(c) - 5) // 2
#             plain_text += chr(x)
#         print("plain text: ", plain_text)
#         print("*" * 40 + "\n")
#     elif choice == "3":
#         print("Goodbye")
#         print("*" * 40 + "\n")
#         break
#     else:
#         print("your choice is wrong!")
#         print("*" * 40 + "\n")
# -----------------------------------------------------------------
# x = 99
# y = int(input("enter text:"))
# for i in range(y):
#
#     print(chr((y-2)//3))
# ----------------------------------
# دومین مینی پروزه از فصل 5 ساخت رمز های عبور قوی برای ایمنی کار بران مثلا در اینستا که خودسیستم این کار را انجام میدهد
# import random
# import string
# lower = string.ascii_lowercase
# upper = string.ascii_uppercase
# symbol = "!@#$%^&*()_+=[]{};><,?/|"
# numbers = "0123456789"
# all = lower + upper + symbols + numbers
#
# while True:
#     print("choose an option:\n\t1)create a password:\n\t2)Exit:")
#     choice = input("your choice:")
#     if choice == "1":
#         length = int(input("Enter the length of the password: "))
#         password = "".join(random.sample(all, length))
#         print(password)
#         print("\n")
#     elif choice == "2":
#         print("tankth of choose")
#         print("goodbye")
#         break
#     else:
#         print("your choice wrong!\n")
# ---------------------------------------------------------------------------
# سومین مینی پروزه ساخت تایمر ساعت
#نمونه اولیه
# import time
# while True:
#     for i in range(10):
#         print(i)
#         time.sleep(1)
#نمونه کامل تر
# import time
# while True:
#     print("choose an option => \n\t1)start time:\n\t2)Exet:")
#     choice = input("enter on number :")
#     if choice == "1":
#         for i in range(10):
#             print(i)
#             time.sleep(1)
#     elif choice == "2":
#         print("good bye")
#         break
#     else:
#         print("please again try,option is wrong")
# ------------------------------------------------------------------------
# نمونه خیلی کامل تر
# import time

# while True:
#     choice = input("do you want start ? (y/n): ")
#     if "y" in choice.lower():
#         hour = int(input("Enter amount of hour:"))
#         minutes = int(input("Enter amount of minutes:"))
#         seconds = int(input("Enter amount of seconds:"))
#         total = hour * 60 * 60 + minutes * 60 + seconds
#         print("timer start now...")
#         time.sleep(1)
#         while total >= 1:
#             print(total)
#             total -= 1
#             time.sleep(1)
#         print("timer ender...")
#     elif "n" in choice.lower():
#         print("exiting")
#         break
#     else:
#         print("invalid input...")
#---------------------------------------------------------------
# مرور سه پروژه
# -------------------------------11111111111111111111------------------------------
# while True:
#     print("options: \n\t1)encrypt\n\t2)decrypt\n\t3)Exit")
#     choose_text = input("choose an option: ")
#     if choose_text == "1":
#         plain_text = input("plain text: ")
#         encrypted_text = ""
#         for c in plain_text:
#             x = ord(c) * 12 - 5
#             encrypted_text += chr(x)
#         print("encrypted text: ", encrypted_text)
#         print("*" * 40 + "\n")
#     elif choose_text == "2":
#         encrypted_text = input("encrypted text :")
#         plain_text = ""
#         for c in encrypted_text:
#             x = (ord(c) + 5) // 12
#             plain_text += chr(x)
#         print("plain text: " , plain_text)
#         print("*" * 40 + "\n")
#     elif choose_text == "3":
#         print("welcome app me")
#         break
#     else:
#         print("your choice is wrong!")
#         print("*" * 40 + "\n")
#-----------------------------111111111111111111111دوباره-----------------------------
# while True:
#     print("your option: \n\t1)encrypt\n\t2)decrypt\n\t3)Exit")
#     choose_option = int(input("choose your option: "))
#     if choose_option == "1":
#         plain_text = input("enter your text: ")
#         enumerated_text = ""
#         for c in plain_text:
#             x = ord(c) * 5 + 11
#             enumerated_text += chr(x)
#         print("encrypted text: ", enumerated_text)
#         print("*" * 40 + "\n")
#     # elif choose_option == "2":
#         # pass
# 2222222222222222222
import random
from types import new_class

from unicodedata import digit


# import string
# lower = string.ascii_lowercase
# upper = string.ascii_uppercase
# symbol = "!@#$%^&*()_+=-{}[]|:;<>?.,/"
# numbers = "0123456789"
# all = lower + upper + symbol + numbers

# while True:
#     print("option: \n\t1)create a password\n\t2)Exit")
#     choose = input("enter an option: ")
#     if choose == "1":
#         length = int(input("enter a length: "))
#         password = "".join(random.sample(all, length))
#         print(password)
#         print("\n")
#         print("thank you create" + "\n")
#     elif choose == "2":
#         print("now exit...")
#         print("goodbye")
#         break
#     else:
#         print("your choose wrong!")
# 3333333333333333333333333333333333---------------------------------

# ----------------------------فصل 6 توابع------------------------------
# def f(x):
#     return 2 * x + 1
# x = int(input(("enter namper: ")))
# print(f(x))
# یتوانستیم هم انتخاب عدد را به کاربر هم ندهیم
# ---------------------------------------------------------------------
# def f():
#     x = int(input(("enter namper: ")))
#     print(x ** 3)
# f()
# f()
# f()
# f()
#--------------------------------------------------------------
# def f():
#     x = int(input(("enter namper: ")))
#     print("ok")
#     return x ** 3
#     print("sdf")
#     print("wqe")
#     print("wqq")
# n = f()
# print(n)
#-------------------------------------------------------------------
# def f(x , y , z):
#     return 2 * x + 1
# x = int(input(("enter namper: ")))
# n = f(10 , 12 , 14)
# print(n)
# -----------------------------------------------------------
# ثال برای توابع در اینجا میخواهیم ببینیم چند تاعدد مثلا3 در رقم 1234567342وجود دارد
# ریاضی طوری

# def repeat(number , digit):
#     count = 0
#     while number > 0:
#         if number % 10 == digit:
#             count += 1
#         number = number // 10
#     return count
#
# number = int(input("number: "))
# digit = int(input("digit: "))
# print(digit , "repeat" , repeat(number,digit), "times" )
# اااااااااااااااااااااااااااااااااااااااااااااااااااااااااااایا
# عامیانه
# def repeat(number , digit):
#     return str(number).count(str(digit))
#
# number = int(input("number: "))
# digit = int(input("digit: "))
# print(digit , "repeat" , repeat(number,digit), "times" )
#------------------------------------------------------------------------------
# فاکتور یللللللللللللللللللللل
# def fact(n):
#     f = 1
#     for i in range(1 , n+1):
#         f *= i
#     return f
# n = int(input("number: "))
# print(fact(n))
# ---------------------------------------------------------------------
# مجموع فاکتور یل چند عدد
# 1! + 2! + 3! + 4! + 5! = 153
# def fact(n):
#     f = 1
#     for i in range(1 , n+1):
#         f *= i
#     return f


# def s_fact(n):
#     s = 0
#     for i in range(1 , n+1):
#         s += fact(i)
#     return s


# number = int(input("Enter a number: "))
# print("s: " , s_fact(number))
# ------------------------------------------------------------------
# مرور
# def repeat(number , gust_number):
#     x = 0
#     while number > 0:
#         if number % 10 == gust_number:
#             x += 1
#         number = number // 10
#     return x
# number = int(input("enter a number: "))
# gust_number = int(input("enter a gust_number: "))
# print(gust_number , "repeat" , repeat(number , gust_number) , "times")
# ---------------
# def fact(n):
#     f = 1
#     for i in range(1 , n+1):
#         f *= i
#     return f


# def s_fact(n):
#     s = 0
#     for i in range(1 , n + 1):
#         s += fact(i)
#     return s

# number = int(input("enter a number: "))
# print("s: " , s_fact(number))
#---------------------------------ادامه-------------------------------
#  از کاربر 3 عدد میگیریم و بزرگ ترین آن ها را انتخواب میکنیم سه روش مختلف مینویسیم
# while True:
#     def max01(a , b , c):
#         return max(a , b , c)
#
#     x = int(input("enter x:"))
#     y = int(input("enter y:"))
#     z = int(input("enter z:"))
#     print("max: ", max01(x,y,z))
# 2
# def max01(a , b , c):
#     return max(a , b , c)

# x = int(input("enter x:"))
# y = int(input("enter y:"))
# z = int(input("enter z:"))
# print("max: ", max01(x,y,z))
# 3ورودینداشته باشد که خود تابع ورودی را میدهد


# def max01():
#     x = int(input("enter x:"))
#     y = int(input("enter y:"))
#     z = int(input("enter z:"))
#     return max(x , y , z)
#
# print("max: ", max01())
#4 ریترن هم نداشته باشد و خود تابع ورودی بگیر و پرینت کند در این روش دیگر تابع جایی در حافظه ستگاه ذخیره نمیشود بلکه فقط اجرا شده و به کار بر نشان داده میشود

# def max01():
#     x = int(input("enter x:"))
#     y = int(input("enter y:"))
#     z = int(input("enter z:"))
#     print("max: " , max(x , y , z))
#
# max01()
# -------------------------------------------------------------------------------------------------
# ویدیوی چهارم از فصل ششم
# 5سینکتکس برای آرگمان ها
# 1)normal
# 2)name = value
# 3)normal + name = value
# 4)*iterable(list,tuple,str,sep,set)
# 5)**dict
# {{{{{{{{{{{{{{{{{{{{{موضوع در باره نوشتن سینتکس های آرگمان ها است}}}}}}}}}}}}}}}}}}
# *iterable=====>>>>> (list , tuple , str , sep , set ,...)
# def bel(a , b , c):
#     print("a:" , a)
#     print("b:" , b)
#     print("c:" , c)
# x = [1,2,3]
# bel(*x)
# ---------سینتکس بعدی برای دیکشنری هست

# def bel(a , b , c):
#     print("a:" , a)
#     print("b:" , b)
#     print("c:" , c)
# d = {"a": 1,"b": 2,"c": 3}
# bel(**d)
#-------------------------------------------------------------
# {{{{{{{{{{{{{{{{{{{{{{{{{سینتکس هایی برای پارامتر ها}}}}}}}}}}}}}}}}}}}}}}
# ویدیوی پنحم از فصل ششم
# 1)normal
# 2)default value
# 3)normal + default value
# 4)* name
# 5)**name به صورت دیکشنری نوشته میشوذ
# مثال برای گزینه 4
# def bel(a , b , *c ,d):
#     print("a:", a)
#     print("b:", b)
#     print("c:", c)
#     print("d:", d)
# bel(1,2,34,2,3,5,d=3)
# ----------------------------------
# مثال برای گزینه 5
# def bel(**a):
#     print("a:", a)
# bel(a=1,b=2,c=3,d=4)
# -----------------------------------
# حالا تمام سینتکس های پارامتر را با هم قاطی میکنیم
# def bel(a, b=0, *c, **d):
#     print("a:", a)
#     print("b:", b)
#     print("c:", c)
#     print("d:", d)
# bel(1,2,3,0,4,5,6, c=9,d=10,e=9)
# -------------------------------------------
# نشان گر هاااااااااااااااااا
# هرگاه از استاره استفاده کنیم پارامتر های بعد از ستاره حتما باید بهصورت ناممقدار نوشته شود
# مثال
# def bel(a , * ,b , c):
#     print("a:", a)
#     print("b:", b)
#     print("c:", c)
#
# bel(1, b=2, c=3)
#------------------------------------
# برعکس مثال قبل اسلش ها هر جا که باشن قبل آن ها هیچ نامی مثل aیاbیاc... نباید ذکر شود فقط وفقط مقدارخالی بعد اسلش ها مورد قبول است

# def bel(a  ,b , /, c):
#     print("a:", a)
#     print("b:", b)
#     print("c:", c)
#
# bel(1, 2, c=3)
# -----------------------------------------
# ترکیبی

# def bel(a  ,b , /, c, d, *,e, f):
#     print("a:", a)
#     print("b:", b)
#     print("c:", c)
#     print("d:", d)
#     print("e:", e)
#     print("f:", f)

# bel(1, 2, 3, d=4, e=5, f=6)
#-------------------------------------------
# داک استرینگ ها که عملکرد یکتابع را به دیگران نشان میدهد(کسانی که برنامه های ما را میخوانند) توضیح میدهد تابعی که ما نوشتیم چیکار میکنه
# def max01(x , y , z):
#     """Receives three numbers as input and returns the largest of them."""
#     return max(x,y,z)
# print(max01.__doc__)
# یااااااااااااااااااااااااااا
# print(help(max01))
# print(print.__doc__)
#-----------------------------------------------------------
# def bel(x: int, y: int = 9, **z: dict) -> tuple:
#     print(x)
#     print(y)
#     print(z)
#
# print(bel(1))
# print(bel.__annotations__)
#--------------------------------------------------------------
# ---------------------------------------ferst class-----------------------------------------
# def mysort(s):
#
#     def ascending(x):
#         print(sorted(x, reverse=True))
#
#     def descending(y):
#         print(sorted(y))
#
#     def error(z):
#         print("error!", z)
#
#     if s == "a":
#         return ascending
#     elif s == "b":
#         return descending
#     else:
#         return error

# action = input("action: ")
# bel = mysort(action)
# bel([5,4,6,7,2,1,3,9,8,5,6,3,0,9])
# --------------------------------------------------------------------
#
#
#  skop فضای نام یا همان num spas و حوضه یا همان اسکوپ
# فضای نام با دیکشنری مشخص میشود
# ا مثلا ممکن است در یک پروژه 1000تا فضای نام داشته باشیم یعنی مثلا ممکن است در یک پروژه1000تا مینی پروژ با شد که بهم مرتبط هستند
# حالا قانون حوضه میگوید اسمی که صدا زده شده برای اجرای کد همیشه نزدیک ترین اسم انتخاب میشود
# فضاهای نام:local < enclosed < global < built-in

# print(globals())
# -------------------------------------------------------------------

# x = 0
# def A():
#     x = 2
#
#     def B():
#         x = 3
#
#         def C():
#             x = 4
#             print(x)
#         C()
#     B()
# A()
#----------------------------------------------------------

# x = 7
# def A():
#     x = 2
#
#     def B():
#         x = 3
#
#         def C():
#             global x
#             x += 10
#             print(x)
#         C()
#     B()
# A()
# ---------------------------------------------------------

# x = 2
# def A():
#     x = 2
#
#     def B():
#         nonlocal x
#         x += 3
#         print(x)
#
#         def C():
#             x = 10
#         C()
#     B()
# A()
# --------------------------------------------------------------

# x = 2
# def A():
#     x = 2
#
#     def B():
#         x = 3
#
#         def C():
#             nonlocal x
#             x += 10
#             print(x)
#         C()
#     B()
# A()
#------------------------------------------------------
# ارسال با مقدار و ارسال با ارجاع
# برای لیست ها
# def bel(a):
#     a += [1, 2, 3]
#     a[0] = 0
#     print(a)
# a = [4,5,6]
# bel(a)
# print(a)
# -------------------------------------------------
# جور دیگر برای دیکشنری ها
# def bel(a):
#     a["c"] = 12
#     print(a)
# a = {"a":1, "b":6}
# bel(a)
# print(a)
# ---------------------------------------
#    جور دیگه برای مجموعه ها با استفاده از اتحاد
# def bel(a):
#     a |= {0,7,8,9}
#     print(a)
# a = {1,2,3,4,5,6}
# bel(a)
# print(a)
# -----------------------------------------
# برای جلو گیری از این رفتار 3 راه داریم 1:[:]aو 2:کپی سطحی و3: کپی عمیق
# 1

# def bel(a):
#     a += [1, 2, 3]
#     print(a)
# a = [4,5,6]
# bel(a[:])
# print(a)

# 2

# def bel(a):
#     a += [1, 2, 3]
#     print(a)
# a = [4,5,6]
# bel(a.copy())
# print(a)

# 3
# import copy
# def bel(a):
#     a[0][3] = 0
#     print(a)
# a = [[1,2,3,7,8,9],4,5,6]
# bel(copy.deepcopy(a))
# print(a)

# --------------------------------------------
# حالا اگر برعکسش 3 حالت بالا داشته باشیم و مقدار های ما تعییر نا پذیر باشند از روش زیر استفاده میکنیم
# def bel(a):
#     a += 2
#     print(a)
#     return a
#
# a = 3
# a = bel(a)
# print(a)
# -------------------------------------------مرور--------------------------------
# def bel(a):
#     a += [1,2,3,4,5,6]
#     a[0] = 10,12
#     a[9] = 7
#     print(a)
# a = [7,8,9,11]
# bel(a)
# print(a)
#----------------------
# import copy
# def bel(a):
#     a[1][2][3] = 1
#     print(a)
# a = [0,[2,45,[45,77,98,90,97],67,87,69],3,8,9]
# bel(copy.deepcopy(a))
# print(a)
# ---------------------
# a = 1,2,3,4,5
# print(len(a))
# print(a)
# ---------------------
# def bel(a):
#     return a
# a = [1,2,3,4,5]
# bel(a)
# print(a)
#-----------------------------
# x = 0
# def bel(a,b,c,d,e):
#     a += 1
#     bel(1,2,3,4,5)
#     return a
#--------------------------------------
# ________________________اولین سری تمرینات فصل 6______________________________
# تمرین 1

# def len2(a):
#     count = 0
#     for _ in a:
#         count += 1
#     return count

# s = "abolfazl yousefi"
# l = [1,2,3,4,5,6,7]
# t = ("1", "2", "3", "4")
#
# print(len2(s))
# print(len2(l))
# print(len2(t))
# ----------------------------1----------------------------
# def bel(a):
#     x = 0
#     for _ in a:
#         x += 1
#     return x
#
# s = "abolfazl"
# t = (1,2,3,4,5,6)
# l = [1,2,3,4]
#
# print(bel(s))
# print(bel(t))
# print(bel(l))
# --------------------مرور تمرین 1--------------------
# def bel(f):
#     countre = 0
#     for _ in f:
#         countre += 1
#     return countre
#
# s = "aboss nemate"
# print(bel(s))
#مرور مجدد بار سوم تمرین ------------------------1---------------------------------
# def bel(a):
#     s = 0
#     for _ in a:
#         s += 1
#     return s
# x = [12,34,23,53]
# print(bel(x))
# ----------------تمرین دوم2-----------------------------------
# def max2(*a):
#     cont = a[0]
#     for i in a:
#         if i > cont:
#             cont = i
#     return cont

# print(max2(1,2,3,4,65,69,8,55,0,-1))
#یا میتوان
# اینف به معنای بینهایت است و میتوان از ان برای پیدا کردن ماکسیمم استفاده کرد
# def max2(*a):
#     cont = float("-inf")
#     for i in a:
#         if i > cont:
#             cont = i
#     return cont
#
# print(max2(1,2,3,4,65,69,8,55,0,-1))
# -----------------------2--------------------------------------------
# def max2(*a):
#     x = 0
#     for i in a:
#         if i > x:
#             x = i
#     return x
#
# f = max2(1,2,32,43,54,35,234,64,432)
# print(f)
# ---------------------------مرور تمرین 2 و طرح جدید ------------------------------
# def bel(*a):
#     number = 0
#     for x in a:
#         if x > number:
#             number = x
#     return number
#
# print(bel(1,2,3,4,65,69,8,55,0,-1))
# مرور مجدد تمرین 2
# def min2(*a):
#     number = 0
#     for i in a:
#         if number < i:
#             number -= 1
#     return number
#
# print(min2(1,2,3,0,-1,-2,-3,-69))

# ------------------------------------- تمرین 3--------------------------------
# def sum2(a):
#     x = 0
#     for i in a:
#         x += i
#     return x
#
# print(sum((1,2,3,4)))
# -------------------3-----------------------------
# def sum2(a):
#     x = 0
#     for i in a:
#         x += i
#     return x
# f = (1,2,3,8,90)
# print(sum2(f))
#----------------------------4444444444444444----------------------------------
# def bel(n):
#     for i in range(1 , n):
#         if i ** 2 == n:
#             print(f"Yes! {i} * {i} = {n}")
#             break
#     else:
#         print("NO!")
#
# x = int(input("enter a number :"))
# bel(x)
# --------------------------------------4---------------------------------------
# def bel(a):
#     for i in range(1 , a):
#         if i ** 2 == a:
#             print(f"Yes! {i} * {i} = {a}")
#             break
#     else:
#         print("no!")
#
# z = int(input("enter a number : "))
# bel(z)
#----------------------------------------------------------
#------------------------------55555555555555555555555------------------------------
# میزان تخفیف

# def bel(gh,t):
#     m_t = int(gh * t / 100)
#     gh_j = gh - m_t
#     print("m_t:", m_t)
#     print("gh_j: ", gh_j)
#
# gh = int(input("gh1: "))
# t = int(input("t: "))
# bel(gh,t)
# --------------------------------5-----------------------------
# def bel(gh,t):
#     m_t = int(gh * t / 100)
#     gh_j = gh - m_t
#     print("m_t : ", m_t)
#     print("gh_j : ", gh_j)
#
# gh = int(input("gh1: "))
# t = int(input("t :"))
# bel(gh,t)
#----------------------------6666666666666666-------------------------------

# def bel(Al):
#
#     if "0" <= Al <= "9":
#         print("your character is a number")
#     elif "A" <= Al <= "Z":
#         print("your character is a uppercase later")
#     elif "a" <= Al <= "z":
#         print("your character is a lowercase later")
#     else:
#         print("other")
#
# x = input("enter your charakter :")
# bel(x)
#-------------------------------------------------------------------

# توابع لامب دا(--------------------------lambda
# کلیات
# l = lambda x: x**3
# print(l(4))
# یاااااااااا
# l = lambda x , y , z , s , r: x**2 + y*2 + z-2 + s+2 + r/2
# print(l(1,2,3,4,5))
#  یااااااااااااااا
# l = lambda x ,y: x**2 + y*2
# print(l(2,3))
#-------------------------------------
# جزییات
# def bel(x):
#     return x**2
#
# li = [1,2,3,4,5]
# print(li)
# new = list(map(bel, li))
# print(new)
# ----------------------------------
# یاااااااااااااااااااااااااااااااااا ی جور دیگههههههههه
# def bel(x):
#     return x**2

# li = [1,2,3,4,5]
# print(li)
# new = list(map(lambda x :x**2 , li))
# print(new)
#-----------------------------------------------
# def abol(a):
#     return a*12
# t = "1,2,3,4,5"
# x = list(map(abol , t))
# print(x)
#------------------------
# li = (56,64,53,78)
# a = list(map(lambda x :x**3 , li ))
# print(a)
# -----------------------
# def bel(a):
#     if a % 5 == 0:
#         return True
#     else:
#         return False
# li = [5,10,30,40,9,8,7,6,1,2,50,1505,3]
# print(li)
# mew = list(filter(bel, li))
# print(mew)
# -------------------------------------------------
# -----------------یجوز دیگهههههههههههههههههههه---------------------

# def bel(a):
#     if a % 5 == 0:
#         return True
#     return False
# li = [5,10,30,40,9,8,7,6,1,2,50,1505,3]
# print(li)
# mew = list(filter(bel, li))
# print(mew)

# ----------------------یجور دیگههههههههههههههههههههههه----------------------------

# def bel(a):
#     return a > 5
# li = [5,10,30,40,9,8,7,6,1,2,50,1505,3]
# print(li)
# mew = list(filter(bel, li))
# print(mew)
# ------------------------------------
# با استفاده از lambda
# li = [5,10,30,40,9,8,7,6,1,2,50,1505,3]
# print(li)
# mew = list(filter(lambda x : x > 5 , li))
# print(mew)
#----------------------------------------------
# from functools import reduce
# def bel(x, y):
#     return x * y
# li = [1,2,3,4]
# print(li)
# new = reduce(bel, li)
# print(new)
# ---------------------------------------------
# ببین مشکل کجاست
# import copy
# def bel(x):
#     x = [1,2,[3,[4],54],3,21]
#     x[2] = 12
#     new = copy.deepcopy(x)
#     print(new)
#     return x
# -------------------------------------------
# def bel(x):
#     return x
#
# li = [6,5,4,5,3,8,9,1,2]
# print(li)
# n = sorted(li)
# print(n)
# -------------------------------

# def bel(x):
#     return x * 3
#
# li = [6,5,4,5,3,8,9,1,2]
# print(li)
# n = sorted(li, key=bel)
# print(n)
#-------------------------------------
# def bel(x):
#     return x
# li0 = ["uhhj", "nujhgfrdftg", "esdrfdf" ,"rfedgum"]
# li = [6,5,4,5,3,8,9,1,2]
# print(li0)
# n = sorted(li0, key=bel)
# print(n)
#----------------------------------------------------------
# -----------------------سری دوم تمرینات-------------------
# --------------------تمرین 111111111111111------------------------
# for _ in range(1 , 100):
#     n = list(map(lambda x: x , range(0 , 100)))
#     print(n)
#     break
# ------------------------تمرین 1 حل دولتی--------------------------
# li = [32,33,87,2,4,8,99,101,44,47]
# print("list:", li)
# print("all namber list : " , len(li))
# zoj = list(filter(lambda x: x % 2 == 0, li))
# number_zoj = len(list(filter(lambda x: x % 2 == 0, li)))
# print("zoj : " , zoj)
# print("number_zoj :" , number_zoj)
# fard = list(filter(lambda x: x % 2 != 0, li))
# number_fard = len(list(filter(lambda x: x % 2 != 0, li)))
# print("fard : " , fard)
# print("number_fard : " , number_fard)

# -------------------------تمرین2222222222222222--------------------------
# li = [("ali",59),("abolfazl",84),("hossin",90),("ozra",66)]
# print("li : ",li)
# li.sort(key=lambda x: x[1] , reverse=True)
# print("sorted li : ", li)
# -------------q22222222222222222-------------------
# li = [("ali",59),("abolfazl",84),("hossin",90),("ozra",66)]
# print("li : ", li)
# li.sort(key=lambda x: x[1])
# print("sort li :" , li)
# --------------------33333333333333333333----------------------
# ---------------3-------------------------------------
# ------------------------4444444444444----------------------------
# for _ in range(0,20):
#     n = list(filter(lambda x : x % 2 == 0 , range(1,20+1)))
#     print(n)
#     z = list(filter(lambda y : y not in n , range(1,20)))
#     print(z)
#     break
# ----------------------------دولتی حل تمرین 4----------------------
# n = list(filter(lambda x : x % 2 == 0 , range(1,20+1)))
# print(n)
# z = list(filter(lambda y : y not in n , range(1,20)))
# print(z)
# -------------------------------جور دیگر-------------------------
# li = [22,29,87,18,20,75,84]
# n = list(filter(lambda x : x % 2 == 0 , li))
# print(n)
# print(len(n))
# z = list(filter(lambda y : y not in n , li))
# print(z)
# print(len(z))
# --------------------5555555555---------------------------

# li = list(input("enter list :").split(","))
# li = [1,2,3,4,78,89,65,55,43,98,20,21]
# print(li)
# n = list(map(lambda x: x**2 , li ))
# z = list(map(lambda y: y**3 , li ))
# print(n," : مربع اعداد")
# print(z," : مکعب اعداد")
# -------------------جور دیگر----------------------------

# for _ in range(0 , 100):
#     print(range)
#     n = list(map(lambda x: x**2 , range(0 , 100)))
#     z = list(map(lambda y: y**3 , range(0 , 100)))
#     print(n," : مربع اعداد")
#     print(z," : مکعب اعداد")
#     break
# ----------------------------5------------------------------




#----------------------666666666666------------------------
# x = ("abolfazl,2,13,4,5,2,reza,908")
# while True:
#     if x == "abplfazl":
    # n = map(lambda y: int(y) == "abofazl" , x)
    # print(n)
    # break
# else:
#     print("not start carecter word abolfazl")
# break
# ------------------------6------------------------
# x = "abolfazl"
# starts_with = lambda x: True if x.startswith("a") else False
# print(starts_with(x))
# ----------------7777777777777777777----------------
# x = "4"
# print(x.isdigit())
# print(x.isnumeric())
# print(x.isdecimal())
#--------------------------
# x = "4.5"
# is_num = lambda x: x.replace(".", "", 1).isdigit()
# print(is_num("4.6"))
# print(is_num("29"))
# print(is_num("abas"))
# print(is_num("198a822"))
# print(is_num("5..7"))
#----------------------------ادامه---------------------------------
# print("__iter__" in dir(range(10)))
# یا
# print(dir([1,2,3]))
# ----------------------------------------------------------
# x = [1,2,3,4]
# print("__next__" in dir(x))
# x = iter(x)
# print("__next__" in dir(x))
# -----------------------------------------------------
# x = [1,2,3,4]
# x = iter(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# ----------------------------------------------------
# iterator هایی که به پایان نمیرسند
# (count)

# from itertools import count
#
# counter = count(10)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#-----------------------------------------------------


# -------------------Decorator---------------------------
# توابع تو در تو
# ارسال تابع به عنوان آرگمان
# دو مفهوم بالا در ویدیوی 9 فصل 6 توضیح داده شده
# -----------
# def dec(func):
#     def inner():
#         print(40 * "*")
#         func()
#         func()
#         print(40 * "*")
#     return inner
#
# def f():
#     print("reza")
#
# new_func = dec(f)
# new_func()
# new_func()
# new_func()
# ---------------------------------------
# مرور
# یک سری iterator ها وجود دارد یا ما خودمان میتوانیم ایجاد کنیم کهبه پایان نمیرسد مثل : count

# from itertools import count
#
# counter = count(10)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print("__next__" in dir(counter))
#------------------------------------------------------
# جور دیگر که بتوانیم دکراتور های بیشتری ایجاد کنیم
# def dec(func):
#     def inner():
#         print(40 * "*")
#         func()
#         func()
#         print(40 * "*")
#     return inner
#
# @dec
# def f():
#     print("reza")
#
# @dec
# def f2():
#     print(("abolfazl"))
#
# f()
#
# f2()
#----------------------------------------------
# جور دیگر
# def dec(func):
#     def inner():
#         print(40 * "*")
#         func()
#         func()
#         print(40 * "*")
#     return inner
#
# def f(x , y):
#     print(x/y)
#
# f(10 ,9)
# --------------------------------------------
#جور دیگر که عدد تقسیم بر صفر خطا ندهد
# def dec(func):
#     def inner(x , y):
#         if y == 0:
#             print("warning!!!")
#         else:
#             func(x,y)
#     return inner
#
# @dec
# def f(x , y):
#     print(x/y)
#
# func1 = dec(f)
# func1(5,10)

#یا

# f(10 ,2)

# ---------------------------------------------
# def bel(func):
#     def able():
#         func()
#         print(2 ** 3 * 10 * "*")
#     return able()
#
# def f():
#     print("abolfazl")
#     print(2 ** 3 * 10 * "*")
#     print("hossin")
#
# bel(f)
# bel(f)
# bel(f)
# bel(f)

# ------------------------------------------
# def bel(a):
#     def able(x , y):
#         if y == 0:
#             print("error")
#         else:
#             a(x,y)
#     return able
#
# def f(x, y):
#     print(x/y)
#
# a = bel(f)
# a(2,0)
# ----------------------------
# def able(z):
#     def bel(x , y):
#         if y == 0:
#             print("erorr")
#             print("False")
#         else:
#             z(x ,y)
#     return bel

# def f(x,y):
#     print(x/y)
#
# new = able(f)
# new(3,0)
#-----------------------------------------
# ین دفعه با@ (ادساین پیش برو)
# def bel(a):
#     def able(x,y):
#         if y == 0:
#             print("rede")
#             print("false")
#         else:
#             a(x,y)
#     return able
#
# @bel
# def mam(x,y):
#     print(x ** y)
#
# mam(2,0)
#----------------------------------------
# باحث بالا رو دوباره مرور کن

# def bel(a):
#     def able(x ,y):
#         if x == y:
#             a(x,y)
#             print("very very good")
#         else:
#             a(x ,y)
#             print("very bad")
#     return able
#
# @bel
# def xxl(x,y):
#     print(x / y)
#
# xxl(8,8)
#-----------------------------------------------

# def bel(a):
#     def able(x , y):
#         if y == 0:
#             return "error"
#         else:
#             return a(x,y)
#     return able
#
# @bel
# def f(x, y):
#     return x/y
#
# print(f(2,9))
#--------------------------------------
# بهای دکراتور رپر هم میگویند یا همان پوشاننده یا پوشش دهنده wrapper
# def able(a):
#     def bel(*x , **y):
#         if y == 0:
#             return "warning!!!"
#         return a(*x , **y)
#     return bel
#
# @able
# def f(x , y , z):
#     print(x * y * z["A"])
#
# print(f(5, 95,{"A":2}))
#----------------------------------------------
# new
# یک ستاره برای تاپل ها و دو ستاره برای دیکشنری ها
# def bel(az):
#     def able(*x , **y):
#      برای اسم های جند تایی زیاد مهم نیست   # print(20 * "*")
#         az(*x , **y)
#         print(20 * "*")
#     return able
#
# @bel
# def f(name):
#     print("I am " + name)
#
# f("abolfazl")
# f("ali")
# f("reza")
# ----------------------------------------------------
# ما میتوانیم چند دکاروتور را روی هم پیاده سازی کنیم مانند رنحیر

# def plus(az):
#     def able(*x , **y):
#         print(20 * "+")
#         az(*x , **y)
#         print(20 * "+")
#     return able
#
#
# def star(az):
#     def able(*x , **y):
#         print(20 * "*")
#         az(*x , **y)
#         print(20 * "*")
#     return able
#
# def dash(az):
#     def able(*x , **y):
#         print(20 * "-")
#         az(*x , **y)
#         print(20 * "-")
#     return able
#
# @dash
# @star
# @plus
# def f(name):
#     print("I am " + name)
#
# f("abolfazl")
#
# ---------------------------
# ی جور دیگه

# def plus(az):
#     def able(*x , **y):
#         print(20 * "+")
#         az(*x , **y)
#         print(20 * "+")
#     return able
#
#
# def star(az):
#     def able(*x , **y):
#         print(20 * "*")
#         az(*x , **y)
#         print(20 * "*")
#     return able
#
# def dash(az):
#     def able(*x , **y):
#         print(20 * "-")
#         az(*x , **y)
#         print(20 * "-")
#     return able
#
#
# def f(name):
#     print("I am " + name)
#
# printer = dash(plus(f))
#
# printer("abolfazl")

# ----------------------------------------------------
# یک لول بالاتر از سطح قبل دقیقه 15 تا 17 فصل 6 قسمت 18
# ----------------------------------------------------
# جلوگیری از تغییر پیدا کردن اطلاعاتی که زوی دکراتور اعمال شده

# import functools
#
# def bel(az):
#     @functools.wraps(az)
#     def able(*x , **y):
#         print(20 * "*")
#         az(*x , **y)
#         print(20 * "*")
#     return able
#
# @bel
# def f(name):
#     """prints a massage"""
#     print("I am " + name)
#
#
# print(f.__doc__)
# print(f.__name__)
# ----------------------------------------------------
# ی جور دیگه

# from functools import wraps
#
# def bel(az):
#     @wraps(az)
#     def able(*x , **y):
#         print(20 * "*")
#         az(*x , **y)
#         print(20 * "*")
#     return able
#
# @bel
# def f(name):
#     """prints a massage"""
#     print("I am " + name)
#
# f("amer")
# print(f.__doc__)
# print(f.__name__)
#------------------------------------------
# قسمت 19

# users = {"ali" : "123432394" , "abolfazl" : "759479339" , "sara" : "97997990" , "david" : "5745656"}
#
# def print_password(username):
#     print(username, ":" , users[username])
#
# print_password("david")


# ------------------------------------

# users = {"ali" : "mamade" , "samad" : "38228392" , "fate" : "36728711" , "sara" : "567823308"}

# def bel(x):
#     print(x , ":" , users[x])
#
# bel("ali")
# --------------------------------------------

# users = {"ali" : "mamade" , "samad" : "38228392" , "fate" : "36728711" , "sara" : "567823308"}
#
# def print_password(username):
#     print(username , ":" , users[username] )
# print_password("ali")
# print_password("fate")
# print(users)
# ------------------------------------------------
# دکوراتوری برای تغییر پسورد و نوشتن حود آن
# password = {"ali" : "86726270" , "samad" : "3828392" , "fate" : "3672871" , "sara" : "56782308" , "abolfazl01" : "63736342"}
# def print_password(username):
#     print(username , ":" , password[username] )
#
# def change_password(username , new_password):
#     password[username] = new_password
#     print(username , ":" , password[username] )
#
# print_password("ali")
# change_password("abolfazl" , "012345")
# print(password)
# ----------------------------------------------
# دکوراتوری که قرار است روی کلی توابع اعمال شود و یکسری یوزر نیم ها را بزاریم در بلک لیست تا کار بر نتواند پسورد را ببیند یا اینکه کار بر ببیند ولی نتواند ان را عوض کند

# password = {"ali" : "86726270" , "samad" : "3828392" , "fate" : "3672871" , "sara" : "56782308" , "abolfazl01" : "63736342"}
# blacklist = {"abolfazl01" , "samad"}
#
# def ban(func):
#     def bel(*args, **kwargs):
#         if args[0] in blacklist:
#             print("this user is blacked")
#         else:
#             func(*args, **kwargs)
#     return bel
#
# @ban
# def print_password(username):
#     print(username , ":" , password[username])
#
# @ban
# def change_password(username , new_password):
#     password[username] = new_password
#     print(username , ":" , new_password)
#
# print_password("sara")
# change_password("abolfazl01" , "012345")
# print(password)
#----------------------------------------------------------------------------------------
# مرور

# password = {"ali" : "86726270" , "samad" : "3828392" , "fate" : "3672871" , "sara" : "56782308" , "abolfazl01" : "63736342"}
# blacklist = {"sara" , "fate"}
#
# def ban(func):
#     def bel(*args, **kwargs):
#         if args[0] in blacklist:
#             print("this is a blacklist")
#         else:
#             func(*args, **kwargs)
#     return bel
#
# @ban
# def print_password(username):
#     print(username, ":" ,password[username])
# @ban
# def change_password(username , new_password):
#     password[username] = new_password
#     print(username, ":" ,password[username])
#
# print_password("ali")
# change_password("sara" , "098765")
# print(password)
# -----------------------------------------------------------
# زمانی که طول میکشد تا یک تابع اجرا شود

# from time import perf_counter
# from functools import wraps
#
# def time_calculation(func):
#     @wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         start_time = perf_counter()
#         value = func(*args, **kwargs)
#         end_time = perf_counter()
#         run_time = end_time - start_time
#         print("the run time of", func.__name__, "is : ", run_time)
#         return value
#     return wrapper_decorator
#
# @time_calculation
# def A(x):
#     z = 0
#     for i in range(x):
#         z += i**3
#
# @time_calculation
# def B(y):
#     k = 1
#     for i in range(y):
#         k *= i
#
# A(1234098)
# B(2989992)

# ---------------------------------------------------
# from time import perf_counter
# from functools import wraps
#
# def time_calculation(func):
#     @wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         start_time = perf_counter()
#         value = func(*args, **kwargs)
#         end_time = perf_counter()
#         run_time = end_time - start_time
#         print("the run time of", func.__name__, "is : " , run_time)
#         return value
#     return wrapper_decorator
#
# @time_calculation
# def A(x):
#     z = 0
#     for i in range(x):
#         z += i**3
#
# @time_calculation
# def B(y):
#     k = 1
#     for i in range(y):
#         k *= i
#
# A(1234098)
# B(2989992)
#--------------------------------------------------
# میخوام مرورکنم و اعداد روتوی بازه مشخصی که خودم میخوام بر عکس تعدادشون چاپ بشه مثلا -20تا
# def A(x ,y):
#     s = 0
#     for i in range(x ,y):
#         s += 1
#     print(s.reversed(10))
#     return s
#
# A(100,90)
#------------------------------------------------------- -----------------------------------------------

# ------------------------------جلسه 20 فصل 6 (ژنراتور ها یا همان مولد ها)------------------

# i = iter([1,2,3,4])
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# ------------------مثال های ساده--------------------

# def func(x):
#     print("abolfazl")
#     yield x**2
#     print("hello")
#     yield 7
#     print("yes")
#     yield x**3-10
#
# x = func(5)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# ---------------------------2--------------------------

# ----------------------------
# iter_a01 = iter([1,2,3])
# for i in iter_a01:
#     print(i)
# ------------------------
# iter_a01 = iter([1,2,3])
# print(next(iter_a01))
# print(next(iter_a01))
# print(next(iter_a01))
# print(next(iter_a01))
# --------------------------------------


# def my_generator():
#     print("welcome")
#     for i in range(5):
#         return i**2
#
# g = my_generator()
# for i in g:
#     print(i)
# ------------------------------------------

# def my_generator():
#     print("welcome")
#     for i in range(5):
#         yield i**2
#
# g = my_generator()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#-------------------------------------------------
# مرور
# x = iter([1,2,21,12])
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# ------------------------
# x = iter([1,2,12,21])
# for i in x:
#     print(i)
#----------------
# x = iter([1,2,3,4,5])
# for i in x:
#     print(i)
# -----------------
# def not_feel(x):
#     print("hi abolfazl")
#     yield x**2
#     print("sede")
#     yield x**3
# v = not_feel(5)
# print(next(v))
# print(next(v))
# print(next(v))
# ------------------------------

# def not_feel(x):
#     print("hi abolfazl")
#     for i in range(10):
        # print(i)
    # yield x*2
#
# v = not_feel(0)
# print(next(v))
#--------------------------------
# def list_range(start, end, step=1):
#     new_range = []
#     while start < end:
#         new_range.append(start)
#         start += step
#     return new_range
#
# r = range(20,40,2)
# print(list(r))
# lr = list_range(20,40,2)
# print(list(lr))
# ---------------------------------------
# حالت اول نوشتن با تابع
# from time import perf_counter
#
# def lest_range(start, end, step=1):
#     new_range = []
#     while start < end:
#         new_range.append(start)
#         start += step
#     return new_range
#
# lr = lest_range(0, 52 , 17)
# print(list(l_r))
# ---------------------------------------------
# حالت دوم نوشتن با متغییر
# l = range(0 ,52 , 17)
# print(list(l))
#----------------------------------------------
# همین کاری که بالا انجام دادیم برا ی زنراتور ها هم میتوان انجام داد
# def grn_range(start, end , step=1):
#     while start < end:
#         yield start
#         start += step
#
# gr = grn_range(20 , 50 , 2)

# print(list(g_r))
#----------------------------------------------
# حالت دوم نوشتن با متغییر ها برای ژنراتور
# ---------------------------------------------

# ---------------------------------


# from time import perf_counter
#
# def lest_range(start, end, step=1):
#     new_range = []
#     while start < end:
#         new_range.append(start)
#         start += step
#     return new_range
#
# lr = lest_range(0, 52 , 17)
# ----------------------------------------------------
#
# def grn_range(start, end , step=1):
#     while start < end:
#         yield start
#         start += step
#
# gr = grn_range(20 , 50 , 2)
# ---------------------------------------------------
#
# start = perf_counter()
# lr = lest_range(1, 100000)
# a = 0
# for i in lr:
#     if i == 3:
#         break
#     a += i**2
# end = perf_counter()
# print("lr:", end-start)
# ---------------------------------------------------

# start2 = perf_counter()
# gr = grn_range(1, 1000000000000000000000000000000000000000000)
# x = 0
# for j in gr:
#     if j == 3:
#         break
#     x += j**2
# end2 = perf_counter()
# print("gr:", end2-start2)
# ------------------------------------------
#  تمام عبارت ها را میتوان لحاظ کرد مانند جمع و ماکسیمم و...
# def my_generator(a=25):
#     for i in range(a+1):
#         yield i**2
#
# lg = my_generator()
# sg = my_generator()
# ming = my_generator()
# mag = my_generator()
# print(list(lg))
# print(sum(sg))
# print(min(ming))
# print(max(mag))

# -----------------------------------------------
# ژنراتور 3تا متد مهم و کاربردی دارد
# به مثال زیر توجه کن

# def my_generator(a=10):
#     for i in range(a+1):
#         yield i**2
#
# mg = my_generator()
# mg.close()
# mg.send()
# mg.throw()
# print(max(mg))
#-----------------------------------------------
# l = ["a","b","c" ,"d"]
#
# for i in range(len(l)):
#     print(i , ":" ,l[i])
# یااااااااااا
# استفاده از enumerate
# l = ["a","b","c" ,"d"]
#
# for i,j in enumerate(l):
#     print(i,":",j)
# -------------------------------------------------
# سری سوم تمرینات فصل 6 جلسه 22
# --------------------------تمرین1------------------
# ژنراتوری که کار enumerate را انجام میدهد
# x = ["a","b","c","d"]
# def my_generator(i,j):
#     for i,j in enumerate(x):
#         yield i,j
#         print(i,":",j)
#
# z = my_generator(0,3)
# print(list(z))
# ------------------1-------------------------

# def my_generator(secuenc, start=0):
#     n = start
#     for i in secuenc:
#         yield n , i
#         n += 1
#
# list = ["ali","ahmad","reza","arash"]
# for i,j in my_generator(list,1000):
#     print(i,"=>",j)
# --------------------تمرین2--------------------------
# def fibonacci():
#     f1 = 0
#     yield f1
#     f2 = 1
#     yield f2
#     while True:
#         f3 = f1 + f2
#         yield f3
#         f1 = f2
#         f2 = f3
#
# fib = fibonacci()
# for _ in range(10):
#     print((next(fib)))

 #-----------------------2------------------------
#فیبو نان چی از جمع دو عدد قبلی خود عدد بعدی بدست می آید

# def fibonacci():
#     f1 = 0
#     yield f1
#     f2 = 1
#     yield f2
#     while True:
#         f3 = f1 + f2
#         yield f3
#         f1 = f2
#         f2 = f3
#
# fib = fibonacci()
# for _ in range(50):
#     print(next(fib))
# ---------------------3-------------------------
# در تمرین 3 دقیقا برعکس تمرین 2 عمل کردیم در فیبوناچی حاصل های ایجاد شده توسط خود سیستم با هم جمع میشوند ولی در تمرین 2 اعدادی که توسظ کاربر ایجاد شده با هم جمع میشوند که آن هم از اول تا آخر تست
# def sum_generator(lst):
#     s = 0
#     for i in lst:
#         s += i
#         yield s
#
# sg = sum_generator([1,2,3,4,5,6,7,8,9,10])
# for i in sg:
#     print(i)
# --------------------تمرین4----------------------------

# def str_generator(lst):
#     s = ""
#     for i in reversed(lst):
#         s += str(i)
#         yield i
#
# sg = str_generator("ali , sara , fate , raza")
# for i in sg:
#     print(i , end="")

# -------------------4---------------------
# --------------------------خود تمرین-------------------
# def rev_str(s):
#     l = len(s)
#     for i in range(l-1, -1, -1):
#         yield s[i]
#
# sg = rev_str("abolfazl yousefi")
# for ch in sg:
#     print(ch)

# --------------------برعکس تمرین------------------

# def rev_str(s):
#     l = len(s)
#     for i in range(l):
#         yield s[i]
#
# sg = rev_str("abolfazl yousefi")
# for ch in sg:
#     print(ch)
# -----------------------------5تمرین-----------------------------
# def my_gen(even_or_odd="e"):
#     n = 0
#     if even_or_odd == "o":
#         n = 1
#
#     while True:
#         yield n
#         n += 2
#
# e_o = my_gen(input("enter => e or o : "))
# for _ in range(10):
#     print(next(e_o))

# --------------------6------------------------------------------
# def num_gen():
#     c = 1
#     while True:
#         s = ""
#         for i in range(1, c+1):
#             s += f"{c}\t"
#         yield s
#         c += 1
#
# n = num_gen()
# for j in range(10):
#     print(next(n))

# -------------------------مرور----->>>>>>>------تمرین 1----------------
# اشتباه
# lst = ["abas","fate","sead","ali","reza"]
# def gr_enumerate(able):
#     e = 0
#     for i in able(lst):
#         e += len(i)
#         yield e
#
# g = gr_enumerate(lst)
# print(list(g))
# ------------------صحیح----------------

# def my_generator(able, start=0):
#     n = start
#     for i in able:
#         yield n , i
#         n += 1
#
# lst = ["abas","fate","sead","ali","reza"]
# for i , j in my_generator(lst,1):
#     print(i,":",j)
#------------------------------------

# -----------------رفتار کوروتین در ژنراتور-----------------

# کورتین
# def my_generator():
#     print("start!")
#     while True:
#         name = yield
#         print("my name is", name)
#
#
# x = my_generator()
# next(x)
# x.send("abolfazl")
# x.send("hamed")
# --------------------------مرور-----------------------

# def my_gna():
#     print("start")
#     for i in range(5,10):
#         name = yield i
#         print("my name is", name)
#
#
# n = my_gna()
# print(next(n))
# print(n.send("babe"))
# print(next(n))
# print(n.send("sara"))
# -------------------------------------------------------
# برنامه ای که یکسری از عبارت ها را سانسور میکند

# def cen_gan(words):
    # print("start")
    # w = None
    # while True:
    #     word = yield w
    #     if word not in words:
    #         w = word
    #     else:
    #         w = "*" * len(word)
#
#
# g = cen_gan(["khar","gav","meymoon"])
# next(g)
# print(g.send("hamed"))
# print(g.send("abolfazl"))
# print(g.send("khar"))
# print(g.send("neda"))
# print(g.send("gav"))
# print(g.send("meymoon"))
# print(g.send("ali"))
#
# ---------------------------------------------------------
# برنامه ای که کار split انجام میدهد

# def cen_gen(ablactor = " "):
#     print("start")
#     s = None
#     while True:
#         line = yield s
#         s = line.split(ablactor)
#
# sg = cen_gen("-")
# next(sg)
# print(sg.send("ali-reza-hamed-fate-neda-sahel"))

# ------------------------------------------------------

# --------------------------مرور------------------------

# def grn_num():
#     print("start!")
#     for i in range(1,10):
#         name = yield i
#         print("my name is ",name)
#
#
# g = grn_num()
# print(next(g))
# print(g.send("abplfazl"))
# print(next(g))
# print(g.send(""))
# print(next(g))
# print(g.send("ali"))
# print(next(g))

# ------------------------------------------------------

# def gen_can(words):
#     print("start")
#     w = None
#     while True:
#         word = yield w
#         if word not in words:
#             w = word
#         else:
#             w = "*" * len(word)
#
# g = gen_can(["khar","gav","meymoon"])
# next(g)
# print(g.send("abolfazl"))
# print(g.send("khar"))
# print(g.send("gav"))
# ----------------------------------------------

# def spl_gen(koba=" "):
#     print("start")
#     s = None
#     while True:
#         line = yield s
#         s = line.split(koba)
#
# g = spl_gen("-")
# next(g)
# print(g.send("ali,reza,neda,fate"))
# -------------------صفات تابع------------------------

# میانگین نمره یا معدل دانش آموزان

# def abl(lit):
#     return sum(lit)/len(lit)
#
# print(abl({20, 18, 15, 14, 17}))
# print(abl([20, 18, 15, 14, 17]))
# --------------------------ایجاد یک صفت میخواهیم بدانیم نمره ای که ایجاد کردیم برای کدام مدرسه است--------------------------
# جلسه 25 فصل 6
# def abl(lit):
#     return sum(lit)/len(lit)
#
#
# def abl2(lit):
#     return sum(lit)/len(lit)
#
#
# abl.school_name = "moyin"
# abl2.school_name = "vosoghe"
#
# print(abl.school_name)
# print(abl([13, 18, 15, 14, 17]))
# print(abl2.school_name)
# print(abl([20, 18, 15, 14, 17]))
#-------------------------------------------------------------
# -------------------------توابع بازگشتی ----------------------
# فصل 6 قسمت 26
# توابع باز گشتی بیشتر زمانی کاربرد دارند که بخواهیم با الگوریتم ها کار کنیم
# تعریف: هر تابعی کهخودش خودش راصدا بزند تابع باز گشتی است
# --------========++++++++++=========--------------

# نوشتن فاکتور یل به صورت عادی

# def fact(x):
#     f = 14
#     for i in range(1, x+1):
#         f *= i
#     return f
#
# print(fact(5))
# print(fact(6))
#-----------------------------------------------------

# نوشتن فاکتور یل با استفاده از توابع بازگشتی

# def fact(x):
#     if x == 0 or x == 1:
#         return 1
#     return x * fact(x-1)
#
# print(fact(5))
#-------------------------------------------------

# from time import sleep
#
# def time_reverse(n):
#     x = 1
#     sleep(1)
#     for _ in reversed(range(n)):
#         while x <= n:
#             x -= 1
#     return x
#
# g = time_reverse(10)
# print(g)
# -------------------------------------------------


# ***********************************تا پایان فصل6 *************************************

# کتاب خانه ترم کالر(termcolor)

# def colored(text, color):
#     colors = {
#         "grey": "\033[90m",
#         "red": "\033[91m",
#         "green": "\033[92m",
#         "yellow": "\033[93m",
#         "blue": "\033[94m",
#         "magenta": "\033[95m",
#         "cyan": "\033[96m",
#         "white": "\033[97m",
#     }
#
#     reset = "\033[0m"
#
#     if color in colors:
#         return colors[color] + text + reset
#     else:
#         return text
#
#
#
#
# from termcolor import colored
# import os
# os.system("")
#
# print(colored("=== برنامه مدیریت ===", "cyan"))
# print(colored("1. شروع برنامه", "green"))
# print(colored("2. تنظیمات", "yellow"))
# print(colored("3. خروج", "red"))
#
# choice = input(colored("انتخاب شما: ", "magenta"))
#
# if choice == "1":
#     print(colored("برنامه اجرا شد ✅", "green"))
# elif choice == "2":
#     print(colored("وارد تنظیمات شدی ⚙", "yellow"))
# elif choice == "3":
#     print(colored("خروج از برنامه ❌", "red"))
# else:
#     print(colored("گزینه نامعتبر!", "red"))


# --------------------کتاب خانه حرفه ای تر برای رنگ بندی-----------------------



# import os
# import sys
#
# # فعال سازی رنگ در ویندوز
# if sys.platform.startswith("win"):
#     os.system("")
#
# class Style:
#     RESET = "\033[0m"
#     BOLD = "\033[1m"
#
# class Color:
#     BLACK = "\033[30m"
#     RED = "\033[31m"
#     GREEN = "\033[32m"
#     YELLOW = "\033[33m"
#     BLUE = "\033[34m"
#     MAGENTA = "\033[35m"
#     CYAN = "\033[36m"
#     WHITE = "\033[37m"
#
# class BgColor:
#     BLACK = "\033[40m"
#     RED = "\033[41m"
#     GREEN = "\033[42m"
#     YELLOW = "\033[43m"
#     BLUE = "\033[44m"
#     MAGENTA = "\033[45m"
#     CYAN = "\033[46m"
#     WHITE = "\033[47m"
#
#
# def styled(text, color="", bg="", bold=False):
#     style = ""
#
#     if bold:
#         style += Style.BOLD
#
#     style += color
#     style += bg
#
#     return f"{style}{text}{Style.RESET}"
#
#
# # استایل‌های آماده
# def success(text):
#     return styled(text, Color.GREEN, bold=True)
#
# def error(text):
#     return styled(text, Color.RED, bold=True)
#
# def warning(text):
#     return styled(text, Color.YELLOW, bold=True)
#
# def info(text):
#     return styled(text, Color.CYAN)
#
# def title(text):
#     return styled(text, Color.MAGENTA, bold=True)
#
#
#
# from terminal_style import *
#
# print(title("=== سیستم مدیریت ==="))
#
# print(success("عملیات با موفقیت انجام شد ✅"))
# print(error("خطایی رخ داده ❌"))
# print(warning("این یک هشدار است ⚠"))
# print(info("اطلاعات بیشتر در ادامه..."))
#
# print(styled("متن با پس زمینه آبی", Color.WHITE, BgColor.BLUE, bold=True))


# x = 7
# print(x)












































































































































