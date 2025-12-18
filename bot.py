from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

TOKEN = "توکن_جدید_اینجا"
CHANNEL_ID = "@BaKrayon"
ADMINS = [123456789]

def is_admin(uid):
    return uid in ADMINS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    await update.message.reply_text("🌟 بات «با کرایون» فعال است")

async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    text = " ".join(context.args)
    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=text + "\n\n— با کرایون | آگاهی · انرژی · تحول"
    )

async def energy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return
    msgs = [
        "✨ کد امروز فعال شد",
        "🌀 هماهنگی در جریان است",
        "🔹 دانایی در جریان است"
    ]
    await update.message.reply_text(msgs[datetime.datetime.now().day % 3])

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("post", post))
app.add_handler(CommandHandler("energy", energy))

app.run_polling()
