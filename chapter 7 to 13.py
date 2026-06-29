from functools import update_wrapper
from tkinter.font import names

# -----------------------------------شروع فصل 7---------------------------
# ----------------------------انواع داده سطح 2------------------------------
# داده ها شامل : تاپل ها لیست ها دیکشنری رشته و... که هرکدام از این نوع داده هامتد های مخلفی دارند


# ----------------------------چهار تابع مهم که باید بلد باشی---------------------------




# --------------مثال ها---------
# 1
# print(divmod(10,3))
# 2
# print(pow(6,5,7))
# 3
# print(round(2.457654579,2))
# 4
# print(abs(-1384))

#----------------------------------int and float----------------------

# اتریبیوت ها یا همان متد های رشته:
# x = 5
# print(dir(int))
#بررسی متد هایی که قبل و بعدشان اندرسکور ندارند
# x = 0.75
# y = 5657909.676
# print(x.as_integer_ratio())
# print(y.as_integer_ratio())

# ---------------

# x = 19
# print(x.bit_count())
# print(bin(2))

# ----------------------
# x = 677890
# print(x)
# print(bin(x))
# print(x.bit_length())

# ----------------

# x = 3 + 4j
# print(x.imag)
# print(x.real)
# print(x.conjugate())

# ------------------

# x = 45
# print(x.denominator)

# ----------------

# x = 76887
# print(x.numerator)

# ---------------------

# to_bytes
# from_bytes
# این دو برعکس هم هستند و زیاد اهمیتی ندارند
# --------------------شروع متد های داده فلویت ها-----------------------
# print(dir(float))
# ----------------------

# f = 16.5
# print(f.hex())
# و برعکس
# f = 16.5
# print(f.fromhex("0x1.0800000000000p+4"))
# ----------------------

# f = 4
# print(f.is_integer())

# ----------------------------------شروع متد های داده لیست ------------------------------

# print(dir(list))

# ------------------------

# li = [1,2,3,4]
# print(li)
# li.append(5)
# print(li)

# ----------یا بجای append----------

# li = [1,2,3,4]
# print(li)
# li[1:3] = [5]
# print(li)
# li[len(li):] = [5]
# print(li)

# ----------------------

# li = [1,2,3,4]
# print(li)
# li.clear()
# print(li)

# ---------------------

# li = [1,2,3,4]
# print(li)
# li2 = li.copy()
# li2[1] = 0
# print(li)
# print(li2)

# --------------------
# from copy import deepcopy
#
# li = [1,[0,2],3,4]
# print(li)
# li2 = deepcopy(li)
# li2[1][0] = 85
# print(li)
# print(li2)

# ----------------------

# li = [1,3,3,2,3,4,3,5]
# print(li.count(2))

# ---------------------
# extend لیست ما را توسعه میدهد

# li = [ 1,2,3,4]
# li.extend([10,20,30,40])
# print(li)

# ----------------------

# li = [22,35,44,22,84,90]
# print(li.index(44, 0,3))

# ------------------------

# li = [1,2,3,4,5,6,7]
# li.insert(4,"a.y")
# print(li)

# یا

# li = [1,2,3,4,5,6,7]
# li.insert(len(li),"a.y")
# print(li)

# -----------------------
# یندکس بده تا عنصر پاک کند
# li = [78,56,65,98,70,12,34,15]
# print(li.pop(3))
# print(li)

# -----------------------
# عنصر را بده تا همان عنصر را پاک کند
# li = [78,56,65,98,70,12,34,15]
# li.remove(70)
# print(li)

# ----------------------

# li = [78,56,65,98,70,12,34,15]
# print(li)
# li.reverse()
# print(li)

# -----------------------

# li = [78,56,65,98,70,12,34,15]
# print(li)
# li.sort()
# print(li)

# نوع دیگر اینظوریه که معکوس مرتب شده باشد از بزرگ به کوچک

# li = [78,56,65,98,70,12,34,15]
# li.sort(reverse=True)
# print(li)

# ----------------------

# li = [78,56,65,98,70,12,34,15]
# li.sort(reverse=True)
# print(li)

# ------------------------

# li = [78,56,65,98,70,12,34,15]
# li.sort(reverse=True, key=lambda x: x % 5)
# print(li)

# -------------------شروع متد های تاپل---------------------

# print(dir(tuple))


# t = (12,32,4,5,3,4,3,4,8,7,9,78,3)
# print(t.count(5))

# ---------------------------

# عنصر مورد نظر رو بده و ایندکس ان را بگیر
# t = (12,32,4,5,3,4,3,4,8,7,9,78,3)
# print(t.index(5))

# --------------شروع متد های داده set------------
# تکراری ها را set ها قبول ندارند

# print(dir(set))
# s = {1,2,3,4,5}
# s.add(8)
# print(s)

# ----------------------

# s = {1,2,3,4,5}
# x = s.copy()
# x.add(9)
# print(x)

# -------------------------

# اگر دو مجموعه هیچ اشتراکی نداشته باشند True به ما میدهد  اگر اشتراک داشته با شند به ما False نشان میدهد

# x = {1,2,3,4}
# y = {3,4,5,6}
# print(x.isdisjoint(x))

# -------------------------

# عناصر را خودش یکی یکی پاک میکند
# x = {1,2,3,4}
# y = {3,4,5,6}
# print(x.pop())
# print(x.pop())
# print(x)

# -----------------شروع متد های دیکشنری-------------

# print(dir(dict))
# print(40 * "-")
# d = {"a": 1, "b": 2}
# d.clear()
# print(d)

# --------------------------------------
# print(dir(dict))
# print(40 * "-")
# d = {"A": 1, "B": 2}
# c = d.copy()
# c["c"]= 3
# print(c)
# ------------------------------------

# d = {"a": 1, "b": 2}
# print(d)
# print(d.fromkeys(("c", "e", "f"), (2,4,3)))

# --------------------------
# get  فرقش با بقیه اینه که اگه کیلید داشته باشیم ولی مقدار نداشته باشیم برامون خطا نمیزنه بلکه Non ایجاد میکنه
# d = {"a": 1, "b": 2}
# print(d.get("c", 0))

# ---------------------------

# d = {"a": 1, "b": 2}
# print(d.values())
# print(d.keys())
# print(d.items())

# ---------------------------
# pop
# d = {"a": 1, "b": 2}
# print(d.pop("c", 3))
# print(d)
#
# یا کلا ارور میدهد
# کار پاپ دیگه
# d = {"a": 1, "b": 2}
# print(d.pop("c"))
# print(d)

# --------------------------
# popitem
# نیازی به گفتن ما نیست که چه چیزی را پاک کند یا نکند خودش از آخر شروع به پاک کردن میکند
# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# print(d.popitem())
# print(d.popitem())
# print(d)

# ---------------------------
# setdefaultفقط زمانی یک کلید مقدار اضافه میکند که کلید مقدار در دیکشنری وجود نداشته باشد اگر باشد و ماثلا دوباره سی نوشته شود نه اضافه و نه کم میشود
# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# print(d.setdefault("p",0))
# print(d)

# ---------------------------
# update  کلید مقدار را جایگزین یک کلید مقدار دیگر میکند البته اگر کلید تکراری در دیکشنری دوم وجود داشته باشد

# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# d.update({"a": 0, "k": 5, "l": 6})
# print(d)

# یا

# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# d.update(a=2, b=3)
# print(d)
# ---------------------------
# عملگر والروس
# print(w := 5)
# print(w + 2)

# ---------------------------

# x = []
#
# while True:
#     s = input("name(q outdore): ")
#     if s == "outsit":
#         break
#     x.append(s)
#
# print("list names: ", x)

# ---------------------------------

# کار بالا رامیتوان به صورت سریع ت ربا عملگر والروس انجام داد

# x = []
# while (s := input("name (q for quit): ").lower()) != "q":
#     x.append(s)
#
# print("names:", x)
#-----------------------------مرور-----------------------------

# x = []
# while True:
#     s = input("enter name (for live take outside): ")
#     if s == "outside":
#         break
#     x.append(s)
#
# print("names: ",x)

# -----------------مرور------------------

# x = []
# while (s := input("enter name (for live take outside): ").lower()) != "outside":
#     x.append(s)
# print("names:", x)

# --------------------والروس مورد استفاده در if-------------------

# a = [1,2,3,4]
# if (n := len(a)) > 2:
#     print(n)

# ----------------------والروس مورد استفاده در توابع-------------------

# def abel(x):
#     print(x ** 2)
#
# abel(z := 6)
# print(z)
#-------------------------------------

# x = [1,2,3,4]
#
# d = {
#     "l": (l := len(x)),
#     "s": (s := sum(x)),
#     "a": s / l
# }
#
# print(d)

# -------------------کالیف والرس----------------
# سوال 1
# s = input('enter a string : ')
# if (AL := len(s)) > 10:
#     print("long string: " , s)
#     print("maseag you: " , AL)
# else:
#     print("short string: " , s)
#     print("masage you: " , AL)

# --------------------------------------
# تمرین 2
# x = [12, 23, 54, 85, 69, 98, 75, 34]
# if (n := len(x)) > 5:
#     print(f"is more then five: {n}")
#     print(f"sum two first: {x[0] + x[1]}")
# else:
#     print("لیست دارای عنصر کمتر از 5 است")
#--------------------------------------------

# ------------------------
# نمونه مثال
# print("normal")
# x = []
# for i in range(10):
#     x.append(i ** 2)
# print(x)
# -------------------نمونه مثال----------------
# print("comprehension")
# x = [i ** 2 for i in range(10)]
# print(x)
# -------------------------------------------------
# ---------------------شروع مثال اثاثی----------------
# ----------------------1----------------------
# print("normal")
# x = []
# for i in range(10):
#     if i % 2 == 0:
#         x.append(i ** 2)
# print(x)
# --------------------------------------------
# print("comprehension")
# x = [i ** 2 for i in range(10) if i % 2 == 0]
# print(x)
# -------------------2----------------
# چون تاپل است i , j را در پرانتز مینویسیم
# print("normal")
# s1 = [1,2,4,5]
# s2 = [2,5,7,8]
# st = []
# for i in s1:
#     for j in s2:
#         if i != j:
#             st.append((i , j))
# print(st)
# ---------------------------------
# print("comprehension")
# s1 = [1,2,4,5]
# s2 = [2,5,7,8]
# x = [(i , j) for i in s1 for j in s2 if i != j]
# print(x)
# -------------------3---------------------
# print("comprehension")
#
# z = [-1, -3, -5, 2, 9, 8]
# x = [n ** 2 for n in z if abs(n) > 3]
# print(x)
# ------------------4----------------------
#  یکسری اسممینویسیم وبعد آن را کلمه به کلمه میکنیم
# print("comprehension")
# names = ["reza", "ali", "sara", "fared"]
# x = [ch for name in names for ch in name]
# x1 = [ch.upper() for name in names for ch in name]
# x2 = [ch.upper() + "***" for name in names for ch in name]
# print(x)
# print(x1)
# print(x2)
#------------------5------------------------
# لیستی ایجاد کنیم که هر بار از اولین رقم pi تا چایی که ما میخواهیم را نشان دهد
# print("normal")
# from math import pi
# print(pi)
# p = []
# for i in range(10):
#     p.append(str(round(pi , i)))
# print(p)



# ------------------------
# print("comprehension")
# from math import pi
# print(pi)
# from math import pi
# p = [str(round(pi , i)) for i in range(10)]
# print(p)
#-----------------------6-------------------------

# -----------------------مثال های پیچیده تر---------------------
# عوض کردن جای سطر ها و ستون ها
# print("normal")
#
# t = []
# for i in range(4):
#     t_row = []
#     for row in matrix:
#         t_row.append((row[i]))
#     t.append(t_row)
#
# for j in t:
#     print(j)
# -------------------------------------
# print("comprehension")
#
# matrix = [[1,2,3,4],
#           [5,6,7,8],
#           [9,10,11,12],
# ]
# t = [[row[i] for row in matrix] for i in range(4)]
# for j in t:
#     print(j)

# -----------------------یا ساده تر هم میتوان نوشت------------------
# تنها تفاوتش با بالایی اینه که لیست نیست و تاپل است
# matrix = [[1,2,3,4],
#           [5,6,7,8],
#           [9,10,11,12],
# ]
#
# t = list(zip(*matrix))
# for j in t:
#     print(j)

# ---------------------------مرور-----------------------------

# matrix = [[1,2,3,4],
#           [5,6,7,8],
#           [9,10,11,12],
# ]

# x = [[row[i] for row in matrix] for i in range(4)]
# for j in x:
#     print(j)
# ----------------------مرور--------------------
# a = []
# for i in range(4):
#     a_row = []
#     for row in matrix:
#         a_row.append(row[i])
#     a.append(a_row)
#
# for j in a:
#     print(j)
#-------------------------------

# x = [2,13,12,24,21,45,66]
# y = []
#
# for i in x:
#     if i % 2 != 0:
#         y.append(i)
#     else:
#         y.append(0)
# print(y)

# -----------------ادراک بالا را به پایین ابدیل کردیم comprehension

# x = [2,13,12,24,21,45,66]
# y = []
# فقط فرد
# z = [i for i in x if i % 2 != 0]
# print(z)
# -------------------------------------
# زوج و فرد
# x = [2,13,12,24,21,45,66]
# y = []

# for i in x:
#     y.append(i if i % 2 != 0 else 0)
# print(y)

# ------------------------------------
# یا بصورت تابع

# def bel(x):
#     if x % 2 != 0:
#         return x
#     else:
#         return 0
#
# x = [2,13,12,24,21,45,66]
#
# z = [bel(j) for j in x]
# print(z)

# ------------------------------------
#
# from random import randrange
# def func():
#     return randrange(50,150)
# x = func()
# x = [n for _ in range(10) if (n := func()) > 100]
# print(x)

# ------------------------------رکیبی از ادراک و لیست و دیکشنری--------------------

# names = ["reza","ali","sarah","fate"]
#
# d = {name : [0 for _ in range(5)] for name in names}
# print(d)

# یا

# names = ["reza","ali","sarah","fate"]
#
# d = {name : [i for i in range(5)] for name in names}
# print(d)

# --------------------------------------------
# encoing and decoding
# Ascii and unicode

# x = "A"

# print(ord("n"))
# print(bin(110))

# ------------------------------------

# name1 = bytes("abolfazl&$", "utf-8")
# name2 = bytes("abolfazl&$", "utf-16")
# name3 = bytes("abolfazl&$", "acscii")
# print(name.decode("utf-8"))
# print(name1)
# print(name2)
# print(name3)

# --------------------------------------
# name = bytes([1,2,4,9,18,20])
# print(name)

# --------------------------متد های داده رشته--------------------------------
# print(dir(str))
# -------------casefold------------------

# s = "ABOLFAZL YOUSEFI"
# print(s.lower())
# print(s.casefold())

# ------------------center----------------------
# طول کاراکتر ها را مشخص میکند
# s = "Abolfazl"
# print(s.center(14 , "-"))
# -------------------count---------------------------
# تعداد کاراکتر های خاص را در یک حمله یا اسم را میشمارد مثلا تغداد a
# s = "abolfazl yosefi"
# print(s.count("a"))
# -------------------encode---------------------------
# راساس بایت ها کلمه را نشان میدهد واگر حمله ای عجیب یا از زبان متفاوت باشد کد های آن را نشان میدهد
# s = "abolfazl"
# print(s.encode("utf-8"))
# ------------------expandtabs--------------------------
# expandtabs کارش اینه که اسپیس ها را جایگذین تب ها بکند
# s = "Abolfazl\tyousefi\t01"
# print(s)
# print(s.expandtabs(4))
# print(s.expandtabs(20))
# -----------------------format_map---------------------------
# x = {"your first name":"Abolfazl" ,"your last name":"yousefi"}
# print("my name is {your first name} {your last name}".format_map(x))
# s = "Abolfazl yousefi"
# print(s)
# -------------------------------index-----------------------------
# index یک کاراکتر را در یک جمله به ما میدهد
# s = "Abolfazl"
# print(s)
# print(s.index("a"))
# print(s.find("y"))
# --------------isalpha--------------------
# s = "abplfazl yousefi"
# print(s.isalpha())
# نکته:اسپیس جزو حروف الفبا نیست
# -----------------isascii----------------------
# print(s.isascii())
# s = "abplfazl yousefi"
# -----------------isdecimal---------------------
# s = "0987668"
# print(s.isdecimal())
# بررسی میکند که آیا همه اعداد صفر تا 9 هستند یا نه
# ------------------------------------------------
# s = "087668"
# print(s.isdecimal())
# print(s.isnumeric())
# print(s.isdigit())
# بررسی میکند که آیا همه کاراکتر ها عدد هستند یا نه
# ------------------------isidentifier------------------------
# اگر اسمی که ما وارد میکنیم برای نام گذاری متغیر ها مجاز باشد True برمیگرداند و برعکس
# s = "x_69"
# print(s)
# print(s.isidentifier())
# ----------------------------islower------------------------------
# بررسی این که ایا همه کاراکتر های استفاده شده حرف کوچک هستند یانه

# s = "xsijddikjddwiuddc"
# print(s)
# print(s.islower())
# ----------------------isprintable-------------------------
# بررسی اینکه ایا همه کاراکتر های ما چاپ میشود یانه

# s = "xsijddikjddwiuddc"
# print(s)
# print(s.islower())
# ------------------------isspace----------------------------
# نکته: هم اسپبیس ها و هم بک اسلش ان و بک اسلش تی را برای ما ترو برمیگرداند برای شناسایی فضا های خالی به کار میرود
# s = "    "
# print(s)
# print(s.isspace())
# -------------------------istitle------------------------
# حرف اول تمام کلمات را به حروف بزرگ تبدیل میکند اگر حرف بزرگ باشد True رت برمیگرداند
# s = "abolfazl yousefi 01 actevete"
# print(s)
# print(s.title())
# ----------------------ljust-------------------------------
# کلمه را به سمت چپ میبرد
# s = "abolfazl"
# print(s)
# print(s.ljust(20,"-"))
# ------------------------rjust--------------------------------
# کلمه را به سمت راست میبرد
# s = "abolfazl"
# print(s)
# print(s.ljust(20,"-"))
# ----------------------------maketrans--------------------------------
# کارش ترجمه کردن است
# s = "abolfazlooo"
# table = str.maketrans("o", "w", "a")
# print(s)
# print(table)
# print(s.translate(table))

# یه جور دیگه

# d = {"b" : "*_*", "f": "+=+"}
# s = "abolfazl"
# table = str.maketrans(d)
# print(s)
# print(table)
# print(s.translate(table))

# ---------------------------partition----------------------------
# هر کاراکتری را که ما بخواهیم ومشخص کنیم برای ما در وسط چاپ میکند وبه صورت جدا گانه اینکار را انجام میدهد
# s = "abolfazl 01 yousefi"
# print(s)
# print(s.partition("l"))
# -----------------------------------------------------------------
# یا اگر بخواهیم این کار را از سمت راست اولین کاراکتر انجام دهیم
# s = "abolfazl 01 yousefi"
# print(s)
# print(s.rpartition("l"))
# -------------------------------removeprefix-----------------------------
# حذف پیشوند از ابتدای رشته

# s = "-------abolfazl 01 yousefi"
# print(s)
# print(s.removeprefix("---"))

# --------------------------------removesuffix----------------------------------
# حذف پسوند از انتهای رشته

# s = "-------abolfazl 01 yousefi"
# print(s)
# print(s.removesuffix("fi"))

# --------------------------تفاوت حذف پسوند و پیشوند با lstrip---------------------------
# از چپ همه را حذف میکند بدون درنظر گرفتن تعداد
# s = "-------====abolfazl1111 01 yousefi"
# print(s)
# print(s.lstrip("- , = , abolfazl"))

# ---------------------------------یا مثلا پایینی هم همینگونه است rstrip-------------------------
# از راست همه را حذف میکند بدون درنظر گرفتن تعداد

# s = "-------abolfazl 01 yousefi"
# print(s)
# print(s.rstrip("fi"))

# -------------------------split------------------------
#  رشته را تبدیل به لیست هایی با کوتیشن جدا جدا میکند و مشخص میکند که با چه چیزی باید جدا شود لیست ما
# s = "abolfazl , yousefi , python , 01"
# print(s)
# print(s.split(","))

# -------------------------rsplit که از سمت راست جدا میکند-----------------------------
# نکته : همچنین مینوانیم تعداد عناصری را هم که میخواهیم چدا کنیم را بدهیم
# s = "abolfazl , yousefi , python , 01"
# print(s)
# print(s.rsplit(",", 1))
# الا در بالا یک عنصر از سمت راست جدا شده و بقیه در عنصری دیگر با هم هستند این موضوع برای strip هم صدق میکند

# -----------------------------------splitlines جدا سازی را بر اساس بک اسلش ان انجام میدهد   --------------------------
# دقت کن اون هایی که رفتن پایین یک عنصر جدا به حساب می آیند
# s = "abolfazl  yousefi\npython\n01"
# print(s)
# print(s.splitlines())

# ------------------------------swapcase تمام حروف کوچک را به بزرگ و بزرگ را به کوچک تبدیل میکند-------------------------------

# s = "Abolfazl Yousefi Python 01"
# print(s)
# print(s.swapcase())

#-----------------------------------zfill کارش اینه که یک رشته عددی را قبلش را اگر چیزی نداشته باشد با صفر پر میکند---------------------------------

# s = "3"
# print(s)
# print(s.zfill(5))

# ----------------------------------******************----------------------------------------

# -------------------------------------in the name of god-------------------------------------

# ------------------------------------شروع فصل 8 ماژول ها--------------------------------------

# ----------------------------------******************----------------------------------------

# کل فصل 8 درمورد ساخت ماژول های اختصاصی است

# import datetime
# print(datetime.date.today())
# ------------------------------------------------------

# import numpy as np
#
# print(np.__version__)

# import sys
#
# print(sys.executable)
# print(sys.version)


# import numpy
# print("OK")
# ----------------------
# 1
# import numpy.random
#
# print(numpy.random.rand())

# ---------------یا---------------------
# 2
# import numpy.random as abo
#
# print(abo.rand())

# --------------------یا----------------
# 3
# from numpy.random import rand
#
# print(rand())

# ------------------یا--------------------
# 4
# from numpy.random import rand as abl
#
# print(abl())
#------------------------------------------

# برای چاپ کردن آدرس ومسیر برای پروژه ها

# import sys
#
# for i in sys.path:
#     print(i)
# print("*" * 60)

# --------------------------------------------------


# btn3 = types.KeyboardButton("گزارش مشکل در ربات")
# btn4 = types.KeyboardButton("ثبت نظرات, پیشنهادات و انتقادات")
# btn5 = types.KeyboardButton("ارتباطی با ما")
# btn6 = types.KeyboardButton("تنظیمات")


































































































































































































































































