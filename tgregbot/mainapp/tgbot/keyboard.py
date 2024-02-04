import telebot
from telebot.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove

# начальное сообщение:
reg_button = InlineKeyboardButton('регистрация', callback_data='reg_btn')
log_button = InlineKeyboardButton('вход', callback_data='log_btn')
start_markup = telebot.types.InlineKeyboardMarkup().row(reg_button, log_button)

# регистрация
send_contact_button = KeyboardButton('отправить номер телефона', request_contact=True)
reg_markup = telebot.types.ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).row(send_contact_button)