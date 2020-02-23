from telegram.ext import Updater, CommandHandler # import modules

TOKEN = '807791564:AAGpeP6bb5tNzSldfyr2d8byolg1yzPzzI8' #WEBLOCTEST_BOT TOKEN KEY

def check_id(bot, update):
    try:
        id = update.message.chat.id
        print('Chat ID', id)
        return id
    except:
        id = update.channel_post.chat.id
        return id

def check_nickname(bot, update):
    try:
        nickname = update.message.from_user.first_name
        print('Chat NickName', nickname)
        return nickname
    except:
        nickname = update.channel_post.from_user.first_name
        return nickname

def start_command(bot, update):
    id = check_id(bot, update)
    nickname = check_nickname(bot, update)
    bot.send_message(chat_id=id, text="안녕하세요 " + nickname +"! 새로운 챗봇입니다!\n\n")

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start_command))

updater.start_polling(poll_interval=0.0,
                          timeout=10,
                          clean=False,
                          bootstrap_retries=0)
updater.idle()