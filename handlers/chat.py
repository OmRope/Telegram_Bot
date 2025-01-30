import google.generativeai as genai
from telegram import Update
from telegram.ext import CallbackContext
from database import get_chat_collection
import os
from pymongo import MongoClient

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def chat_with_gemini(update: Update, context: CallbackContext):
    user_message = update.message.text  # Get user input
    chat_id = update.message.chat_id

    if not user_message:
        await update.message.reply_text("❌ Please provide a message.")
        return

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)
        print(response)
        response_text = str(response._result.candidates[0].content.parts[0].text)
        print("RESPONSE :",response_text)

        get_chat_collection().insert_one({
            "chat_id": chat_id,
            "user_message": user_message,
            "bot_response": response_text,  
            "timestamp": update.message.date
        })

        await update.message.reply_text(response_text)

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")
