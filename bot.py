import telebot
from google import genai

TELEGRAM_BOT_TOKEN = "6201776250:AAESRNvFpmiVLGGxA49jmCFaOMuwk6M_V6s"

client = genai.Client(
    api_key="AQ.Ab8RN6IEK5-nRKP1gGvo4zK7QuAtslvtW7jvJ-Sn-01BOgUAXw",
)

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

tools = [
    {
        'type': 'google_search',
    },
]

generation_config = {
    'max_output_tokens': 65536,
    'thinking_level': 'medium',
}

@bot.message_handler(func=lambda message: True)
def handle_telegram_message(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')

        interaction = client.interactions.create(
            model='models/gemini-3.8-flash',
            input=message.text,
            tools=tools,
            generation_config=generation_config,
        )

        bot_reply = interaction.steps[-1]
        bot.reply_to(message, str(bot_reply))

    except Exception as e:
        bot.reply_to(message, f"خطأ: {str(e)}")

print("البوت شغال الآن في السحاب بنجاح!")
bot.infinity_polling()
