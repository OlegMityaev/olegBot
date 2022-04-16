import telebot
from telebot import types
import requests
import bs4
import speech_recognition as sr
import os
import pyttsx3
import time
from pydub import AudioSegment

AudioSegment.converter = os.getcwd() + "\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = os.getcwd() + "\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = os.getcwd() + "\\ffmpeg\\bin\\ffprobe.exe"
text_to_speach = pyttsx3.init()
voices = text_to_speach.getProperty('voices')
for voice in voices:
    print('--------------------')
    print('Имя: %s' % voice.name)
    print('ID: %s' % voice.id)

RU_VOICE_ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
text_to_speach.setProperty('voice', RU_VOICE_ID)

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

token = '5396396730:AAHtckjLxFRDfAqjEVREUXaY_OGASGeHZIM'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Начало работы бота')
    bot.send_message(message.chat.id, 'Введите /com для просмотра списка комманд')


@bot.message_handler(commands=['info'])
def info(message):
    mid = bot.send_message(message.chat.id, 'Здравствуйте! Меня зовут Ирина и я Ваш личный гид по Кванториуму!')
    btext = mid.text.lower()
    src = str(message.chat.id) + str(mid.message_id - 1) + '_answer.oga'
    text_to_speach.save_to_file(btext[:], src)
    text_to_speach.runAndWait()
    time.sleep(1)
    voice = open(src, 'rb')
    bot.send_audio(message.chat.id, voice)

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item9 = types.KeyboardButton('Направления')
    item10=types.KeyboardButton('Адрес')
    item11=types.KeyboardButton('ЧаВо')
    item12=types.KeyboardButton('Как связаться')
    markup.add(item9,item10,item11,item12)
    bot.send_message(message.chat.id, 'Выберите, что Вас интересует', reply_markup=markup)

@bot.message_handler(commands=['com'])
def d(message):
    bot.send_message(message.chat.id,'/start - начало')
    bot.send_message(message.chat.id,'/info - инфо')
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

@bot.message_handler(commands=['dialog'])
def dialog(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item13 = types.KeyboardButton('Представься')
    item14 = types.KeyboardButton('Возможности')
    item15 = types.KeyboardButton('Аня есть')
    item16 = types.KeyboardButton('ББ')
    markup.add(item13, item14, item15, item16)
    bot.send_message(message.chat.id, 'Выберите, что Вас интересует', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def aaa(message):
    def golos(mid):
        btext = mid.text.lower()
        src = str(message.chat.id) + str(mid.message_id - 1) + '_answer.oga'
        text_to_speach.save_to_file(btext[:], src)
        text_to_speach.runAndWait()
        time.sleep(1)
        voice = open(src, 'rb')
        bot.send_audio(message.chat.id, voice)
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

    if message.text == 'Представься':
        golos(bot.send_message(message.chat.id, 'Здравствуйте! Меня зовут Ирина'))
    elif message.text == "Возможности":
        golos(bot.send_message(message.chat.id, 'Я умею выдавать расписание квантумов, которые я успешно выгрузила с официального сайта Кванториума. Могу скинуть геолокацию кванториума. И выдавать полезную информацию'))
    elif message.text == 'Аня есть':
        golos(bot.send_message(message.chat.id, 'Но для этого есть Аня'))
    elif message.text == 'ББ':
        golos(bot.send_message(message.chat.id, 'До свидания'))

    if message.text=="Направления":

        golos(bot.send_message(message.chat.id, 'Vr/Ar - моделирование 3D объектов и миров. Программирование и создание собственных Vr и Ar приложений'))
        golos(bot.send_message(message.chat.id,'Хайтек - работа с 3D принтером, станком с ЧПУ, моделирование в 2D и 3D, лазерные технологии'))

        golos(bot.send_message(message.chat.id, 'Наноквантум - изучение материалов на микро и наноуровнях с помощью современных микроскопов и другого оборудования'))
        golos(bot.send_message(message.chat.id, 'Геоквантум - изучение поверхности Земли, картостроение, создание систем навигации'))
        golos(bot.send_message(message.chat.id, 'Аэроквантум - беспилотные летательные аппараты. Проектирование, запуск, сборка'))
        golos(bot.send_message(message.chat.id, 'Промробоквантум - конструирование и программирование роботов'))
        golos(bot.send_message(message.chat.id, 'Также проходят занятия по английскому языку, шахматам и математике'))
    elif message.text =='Адрес':
        bot.send_message(message.chat.id, 'Иркутский переулок 2')
        bot.send_location(message.chat.id, 57.81219, 28.35942)
    elif message.text == 'ЧаВо':
        golos(bot.send_message(message.chat.id, 'Бесплатное ли обучение? Да, обучение абсолютно бесплатно :)'))
        golos(bot.send_message(message.chat.id, 'Со скольки лет можно ходить? На шахматы можно записаться с 6 лет, а на все остальные направления с 12.'))
        golos(bot.send_message(message.chat.id, 'Договор! Обязательно не забудьте взять, заполнить и принести договор на обучений!'))
        golos(bot.send_message(message.chat.id, 'Ссылка на договор : https://vk.com/doc-161543134_610773790?hash=56f7e51ec0fa6ab503&dl=5798c9a12377ee7be6'))
    elif message.text == 'Как связаться':
        bot.send_message(message.chat.id, 'Тел. +7(8112)79-70-79')
        bot.send_message(message.chat.id, 'https://vk.com/kvantoriumpskov')
        bot.send_message(message.chat.id, 'https://vk.com/golikovaao')
        bot.send_message(message.chat.id, 'kvantoriumpskov@gmail.com')

# def rofl(message):
    text = message.text.lower()
    print(message.message_id)
    if 'porofly' in text: #and text.split(' ')[0] == 'porofly':
        mid = bot.send_message(message.chat.id, 'Обкодился')
        btext = mid.text.lower()
        src = str(message.chat.id) + str(mid.message_id-1) + '_answer.oga'
        print(src)
        text_to_speach.save_to_file(btext[:], src)
        text_to_speach.runAndWait()
        time.sleep(1)
        voice = open(src, 'rb')
        bot.send_audio(message.chat.id, voice)
        bot.send_photo(message.chat.id, 'http://img2.safereactor.cc/pics/post/full/it-%D1%8E%D0%BC%D0%BE%D1%80-geek-doge-%D0%9C%D0%B5%D0%BC%D1%8B-5952251.png')

        mid = bot.send_message(message.chat.id, 'Обпитонился')
        btext = mid.text.lower()
        src = str(message.chat.id) + str(mid.message_id - 1) + '_answer.oga'
        print(src)
        text_to_speach.save_to_file(btext[:], src)
        text_to_speach.runAndWait()
        time.sleep(1)
        voice = open(src, 'rb')
        bot.send_audio(message.chat.id, voice)
        bot.send_photo(message.chat.id, 'https://cs12.pikabu.ru/post_img/2021/05/19/1/1621376414120131742.png')

        mid = bot.send_message(message.chat.id, 'Обсишарпился')
        btext = mid.text.lower()
        src = str(message.chat.id) + str(mid.message_id - 1) + '_answer.oga'
        print(src)
        text_to_speach.save_to_file(btext[:], src)
        text_to_speach.runAndWait()
        voice = open(src, 'rb')
        bot.send_audio(message.chat.id, voice)
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/i?id=3408794366b2cb0e99df8719c128b8cd-5173372-images-thumbs&n=13')

@bot.message_handler(content_types=["voice"])
def bot_messages(message):
    file_info = bot.get_file(message.voice.file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))
    src = file_info.file_path[:6] + 'oga' + file_info.file_path[5:]
    dst = file_info.file_path[:6] + 'wav' + file_info.file_path[5:-3] + 'wav'
    with open(src, 'wb') as f:
        f.write(file.content)
    sound = AudioSegment.from_oga(src)
    sound.export(dst, format="wav")
    del sound
    rec = sr.Recognizer()
    with sr.WavFile(dst) as source:
        audio = rec.record(source)
    try:
        text = rec.recognize_google(audio, language="ru-RU").lower()
        error = 0
    except LookupError:
        bot.send_message(message.chat.id, 'Не понимаю Ваш восхитительный голос :(')
        error = 1
    if error == 0:
        if '' in text: # and text.split(' ')[0] == 'porofly':
            text_to_speach.save_to_file(text[:], file_info.file_path[:6] + 'answer' + file_info.file_path[5:])
            text_to_speach.runAndWait()
            time.sleep(1)
            voice = open(file_info.file_path[:6]+'answer'+ file_info.file_path[5:], 'rb')
            bot.send_audio(message.chat.id, voice)
    else:
        bot.send_message(message.chat.id, 'Не понял команду :(')

bot.infinity_polling()()