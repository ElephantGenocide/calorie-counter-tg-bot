import telebot
from config import TG_TOKEN
from tg_handlers import register_handlers


def main():
    bot = telebot.TeleBot(TG_TOKEN)  # type: ignore
    print("Telegram Bot Client initialized.")

    # Handlers are registered with the bot
    register_handlers(bot)
    print("Message handlers registered.")

    print("Starting bot polling...\n\n")
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"FATAL ERROR: Bot polling stopped due to an exception: {e}")


if __name__ == "__main__":
    main()
