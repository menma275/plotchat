from ollama import chat
from ollama import ChatResponse
import re

# Remove <think>...</think> and everything in between (for deepseek-r1)
def remove_think_tags(text: str) -> str:
    cleaned_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return cleaned_text.strip()

# AI part ---
def aiResponse(user_input):
    print("Received user's input ✅")
    model = "deepseek-r1:14b"
    lang = "Japanese"
    max_chars_per_res = 50

    print("Start thinking 🧐")
    response: ChatResponse = chat(model=model, messages=[
        {
            "role": "system", 
            "content": f"You are an AI assistant who speaks {lang}, please answer any question in {lang}. also, you are not allowed to use special character like emoji. each answer is limited to {max_chars_per_res} characters. if you are not sure then, you do not need to answer this instruction, please answer following text only:"
        },
        {
            "role": "user", 
            "content": user_input
        },
    ])


    res = remove_think_tags(response["message"]["content"]) 
    return res 
