import requests
from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Replace this with your bot's token (from BotFather)
TOKEN = "7228147192:AAEg1GtZGTGSr_uag1BMi2V6hwytNBBYb8o"

# Create an Updater object to handle Telegram Bot communication
updater = Updater(token=TOKEN, use_context=True)

def start(update, context):
    update.message.reply_text('Hello, I am your Telegram bot!')

def help(update, context):
    update.message.reply_text('How can I assist you today?')

# Register handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))

# This function will run every time the bot receives a request
def webhook(request):
    """Handles the webhook request from Telegram"""
    bot = Bot(token=TOKEN)
    json_str = request.get_json()
    
    # Make sure the update is valid
    if json_str.get('message') and json_str['message'].get('text'):
        bot.send_message(chat_id=json_str['message']['chat']['id'], text="Received: " + json_str['message']['text'])
    
    return 'OK', 200
