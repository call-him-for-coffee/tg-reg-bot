import telebot
from telebot import types
from .. import models
from . import keyboard as kb


bot = telebot.TeleBot("5996914631:AAEsGlNv2tG23PsX9THjkT_09Rv3ZRFEEm0", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    text = "привет! выбери, что хочешь сделать:"
    bot.send_message(message.chat.id, text, reply_markup=kb.start_markup)


@bot.callback_query_handler(func=lambda c: c.data == 'reg_btn')
def reg_callback(callback_query: types.CallbackQuery):
    text = "для того, чтобы зарегистрироваться, отправь свой номер телефона"
    bot.answer_callback_query(callback_query.id)
    bot.send_message(callback_query.from_user.id, text, reply_markup=kb.reg_markup)


def is_sender(message, sender_id):
    if message.chat.id == sender_id:
        return True
    else:
        return False


@bot.message_handler(content_types=["contact"])
def registration(message):
    if is_sender(message, message.contact.user_id):
        text = "классная аватарка!"
        user = models.User(chat_id=message.chat.id, phone_number=message.contact.phone_number)
        user.save()
        print(user)
    else:
        text = "вы не можете зарегистрировать другого человека ;)"

    bot.send_message(message.chat.id, text, reply_markup=kb.ReplyKeyboardRemove())


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text, reply_markup=kb.ReplyKeyboardRemove())


def run():
    bot.infinity_polling()
