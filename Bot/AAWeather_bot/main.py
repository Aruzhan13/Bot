from constants import TOKEN
from messages import HELLO

import messages
import database
# pytelegrambotapi
import telebot
import requests


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, messages.HELLO)
    msg = ''
    for i in database.get():
        msg += str(i)
    bot.send_message(message.chat.id, msg)



if __name__ == '__main__':
    print('Starting AAweatherbot')
bot.polling()