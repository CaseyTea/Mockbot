import discord 
from discord.commands import Option
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(intents=intents)
print("The bot is now running")

# Create funtion for mocked text
def create_mock(msg): 
    return ''.join(
            char.lower() if i % 2 == 0 else char.upper()
            for i, char in enumerate(msg)
            )

# Creating slash command for mocking 
# /@user
@bot.slash_command(name="mock", description="Mock a user you @")
async def mock(
        ctx: discord.ApplicationContext,
        user: discord.Option(discord.Member, "The user to mock", required=False), 
        message: discord.Option(str, "The custom message to mock", required=False), 
        ):
    if user:
        print("We get into the user slash command here") 
        try:
            # Fetch the last 100 messages in the channel
            print("This is what is inside the message list:")
            print(ctx.channel.history(limit=20))
            async for message in (ctx.channel.history(limit=20)):
                if message.author == user:
                    print(user)
                    print(f"\nWe find the user's message here: {message.content}")
                    # Mock the message content
                    mocked_text = create_mock(message.content)
                    print(f" This is the message: {mocked_text}")
                    await ctx.respond(f"{mocked_text}")
                    return
        # Error Checking 
            await ctx.respond(f"No recent messages found from {user.display_name} in this channel.")
        except discord.Forbidden as e:
            print(f"403 Forbidden Error: {e}")
            await ctx.respond("I don’t have permission to perform this action. Please check my permissions.")
        except Exception as e:
            print(f"Unexpected Error: {e}")
            await ctx.respond("An error occurred. Please try again later.")     
    # Check if the user entered in a message 
    elif message: 
        print(f"There is where the custom message is createed: {message}")
        mocked_message = create_mock(message)
        await ctx.respond(f": {mocked_message}")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

bot.run(os.environ["DISCORD_TOKEN"])