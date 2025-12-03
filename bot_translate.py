import os
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext
from googletrans import Translator

TOKEN = "8369100535:AAHR9CpRr4rffGFXQ5RMTstA2DBXP1kP3eU"

translator = Translator()

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "👋 Halo!\nKirim teks bahasa apa saja → saya terjemahkan ke Indonesia 🇮🇩"
    )

def translate_to_id(update: Update, context: CallbackContext):
    text = update.message.text

    try:
        result = translator.translate(text, dest='id')
        update.message.reply_text(
            f"🌍 Dari: {result.src}\n"
            f"🇮🇩 Hasil:\n{result.text}"
        )
    except:
        update.message.reply_text("❌ Gagal menerjemahkan")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_to_id))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
