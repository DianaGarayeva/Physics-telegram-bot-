import telebot
from telebot import types




bot = telebot.TeleBot('8341311059:AAGMOhs6HqQiQt-jge_H6HRTljdfGecD6xQ')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Help", callback_data='help')
    btn2 = types.InlineKeyboardButton("Go to the main menu", callback_data='main_menu')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id," Hello, let\'s start to study physics with I_like_physics_bot", reply_markup=markup)



@bot.message_handler(commands=['help'])
def help_cmd(message): # ! Help information
    bot.send_message(message.chat.id, 'Help information') 



@bot.message_handler(commands=['menu'])
def menu_cmd(message): # ! Main menu
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Plan for self study")
    btn2 = types.KeyboardButton("All sections")
    btn3 = types.KeyboardButton("Quiz")
    btn4 = types.KeyboardButton("My achievements")
    btn5 = types.KeyboardButton("Send a message")
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5)
    bot.send_message(message.chat.id, "Choose the option", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callbacks(callback):
    if callback.data == "main_menu":
        menu_cmd(callback.message)
    if callback.data == "help":
        help_cmd(callback.message)

bot.polling(non_stop=True)

