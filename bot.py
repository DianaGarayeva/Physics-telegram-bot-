import telebot
from telebot import types
bot = telebot.TeleBot('8341311059:AAGMOhs6HqQiQt-jge_H6HRTljdfGecD6xQ')

help_file = open('help.txt', 'r') # ! File with help information
help_text = help_file.read() 



@bot.message_handler(commands=['start']) # ! /start
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Help", callback_data='help') # button for helping information
    btn2 = types.InlineKeyboardButton("Go to the main menu", callback_data='main_menu') # button for main menu
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id," Hello, let\'s start to study physics with I_like_physics_bot", reply_markup=markup)


@bot.message_handler(commands=['help']) # ! Help information
def help_cmd(message): 
    global help_text
    bot.send_message(message.chat.id, help_text, parse_mode='HTML') 



@bot.message_handler(commands=['menu'])  # ! Main menu
def menu_cmd(message):
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



@bot.message_handler(func=lambda message: message.text == "Plan for self study") # TODO How to add command to ReplyKeyboardButton

def plan_button(message): # ! Plan
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Start self study", callback_data="start_self_study") # button to start self study
    markup.add(btn)
    bot.send_message(message.chat.id, "See the plan for self study", reply_markup=markup)


def start_self_study_cmd(message): # !Start self study
    bot.send_message(message.chat.id, "Let's start")



@bot.callback_query_handler(func=lambda callback: True)
def callbacks(callback):
    if callback.data == "main_menu":
        menu_cmd(callback.message)
    elif callback.data == "help":
        help_cmd(callback.message)


        

bot.polling(non_stop=True)

help_file.close()
