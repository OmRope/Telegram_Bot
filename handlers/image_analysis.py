import google.generativeai as genai
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import CallbackContext
from database import get_files_collection
from PIL import Image
import io
import pymupdf as fitz 

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def analyze_file(update: Update, context: CallbackContext) -> None:
    """Handles file/image analysis using Gemini AI."""
    file = update.message.document or update.message.photo[-1]
    file_id = file.file_id
    file_info = await context.bot.get_file(file_id)
    file_data = await file_info.download_as_bytearray()

    file_name = getattr(file, "file_name", "Image") 

    try:
        if update.message.document:  
            mime_type = file.mime_type

            if mime_type.startswith("image/"): 
                image = Image.open(io.BytesIO(file_data))
                content = ["Describe this image:", image]

            elif mime_type == "application/pdf":  
                pdf_doc = fitz.open(stream=file_data, filetype="pdf")
                text = "\n".join([page.get_text() for page in pdf_doc])
                content = f"Describe the following PDF content: {text}" 

            else:
                await update.message.reply_text("❌ Unsupported file type.")
                return

        else:  
            image = Image.open(io.BytesIO(file_data))
            content = ["Describe this image:", image]

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(content)

        if response and response.candidates:
            description_text = response.candidates[0].content.parts[0].text
        else:
            description_text = "No description available."

        get_files_collection().insert_one({
            "chat_id": update.message.chat_id,
            "file_id": file_id,
            "file_name": file_name,
            "description": description_text
        })

        await update.message.reply_text(f"📄 **File Analysis:** {description_text}")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")
