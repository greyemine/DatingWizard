import telebot
from telebot import types


def completing_the_final_line(summaru):
#Return final string from global list

    SumTxtInFunction = ""

    for i,elem in enumerate(summaru):
        if elem != "stop":
            if i % 2 == 0:
                SumTxtInFunction = SumTxtInFunction + elem + "\n"
            else:
                SumTxtInFunction = SumTxtInFunction + elem + ": "



    return SumTxtInFunction

def generate_basic_keyboard_buttons(keyboardForm):

#Generate (and return) keyboard with basic button

    #вынести эти константы в конфиг
    url_button = types.InlineKeyboardButton(text="Бот анкет", url="https://t.me/NewBottomFormBot")
    url_button1 = types.InlineKeyboardButton(text="Канал публикаций", url="https://t.me/club2_service_dating")
    url_button2 = types.InlineKeyboardButton(text="Внутренний чат", url="https://t.me/+pzxtFYbKWiJiNDEy")

    keyboardForm.add(url_button,url_button1,url_button2)
    return keyboardForm

