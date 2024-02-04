import telebot
from telebot.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove


# регистрация и авторизация
send_contact_button = KeyboardButton('отправить номер телефона', request_contact=True)
send_markup = telebot.types.ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).row(send_contact_button)

# ссылка для входа
log_button = InlineKeyboardButton('войти', callback_data='log_btn', url='http://127.0.0.1:8000/message/')
login_markup = telebot.types.InlineKeyboardMarkup().row(log_button)