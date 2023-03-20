from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = '6023630281:AAGTRRg4-D44P6CEWFuEcEetujQjoot_n2s'
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

@csrf_exempt
def telegram_bot(request):
    if request.method == 'POST':
        update = Update.de_json(request.body, updater.bot)
        dispatcher.process_update(update)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)

