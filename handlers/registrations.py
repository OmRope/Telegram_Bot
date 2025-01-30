from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from database import get_users_collection

async def start(update: Update, context: CallbackContext) -> None:
    """Handles the /start command and registers the user."""
    print("START")
    user = update.message.from_user
    chat_id = update.message.chat_id
    users = get_users_collection()

    if users.find_one({"chat_id": chat_id}):
        await update.message.reply_text("You're already registered!")
    else:
        first_name = update.message.from_user.first_name
        username = update.message.from_user.username
        users.insert_one({
            "chat_id": chat_id,
            "first_name": first_name,
            "username": username,
            "phone_number": None
        })
        
        keyboard = [[KeyboardButton("Share Phone Number", request_contact=True)]]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        await update.message.reply_text("Please share your phone number:", reply_markup=reply_markup)

async def handle_contact(update: Update, context: CallbackContext) -> None:
    """Handles phone number collection."""
    print("HANDLE CONTACT")
    user = update.message.from_user
    chat_id = update.message.chat_id
    contact = update.message.contact
    users = get_users_collection()

    if contact and contact.user_id == user.id:
        users.update_one({"chat_id": chat_id}, {"$set": {"phone_number": contact.phone_number}})
        await update.message.reply_text("Thank you! Your phone number has been saved.")
    else:
        await update.message.reply_text("Please share your own contact.")

