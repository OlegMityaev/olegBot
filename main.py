import telebot
from telebot import types
token = '5114669449:AAFBSdAX9N0dhcs71r6U4oICP1_AdBriWVo'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Начало работы бота')
@bot.message_handler(commands=['com'])
def d(message):
    bot.send_message(message.chat.id,'/start - начало')
    bot.send_message(message.chat.id,'/valuta - Курс валюты')
    bot.send_message(message.chat.id,'/Wiki - Поиск статьи википедии по слову')
@bot.message_handler(commands=['valuta'])
def button(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton('Доллар')
    item2=types.KeyboardButton('Евро')
    markup.add(item1,item2)
    bot.send_message(message.chat.id, 'Выбери валюту', reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=='Евро':
        bot.send_message(message.chat.id,'https://www.finversia.ru/publication/currency/evro-565')
    elif message.text=='Доллар':
        bot.send_message(message.chat.id, 'https://www.finversia.ru/publication/currency/dollar-ssha-533')
@bot.message_handler(content_types=['text'])
def kekts(message):
    bot.send_message(message.chat.id,'https://www.google.com/search?q='+ message.text + '&oq='+ message.text + '&aqs=chrome..69i57j46i433i33i512j0i433i512j0i512l5j46i512j0i512.2088j0j7&sourceid=chrome&ie=UTF-8')
bot.infinity_polling()