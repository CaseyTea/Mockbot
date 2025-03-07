import discord 
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Bot()

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

        try:
            # Fetch the last 100 messages in the channel
            async for message in (ctx.channel.history(limit=20)):
                if message.author == user:
                    # Mock the message content
                    mocked_text = create_mock(message.content)
                    print(f" This is the message: {mocked_text}")
                    await ctx.respond(f" : {mocked_text}")
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
        mocked_message = create_mock(message)
        print(f"This is the message: {mocked_message}")
        await ctx.respond(f": {mocked_message}")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

