from telegram import Update
from telegram.ext import CallbackContext
from googlesearch import search  
import google.generativeai as genai 

async def web_search(update: Update, context: CallbackContext):
    user_query = " ".join(context.args) if context.args else None

    if not user_query:
        await update.message.reply_text("❌ Please provide a search query.\nExample: `/websearch AI news`")
        return

    try:
        search_results = list(search(user_query))  

        if not search_results:
            await update.message.reply_text("❌ No results found. Try a different query.")
            return

        top_results = "\n".join(f"{idx+1}. {result}" for idx, result in enumerate(search_results[:5]))


        model = genai.GenerativeModel("gemini-1.5-flash") 
        prompt = f"Summarize the following search results in a concise way:\n{top_results}"
        summary_response = model.generate_content(prompt)

        ai_summary = summary_response.text if summary_response else "No summary available."

        response = f"🔎 **AI Search Summary:**\n\n_{ai_summary}_\n\n🔗 **Top Results:**\n{top_results}"

        await update.message.reply_text(response, disable_web_page_preview=True, parse_mode="Markdown")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error fetching results: `{e}`")
