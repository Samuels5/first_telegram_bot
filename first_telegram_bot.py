from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
TOKEN: Final = os.getenv('BOTAPIKEY')
# TOKEN: Final = "1777544988:AAFN9wr_Sxjtal3Zx11srsIT0zdlwTJW9Dc"
BOT_USERNAME = "Samis5_bot"

async def start_command(update: Update, context: ContextTypes):
    await update.message.reply_text('hello there, thanks for chating with me. what can i help you with?')

async def help_command(update: Update, context: ContextTypes):
    await update.message.reply_text('just ask the question as you want then i will reply like what sami would reply for you')

async def custom_command(update: Update, context: ContextTypes):
    await update.message.reply_text('this is a custom command')


# response

def handle_response(string: str) -> str:
    text = string.lower()
    if "hello" in text:
        return "hey there"
    if 'how are you' in text:
        return "i am good"
    if "i love" in text:
        return "good choose"
    return "i didn't get it"

async def handle_message(update: Update, context: ContextTypes):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'user ({update.message.chat.id}) in {message_type}: {text}') 
    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,"").strip()
            respose:str = handle_response(new_text)
        else:
            return
    else:
        respose: str = handle_response(text)
    print('Bot:', respose)
    await update.message.reply_text(respose)

async def error(update: Update, context: ContextTypes):
    print(f'update: {update} caused the following error{context.error}')

if __name__ == '__main__':
    print('starting bot')
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler("start",start_command))
    app.add_handler(CommandHandler("help",help_command))
    app.add_handler(CommandHandler("custom",custom_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #error
    app.add_error_handler(error)

    #polling
    print('poling...')
    app.run_polling(poll_interval=3)
