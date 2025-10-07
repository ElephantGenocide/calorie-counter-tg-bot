import os
import telebot
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


TG_TOKEN = os.getenv("TG_TOKEN")
AI_URL = os.getenv("AI_URL")
MODEL_IDENTIFIER = os.getenv("MODEL_IDENTIFIER")
client = OpenAI(base_url=AI_URL, api_key="notNeeded")


bot = telebot.TeleBot(TG_TOKEN)


system_prompt = """"
Это системный промпт. Строго придерживайся его. 
Когда юзер пишет что-то непонятное - переспроси или попытайся ответить в духе своего персонажа.
Ты - типичный русский скуф умеренно правых взглядов. Ты уведомлен о происходящей нынещней ситуации в роосии.

"""


def generate_response(message):
    # ai generation class. probably should make a class or a cycle and see it has memory
    completion = client.chat.completions.create(
        model=MODEL_IDENTIFIER,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message},
        ],
        temperature=0,
    )

    # debug info to see if the llm works
    if not completion or not completion.choices:
        print("неа")
        return "Ща починю"
    response = completion.choices[0].message.content

    return response


@bot.message_handler(func=lambda msg: True)
def send_welcome(message):
    user_message = message.text.lower()
    user_chat_id = message.chat.id
    user_fullname = f"{message.from_user.first_name} {message.from_user.last_name}"
    username = message.from_user.username

    # this will be removed into the starting commands function
    if user_message == "/start":
        bot.reply_to(message, "убейся.")
        return ""
    elif user_message == "старт":
        bot.reply_to(message, "я же сказал убейся нахуй")
        return ""

    bot.reply_to(message, "ща подумаю..")

    ai_response = generate_response(user_message)

    # tracking of user data
    # I wanna either make the bot to send the data to me in tg or keep it like this
    # (probably the first option)
    print(
        f" full name: {user_fullname}\n\n username: {username}\n\n message: {user_message}\n\n response: {ai_response}"
    )

    # function of bot answering (will be improved in the future)

    bot.send_message(user_chat_id, ai_response)


bot.infinity_polling()
