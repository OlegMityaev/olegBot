import telebot
from telebot import types
import requests
import bs4
def get_kartinka(napr):
    global vr_fin2
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    r3 = requests.get('https://www.kvantoriumpskov.ru/расписание-' + napr, headers=headers)
    che1 = bs4.BeautifulSoup(r3.text)
    ssi1 = che1.find_all('div', {'data-testid': 'linkElement'})
    text1 = []
    for i in ssi1:
        text1.append(str(i))
    text1[0].find('src="')
    list_links = []
    c = 0
    while True:
        n = text1[2].find('src="', c)
        e = text1[2].find('"', n+5)
        list_links.append(text1[2][n+5:e])
        if n == -1:
            break
        c = e
    vr = list_links[1]
    st1 = vr.find('w_')+2
    end1 = vr.find('w_')+5
    vr1 = vr[st1:end1]
    st2 = vr.find('h_')+2
    end2 = vr.find('h_')+5
    vr2 = vr[st2: end2]
    st3 = vr.find('bl')
    end3 = vr.find('bl')+7
    vr3 = vr[st3:end3]
    vr_fin = vr.replace(vr1, '999')
    vr_fin1 = vr_fin.replace(vr2, '800')
    vr_fin2 = vr_fin1.replace(vr3, '')
    return vr_fin2

token = '5114669449:AAFBSdAX9N0dhcs71r6U4oICP1_AdBriWVo'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Начало работы бота')
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Меня зовут Олег и я Ваш личный гид по Кванториуму!')
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item9 = types.KeyboardButton('Направления')
    item10=types.KeyboardButton('Адрес')
    item11=types.KeyboardButton('ЧаВо')
    item12=types.KeyboardButton('Как связаться')
    markup.add(item9,item10,item11,item12)
    bot.send_message(message.chat.id, 'Выберите, что Вас интересует', reply_markup=markup)
@bot.message_handler(content_types='text')
def bbb(message):
    if message.text=="Направления":
        bot.send_message(message.chat.id, 'Vr/Ar - моделирование 3D объектов и миров. Программирование и создание собственных Vr и Ar приложений')
        bot.send_message(message.chat.id,'Хайтек - работа с 3D принтером, станком с ЧПУ, моделирование в 2D и 3D, лазерные технологии')
        bot.send_message(message.chat.id, 'Наноквантум - изучение материалов на микро и наноуровнях с помощью современных микроскопов и другого оборудования')
        bot.send_message(message.chat.id, 'Геоквантум - изучение поверхности Земли, картостроение, создание систем навигации')
        bot.send_message(message.chat.id, 'Аэроквантум - беспилотные летательные аппараты. Проектирование, запуск, сборка')
        bot.send_message(message.chat.id, 'Промробоквантум - конструирование и программирование роботов')
        bot.send_message(message.chat.id, 'Также проходят занятия по английскому языку, шахматам и математике')
    elif message.text =='Адрес':
        bot.send_message(message.chat.id, 'Иркутский переулок 2')
        bot.send_location(message.chat.id, 57.81219, 28.35942)
    elif message.text == 'ЧаВо':
        bot.send_message(message.chat.id, 'Бесплатное ли обучение? Да, обучение абсолютно бесплатно :)')
        bot.send_message(message.chat.id, 'Со скольки лет можно ходить? На шахматы можно записаться с 6 лет, а на все остальные направления с 12.')
        bot.send_message(message.chat.id, 'Договор! Обязательно не забудьте взять, заполнить и принести договор на обучений!')
        bot.send_message(message.chat.id, 'Ссылка на договор : https://vk.com/doc-161543134_610773790?hash=56f7e51ec0fa6ab503&dl=5798c9a12377ee7be6')
    elif message.text == 'Как связаться':
        bot.send_message(message.chat.id, 'Тел. +7(8112)79-70-79')
        bot.send_message(message.chat.id, 'https://vk.com/kvantoriumpskov')
        bot.send_message(message.chat.id, 'https://vk.com/golikovaao')
        bot.send_message(message.chat.id, 'kvantoriumpskov@gmail.com')
@bot.message_handler(commands=['com'])
def d(message):
    bot.send_message(message.chat.id,'/start - начало')
    bot.send_message(message.chat.id,'/valuta - Курс валюты')
    bot.send_message(message.chat.id, '/Raspisanie - расписание квантумов')
@bot.message_handler(commands=['Raspisanie'])
def b(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3=types.KeyboardButton('Vr/Ar')
    item4=types.KeyboardButton('Промробоквантум')
    item5 = types.KeyboardButton('Геоквантум')
    item6 = types.KeyboardButton('Аэроквантум')
    item7 = types.KeyboardButton('Наноквантум')
    item8 = types.KeyboardButton('Хайтек')
    markup.add(item3,item4,item5,item6,item7,item8)
    bot.send_message(message.chat.id, 'Выберите интересующий квантум', reply_markup=markup)
@bot.message_handler(content_types='text')
def aaa(message):
    if message.text=='Vr/Ar':
        get_kartinka('vr')
        bot.send_photo(message.chat.id, vr_fin2)
    elif message.text=="Промробоквантум":
        get_kartinka('промробо')
        bot.send_photo(message.chat.id, vr_fin2)
    elif message.text=='Геоквантум':
        get_kartinka('гео')
        bot.send_photo(message.chat.id, vr_fin2)
    elif message.text =='Аэроквантум':
        get_kartinka('аэро')
        bot.send_photo(message.chat.id, vr_fin2)
    elif message.text=='Наноквантум':
        get_kartinka('нано')
        bot.send_photo(message.chat.id, vr_fin2)
    elif message.text == 'Хайтек':
        get_kartinka('хайтек')

        bot.send_photo(message.chat.id, vr_fin2)

bot.infinity_polling()