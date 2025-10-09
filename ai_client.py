from openai import OpenAI
from config import SYSTEM_PROMPT, AI_URL, MODEL_IDENTIFIER


client = OpenAI(base_url=AI_URL, api_key="notNeeded")  # type: ignore


def generate_ai_response(user_message: str) -> str | None:
    try:
        completion = client.chat.completions.create(
            model=MODEL_IDENTIFIER,  # type: ignore
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            temperature=0,
        )

        if not completion or not completion.choices:
            print("DEBUG: API returned empty completion or choices list.")
            return "Я поломался сука доволен??!?!?! Жди пока починят."

        response: str | None = completion.choices[0].message.content
        return response

    except Exception as e:
        print(f"ERROR during AI generation: {e}")
        return "Что-то сломалось в моём компьютере. Попробуй позже."
