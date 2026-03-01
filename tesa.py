import discord
from discord.ext import commands, tasks
import asyncio
import sys
import json
import msg
from dotenv import load_dotenv

load_dotend()

if len(sys.argv) < 2:
    print("Error: JSON config tidak diberikan.")
    sys.exit(1)

raw_config = sys.argv[1]
config = json.loads(raw_config)


place = config["place"]
channel_idbg = config["channel_idbg"]
channel_idsign = config["channel_idsign"]
channel_idplat = config["channel_idplat"]
channel_idconsumable = config["channel_idconsumable"]
channel_idblock = config ["channel_idblock"]
channel_idguild = config["channel_idguild"]
channel_test = config["channel_test"]
channel_iddoor = config["channel_iddoor"]
channel_winterfest = config["channel_winterfest"]
channel_ubiweek = config["channel_ubiweek"]
channel_carni = config["channel_carni"]
channel_valentine = config["channel_valentine"]

msg_bg = msg.msg_bg.replace("{place}", place)
msg_sign = msg.msg_sign.replace("{place}", place)
msg_plat = msg.msg_plat.replace("{place}", place)
msg_consumable = msg.msg_consumable.replace("{place}", place)
msg_block = msg.msg_block.replace("{place}",place)
msg_guild = msg.msg_guild.replace("{place}",place)
msg_door = msg.msg_door.replace ("{place}",place)
msg_winterfest = msg.msg_winterfest.replace("{place}",place)
msg_ubiweek = msg.msg_ubiweek.replace("{place}",place)
msg_carni = msg.msg_carnival.replace("{place}",place)
msg_valen = msg.msg_valen.replace("{place}",place)


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(),selfbot = True)

@bot.event
async def on_ready():
    print(f"[{place}] {bot.user.name} is online")
    print(f"[{place}] {bot.user.name} is online")
    channel = bot.get_channel(channel_test)
    if channel :
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        await channel.send(f"[{place}]  Bot is online at {now}")
    else:
        print(f"[{place}] Channel A (status) not found.")
    await asyncio.sleep(10)

    send_loop.start()
    send_loop1.start()

@tasks.loop(seconds=0, hours=2) 
async def send_loop():
    try:
        channel = bot.get_channel(channel_idbg)
        if channel:
            await channel.send(msg_bg)
            print(f"[{place}] Sent msg_bg")
        else:
            print(f"[{place}] Channel tidak ditemukan.")
    except discord.HTTPException:
        print(f"[{place}] Cooldown... Waiting 20s")
        await asyncio.sleep(20)
    try:
        await asyncio.sleep(5)
        channel = bot.get_channel(channel_idsign)
        await channel.send(msg_sign)
        print(f"[{place}] Sent msg_sign")
    
    except discord.errors.HTTPException:
        print("[Cooldown] sign too fast, waiting 20s...")
        await asyncio.sleep(20)

    try:
        await asyncio.sleep(5)
        channel = bot.get_channel(channel_idplat)
        await channel.send(msg_plat)
        print(f"[{place}] Sent msg_plat")

    except discord.errors.HTTPException:
        print("[Cooldown] plat too fast, waiting 20s...")
        await asyncio.sleep(20)
    try:
        await asyncio.sleep(5)
        channel = bot.get_channel(channel_idconsumable)
        await channel.send(msg_consumable)
        print(f"[{place}] Sent msg_consumable")

    except discord.errors.HTTPException:
        print("[Cooldown] plat too fast, waiting 20s...")
        await asyncio.sleep(20)
    try:
        await asyncio.sleep(5)
        channel = bot.get_channel(channel_idguild)
        await channel.send(msg_guild)
        print(f"[{place}] Sent msg_guild")

    except discord.errors.HTTPException:
        print("[Cooldown] plat too fast, waiting 20s...")
        await asyncio.sleep(20)
    try:
        await asyncio.sleep(5)
        channel = bot.get_channel(channel_iddoor)
        await channel.send(msg_door)
        print(f"[{place}] Sent msg_door")
    except discord.errors.HTTPException:
        print("[Cooldown] plat too fast, waiting 20s...")
        await asyncio.sleep(20)
    try:
        await asyncio.sleep(5)
        channel = bot.get_channel(channel_winterfest)
        await channel.send(msg_winterfest)
        print(f"[{place}] Sent msg_winterfest")
    except discord.errors.HTTPException:
        print("[Cooldown] plat too fast, waiting 20s...")
        await asyncio.sleep(20)
    try:
        await asyncio.sleep(5)
        channel = bot.get_channel(channel_ubiweek)
        await channel.send(msg_ubiweek)
        print(f"[{place}] Sent msg_ubiweek")
    except discord.errors.HTTPException:
        print("[Cooldown] plat too fast, waiting 20s...")
        await asyncio.sleep(20)
    # try:
    #     await asyncio.sleep(5)
    #     channel = bot.get_channel(channel_carni)
    #     await channel.send(msg_carni)
        # print(f"[{place}] Sent msg_carni")

    # except discord.errors.HTTPException:
    #     print("[Cooldown] plat too fast, waiting 20s...")
    #     await asyncio.sleep(20)
    try:
        await asyncio.sleep(5)
        channel = bot.get_channel(channel_valentine)
        await channel.send(msg_valen)
        print(f"[{place}] Sent msg_valen")

    except discord.errors.HTTPException:
        print("[Cooldown] plat too fast, waiting 20s...")
        await asyncio.sleep(20)
@tasks.loop(seconds=0, hours=6)
async def send_loop1():
    try:
        await asyncio.sleep(5)
        channel = bot.get_channel(channel_idblock)
        await channel.send(msg_block)
        print(f"[{place}] Sent msg_block")

    except discord.errors.HTTPException:
        print("[Cooldown] block too fast, waiting 20s...")
        await asyncio.sleep(20)
# token

bot.run("",bot = False)  
