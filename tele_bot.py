import sys
import platform
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

uname = platform.uname()
sys_name = (platform.system())
arch = (platform.architecture())
host = (platform.node())
cpu = (platform.processor())

updater = Updater("5508129069:AAHJ6YdA2-6OrYJ6b-ie8deGGV9cAgS6EUs",
        use_context=True)


def start(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Hello Master. How can I assist you today?")

def status_url(update: Update, context: CallbackContext):
  update.message.reply_text(
    "I am ok. I can see the internet.")

def stats_url(update: Update, context: CallbackContext):
  update.message.reply_text(f"My system stats are: {sys_name}, {arch}, {host}, {cpu}")

def unknown(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Sorry I don't understand , you said '%s'" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('status', status_url))
updater.dispatcher.add_handler(CommandHandler('stats', stats_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
