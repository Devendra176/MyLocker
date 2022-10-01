from django.conf import settings
from telegramBot.command_function import call_phone_register_api, call_phone_verification_api, get_website_data

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


updater = Updater(settings.TELEGRAM_BOT_TOKEN,
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hey! Welcome to the 'MyLocker' enter '/help' to see available command")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""
    /start
    /login
    /websitedata
    /help""")

def login(update: Update, context: CallbackContext):
    update.message.reply_text("Please Enter your Number ex: phone 1234567890")


def website_data(update: Update, context: CallbackContext):
    data = get_website_data(context.user_data)
    if not context.user_data.get('is_authenticated'):
        update.message.reply_text("Please login first try /login command")

    if data:
        for i in data['website_data']:
            update.message.reply_text(
            """
            website_url : %s
            website_username: %s
            website_password: %s
            """%(i.get('website_url'), i.get('website_username'), i.get('website_password')))

    else:
        update.message.reply_text("No Data found for user %s"%context.user_data.get('phone'))

def unknown_text(update: Update, context: CallbackContext):

    if update.message.text.split()[0] == 'phone':
        data = call_phone_register_api(update.message.text.split()[1])
        context.user_data['phone'] = update.message.text.split()[1]
        update.message.reply_text(
            "OTP: %s Enter OTP with phone ex: otp 1234" % data.get('otp'))

    if update.message.text.split()[0] == 'otp':
        data = call_phone_verification_api(update.message.text.split()[1], context.user_data.get('phone'))
        context.user_data['token'] = data.get('token')
        context.user_data['is_authenticated'] = True
        update.message.reply_text(
            "you are login with %s" % context.user_data['phone'])
    else:
        update.message.reply_text("Hello, try /help to see available command")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('login', login))
updater.dispatcher.add_handler(CommandHandler('websitedata', website_data))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))