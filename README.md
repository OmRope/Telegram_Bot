# Telegram AI Chatbot

## Overview
This is a Telegram AI chatbot that provides the following functionalities:
- **User Registration:** Registers users and stores their details in MongoDB.
- **Chat with AI:** Uses Gemini AI to respond to user queries in real-time.
- **Image & File Analysis:** Users can send images and PDFs for AI-based analysis.
- **Web Search:** Fetches AI-generated web search summaries for user queries.
- **Language Translation:** Translates text into multiple languages.
- **Session Management:** Ensures users register before accessing chatbot features.

## Features
### 1. **User Registration & Interactive Menu**
- Upon first interaction, users are prompted to register.
- First name, username, and chat ID are stored in MongoDB.
- Users must share their phone number via the Telegram contact button.

### 2. **Chat with AI (Gemini-Powered)**
- Users can enter queries in natural language.
- The chatbot responds with intelligent and context-aware answers.
- AI remembers short-term context for smoother conversations.

### 3. **Image & File Analysis**
- Users can send **images (JPG, PNG)** or **PDFs** to the bot.
- The bot uses AI to analyze content and provide descriptions.
- Use cases include object detection, scene recognition, and OCR (text extraction from PDFs/images).

### 4. **Web Search with AI Summary**
- Users can perform web searches by entering queries.
- The bot fetches top web results and generates a concise AI summary.
- Provides clickable links for further exploration.

### 5. **Language Translation**
- Users can translate text into multiple languages.
- Supported format: `/translate <language_code> <text>`
- Example: `/translate es Hello, how are you?` → "Hola, ¿como estas?"

## Installation & Setup
### **1. Clone the Repository**
```bash
git clone https://github.com/OmRope/Telegram_Bot.git
cd Telegram_Bot
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run the Bot**
```bash
python bot.py
```

## Usage
- Start the bot by typing `/start`.
- Register by providing your full name and sharing your phone number.
- Choose from the available options in the interactive menu:
  - 💬 Chat with AI (Gemini-powered)
  - 📷 Image & File Analysis
  - 🔎 AI-Powered Web Search
  - 🌍 Language Translation

## Contribution
1. Fork the repository.
2. Make necessary changes.
3. Submit a pull request.

## License
This project is licensed under the **MIT License**.

---
For any issues or suggestions, feel free to open an issue on GitHub. 🚀

