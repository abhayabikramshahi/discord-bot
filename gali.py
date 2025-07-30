import discord
from discord.ext import commands
from discord import app_commands
import random
import os
from dotenv import load_dotenv

# ====== Load Token from .env ======
load_dotenv()
TOKEN = os.getenv("INTERACTION_AI")

# ====== Bot Intents ======
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# ====== Create Bot & Command Tree ======
bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

# ====== Data ======
flirty_lines = [
    "Are you made of copper and tellurium? Because you're Cu-Te 💘",
    "Do you have a name, or can I call you mine? 😏",
    "Are you a magician? Because whenever I look at you, everyone else disappears.",
]

code_snippets = {
    "php": "<?php echo 'Hello, World!'; ?>",
    "hack": "nmap -sS -T4 target.com",
    "python": "print('Hello from your bot!')"
}

# ====== Events ======

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await tree.sync()
        print(f"✅ Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"❌ Sync failed: {e}")

# ====== Slash Commands ======

@tree.command(name="code", description="📜 Get a code snippet")
@app_commands.describe(topic="Choose a language: php, hack, or python")
async def code(interaction: discord.Interaction, topic: str):
    topic = topic.lower()
    if topic in code_snippets:
        await interaction.response.send_message(
            f"🧠 Here's your `{topic}` code:\n```{code_snippets[topic]}```"
        )
    else:
        await interaction.response.send_message(
            "❌ Unknown topic. Try: `php`, `hack`, or `python`."
        )

@tree.command(name="talk", description="💬 Start a casual chat with the bot")
async def talk(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hey {interaction.user.mention}! Let's talk 😊 Ask me anything."
    )

@tree.command(name="hi", description="👋 Say hi to the bot")
async def hi(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hii {interaction.user.name}! ❤️ How's your day?")

@tree.command(name="howareyou", description="😊 Ask how the bot is doing")
async def howareyou(interaction: discord.Interaction):
    await interaction.response.send_message("I'm good! Just vibin' in the cloud ☁️ What about you?")

@tree.command(name="flirt", description="😏 Get a flirty pickup line")
async def flirt(interaction: discord.Interaction):
    line = random.choice(flirty_lines)
    await interaction.response.send_message(f"😏 {line}")

@tree.command(name="bye", description="👋 Say bye to the bot")
async def bye(interaction: discord.Interaction):
    await interaction.response.send_message("👋 Bye bye! See ya soon!")

@tree.command(name="help", description="📘 Show all bot commands")
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "**🤖 Hackademy Bot Help Menu**\n\n"
        "`/code [php|hack|python]` — Get useful code snippets\n"
        "`/talk` — Start a casual convo\n"
        "`/hi` — Say hi to the bot\n"
        "`/howareyou` — Ask how I’m doing\n"
        "`/flirt` — Get a flirty pickup line\n"
        "`/bye` — Say goodbye\n"
        "`/suggestion` — Submit feedback to the dev\n"
        "`/help` — Show this menu"
    )

@tree.command(name="suggestion", description="📨 Send a suggestion or idea to the dev")
@app_commands.describe(message="Your suggestion or feedback")
async def suggestion(interaction: discord.Interaction, message: str):
    user = interaction.user
    await interaction.response.send_message("✅ Thanks! Your suggestion has been received.", ephemeral=True)

    # Log channel ID (change this to your actual channel ID)
    log_channel_id = 123456789012345678  # 🔁 Replace with a real channel ID
    log_channel = bot.get_channel(log_channel_id)
    if log_channel:
        await log_channel.send(
            f"📬 **New Suggestion Received**\n"
            f"👤 From: `{user.name}` (ID: `{user.id}`)\n"
            f"💬 Message: {message}"
        )

    # Also save to a file
    with open("suggestions.txt", "a") as f:
        f.write(f"{user.name} ({user.id}): {message}\n")

# ====== Run the Bot ======
bot.run(TOKEN)
