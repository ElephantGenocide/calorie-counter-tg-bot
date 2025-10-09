import telebot
from ai_client import generate_ai_response


def register_handlers(bot: telebot.TeleBot):
    @bot.message_handler(commands=["start"])
    def _handle_start_command(message):
        bot.reply_to(message, "убейся.")

    @bot.message_handler(func=lambda msg: True)
    def _handle_all_messages(message):
        user_message = message.text
        user_chat_id = message.chat.id

        sent_message = bot.reply_to(message, "🤔")

        ai_response: str = generate_ai_response(user_message)  # type: ignore

        user_fullname = f"{message.from_user.first_name} {message.from_user.last_name}"
        username = message.from_user.username

        print("--- USER INTERACTION ---")
        print(f"Full Name: {user_fullname}")
        print(f"Username: {username}")
        print(f"Message: {user_message}")
        print(f"Response: {ai_response}")
        print("------------------------\n\n")

        bot.edit_message_text(
            chat_id=user_chat_id, message_id=sent_message.message_id, text=ai_response
        )
