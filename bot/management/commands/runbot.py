from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler, Updater
from django.core.management import BaseCommand
from bot.views import *
TOKEN = "6333308173:AAFCJdNBssJAIabAhvQ0v19cPCMSssnUGH0"
# TOKEN = "5028779716:AAHJIfeuX9nx0A5YwZuDsDCDKegBvNmUN5A"


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(TOKEN)
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
        updater.dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
        updater.dispatcher.add_handler(CallbackQueryHandler(inline_handler))
        updater.start_polling()
        updater.idle()
