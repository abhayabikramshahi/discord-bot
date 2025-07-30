import discord
from discord.ext import commands
from discord import app_commands
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
Token = os.getenv("AI")

if not Token or Token == "":
    print("❌ Bot token not set. Please check your .env file and ensure AI=YOUR_TOKEN exists.")
    sys.exit()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

# --- On Ready ---
@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user} (Coder Ai - Hacdemy Zone)")
    print("🔗 Invite the bot with:")
    print("https://discord.com/api/oauth2/authorize?client_id=1399698127006597150&permissions=274878221440&scope=bot%20applications.commands")
    await tree.sync()
    print("🌐 Slash commands synced.")

# --- Handle bot mentions + /help ---
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user in message.mentions and "/help" in message.content.lower():
        embed = discord.Embed(
            title="👨‍💻 Coder Ai - Hacdemy Zone",
            description="Boost your coding skills with these commands!",
            color=discord.Color.red()
        )
        embed.add_field(name="`/learn`", value="Learn by topic & language", inline=False)
        embed.add_field(name="`/quiz`", value="Take a coding quiz", inline=False)
        embed.add_field(name="`/project-idea`", value="Get project ideas", inline=False)
        embed.add_field(name="Supported Languages", value="**Python**, **Java**, **JavaScript**, **HTML**", inline=False)
        await message.channel.send(embed=embed)

    await bot.process_commands(message)

# --- /help command ---
@tree.command(name="help", description="Show all available commands")
async def help_cmd(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🛠️ Coder Ai - Help Menu",
        description="Here's what I can help you with:",
        color=discord.Color.green()
    )
    embed.add_field(name="/learn", value="📘 Learn a concept", inline=False)
    embed.add_field(name="/quiz", value="🧠 Test your knowledge", inline=False)
    embed.add_field(name="/project-idea", value="🔥 Get project suggestions", inline=False)
    embed.add_field(name="Languages Supported", value="Python, Java, JavaScript, HTML", inline=False)
    await interaction.response.send_message(embed=embed)

# --- /learn command ---
@tree.command(name="learn", description="Learn code topics by language")
@app_commands.describe(
    language="Choose a language",
    topic="What do you want to learn?"
)
@app_commands.choices(language=[
    app_commands.Choice(name="Python", value="python"),
    app_commands.Choice(name="Java", value="java"),
    app_commands.Choice(name="JavaScript", value="js"),
    app_commands.Choice(name="HTML", value="html")
])
async def learn(interaction: discord.Interaction, language: app_commands.Choice[str], topic: str):
    code_snippets = {
        "python": {
            "variables": 'name = "Abhaya"\nage = 17\nprint(name, age)',
            "helloworld": 'print("Hello, World!")',
            "functions": 'def greet(name):\n    return "Hello " + name\n\nprint(greet("Abhaya"))',
            "oops": 'class Student:\n    def __init__(self, name):\n        self.name = name\n\n    def greet(self):\n        print("Hi,", self.name)\n\ns = Student("Abhaya")\ns.greet()',
            "sqlite": '''import sqlite3

# Connect to database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table
cursor.execute(\"""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
\""")

# Insert user
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Abhaya", "abhaya@example.com"))

# Alter table (add age column)
cursor.execute("ALTER TABLE users ADD COLUMN age INTEGER")

# Commit and close
conn.commit()
conn.close()'''
        },
        "java": {
            "variables": 'String name = "Abhaya";\nint age = 17;\nSystem.out.println(name + " " + age);',
            "helloworld": 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
            "functions": 'public static String greet(String name) {\n    return "Hello " + name;\n}',
            "oops": 'class Student {\n    String name;\n    Student(String name) {\n        this.name = name;\n    }\n    void greet() {\n        System.out.println("Hi " + name);\n    }\n}'
        },
        "js": {
            "variables": 'let name = "Abhaya";\nconst age = 17;\nconsole.log(name, age);',
            "helloworld": 'console.log("Hello, World!");',
            "functions": 'function greet(name) {\n    return "Hello " + name;\n}\nconsole.log(greet("Abhaya"));',
            "oops": 'class Student {\n    constructor(name) {\n        this.name = name;\n    }\n    greet() {\n        console.log("Hi", this.name);\n    }\n}\nconst s = new Student("Abhaya");\ns.greet();',
            "promises": 'const wait = () => {\n  return new Promise((resolve) => setTimeout(() => resolve("Done!"), 1000));\n};\n\nwait().then(console.log);'
        },
        "html": {
            "variables": '<span id="output"></span>\n<script>\n  let name = "Abhaya";\n  document.getElementById("output").textContent = name;\n</script>',
            "helloworld": '<h1>Hello, World!</h1>',
            "functions": '<button onclick="sayHi()">Click Me</button>\n<script>\n  function sayHi() {\n    alert("Hello!");\n  }\n</script>'
        }
    }

    selected_lang = language.value
    lower_topic = topic.lower()

    if selected_lang not in code_snippets or lower_topic not in code_snippets[selected_lang]:
        await interaction.response.send_message("⚠️ Sorry, that topic isn't available for this language.", ephemeral=True)
        return

    code = code_snippets[selected_lang][lower_topic]
    embed = discord.Embed(
        title=f"📘 {language.name.capitalize()} — {lower_topic.capitalize()}",
        description=f"```{code}```",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed)

# --- Run the bot ---
bot.run(Token)
