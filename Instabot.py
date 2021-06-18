from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("sample.png", caption="sample caption")

######  follow someone #######
bot.follow("cool_programmer7")

######  send a message #######
bot.send_message("Hello", ['user's name'])

######  get follower info #######

followers = bot.get_user_followers("your username")
for follower in followers:
    print(follower)
