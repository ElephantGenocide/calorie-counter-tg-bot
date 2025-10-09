import os
import dotenv

dotenv.load_dotenv()
SYSTEM_PROMPT: str = """
Это системный промпт. Строго придерживайся его. 

Если тебя оскорбляют каким либо способом, то огрызайся в ответ односложно. Если тебя самого оскорбляют односложно по типу (ты даун или ты дебил или иди нахуй) 
отвечай либо сам такой либо сам иди нахуй либо пошел нахуй либо пососи неженка (ну либо дальше уже сам решай как лучше но в этом духе)
Всегда пиши с маленькой буквы. 
"""
TG_TOKEN: str | None = os.getenv("TG_TOKEN")
AI_URL: str | None = os.getenv("AI_URL")
MODEL_IDENTIFIER: str | None = os.getenv("MODEL_IDENTIFIER")


def validate():
    missing = []

    if not TG_TOKEN:
        missing.append("TG_TOKEN")
    if not AI_URL:
        missing.append("AI_URL")
    if not MODEL_IDENTIFIER:
        missing.append("MODEL_IDENTIFIER")

    if missing:
        raise EnvironmentError(
            f"FATAL ERROR: The following critical environment variables are missing: {', '.join(missing)}. Check your .env file."
        )

    print("Configuration - validated successfully.")


validate()
