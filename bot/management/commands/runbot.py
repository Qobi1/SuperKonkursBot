from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler, Updater
from django.core.management import BaseCommand
from bot.views import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater("5028779716:AAHPX6MXluEDtwPUHfoaG17SbZcqI2rpejw")
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
        updater.dispatcher.add_handler(MessageHandler(Filters.contact, contact_hanlder))
        updater.dispatcher.add_handler(CallbackQueryHandler(inline_handler))
        updater.start_polling()
        updater.idle()
