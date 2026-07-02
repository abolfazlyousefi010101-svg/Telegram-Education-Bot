from telebot import types

# =========================
# Reply Keyboard
# =========================

markup_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)

markup_fos = types.ReplyKeyboardMarkup(resize_keyboard=True)

markup_base = types.ReplyKeyboardMarkup(resize_keyboard=True)

markup_question = types.ReplyKeyboardMarkup(resize_keyboard=True)

markup_konkur = types.ReplyKeyboardMarkup(resize_keyboard=True)

# =========================
# Reply Buttons
# =========================

btn_learning = types.KeyboardButton("شروع یادگیری")
btn_ai_teacher = types.KeyboardButton("معلم خصوصی هوشمند")

btn_tajrobi = types.KeyboardButton("تجربی")
btn_riazi = types.KeyboardButton("ریاضی")
btn_ensani = types.KeyboardButton("انسانی")

btn_base10 = types.KeyboardButton("دهم")
btn_base11 = types.KeyboardButton("یازدهم")
btn_base12 = types.KeyboardButton("کنکوری(دوازدهم)")

btn_question1 = types.KeyboardButton("سوالات کنکور و مشابه آن")
btn_question2 = types.KeyboardButton("سوالات امتحان نهایی و مشابه آن")

btn_back = types.KeyboardButton("🔙 بازگشت")

# =========================
# Add Buttons
# =========================

markup_btn.add(btn_learning)
markup_btn.add(btn_ai_teacher)

markup_fos.add(btn_tajrobi, btn_riazi)
markup_fos.add(btn_ensani)
markup_fos.row(btn_back)

markup_base.add(btn_base10)
markup_base.add(btn_base11)
markup_base.add(btn_base12)
markup_base.row(btn_back)

markup_question.add(btn_question1)
markup_question.add(btn_question2)
markup_question.row(btn_back)

markup_konkur.add(btn_question1)
markup_konkur.row(btn_back)

# =========================
# Inline Keyboard
# =========================

markup_dars = types.InlineKeyboardMarkup()

btn_zist = types.InlineKeyboardButton("زیست", callback_data="zist")
btn_shimi = types.InlineKeyboardButton("شیمی", callback_data="shimi")
btn_riazi_inline = types.InlineKeyboardButton("ریاضی", callback_data="riazi")
btn_fizik = types.InlineKeyboardButton("فیزیک", callback_data="fizik")

markup_dars.row(btn_zist, btn_shimi)
markup_dars.row(btn_riazi_inline, btn_fizik)















