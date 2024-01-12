import telebot
import config
import utils

from telebot import types

from utils import completing_the_final_line
from utils import generate_basic_keyboard_buttons

bot = telebot.TeleBot(config.token)

summaru = ["Анкета"]
SummaImage = ""
finalString = ""

keyboardForm = types.InlineKeyboardMarkup()
keyboardForm = generate_basic_keyboard_buttons(keyboardForm)

@bot.message_handler(commands=['runTestKeyboa'])

def Running_a_keyboa_test(message):

    from keyboa import Keyboa

    menu = [["spam", "eggs"], ["ham", "bread"], "spam"]
    keyboard = Keyboa(items=menu)
    bot.send_message(message.chat.id, message.text, reply_markup=keyboard()) 

@bot.message_handler(commands=['runTest'])

def Running_a_bot_test(message):

    global summaru
    global SummaImage
    global keyboardForm
    global finalString

    #global url_button 
    summaru = ["Анкета", "Имя", "Максим", "Возраст", "29", "Пол", "Мужской", 
           "Место проживания (район, ст.метро)", "СПб, Колпино, Шушары",
           "Ваше позиционирование", "Низ", "Интересы, максимально подробно, что пробовал/а, чего хочется попробовать", 
           "Мои пожелания", "О себе", "Белый и пушистый", 
           "Семейное положение", "Свободен", "Кого ищу", "Верха", 
           "Контакт телеграмм (ник)", "Телега", "stop"]
    
    finalString = completing_the_final_line(summaru)

    summaru.clear()
    summaru = ["Анкета"]

    callback_button = types.InlineKeyboardButton(text="Опубликовать тестовую запись", callback_data="PressTestPublish")
    keyboardForm.add(callback_button)

    bot.send_message(message.chat.id, finalString, reply_markup=keyboardForm)

@bot.message_handler(content_types=['text'])

def assemble_txt_form(message): # Название функции не играет никакой роли, важно не повторяться

    global summaru
    global keyboardForm
    SumTxt = ""
    global finalString
    
    summaru.append(message.text)
    
    if message.text == "stop":  
        finalString = completing_the_final_line(summaru)

        summaru.clear()
        summaru = ["Анкета"]

        callback_button = types.InlineKeyboardButton(text="Опубликовать", callback_data="PressTestPublish")
        keyboardForm.add(callback_button)
    
        bot.send_message(message.chat.id, finalString, reply_markup=keyboardForm)

@bot.message_handler(content_types=['photo'])

def assemble_photo_form(message): # Название функции не играет никакой роли, важно не повторяться

    global keyboardForm
    SumTxt = ""
    global finalString

    file_id = message.photo[-1].file_id

    callback_button = types.InlineKeyboardButton(text="Опубликовать тестовое фото", callback_data="PressPhotoTestPublish")
    callback_button1 = types.InlineKeyboardButton(text="Опубликовать фото", callback_data="PressPhotoPublish")
    keyboardForm.add(callback_button,callback_button1)

    bot.send_photo(message.chat.id, file_id,caption = finalString,reply_markup=keyboardForm)
     
# В большинстве случаев целесообразно разбить этот хэндлер на несколько маленьких
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    global finalString

    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "PressTestPublish":
            bot.send_message(config.channel_name, finalString)
            bot.send_message(config.inner_chat_name, finalString, message_thread_id = config.message_thread_id)
        elif call.data == "PressPhotoTestPublish":
            file_id = call.message.photo[-1].file_id
            bot.send_photo(config.channel_name, file_id,caption = finalString)
            bot.send_photo(config.test_inner_chat_name, file_id,caption = finalString, message_thread_id = config.test_message_thread_id)
        elif call.data == "PressPhotoPublish":
            file_id = call.message.photo[-1].file_id
            bot.send_photo(config.channel_name, file_id,caption = finalString)
            bot.send_photo(config.inner_chat_name, file_id,caption = finalString, message_thread_id = config.message_thread_id)    
    
if __name__ == "__main__":
    bot.infinity_polling()
