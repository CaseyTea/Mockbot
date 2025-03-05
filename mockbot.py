import discord 
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Bot()

# Creating slash command for mocking 
# /@user
@bot.slash_command(name="mock", description="Mock a user you @")
async def mock(ctx, user: discord.Member):
    try:
        # Fetch the last 100 messages in the channel
        async for message in (ctx.channel.history(limit=100)):
            print(message)
            if message.author == user:
                # Mock the message content
                mocked_text = ''.join(
                    char.upper() if i % 2 == 0 else char.lower()
                    for i, char in enumerate(message.content)
                )
                await ctx.respond(f"{user.display_name} says: {mocked_text}")
                if mocked_text: 
                    print(f"There is something in here{mocked_text}")
                return
        await ctx.respond(f"No recent messages found from {user.display_name} in this channel.")
    except discord.Forbidden as e:
        print(f"403 Forbidden Error: {e}")
        await ctx.respond("I don’t have permission to perform this action. Please check my permissions.")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        await ctx.respond("An error occurred. Please try again later.")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")
    
