# -*- coding: utf-8 -*-
import redis
import os
import telebot
import apiai, json
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['439378420:AAEe6ebLHPbsOLwnNAv_eSCravY-iIJ5FSA']
some_api_token = os.environ['SOME_API_TOKEN']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='439378420:AAEe6ebLHPbsOLwnNAv_eSCravY-iIJ5FSA')
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    request = apiai.ApiAI('914d87a0b7734dabb5207cc8574b4ddf').text_request()
    request.lang = 'ru'
    request.session_id = 'BatlabAIBot'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()


