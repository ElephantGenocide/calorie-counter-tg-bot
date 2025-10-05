import os
import telebot
from dotenv import load_dotenv
from google import genai

load_dotenv()



TG_TOKEN = os.getenv("TG_TOKEN")
GEMINI_TOKEN = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=GEMINI_TOKEN)
bot = telebot.TeleBot(TG_TOKEN)

print(TG_TOKEN, GEMINI_TOKEN)
greetings = ["/start", "старт"]

def generate_response(message):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message,
    )
    return response.text

@bot.message_handler(func=lambda msg: True)
def send_welcome(message):
    user_message = message.text.lower()
    user_chat_id = message.chat.id

    if user_message == "/start":             
        bot.reply_to(message, "убейся.")
        return ""
    elif user_message == "старт":
       bot.reply_to(message, "я же сказал убейся нахуй")
       return ""
    
    print(user_message)

    bot.reply_to(message, "ща подумаю..")
    bot.send_message(user_chat_id, generate_response(user_message))


bot.infinity_polling()
