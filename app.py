import discord
from discord.ext import commands
from tenshi import Tenshi
import os
from dotenv import load_dotenv
import random
from discord.ui import Button, View

# Load token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Put your token in your .env file

# Setup intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot setup
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

# Setup Tenshi AI
tenshi = Tenshi(api_keys=["AIzaSyCw2H-Jg_dhlKLs0j5_AEedl1qdrFmiL_Q"])  # Validate your API key!
tenshi.set_system("You are Rubin EXE, an AI/ML developer who answers questions helpfully.")

@bot.event
async def on_ready():
    print(f'[LOGGED IN] as {bot.user} (ID: {bot.user.id})')

@bot.command()
async def intro(ctx):
    await ctx.send('👨‍💻 Developed by Abhaya Bikram Shahi — Fullstack Dev (PHP, React JS)! 🔥')

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'🏓 Pong! Latency is {latency}ms.')

@bot.command()
async def flirting(ctx):
    await ctx.send('💘 Flirting is not my thing, but I can help with coding!')

@bot.command()
async def info(ctx):
    await ctx.send(
        "👋 **Hello!** I am Hackademy Zone — the official bot of Hackademy.\n"
        "I’ll help you dive into professional learning with AI and our awesome members!\n\n"
        "Use `!help` to see what I can do! 💡"
    )

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hey {ctx.author.mention}! What’s up? 👋')

@bot.command()
async def developers(ctx):
    await ctx.send(
        '👨‍💻 **Developers:**\n'
        'Abhaya Bikram Shahi - Fullstack Dev (PHP, React JS) 🔥\n'
        '\nRubin EXE - AI/ML Developer 🤖\n'
    )

@bot.command()
async def help(ctx):
    await ctx.send(
        "🛠️ **Hackademy Bot — Commands Menu**\n"
        "Here’s what I can do to boost your learning 📚💻\n\n"
        "**💬 General:**\n"
        "`!intro` — Shows dev info\n"
        "`!hello` — Say hi to the bot\n"
        "`!info` — Learn what this bot is all about\n"
        "`!from` — Know my origin 🌏\n"
        "`!ping` — Check latency (for nerds)\n"
        "`!members` — Mention all non-bot members\n\n"
        "**👨‍💻 Developer & AI Commands:**\n"
        "`!developers` — List who built me\n"
        "`!rubin <your question>` — Ask Rubin (AI/ML Dev Bot) anything 🤖\n\n"
        "**💻 Programming Help:**\n"
        "`!code <language>` — Get beginner Hello World code (e.g. python, c++, go, etc)\n\n"
        "✨ More commands coming soon... Stay tuned!\n\n"
        "`!mentor` — Meet our awesome mentors 👩‍🏫\n"
        "`!fun` — Get a random programming joke or fun fact 🤣\n"
        "`!roleinfo` — Show Teen & Adult role info with buttons\n"
        "`!teamuser150` — Show all the hacker team\n"
        "`!quiz` — Take a quiz and test your skills 🎯"
    )


@bot.command(name="from")
async def from_(ctx):
    await ctx.send("🌏 I'm coded by a proud dev from Nepal 🇳🇵!")

@bot.command()
async def members(ctx):
    if not ctx.guild:
        await ctx.send("❌ This command only works in servers, not DMs.")
        return

    # Get all non-bot members
    mentions = [member.mention for member in ctx.guild.members if not member.bot]

    if not mentions:
        await ctx.send("No non-bot members found.")
        return

    chunk_size = 50  # Discord message limit safety chunk

    for i in range(0, len(mentions), chunk_size):
        chunk = mentions[i:i+chunk_size]
        await ctx.send(" ".join(chunk))

@bot.command()
async def abhaya(ctx):
    await ctx.send(
        "babu \n"
        "padna jau"
    )

@bot.command()
async def rubin(ctx, *, question: str):
    await ctx.send("🤖 Thinking...")
    try:
        response = tenshi.generate(question)
        await ctx.send(f"🧠 Rubin says: {response}")
    except Exception as e:
        await ctx.send(f"⚠️ Oops, something went wrong: {str(e)}")

@bot.command()
async def code(ctx, language: str):
    language = language.lower().strip()

    code_snippets = {
        "python": '''```python
# 🐍 Python - Beginner Hello World
print("Hello, world!")
```''',

        "java": '''```java
// ☕ Java - Hello World for beginners
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
```''',

        "html": '''```html
<!-- 🌐 HTML - Basic HTML page -->
<!DOCTYPE html>
<html>
  <head>
    <title>Hello</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>
```''',

        "c": '''```c
// 🔧 C - Systems language classic
#include <stdio.h>

int main() {
    printf("Hello, world!\\n");
    return 0;
}
```''',

        "cpp": '''```cpp
// 🚗 C++ - Object-oriented power
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, world!" << endl;
    return 0;
}
```''',

        "csharp": '''```csharp
// 🎮 C# - Used for Windows and Unity
using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello, world!");
    }
}
```''',

        "go": '''```go
// 🌀 Go (Golang) - Google’s system language
package main
import "fmt"

func main() {
    fmt.Println("Hello, world!")
}
```''',

        "bash": '''```bash
# 🖥️ Bash - Shell scripting on Linux/macOS
echo "Hello, world!"
```'''
    }

    if language in ["list", "languages"]:
        await ctx.send("📚 Supported languages:\n`python`, `java`, `html`, `c`, `cpp`, `csharp`, `go`, `bash`")
        return

    if language in code_snippets:
        await ctx.send(code_snippets[language])
    else:
        await ctx.send(
            f"❌ Sorry, I don't have a snippet for `{language}`.\n"
            "Try `!code list` to see all supported languages."
        )

@bot.command(name="mentor")
async def mentor(ctx):
    mentors_list = [
        {"id": 1263033024489197569, "language": "FullStack Developer, Cyber Security"},      # Abhaya
        {"id": 1375802098821627926, "language": "Python, JavaScript"},                      # Rubin EXE
        {"id": 782528248072372225, "language": "JavaScript, Node.js, React.js, TypeScript"},# Aashish Sharma
        {"id": 775009937456889876, "language": "Full Stack Developer"},                     # Bibash Jhaprel
        {"id": 731354646542549053, "language": "FullStack Developer, Cyber Security"},      # Gaurab Budha
        {"id": 1034721430606184478, "language": "Gamer, Hacker"},
        {"id": 735057444514037760, "language": "AI/ML Developer, Web Developer"},
    ]

    embed = discord.Embed(
        title="👨‍🏫 Our Mentors",
        description="Here's a list of our top mentors and their specialties:",
        color=discord.Color.blue()
    )

    for mentor in mentors_list:
        embed.add_field(
            name=f"<@{mentor['id']}>",
            value=f"Specializes in: **{mentor['language']}**",
            inline=False
        )

    await ctx.send(embed=embed)

@bot.command()
async def fun(ctx):
    fun_messages = [
        "🤣 Why do programmers prefer dark mode? Because light attracts bugs!",
        "😎 Keep calm and code on!",
        "👾 Did you hear about the computer that caught a virus? It had to go to the doctor!",
        "🧠 Fun fact: The first computer bug was an actual moth stuck in a relay.",
        "🐍 Python walks into a bar and says, 'I’m feeling a bit scripting today!'",
        "💻 Why do Java developers wear glasses? Because they don’t C#!",
        "⚡ Pro Tip: If debugging is the process of removing bugs, then programming must be the process of putting them in!",
        "Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25! 🎃🎄",
        "Debugging: Being the detective in a crime movie where you’re also the murderer. 🕵️‍♂️💥",
    ]
    joke = random.choice(fun_messages)
    await ctx.send(joke)

# REPLACED roles command with professional roleinfo command with buttons
@bot.command(name="roleinfo")
async def roleinfo(ctx):
    roles_to_show = {
        "🧒 Teen": "Teen",
        "🧑 Adult": "Adult"
    }

    embed = discord.Embed(
        title="🗂️ Role Categories & Member Counts",
        description="Click the buttons below to toggle your Teen or Adult roles!",
        color=discord.Color.dark_blue()
    )

    for emoji_label, role_name in roles_to_show.items():
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if role:
            count = len(role.members)
            embed.add_field(
                name=f"{emoji_label} {role_name}",
                value=f"Members: **{count}**",
                inline=False
            )
        else:
            embed.add_field(
                name=f"{emoji_label} {role_name}",
                value=f"Role not found on this server.",
                inline=False
            )

    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url=ctx.guild.icon.url if ctx.guild.icon else discord.Embed.Empty)

    class RoleView(View):
        def __init__(self):
            super().__init__(timeout=None)  # buttons never timeout

        @discord.ui.button(label="Teen", style=discord.ButtonStyle.primary, emoji="🧒", custom_id="role_teen")
        async def teen_button(self, interaction: discord.Interaction, button: Button):
            role = discord.utils.get(interaction.guild.roles, name="Teen")
            if not role:
                await interaction.response.send_message("❌ 'Teen' role not found on this server.", ephemeral=True)
                return

            member = interaction.user
            if role in member.roles:
                await member.remove_roles(role)
                await interaction.response.send_message("✅ Removed your Teen role.", ephemeral=True)
            else:
                await member.add_roles(role)
                await interaction.response.send_message("✅ Added you to Teen role!", ephemeral=True)

        @discord.ui.button(label="Adult", style=discord.ButtonStyle.success, emoji="🧑", custom_id="role_adult")
        async def adult_button(self, interaction: discord.Interaction, button: Button):
            role = discord.utils.get(interaction.guild.roles, name="Adult")
            if not role:
                await interaction.response.send_message("❌ 'Adult' role not found on this server.", ephemeral=True)
                return

            member = interaction.user
            if role in member.roles:
                await member.remove_roles(role)
                await interaction.response.send_message("✅ Removed your Adult role.", ephemeral=True)
            else:
                await member.add_roles(role)
                await interaction.response.send_message("✅ Added you to Adult role!", ephemeral=True)

    view = RoleView()
    await ctx.send(embed=embed, view=view)


@bot.command()
async def teamuser150(ctx):
    members = [
        1263033024489197569,
        1399030256987541551
    ]
    mentions = [f"<@{member_id}>" for member_id in members]
    message = (
        "🕶️ **Team user150 Active**\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"{' | '.join(mentions)}\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "💻 Watch out, the digital shadows are moving."
    )
    await ctx.send(message)



quiz_data = {
    "english": {"question": "📝 What is the synonym of 'happy'?", "answer": "joyful"},
    "science": {"question": "🔬 What planet is known as the Red Planet?", "answer": "mars"},
    "computer": {"question": "💻 What does 'CPU' stand for?", "answer": "central processing unit"},
    "hacking": {"question": "🕶️ What is the most common attack type in hacking that tricks users into giving info?", "answer": "phishing"},
}

@bot.command()
async def quiz(ctx):
    await ctx.send("🎯 **Choose a quiz category:**\n`english`, `science`, `computer`, `hacking`\n(Type one to start)")

    def check_category(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in quiz_data.keys()

    try:
        category_msg = await bot.wait_for("message", timeout=30.0, check=check_category)
        category = category_msg.content.lower()
        data = quiz_data[category]

        await ctx.send(f"📚 **{category.title()} Quiz:** {data['question']} (You have 20 seconds!)")

        def check_answer(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        answer_msg = await bot.wait_for("message", timeout=20.0, check=check_answer)

        if answer_msg.content.lower().strip() == data['answer']:
            await ctx.send("✅ **Correct! You're a genius 🤓🔥**\nKeep flexing that brain power 🧠💥")
        else:
            await ctx.send(f"❌ **Oops! That's not it.**\nThe correct answer was **{data['answer'].title()}**. Keep trying! 💪")

    except Exception:
        await ctx.send("⏰ You took too long or something went wrong. Try `!quiz` again!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    await bot.process_commands(message)

# Run bot
if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ Bot token not found. Make sure it's in your .env file.")
