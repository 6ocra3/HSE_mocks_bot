import telebot;
import json;
from utils import Number, Name, City, Date, Uuid, Email, PhoneNumber, Login, Password
#Name, City, Date, Number, Uuid, Email,PhoneNumber, Login, Password.
bot = telebot.TeleBot('6977780793:AAHddHSS_H5XI_xjt9X7vRZ9U05RmbqaKoc');
dataType = {
    "number": Number,
    "name": Name,
    "city": City,
    "date": Date,
    "id": Uuid,
    "email": Email,
    "phonenumber": PhoneNumber,
    "login": Login,
    "password": Password
}

defKeyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
button_start = telebot.types.KeyboardButton(text="Начать генерацию")
button_help = telebot.types.KeyboardButton(text="/help")
defKeyboard.add(button_start, button_help)

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == "Начать генерацию":
        bot.send_message(message.from_user.id, "Привет, напиши сколько элементов в массиве тебе нужно (одно число)", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_field)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Бот создаёт моки (поддельные объекты, которые создаются для тестирования программного кода) по заданным пользователем параметрам.\n"
                                               "Бот умеет генерировать 9 типов данных для тестов:\n"
                                               "Name - русское имя\n"
                                               "Number - число в диапазоне [1, 100]\nCity - российский город\nDate - дата в диапазоне [1923, 2023]\n"
                                               "Uuid - уникальный ID\nPassword - пароль \nEmail - электронная почта\nLogin - username пользователя\n PhoneNumber - номер телефона\n"
                                               "И возвращает массив коллекций созданных моков.\n Чтобы получить от БОТа нужные моки, пользователь должен запросить их указанным образом:\n"
                                               "Формат <имя поля>: <тип данных>\nимя: Name\nномер: Number\nгород: City\n"
                                               "дата_рождения: Date\nID: Uuid\nпароль: Password\nэлектронная_почта: Email\n"
                                               "логин: Login\nтелефон: PhoneNumber\n")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понял", reply_markup=defKeyboard)



cnt = 0
def get_field(message):
    try:
        global cnt
        cnt = int(message.text)
        bot.send_message(message.from_user.id, "Напиши формат данных для одного элемента. <имя поля>: <тип данных>", reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, parser)
    except Exception as e:
        bot.send_message(message.from_user.id, "Что-то пошло не так, возвращаем в начало", reply_markup=defKeyboard)
        bot.register_next_step_handler(message, handle_text_messages)


def parser(message):
    global defKeyboard
    try:
        global cnt
        global dataType
        data = message.text.split()
        mask = []
        if len(data) < 2:
            raise Exception
        for i in range(1, len(data), 2):
            if ":" in data[i - 1]:
                mask.append(dataType[data[i].lower()](data[i - 1][:-1]))
            else:
                mask.append(dataType[data[i].lower()](data[i - 1]))
        itog = []
        for i in range(cnt):
            a = {}
            for j in mask:
                a[j.field] = j.generate()
            itog.append(a)
        print(itog)
        bot.send_message(message.from_user.id, json.dumps(itog, ensure_ascii=False), reply_markup=defKeyboard)
    except Exception as e:

        bot.send_message(message.from_user.id, "Что-то пошло не так, возвращаем в начало", reply_markup=defKeyboard)
        bot.register_next_step_handler(message, handle_text_messages)

bot.polling(none_stop=True, interval=0)