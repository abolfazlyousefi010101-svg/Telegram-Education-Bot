
# ورودی تلگرام

import telebot
import json
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# =========================
# Token
# =========================
import os

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

# =========================
# ذخیره اطلاعات کاربران
# =========================

user_data = {}

# =========================
# بخش دیکشنری
# =========================

# برای زیست

zist = {
    "دهم": [
        "فصل ۱",
        "فصل ۲",
        "فصل ۳",
        "فصل ۴",
        "فصل ۵",
        "فصل ۶",
        "فصل ۷"
    ],

    "یازدهم": [
        "فصل ۱",
        "فصل ۲",
        "فصل ۳",
        "فصل ۴",
        "فصل ۵",
        "فصل ۶",
        "فصل ۷",
        "فصل ۸",
        "فصل ۹"
    ],

    "دوازدهم": [
        "فصل ۱",
        "فصل ۲",
        "فصل ۳",
        "فصل ۴",
        "فصل ۵",
        "فصل ۶",
        "فصل ۷",
        "فصل ۸"
    ]
}

# برای شیمی

shimi = {
    "دهم": [
        "فصل ۱",
        "فصل ۲",
        "فصل ۳"
    ],

    "یازدهم": [
        "فصل ۱",
        "فصل ۲",
        "فصل ۳"
    ],

    "دوازدهم": [
        "فصل ۱",
        "فصل ۲",
        "فصل ۳"
    ]
}

# برای ریاضی

riazi = {

    "دهم": [
        "آنالیز (شمارش بدون شمردن)",
        "معادلات و نامعادلات درجه دوم",
        "تابع نمایی و لگاریتم",
        "تابع قدرمطلق و جزء صحیح",
        "هندسه تحلیلی",
        "مجموعه، الگو و دنباله",
        "هندسه",
        "پیوستگی",
        "آمار"
    ],

    "یازدهم": [
        "آنالیز (شمارش بدون شمردن)",
        "معادلات و نامعادلات درجه دوم",
        "تابع نمایی و لگاریتم",
        "تابع قدرمطلق و جزء صحیح",
        "هندسه تحلیلی",
        "مجموعه، الگو و دنباله",
        "هندسه",
        "پیوستگی",
        "آمار"
    ],

    "دوازدهم": [
        "توابع",
        "مثلثات",
        "حد",
        "مشتق",
        "کاربرد مشتق",
        "هندسه",
        "احتمال"
    ]
}

# برای فیزیک

fizik = {
    "دهم": [
        "فصل ۱",
        "فصل ۲",
        "فصل ۳",
        "فصل ۴"
    ],

    "یازدهم": [
        "فصل ۱",
        "فصل ۲",
        "فصل ۳"
    ],

    "دوازدهم": [
        "فصل ۱",
        "فصل ۲",
        "فصل ۳",
        "فصل ۴"
    ]
}

# -------------------------------------------------
# گفتار های زیست
# -------------------------------------------------

zist_goftar_10 = {"فصل ۱": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۲": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۳": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۴": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۵": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۶": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۷": ["گفتار ۱","گفتار ۲","گفتار ۳"],}

zist_goftar_11 = {"فصل ۱": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۲": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۳": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۴": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۵": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۶": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۷": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۸": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۹": ["گفتار ۱","گفتار ۲","گفتار ۳"],}


zist_goftar_12 = {"فصل ۱": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۲": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۳": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۴": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۵": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۶": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۷": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۸": ["گفتار ۱","گفتار ۲","گفتار ۳"],}

# -------------------------------------------------
# مباحث شیمی
# -------------------------------------------------
shimi_mabhas_10 = {"فصل ۱": ["مبحث ۱","مبحث ۲","مبحث ۳","مبحث ۴"],
"فصل ۲": ["مبحث ۱","مبحث ۲","مبحث ۳","مبحث ۴"],
"فصل ۳": ["مبحث ۱","مبحث ۲","مبحث ۳","مبحث ۴"],}



shimi_mabhas_11 = {"فصل ۱": ["مبحث ۱","مبحث ۲","مبحث ۳","مبحث ۴"],
"فصل ۲": ["مبحث ۱","مبحث ۲","مبحث ۳","مبحث ۴"],
"فصل ۳": ["مبحث ۱","مبحث ۲","مبحث ۳","مبحث ۴"],}



shimi_mabhas_12 = {"فصل ۱": ["مبحث ۱","مبحث ۲","مبحث ۳","مبحث ۴"],
"فصل ۲": ["مبحث ۱","مبحث ۲","مبحث ۳","مبحث ۴"],
"فصل ۳": ["مبحث ۱","مبحث ۲","مبحث ۳","مبحث ۴"],}



# -------------------------------------------------
# مباحث ریاضی
# -------------------------------------------------
riazi_mabhas_10 = {"آنالیز (شمارش بدون شمردن)": [
    "مبحث ۱",
    "مبحث ۲",
    "مبحث ۳"
],

"معادلات و نامعادلات درجه دوم": [
    "مبحث ۱",
    "مبحث ۲"
],

"تابع نمایی و لگاریتم": [
    "مبحث ۱",
    "مبحث ۲"
],

"تابع قدرمطلق و جزء صحیح": [
    "مبحث ۱",
    "مبحث ۲"
],

"هندسه تحلیلی": [
    "مبحث ۱",
    "مبحث ۲"
],

"مجموعه، الگو و دنباله": [
    "مبحث ۱",
    "مبحث ۲"
],

"هندسه": [
    "مبحث ۱",
    "مبحث ۲"
],

"پیوستگی": [
    "مبحث ۱",
    "مبحث ۲"
],

"آمار": [
    "مبحث ۱",
    "مبحث ۲"
],}


riazi_mabhas_11 = {"آنالیز (شمارش بدون شمردن)": [
    "مبحث ۱",
    "مبحث ۲",
    "مبحث ۳"
],

"معادلات و نامعادلات درجه دوم": [
    "مبحث ۱",
    "مبحث ۲"
],

"تابع نمایی و لگاریتم": [
    "مبحث ۱",
    "مبحث ۲"
],

"تابع قدرمطلق و جزء صحیح": [
    "مبحث ۱",
    "مبحث ۲"
],

"هندسه تحلیلی": [
    "مبحث ۱",
    "مبحث ۲"
],

"مجموعه، الگو و دنباله": [
    "مبحث ۱",
    "مبحث ۲"
],

"هندسه": [
    "مبحث ۱",
    "مبحث ۲"
],

"پیوستگی": [
    "مبحث ۱",
    "مبحث ۲"
],

"آمار": [
    "مبحث ۱",
    "مبحث ۲"
],}


riazi_mabhas_12 = {"توابع": ["مبحث ۱","مبحث ۲","مبحث ۳"],
"مثلثات": ["مبحث ۱","مبحث ۲"],
"حد": ["مبحث ۱","مبحث ۲"],
"مشتق": ["مبحث ۱","مبحث ۲","مبحث ۳"],
"کاربرد مشتق": ["مبحث ۱","مبحث ۲"],
"هندسه": ["مبحث ۱","مبحث ۲"],
"احتمال": ["مبحث ۱","مبحث ۲"],}


# -------------------------------------------------
# مباحث فیزیک
# -------------------------------------------------
fizik_mabhas_10 = {"فصل ۱": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۲": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۳": ["گفتار ۱","گفتار ۲","گفتار ۳"],
"فصل ۴": ["گفتار ۱","گفتار ۲","گفتار ۳"],}


fizik_mabhas_11 = {"فصل ۱": ["گفتار ۱","گفتار ۲"],
"فصل ۲": ["گفتار ۱","گفتار ۲"],
"فصل ۳": ["گفتار ۱","گفتار ۲"],}


fizik_mabhas_12 = {"فصل ۱": ["گفتار ۱","گفتار ۲"],
"فصل ۲": ["گفتار ۱","گفتار ۲"],
"فصل ۳": ["گفتار ۱","گفتار ۲"],
"فصل ۴": ["گفتار ۱","گفتار ۲"],}


# -------------------------------------------------
dars_data = {

    "zist": zist,
    "shimi": shimi,
    "riazi": riazi,
    "fizik": fizik
    }


# --------------------------------------------------

base_number = {
    "دهم": "10",
    "یازدهم": "11",
    "دوازدهم": "12"
}

# --------------------------------------------------
goftar_data = {
    "zist10": zist_goftar_10,
    "zist11": zist_goftar_11,
    "zist12": zist_goftar_12,
    "shimi10": shimi_mabhas_10,
    "shimi11": shimi_mabhas_11,
    "shimi12": shimi_mabhas_12,
    "riazi10": riazi_mabhas_10,
    "riazi11": riazi_mabhas_11,
    "riazi12": riazi_mabhas_12,
    "fizik10": fizik_mabhas_10,
    "fizik11": fizik_mabhas_11,
    "fizik12": fizik_mabhas_12
}

# --------------------------------


# -------------------------------
# توابع و حلقه ها
# -------------------------------
def make_inline_keyboard(items):
    keyboard = InlineKeyboardMarkup()
    for item in items:
        keyboard.add(InlineKeyboardButton(item,callback_data=item))
    return keyboard


def load_questions(file_name):
    with open(f"data/{file_name}", "r", encoding="utf-8") as file:
        return json.load(file)





# =========================
# Reply Keyboard
# =========================

markup_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)

markup_fos = types.ReplyKeyboardMarkup(resize_keyboard=True)

markup_base = types.ReplyKeyboardMarkup(resize_keyboard=True)

markup_question = types.ReplyKeyboardMarkup(resize_keyboard=True)

markup_konkur = types.ReplyKeyboardMarkup(resize_keyboard=True)

# =========================
# دکمه های Reply Keyboard
# =========================

btn1 = types.KeyboardButton("شروع یادگیری")
btn2 = types.KeyboardButton("معلم خصوصی هوشمند")

fos1 = types.KeyboardButton("تجربی")
fos2 = types.KeyboardButton("ریاضی")
fos3 = types.KeyboardButton("انسانی")

base1 = types.KeyboardButton("دهم")
base2 = types.KeyboardButton("یازدهم")
base3 = types.KeyboardButton("کنکوری(دوازدهم)")

question1 = types.KeyboardButton("سوالات کنکور و مشابه آن")
question2 = types.KeyboardButton("سوالات امتحان نهایی و مشابه آن")
# =========================
#   add Reply Keyboard
# =========================

markup_btn.add(btn1)
markup_btn.add(btn2)

markup_fos.add(fos1, fos2)
markup_fos.add(fos3)

markup_base.add(base1)
markup_base.add(base2)
markup_base.add(base3)

markup_question.add(question1)
markup_question.add(question2)

markup_konkur.add(question1)

# =========================
# کیبورد نوع 2
# =========================

markup_dars = InlineKeyboardMarkup()
# نکتهکیبورد های مربوط به انتخاب درس ها در قسمت مربوط به پاسخ به دکمه های روی صفحه قرار دارند


# =========================
# Inline Keyboard
# =========================
btn_zist = InlineKeyboardButton("زیست",callback_data="zist")

btn_shimi = InlineKeyboardButton("شیمی",callback_data="shimi")

btn_riazi = InlineKeyboardButton("ریاضی",callback_data="riazi")

btn_fizik = InlineKeyboardButton("فیزیک",callback_data="fizik")
# =========================
# ضافه کردن دکمه به Inline Keyboard
# =========================

markup_dars.row(btn_zist, btn_shimi)
markup_dars.row(btn_riazi, btn_fizik)

# =========================
# شروع ربات
# =========================

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"سلام به ربات درس یار خوش آمدید.\nچطور می‌توانم کمکتان کنم؟",reply_markup=markup_btn)

# =========================
# شروع یادگیری
# =========================

@bot.message_handler(func=lambda message: message.text == "شروع یادگیری")
def learning(message):
    bot.send_message(message.chat.id,"لطفاً رشته تحصیلی خود را انتخاب کنید.",reply_markup=markup_fos)

# =========================
# انتخاب رشته
# =========================

@bot.message_handler(func=lambda message: message.text == "تجربی")
def tajrobi(message):

    user_data[message.chat.id] = {}

    user_data[message.chat.id]["fos"] = "تجربی"

    bot.send_message(message.chat.id,"لطفاً پایه تحصیلی خود را انتخاب کنید.",reply_markup=markup_base)


@bot.message_handler(func=lambda message: message.text == "ریاضی")
def riazi_field(message):

    user_data[message.chat.id] = {}

    user_data[message.chat.id]["fos"] = "ریاضی"

    bot.send_message(message.chat.id,"لطفاً پایه تحصیلی خود را انتخاب کنید.",reply_markup=markup_base)


@bot.message_handler(func=lambda message: message.text == "انسانی")
def ensani(message):

    user_data[message.chat.id] = {}

    user_data[message.chat.id]["fos"] = "انسانی"

    bot.send_message(message.chat.id,"لطفاً پایه تحصیلی خود را انتخاب کنید.",reply_markup=markup_base)

# =========================
# انتخاب پایه
# =========================

@bot.message_handler(func=lambda message: message.text == "دهم")
def ten(message):

    user_data[message.chat.id]["base"] = "دهم"

    bot.send_message(message.chat.id,"روی گزینه موجود در منو ضربه بزن.",reply_markup=markup_konkur)


@bot.message_handler(func=lambda message: message.text == "یازدهم")
def eleven(message):
    user_data[message.chat.id]["base"] = "یازدهم"
    bot.send_message(message.chat.id,"یکی از گزینه‌های زیر را انتخاب کنید.",reply_markup=markup_question)


@bot.message_handler(func=lambda message: message.text == "کنکوری(دوازدهم)")
def twelve(message):
    user_data[message.chat.id]["base"] = "دوازدهم"
    bot.send_message(message.chat.id,"یکی از گزینه‌های زیر را انتخاب کنید.",reply_markup=markup_question)

# =========================
# انتخاب نوع سوال
# =========================

@bot.message_handler(func=lambda message: message.text == "سوالات کنکور و مشابه آن")
def question(message):

    bot.send_message(message.chat.id,"لطفاً درس مورد نظر را انتخاب کنید.",reply_markup=markup_dars)

# =========================
# پاسخ به دکمه های روی صفحه
# =========================

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data in dars_data:

        user_data[call.message.chat.id]["dars"] = call.data

        base = user_data[call.message.chat.id]["base"]

        markup = make_inline_keyboard(dars_data[call.data][base])

        bot.send_message(call.message.chat.id,"لطفاً یکی از گزینه‌های زیر را انتخاب کنید:",reply_markup=markup)


    elif call.data.startswith("فصل") or call.data.startswith("آنالیز") or call.data.startswith("معادلات") or call.data.startswith("تابع") or call.data.startswith("هندسه") or call.data.startswith("پیوستگی") or call.data.startswith("آمار") or call.data.startswith("مثلثات") or call.data.startswith("حد") or call.data.startswith("مشتق") or call.data.startswith("کاربرد") or call.data.startswith("احتمال"):

        dars = user_data[call.message.chat.id]["dars"]
        base = user_data[call.message.chat.id]["base"]
        user_data[call.message.chat.id]["chapter"] = call.data

        key = dars + base_number[base]

        markup = make_inline_keyboard(goftar_data[key][call.data])

        bot.send_message(call.message.chat.id,"یکی از گزینه‌های زیر را انتخاب کنید:",reply_markup=markup)

    else:

        dars = user_data[call.message.chat.id]["dars"]
        base = user_data[call.message.chat.id]["base"]
        user_data[call.message.chat.id]["goftar"] = call.data

        bot.send_message(
            call.message.chat.id,
            f"""
درس : {dars}

پایه : {base}

بخش انتخاب شده :

{call.data}
"""
        )

print("Bot started")

bot.infinity_polling()






























































