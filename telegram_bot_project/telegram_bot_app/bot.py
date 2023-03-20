from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello, I'm your new Telegram bot!")

def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    keyboard = [[InlineKeyboardButton("Stupid", callback_data='stupid'),             InlineKeyboardButton("Fat", callback_data='fat'),             InlineKeyboardButton("Dumb", callback_data='dumb')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose a category:', reply_markup=reply_markup)
def button(update, context):
    query = update.callback_query

    if query.data == 'stupid':
        joke_text = 'Why did the chicken cross the road? To get to the other side!'
        button_name = 'stupid'
    elif query.data == 'fat':
        joke_text = 'Why did the tomato turn red? Because it saw the salad dressing!'
        button_name = 'fat'
    elif query.data == 'dumb':
        joke_text = 'Why did the bicycle fall over? Because it was two-tired!'
        button_name = 'dumb'

    query.edit_message_text(text=joke_text)

    button, created = Button.objects.get_or_create(name=button_name)
    button.calls += 1
    button.save()
updater = Updater(token='6023630281:AAGTRRg4-D44P6CEWFuEcEetujQjoot_n2s', use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(filters.text & ~filters.command, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
