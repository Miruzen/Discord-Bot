import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import discord
import responses

async def send_message(message, user_message, is_private):
    """Sends a message to the user or channel."""
    try:
        response = responses.get_response1(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_bot():
    """Runs the Discord bot."""
    TOKEN = "Enter your discord token here "
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        """Prints a message when the bot is ready."""
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        """Processes incoming messages."""
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f'{username} said: "{user_message}", Channel: {channel}')

        if user_message[0] == '?':
            await send_message(message, user_message , is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)