import platform
import subprocess
import re
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

# function to get ping averages but only runs at initial code start so need to add threading and timer
def get_statistics():
    statistics = {}
    matcher = re.compile('\d+')
    ping_result = subprocess.run(['ping', '-i 5', '-c 5', 'google.com'], stdout=subprocess.PIPE).stdout.decode(
        'utf-8').split('\n')

    min, avg, max = ping_result[-2].split('=')[-1].split('/')[:3]
    statistics['network_latency'] = dict(
        {
            'min': min.strip(),
            'avg': avg.strip(),
            'max': max.strip(),
        }
    )
    return statistics

statistics = get_statistics()

# telegram bot's key goes here between double quotes
updater = Updater("telegram bot's key goes here - leave it in double quotes",
        use_context=True)

def start(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Hello Master. How can I assist you today?")

def status_url(update: Update, context: CallbackContext):
  update.message.reply_text(
    "I am ok. I can see the internet.")

def stats_url(update: Update, context: CallbackContext):
  update.message.reply_text(f"My system stats are: {sys_name}, {arch}, {host}, {cpu}")

def ping_url(update: Update, context: CallbackContext):
  update.message.reply_text(f"My network is: {statistics}")

def unknown(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
  update.message.reply_text(
    "Sorry I don't understand , you said '%s'" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('status', status_url))
updater.dispatcher.add_handler(CommandHandler('ping', ping_url))
updater.dispatcher.add_handler(CommandHandler('stats', stats_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) # unknown commands filter
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text)) # unknown message handler

updater.start_polling()
