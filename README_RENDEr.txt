
# SmartBot (English Version)

This is a simple Telegram bot that:
- Greets users with a welcome message
- Waits for user messages
- Sends an automatic reminder if the user doesn't respond within 2 minutes

## 🚀 How to Run Locally
1. Make sure you have Python 3.10 installed
2. Install dependencies:
   pip install -r requirements.txt
3. Run the bot:
   python bot.py

## 🌐 How to Host on Render (Free)
1. Go to https://render.com and sign up
2. Click "New" → "Web Service"
3. Connect your GitHub repo (or upload this bot)
4. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
   - **Runtime**: Python 3.10
5. Add an environment variable:
   - `BOT_TOKEN=your_bot_token`

Done! Your bot will now stay online 24/7 on Render's free tier.
