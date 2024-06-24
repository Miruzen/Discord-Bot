# import discord
# import os 
# from dotenv import load_dotenv
# import neuralintents
# from neuralintents.assistants import BasicAssistant

# Chatbot = BasicAssistant('intents.json')
# Chatbot.fit_model(epochs=50) 
# Chatbot.save_model()

# print ("Bot running....")

# client = discord.client() 
# load_dotenv()
# TOKEN = os.getenv('TOKEN')

# @client.event 
# async def on_message (message) :
#     if message.author == client.user : 
#         return
    
#     if message.content.startswith("$aibot") :
#         response = Chatbot.request(message.content[7:])
#         await message.channel.send(response) 

# client.run(TOKEN)