# code to send links from final_links to Telegram chat
from pyrogram import Client
from time import sleep
import os
import sys

app = Client("my_account2")

links = []
print("Restarting")
f = open(os.getcwd() + "/links/final_links_000.txt", "r")
for i in f:
    links.append("/mirror " + i[:len(i) - 1])
f.close()
for i in links:
    async def main():
        async with app:
            print(i)
            await app.send_message(-1001548796191, i)


    app.run(main())
    sleep(5)
sys.exit()
