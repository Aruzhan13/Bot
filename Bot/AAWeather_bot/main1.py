from constants import TOKEN
from messages import HELLO, CURRENT_WEATHER
from telebot import types
import messages
import database
# pytelegrambotapi
import telebot
import requests

bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('Almaty')
itembtn2 = types.KeyboardButton('Astana')
itembtn3 = types.KeyboardButton('Shymkent')
itembtn4 = types.KeyboardButton('Dubai')
markup.row(itembtn1, itembtn2)
markup.row(itembtn3, itembtn4)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, messages.HELLO)
    msg = ''
    for i in database.get():
        msg += str(i)
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['cities'])
def get_weather(message):
    print('inserted')
    bot.send_message(message.chat.id, "Choose City from the buttons or type the city that you need: ", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def func_name(message):
    try:
        yahooql = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='%s') and u='c'" % message.text
        url = "https://query.yahooapis.com/v1/public/yql?q=%s&format=json" % yahooql
        r = requests.get(url)
        data = r.json()
        temp = data['query']['results']['channel']['item']['condition']['temp']
        bot.send_message(message.chat.id, "In %s %s C at the moment" % (message.text, temp), reply_markup = markup)
    except Exception:
        bot.send_message(message.chat.id, "I can't find %s in my database" % message.text, reply_markup = markup)

if __name__ == '__main__':
    print('Starting Aiaru')
    bot.polling()