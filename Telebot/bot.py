import sqlite3
import config
import telebot
from telebot import types
token = config.token
conn = sqlite3.connect('mydatabase.db', check_same_thread=False)
cursor = conn.cursor()
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def category(message):
    keyboard_category = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_1_1 = types.KeyboardButton('Skoda')
    key_1_2 = types.KeyboardButton('Opel')
    key_1_3 = types.KeyboardButton('Volkswagen')
    key_1_4 = types.KeyboardButton('BMW')
    keyboard_category.add(key_1_1)
    keyboard_category.add(key_1_2)
    keyboard_category.add(key_1_3)
    keyboard_category.add(key_1_4)

    bot.reply_to(message, "Привіт, яка марка автомобіля Вас цікавить?", reply_markup=keyboard_category)


@bot.message_handler(content_types=['text'])
def subcategory(message):
    if message.text == "Skoda":
        keyboard_subcategory = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_2_1 = types.KeyboardButton('Fabia')
        key_2_2 = types.KeyboardButton('Octavia')
        keyboard_subcategory.add(key_2_1)
        keyboard_subcategory.add(key_2_2)

        msg = bot.send_message(message.chat.id, 'Виберіть модель', reply_markup=keyboard_subcategory)
        bot.register_next_step_handler(msg, subcategory2)

    elif message.text == "Opel":
        keyboard_subcategory = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_2_1 = types.KeyboardButton('Astra J')
        key_2_2 = types.KeyboardButton('Insignia')
        keyboard_subcategory.add(key_2_1)
        keyboard_subcategory.add(key_2_2)

        msg = bot.send_message(message.chat.id, 'Виберіть модель', reply_markup=keyboard_subcategory)
        bot.register_next_step_handler(msg, subcategory2)

    elif message.text == "Volkswagen":
        keyboard_subcategory = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_2_1 = types.KeyboardButton('Golf VI')
        key_2_2 = types.KeyboardButton('Golf VII')
        key_2_3 = types.KeyboardButton('Passat B7')
        keyboard_subcategory.add(key_2_1)
        keyboard_subcategory.add(key_2_2)
        keyboard_subcategory.add(key_2_3)

        msg = bot.send_message(message.chat.id, 'Виберіть модель', reply_markup=keyboard_subcategory)
        bot.register_next_step_handler(msg, subcategory2)

    elif message.text == "BMW":
        keyboard_subcategory = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_2_1 = types.KeyboardButton('320')
        key_2_2 = types.KeyboardButton('318')
        keyboard_subcategory.add(key_2_1)
        keyboard_subcategory.add(key_2_2)

        msg = bot.send_message(message.chat.id, 'Виберіть модель', reply_markup=keyboard_subcategory)
        bot.register_next_step_handler(msg, subcategory2)

def subcategory2(message):

    if message.text == "Fabia":
        keyboard_subcategory2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Elegance')
        key_3_2 = types.KeyboardButton('Ambition')
        key_3_3 = types.KeyboardButton('Style')
        keyboard_subcategory2.add(key_3_1)
        keyboard_subcategory2.add(key_3_2)
        keyboard_subcategory2.add(key_3_3)

        msg = bot.send_message(message.chat.id, 'Яка комплектація Вас цікавить', reply_markup=keyboard_subcategory2)
        bot.register_next_step_handler(msg, subcategory3)

    elif message.text == "Octavia":
        keyboard_subcategory2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Elegance')
        key_3_2 = types.KeyboardButton('Ambition')
        key_3_3 = types.KeyboardButton('Style')
        keyboard_subcategory2.add(key_3_1)
        keyboard_subcategory2.add(key_3_2)
        keyboard_subcategory2.add(key_3_3)

        msg = bot.send_message(message.chat.id, 'Яка комплектація Вас цікавить', reply_markup=keyboard_subcategory2)
        bot.register_next_step_handler(msg, subcategory3)

    elif message.text == "Astra J":
        keyboard_subcategory2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Enjoi')
        key_3_2 = types.KeyboardButton('Sports Tourer')
        key_3_3 = types.KeyboardButton('Cosmo')
        keyboard_subcategory2.add(key_3_1)
        keyboard_subcategory2.add(key_3_2)
        keyboard_subcategory2.add(key_3_3)

        msg = bot.send_message(message.chat.id, 'Яка комплектація Вас цікавить', reply_markup=keyboard_subcategory2)
        bot.register_next_step_handler(msg, subcategory3)

    elif message.text == "Insignia":
        keyboard_subcategory2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Enjoi')
        key_3_2 = types.KeyboardButton('Sports Tourer')
        key_3_3 = types.KeyboardButton('Cosmo')
        keyboard_subcategory2.add(key_3_1)
        keyboard_subcategory2.add(key_3_2)
        keyboard_subcategory2.add(key_3_3)

        msg = bot.send_message(message.chat.id, 'Яка комплектація Вас цікавить', reply_markup=keyboard_subcategory2)
        bot.register_next_step_handler(msg, subcategory3)

    elif message.text == "Golf VI":
        keyboard_subcategory2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Comfortline')
        key_3_2 = types.KeyboardButton('Highline')
        keyboard_subcategory2.add(key_3_1)
        keyboard_subcategory2.add(key_3_2)

        msg = bot.send_message(message.chat.id, 'Яка комплектація Вас цікавить', reply_markup=keyboard_subcategory2)
        bot.register_next_step_handler(msg, subcategory3)

    elif message.text == "Golf VII":
        keyboard_subcategory2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Comfortline')
        key_3_2 = types.KeyboardButton('Highline')
        keyboard_subcategory2.add(key_3_1)
        keyboard_subcategory2.add(key_3_2)

        msg = bot.send_message(message.chat.id, 'Яка комплектація Вас цікавить', reply_markup=keyboard_subcategory2)
        bot.register_next_step_handler(msg, subcategory3)

    elif message.text == "Passat B7":
        keyboard_subcategory2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Comfortline')
        key_3_2 = types.KeyboardButton('Highline')
        keyboard_subcategory2.add(key_3_1)
        keyboard_subcategory2.add(key_3_2)

        msg = bot.send_message(message.chat.id, 'Яка комплектація Вас цікавить', reply_markup=keyboard_subcategory2)
        bot.register_next_step_handler(msg, subcategory3)


    elif message.text == "320":
        keyboard_subcategory2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('xDrive')
        keyboard_subcategory2.add(key_3_1)

        msg = bot.send_message(message.chat.id, 'Яка комплектація Вас цікавить', reply_markup=keyboard_subcategory2)
        bot.register_next_step_handler(msg, subcategory3)

    elif message.text == "318":
        keyboard_subcategory2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('xDrive')
        keyboard_subcategory2.add(key_3_1)

        msg = bot.send_message(message.chat.id, 'Яка комплектація Вас цікавить', reply_markup=keyboard_subcategory2)
        bot.register_next_step_handler(msg, subcategory3)

#search the database
def subcategory3(message):

    sql = "SELECT * FROM car WHERE komplektacia=?"
    cursor.execute(sql, [(message.text)])
    finds = [[cursor.fetchall()]]
    bot.send_message(message.chat.id, finds)
    bot.send_message(message.chat.id, 'Більше інформації по телефону +380692694000')

bot.polling()