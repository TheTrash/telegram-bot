from telegram.ext import Updater
from telegram import User, Bot
from random import randint
from rec_catdog import recognition
import os
import threading

updater = Updater(token=open("token.txt", "r").readline())
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello_world!")

def get_id(update, context):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text='tuo ID: ' + str(user.id) + '\nUser: ' + str(user.username))


def image_handler(update, context):
    def remove_image(filename):
        if os.path.exists(filename):
            os.remove(filename)

    photos = update.message.photo
    if photos:
        user = update.message.from_user
        update.message.reply_text("I'm working on it...")
        logging.info(f"Photo received from {user.username}")

        # Download the best photo version
        photo_id = photos[-1].file_id
        filename = f"img{randint(0,10000)}_from_{user.username}.jpg"
        context.bot.get_file(photo_id).download(filename)

        cl, pred = recognition(filename)
        remove_image(filename)

        update.message.reply_text(f'I\'m {pred}% sure, that shit is totally a {cl}')
        update.message.reply_text(f'See Ya, Pal')


from telegram.ext import CommandHandler, MessageHandler, Filters
start_handler = CommandHandler('start',start)
get_handler = CommandHandler('get_id', get_id)

dispatcher.add_handler(MessageHandler(Filters.photo, image_handler))

dispatcher.add_handler(start_handler)
dispatcher.add_handler(get_handler)


updater.start_polling()
updater.idle()