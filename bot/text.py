def dictionary(language, command, people=None, user=None):

    dict = {
        'uzb': {
            'start': """Siz uning ovozini minglab boshqa ovozlar orasidan taniysiz 🥰\nBiz nihoyatda go‘zal iqtidor sohibasi Sevara Nazarxon bilan o‘tkaziladigan o‘yin boshlanayotganini rasman e’lon qilamiz 🎉🎊\nIshtirok eting va PlayStation 5 vaaaa… MacBook Air yutib oling! 😎\nO‘yinning barcha shartlarini bu yerdan topasiz:""",
            'present': """🎁 Barcha kanallarga obuna bo‘lgandan so‘ng "Ishtirok etishni tekshirish" tugmasini bosing.\n\nO‘yin o‘tadigan sana: 2023 yil 20 sentabr.""",
            'subscribed': f"""Sizning ID: {user.id}\n\n✅ PlayStation 5\n\n❌ MacBook Air o'yini ishtirokchisi (sizning do‘stlaringiz ham kanallarga obuna bo‘lishi kerak, kamida 2 do'st)\n\nAktivlangan do‘stlaringiz soni: {people} dona.\n\nO‘yin o‘tadigan sana: 2023 yil 20 sentabr.""",
            "subscribed2": f"Sizning ID: {user.id}\n\n✅ PlayStation 5\n\n✅ MacBook Air o'yini ishtirokchisi\n\nAktivlangan do‘stlaringiz soni: {people}  dona.\n\nO‘yin o‘tadigan sana: 2023 yil 20 sentabr.",
            'check': "☑️Ishtirok etishni tekshirish",
            'phone': "📞 Raqamni yuborish",
            'phone text': """Ro'yhatdan o'tish uchun o'z telefon raqamingizni +998xxxxxxxxx formatda yuboring yoki "📞 Raqamni yuborish" tugmasini bosing""",
            "yourfriendsubscribed": f"""🎁 Sizning do'stingiz {user.first_name} tanlovning barcha shartlarini bajardi va sizning referalingizga aylandi""",
            'phone error': "Raqamni yuborish knopkasini bosing👇",
            "error": "Xatolik⚠",
            'link_share': "🔗 Havola blan o'rtoqlashish"
        },
        'rus':  {
            'start': "Вы узнаете ее голос среди тысяч других голосов 🥰\nМы официально объявляем о старте игры с удивительно красивым талантом Севарой Назархан 🎉🎊\nУчаствуйте и выигрывайте PlayStation 5 ваааааа… MacBook Air! 😎\nВсе условия игры вы найдете здесь:",
            "present": """🎁 После подписки на все каналы нажмите кнопку "☑️Проверка подписку".\n\nДата розыгрыша: 20 сентября 2023 г.""",
            'subscribed': f"Ваш ID: {user.id}\n\n ✅ PlayStation 5\n\n❌ Участник игры MacBook Air (ваши друзья также должны быть подписаны на каналы, минимум 2 друга)\n\nВаше активированное количество друзей: {people} ед.\n\nДата розыгрыша: 20 сентября 2023 г.",
            "subscribed2": f"Ваш ID: {user.id}\n\n✅ PlayStation 5\n\n✅ Участник игры MacBook Air\n\nКоличество активированных друзей: {people}.\n\nДата игры: 20 сентября 2023 года",
            "check": "☑️Проверка подписку",
            "phone": "📞 Отправить номер",
            "phone text": """Для регистрации отправьте свой номер телефона в формате +998xxxxxxxxx или нажмите кнопку "📞 Отправить номер" """,
            "yourfriendsubscribed": f"""🎁 Ваш друг {user.first_name} выполнил все условия конкурса и стал вашим рефералом""",
            'phone error': "Нажмите кнопку Отправить номер👇",
            "error": "Ошибка⚠",
            'link_share': "🔗 Поделись ссылкой"
        }
    }
    return dict[language][command]
