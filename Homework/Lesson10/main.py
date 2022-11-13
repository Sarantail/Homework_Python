import controller as c
import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler, RegexHandler, \
    messagequeue as mq


def start(bot, update):
    text = 'Для того чтобы начать введите: /start_game.'
    update.message.reply_text(text)


c.button_click()
