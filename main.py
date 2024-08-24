from typing import Final
from telegram import Update  
from telegram.ext import *
from dotenv import load_dotenv as l
import ChatBot_Ai as google
import os

l()

TOKEN:Final = os.getenv("telegram_api")
BOT_Name:Final = "@Oneknown3bot"

help_menu  = """
    /start = Start the bot
    /help = Display help menu
    /fact 4 = Usage /fact number
    /ask simple joke   
    /myinfo = Display info
            """

# Commands
async def start_cmd(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hello! {update.message.chat.first_name}")
    


async def help_cmd(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(help_menu)

async def fact_cmd(update:Update,context:ContextTypes.DEFAULT_TYPE):
    try:
        num = int((update.message.text).split()[1])
    except Exception:
        num = 0 
        await update.message.reply_text(f"please pass number after fact")
    if num > 1000:
        await update.message.reply_text(f"please give number under 10000")
    else:
        f =1 
        for i in range(1,num+1):
            f*=i
    await update.message.reply_text(f"factoria {num} = {f}")

async def fetchmyDetail_cmd(update:Update,context:ContextTypes.DEFAULT_TYPE):
    user = f"Account Name = {update.message.chat.first_name}"
    usernm = f"Username @{update.message.chat.username}"

    await update.message.reply_text(f"Info:\n{user}\n{usernm}")

async def AI_cmd(update:Update ,contex:ContextTypes.DEFAULT_TYPE):
    reponses = google.Ask(update.message.text.split('/ask')[1].strip())
    await update.message.reply_markdown(reponses)
    
# Responses

def handle_reponses(text:str ) -> str:
    text = text.lower()
    if "hello" in text:
        return "Hello User"
    
    if "about" in text:
        return "i am a Bot"
    
    if "how are you" in text:
        return "i am Fine , What about u"
    
    if "who are u " in text:
        return "I am OneKnown bot"
    
    return google.default_reply(text)
    
    #return "sorry ,i can't answer your question"


async def handle_msg(update:Update,context:ContextTypes.DEFAULT_TYPE):
    msg_type:str =update.message.chat.type
    text:str = update.message.text

    print(f"User({update.message.chat.id}) in {msg_type}: '{text}'")

    if msg_type == "group":
        if BOT_Name in text:
            new_text:str = text.replace(BOT_Name,'').strip()
            reponses:str = handle_reponses(new_text)
        else:
            return
    else:
        reponses:str = handle_reponses(text)
    
    print('Bot',reponses)
    await update.message.reply_text(reponses)

async def error(update:Update,context:ContextTypes.DEFAULT_TYPE):
    print(f'{update} caused error {context.error}')

if __name__ == '__main__':
    print("starting bot ... ")
    app = Application.builder().token(TOKEN).build()

    # Configure request settings with timeouts
    # app.bot.request_kwargs = {
    #     'read_timeout': 20,
    #     'connect_timeout': 20
    # }
    #commands
    app.add_handler(CommandHandler('start',start_cmd))
    app.add_handler(CommandHandler('help',help_cmd))
    app.add_handler(CommandHandler('fact',fact_cmd))
    app.add_handler(CommandHandler('myinfo',fetchmyDetail_cmd))
    app.add_handler(CommandHandler('ask',AI_cmd))
    
    #Message
    #app.add_handler(MessageHandler(filters.TEXT),handle_msg)
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_msg))


    #Error
    app.add_error_handler(error)
    print("polling...")
    app.run_polling(poll_interval=5)