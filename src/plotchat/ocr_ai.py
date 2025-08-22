import asyncio
from ollama import chat
from ollama import ChatResponse


# AI part ---
async def ocrAi(img_base64, lang):
    print("📮 Received your message")

    model = "gemma3"

    print("👀 Reading...")
    response: ChatResponse = chat(
        model=model,
        messages=[
            # {
            #     "role": "system",
            #     "content": f"You are an AI assistant who speaks {lang}. this is a image which includes {lang} texts. so please return the {lang} text in this picutre. answer does not need to include any explaination."
            # },
            {
                "role": "user",
                "content": f"You are an AI assistant who speaks {lang}. A user has extracted some text from an image. Your task is to return the clean and readable version of the following {lang} text, with no explanation or commentary.",
                "images": [img_base64],
            }
        ],
    )

    res = response["message"]["content"]
    print("Your message is... " + res)

    return res
