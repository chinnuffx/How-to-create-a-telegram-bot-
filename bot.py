import telebot
import time

BOT_TOKEN = "Your_bot_token"
bot = telebot.TeleBot(BOT_TOKEN)

love_messages = [
    "Love you 💞 Baby 🤍🖤",
    "Miss you so much 🥺💖",
    "You're my favorite person 💘",
    "Can't stop thinking about you 😍",
    "You make my world better 🌍💞",
    "Forever yours ❤️✨",
    "My heart is all yours 💓"
]

@bot.message_handler(func=lambda message: True)
def reply(message):
    chat_id = message.chat.id

    # 7 messages
    for i, msg in enumerate(love_messages, start=1):
        bot.send_message(chat_id, f"{i}. {msg}")
        time.sleep(0.4)

    # OPTION 1: three separate dot messages
    bot.send_message(chat_id, ".")
    time.sleep(0.3)
    bot.send_message(chat_id, ".")
    time.sleep(0.3)
    bot.send_message(chat_id, ".")
    time.sleep(0.3)

    # OPTION 2 (use instead of above if you want single line)
    # bot.send_message(chat_id, ".............")
    # time.sleep(0.5)

    # Final message
    bot.send_message(chat_id, "7 Thala For a Reason 🗣️")

print("Bot started...")
bot.infinity_polling()
