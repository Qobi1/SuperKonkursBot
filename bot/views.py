import telegram.error
from django.shortcuts import render
# Create your views here.
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from .models import Data
from .text import dictionary
CHANNELS = [("Test 1", -1001610436325, 'https://t.me/teeessttttt_1'), ("Test 2", -1001737589089, "https://t.me/test_22222222221")]


def start(update: Update, context: CallbackContext):
    msg = update.message.text
    msg = msg.split(' ')
    user = update.effective_user
    data = Data.objects.filter(user_id=user.id).first()

    if data is None:
        update.message.reply_text("🇺🇿 - Tilni tanlang!\n🇷🇺 - Выберите язык", reply_markup=inline_buttons(type='language'))
        if len(msg) == 1:
            Data.objects.create(user_id=user.id, state=1).save()
        elif len(msg) == 2:
            Data.objects.create(user_id=user.id, state=1, invited_by=msg[1]).save()

    elif data is not None:
        try:
            context.bot.send_video(chat_id=user.id, video=open("videos/video1.mp4", 'rb'), supports_streaming=True,
                               caption=dictionary(language=data.language, command='start', user=user),
                               reply_markup=inline_buttons(type='start'))
            data.state = 3
            data.save()
        except KeyError:
            update.message.reply_text("🇺🇿 - Tilni tanlang!\n🇷🇺 - Выберите язык", reply_markup=inline_buttons(type='language'))


def inline_handler(update: Update, context: CallbackContext):
    user = update.effective_user
    query = update.callback_query
    data = Data.objects.filter(user_id=user.id).first()
    if data.state == 1 or data.state == 2 and query.data in ['uzb', 'rus']:
        data.language = query.data
        query.delete_message()
        data.state = 2
        btn = [[KeyboardButton(dictionary(language=query.data, command='phone', user=user), request_contact=True)]]
        query.message.reply_text(dictionary(language=query.data, command='phone text', user=user), reply_markup=ReplyKeyboardMarkup(btn, resize_keyboard=True))
    elif data.state == 3 and query.data in ['start', 'check']:
        check = check_member_status(update, context, user, boolean=True)
        if data.invited_by is not None and data.message is False and check == len(CHANNELS):
            language = Data.objects.filter(user_id=data.invited_by).first()
            context.bot.send_message(text=dictionary(language=language.language, command='yourfriendsubscribed', user=user), chat_id=data.invited_by)
            data.message = True
        else:
            pass
        if query.data == 'check':
            query.delete_message()
        check_status = check_member_status(update, context, user)
        context.bot.send_video(chat_id=user.id, video=check_status[0], caption=check_status[1], reply_markup=check_status[2], timeout=100000)
    data.save()


def message_handler(update: Update, context: CallbackContext):
    user = update.effective_user
    data = Data.objects.filter(user_id=user.id).first()
    if data.state == 2:
        btn = [[KeyboardButton(dictionary(language=data.language, command='phone', user=user), request_contact=True)]]
        update.message.reply_text(dictionary(language=data.language, command='phone error', user=user), reply_markup=ReplyKeyboardMarkup(btn, resize_keyboard=True))
    else:
        update.message.reply_text(dictionary(language=data.language, command='error', user=user))


def contact_hanlder(update: Update, context: CallbackContext):
    user = update.effective_user
    contact = update.message.contact
    data = Data.objects.filter(user_id=user.id).first()
    data.contact = contact.phone_number
    data.state = 3
    dot = update.message.reply_text('.', reply_markup=ReplyKeyboardRemove())
    context.bot.delete_message(chat_id=user.id, message_id=dot.message_id)
    context.bot.send_video(chat_id=user.id, video=open("videos/video1.mp4", 'rb'), supports_streaming=True, caption=dictionary(language=data.language, command='start', user=user), reply_markup=inline_buttons(type='start'), timeout=100000)
    data.save()


def inline_buttons(type=None, user=None):
    btn = []
    if type == 'language':
        btn = [[InlineKeyboardButton("🇺🇿O'zbek tili", callback_data="uzb"), InlineKeyboardButton("🇷🇺Rus tili", callback_data="rus")]]
    elif type == 'start':
        btn = [[InlineKeyboardButton('start', callback_data='start')]]
    elif type == "share":
        data = Data.objects.filter(user_id=user.id).first()
        btn = [
            [InlineKeyboardButton("🔗 Havola blan o'rtoqlashish", url=f"https://telegram.me/share/url?url=https://t.me/d_acc_Bot?start={user.id}&text=Havoladan%20o%E2%80%98ting%2C%20kanallarga%20a%E2%80%99zo%20bo%E2%80%98ling%20va%20o%E2%80%98yin%20ishtirokchisiga%20aylaning!", callback_data='havola')],
            [InlineKeyboardButton(dictionary(language=data.language, command='check', user=user), callback_data='check')]
]
    return InlineKeyboardMarkup(btn)


def check_member_status(update: Update, context: CallbackContext, user=None, boolean=False):
    btn = []
    count = 0
    data = Data.objects.filter(user_id=user.id).first()
    for i in CHANNELS:
        channel = context.bot.getChatMember(user_id=user.id, chat_id=i[1])
        if channel['status'] not in ['member', 'creator']:
            btn.append([InlineKeyboardButton(i[0], callback_data=f"{i[1]}", url=i[2])])
        else:
            btn.append([InlineKeyboardButton(f"✅{i[0]}", callback_data=f"{i[1]}", url=f'{i[2]}')])
            count += 1
    btn.append([InlineKeyboardButton(dictionary(language=data.language, command='check', user=user), callback_data='check')])
    if boolean is True:
        return count
    if count == len(CHANNELS):
        queryset = Data.objects.filter(invited_by=user.id).values()
        result = 0
        number = 0
        if queryset:
            for i in queryset:
                for j in CHANNELS:
                    try:
                        channel = context.bot.getChatMember(user_id=i['user_id'], chat_id=j[1])
                        if channel['status'] in ['member', 'creator']:
                           number += 1
                    except telegram.error.BadRequest:
                        pass
                if number == 2:
                    result += 1
                number = 0
        if result >= 2:
            return open('videos/video3.mp4', 'rb'), dictionary(language=data.language, user=user, command='subscribed2', people=result), inline_buttons(type='share', user=user)
        else:
            return open('videos/video3.mp4', 'rb'), dictionary(language=data.language, user=user, command='subscribed', people=result), inline_buttons(type='share', user=user)
    elif count != len(CHANNELS):
        return open('videos/video2.mp4', 'rb'), dictionary(language=data.language, user=user, command='present'), InlineKeyboardMarkup(btn)