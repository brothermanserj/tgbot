# -*- coding: utf-8 -*-
import config
import telebot
import random
import time

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
You are talking to an Alpha-version of private bot by Sergei N.\
""")
    
@bot.message_handler(commands=['pepe'])
def random_sticker(message):
    a = random.randint(0,3)
    if a == 0:
       bot.reply_to(message, message.chat.first_name +", " + """Сегодня ты Классный Пепе. Весь сегодняшний день тебя ждет удача. Так держать!""")
       bot.send_sticker(message.chat.id, "CAADAgADOyYAAktqAwABU3EJXSaKHCQC")
    elif a == 1:
       bot.reply_to(message, message.chat.first_name +", " + """Сегодня ты Грустный Пепе. Но не стоит унывать, все наладится!""")
       bot.send_sticker(message.chat.id, "CAADAgADMSYAAktqAwAB5LUCSor2LWUC")
    elif a == 2:
        bot.reply_to(message, message.chat.first_name +", " +  """Сегодня ты слегка Счастливый Пепе. Сегодня может произойти что-то хорошее!""")
        bot.send_sticker(message.chat.id, "CAADAgAD3CYAAktqAwABpWXjZ5gMf_0C")
    elif a == 3:
        bot.reply_to(message, message.chat.first_name +", " +  """Сегодня ты Успешный Пепе. Не думай, что о тебе говорят другие!""")
        bot.send_sticker(message.chat.id, "CAADAgADTCoAAktqAwAB23eiivB_NN0C")

        
@bot.message_handler(commands=['time'])
def get_time(message):
   currenttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
   bot.reply_to(message, """Текущее время: """ + """\n"""+ currenttime)
   
@bot.message_handler(commands=['meme'])
def get_meme(message):
    bot.reply_to(message, """Random meme incoming!""")
   
    


bot.polling()
