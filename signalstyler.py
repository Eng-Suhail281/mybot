from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from datetime import datetime

# إعداداتك
BOT_TOKEN = "8217048518:AAFmuirZv3RluA-CorQpSduTjg_jS_SsOIQ"
CHANNEL_ID = "@tttessstty"

# قالب التنسيق الجمالي
def format_message(raw_text: str) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""
<pre>{raw_text}</pre>

📅 <b><i>{now}</i></b>
<i>🧠 تذكير: لا تنس إدارة رأس المال!</i>
<b>X TRADING</b>♟️.
"""

# التعامل مع الرسائل الخاصة
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == 'private':
        raw_text = update.message.text
        formatted = format_message(raw_text)
        await context.bot.send_message(chat_id=CHANNEL_ID, text=formatted, parse_mode="HTML")
        await update.message.reply_text("✅ تم النشر في القناة بتنسيق احترافي.")

# تشغيل البوت
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
