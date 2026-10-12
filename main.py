import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is missing. Add your token in the hosting platform's Secrets/Variables.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 👋 به ربات شیکاگو خوش اومدی.\n\n"
        "دستورهای من:\n"
        "/start - شروع\n"
        "/help - راهنما\n"
        "/id - نمایش شناسه عددی خودت"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "راهنمای ربات شیکاگو 🏙️\n"
        "/start - شروع ربات\n"
        "/help - راهنما\n"
        "/id - شناسه عددی تلگرام شما\n\n"
        "امکانات بیشتر را بعداً می‌توانیم به ربات اضافه کنیم."
    )

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if user:
        await update.message.reply_text(f"شناسه عددی شما: {user.id}")

async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("پیامت رسید 🙂 برای دیدن دستورها /help رو بزن.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("id", id_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_text))
    print("Chicago bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
