import discord
from discord import app_commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


#commands lists

summon_animations = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_gogeta = [
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1027960_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1027270_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1026110_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1024910_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1026800_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1020020_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1019800_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1018980_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1019030_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1016070_thumb.png"
]

random_ssr_gogeta = [
    "<:SSR_eclair:971672682712141844> Random"
]

random_sr_gogeta = [
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1012940_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000030_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000090_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000110_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000850_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000870_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1000890_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1001620_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1002130_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1003750_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1004460_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_2000760_thumb.png",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

featured_ssr_broly = [
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1028020_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1028220_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1027200_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1025710_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1024810_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1022360_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1019970_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1018600_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1018630_thumb.png",
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1015990_thumb.png"
]

random_ssr_broly = [
    "<:SSR_eclair:971672682712141844>"
]

sr_broly = [
    "https://jpn.dokkan.wiki/assets/japan/character/thumb/card_1002470_thumb.png",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

discord_token = os.environ.get('DISCORD_TOKEN')

@client.event
async def on_ready():
	await client.change_presence(
	    status=discord.Status.online,
	    activity=discord.Game(name="Now with slash commands (/)"))
     
@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")


@app_commands.command(name="multigogeta", description="Multisummon 9th Anniversary event (Gogeta) [Carnival]")
async def multigogeta(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(summon_animations))
    channel = client.get_channel(1200486065245532223)
    for i in range(0, 9):
            number = random.randint(1, 10000)
            if number >= 9300:
                random2 = random.choice(featured_ssr_gogeta)
                await channel.send(random2)
            elif number >= 9000:
                await channel.send(random.choice(random_ssr_gogeta))
            elif number >= 3000:
                await channel.send(random.choice(random_sr_gogeta))
            else:
                await channel.send("<:R_eclair:971673105024045056> random")  
    await channel.send(random.choice(featured_ssr_gogeta))
    await channel.send("**Multisummon finished**")

tree.add_command(multigogeta)


@app_commands.command(name="multibroly", description="Multisummon 9th Anniversary event (Broly) [Dokkan festival]")
async def multibroly(interaction: discord.Interaction):
    channel = client.get_channel(1200486065245532223)
    await interaction.response.send_message(random.choice(summon_animations))
    for i in range(0, 9):
            number = random.randint(1, 10000)
            if number >= 9300:
                random2 = random.choice(featured_ssr_broly)
                await channel.send(random2)
            elif number >= 9000:
                await channel.send(random.choice(random_ssr_broly))
            elif number >= 3000:
                await channel.send(random.choice(sr_broly))
            else:
                await channel.send("<:R_eclair:971673105024045056> Random")  
    await channel.send(random.choice(featured_ssr_broly))
    await channel.send("**Multisummon finished**")

tree.add_command(multibroly)

@app_commands.command(name='probs',description='Probabilities of the current multisummons')
async def probs(interaction: discord.Interaction):
    embed=discord.Embed(title="Probabilities",  description="Probabilities of the multisummons", color=discord.Color.blue())
    embed.add_field(name="SSR featured:", value="5% <:SSR_eclair:971672682712141844> Featured | 95% <:SSR_eclair:971672682712141844> not featured", inline=False)
    embed.add_field(name="SSR not featured:", value="5% <:SSR_eclair:971672682712141844> Featured | 5% <:SSR_eclair:971672682712141844> not featured | 60% <:SR_eclair:971673046496731166> Random | 30% <:R_eclair:971673105024045056> Random", inline=False)
    embed.set_footer(text="Thank you for using the bot!")
    await interaction.response.send_message(embed=embed)

tree.add_command(probs)


@app_commands.command(name='ping',description='Returns the latency of the bot')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"pong! ({client.latency*1000:.2f} ms)")

tree.add_command(ping)

# bot token
client.run(discord_token)  
