# code to send links from final_links to Telegram chat
from pyrogram import Client
from time import sleep

app = Client("my_account2")

links = []
print("Restarting")
f = open("final_links1.txt", "r")
for i in f:
    links.append("/mirror " + i[:len(i) - 1])
f.close()

for i in links:
    async def main():
        async with app:
            print(i)
            await app.send_message(-1001548796191, i)


    app.run(main())

    sleep(10)
