import telebot
from telebot.types import InlineKeyboardButton
from .. import models
from . import keyboard as kb

TOKEN = "5996914631:AAEsGlNv2tG23PsX9THjkT_09Rv3ZRFEEm0"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

MethodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates'.format(token=TOKEN)


def is_sender(message_id, sender_id):
    if message_id == sender_id:
        return True
    else:
        return False
    
def already_exists(id):
    try:
        user = models.MyUser.objects.get(chat_id = id)
        print (user)
        return True
    except models.MyUser.DoesNotExist:
        return False
    

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    text = "привет! для того, чтобы зарегистрироваться или войти, отправьте свой номер телефона"
    bot.send_message(message.chat.id, text, reply_markup=kb.send_markup)


@bot.message_handler(content_types=["contact"])
def handle_contact(message):
    if is_sender(message.chat.id, message.contact.user_id):
        if already_exists(message.contact.user_id):
            text = "вы уже зарегистрированы! для входа на сайт перейдите по ссылке:"
        else:
            user = models.MyUser(
                username = " ".join(message.contact.first_name, message.contact.last_name) \
                    if message.contact.last_name != None \
                    else message.contact.first_name,
                chat_id=message.chat.id, 
                phone_number=message.contact.phone_number
            )
            user.save()
            text = "вы успешно зарегистрированы. для входа на сайт перейдите по ссылке:"
        
        log_button = InlineKeyboardButton('войти', callback_data='log_btn', url=f'http://127.0.0.1:8000/login/{message.chat.id}/')
        markup = telebot.types.InlineKeyboardMarkup().row(log_button)
    else: 
        text = "вы не можете зарегистрироваться или войти за другого человека ;)"
        markup = kb.ReplyKeyboardRemove()

    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(content_types=["text"])
def default_response(message):
    text = "пожалуйста, воспользуйтесь командами /start или /help для запуска бота"
    bot.send_message(message.chat.id, text, reply_markup=kb.ReplyKeyboardRemove())


def run():
    bot.infinity_polling()
    
