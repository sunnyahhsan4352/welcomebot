
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import asyncio
from datetime import datetime

# Store user last activity
user_last_active = {}

# Bot Token
BOT_TOKEN = "8125058608:AAHFjGxSsTO0QoESqC-MkH_1WKSIh7Ed7h4"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_last_active[user_id] = datetime.now()
    await update.message.reply_text(
        "👋 Hello! Welcome to SmartBot.

You can chat with me freely. I'll remind you if you go quiet. 😊"
    )
    asyncio.create_task(send_reminder(update, context, delay=120))

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_last_active[user_id] = datetime.now()
    await update.message.reply_text("Thanks for your message! Feel free to continue. 👍")

# Auto reminder if user inactive
async def send_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE, delay=120):
    await asyncio.sleep(delay)
    user_id = update.effective_user.id
    last_time = user_last_active.get(user_id)

    if last_time and (datetime.now() - last_time).total_seconds() >= delay:
        await context.bot.send_message(chat_id=user_id, text="You're a bit quiet! Say something 😊")

# Main function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
