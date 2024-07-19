from kahoot import client
bot = client()
bot.join(input("Code: "),"KahootPY")
def joinHandle():
  pass
bot.on("joined",joinHandle)