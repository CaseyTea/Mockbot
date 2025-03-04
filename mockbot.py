import discord 
from discord.ext import commands
import os

intents = discord.Intents.default()

# Creating slash command for mocking 
# /@user
@bot.slash_command(name="mock", description="Mock a user you @")
async def mock(context, user: discord.Member): 
    async for message in context.channel.history(limit=20):
        if message.author == user:
            mocked_text = ''.join(
                char.lower() if i % 2 == 0 else char.upper()
                for i, char in enumerate(user.display_name)
        )
    await context.respond(f"{mocked_text}")
    return

    await context.respond(f"No recent message found from {user.display_name} in thic channel")
    
    bot.run(os.environ["DISCORD_TOKEN"])