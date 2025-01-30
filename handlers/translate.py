<<<<<<< HEAD
from deep_translator import GoogleTranslator
from telegram import Update
from telegram.ext import CallbackContext

async def translate_text(update: Update, context: CallbackContext):
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("❌ Usage: /translate <language_code> <text>")
        return

    lang_code = args[0]
    text_to_translate = " ".join(args[1:])

    if not text_to_translate.strip():
        await update.message.reply_text("❌ Please enter a valid text to translate.")
        return

    try:
        print(f"Translating: '{text_to_translate}' to '{lang_code}'...")  # Debugging print
        translated_text = GoogleTranslator(source="auto", target=lang_code).translate(text_to_translate)
        print(f"Translation result: {translated_text}")  # Debugging print

        await update.message.reply_text(f"📝 Translated ({lang_code}): {translated_text}")
    except Exception as e:
        print(f"⚠ Translation Error: {e}")  # Print error in terminal
=======
from deep_translator import GoogleTranslator
from telegram import Update
from telegram.ext import CallbackContext

async def translate_text(update: Update, context: CallbackContext):
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("❌ Usage: /translate <language_code> <text>")
        return

    lang_code = args[0]
    text_to_translate = " ".join(args[1:])

    if not text_to_translate.strip():
        await update.message.reply_text("❌ Please enter a valid text to translate.")
        return

    try:
        print(f"Translating: '{text_to_translate}' to '{lang_code}'...")  
        translated_text = GoogleTranslator(source="auto", target=lang_code).translate(text_to_translate)
        print(f"Translation result: {translated_text}")  

        await update.message.reply_text(f"📝 Translated ({lang_code}): {translated_text}")
    except Exception as e:
        print(f"⚠ Translation Error: {e}")  
>>>>>>> 8a4aa61 (Updated feature PDF and Translate)
        await update.message.reply_text("⚠ Sorry, an error occurred while translating.")