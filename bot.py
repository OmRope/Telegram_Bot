import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from handlers.registrations import start, handle_contact
from handlers.chat import chat_with_gemini
from handlers.image_analysis import analyze_file
from handlers.web_search import web_search
from handlers.translate import translate_text

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.CONTACT, handle_contact))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_gemini))
    application.add_handler(MessageHandler(filters.PHOTO | filters.Document.ALL, analyze_file))
    application.add_handler(CommandHandler("websearch", web_search))
    application.add_handler(CommandHandler("translate", translate_text))

    print("Bot running")
    application.run_polling()

if __name__ == "__main__":
    main()
