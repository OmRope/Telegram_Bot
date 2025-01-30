import google.generativeai as genai
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext
from database import get_files_collection
from PIL import Image
import io

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def analyze_file(update: Update, context: CallbackContext) -> None:
    """Handles file/image analysis using Gemini AI."""
    file = update.message.document or update.message.photo[-1]
    file_id = file.file_id
    file_info = await context.bot.get_file(file_id)
    file_path = file_info.file_path

    file_data = await file_info.download_as_bytearray()
    image = Image.open(io.BytesIO(file_data))
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
                    ["Describe this image:", image]  
                    )

        if response and response.candidates:
            description_text = str(response.candidates[0].content.parts[0].text)
        else:
            description_text = "No description available."

        print("RESPONSE :",description_text)
        get_files_collection().insert_one({
            "chat_id": update.message.chat_id,
            "file_id": file_id,
            "file_name": file.file_name if hasattr(file, "file_name") else "Image",
            "description": description_text
        })

        await update.message.reply_text(f"Analysis: {description_text}")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")