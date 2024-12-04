import discord
from discord.ext import commands
from Model import get_class
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
  print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Guarda la imagen en ./{attachment.filename}")
            clase = get_class("keras_model.h5", "labels.txt", file_name)
            if clase [0] == "Contaminadas":
                await ctx.send(f"Below are some interesting facts about environmental pollution: Air pollution in cities and rural areas around the world is responsible for 4.2 million premature deaths per year. Air pollution in homes causes heart disease, lung cancer, strokes and other deadly ailments. 73% of beach trash is plastic. The Yangtze River is the most polluted river in the world, transporting 91% of the plastic waste that reaches the sea. In the town of Kabwe, Zambia, children have blood lead levels 5 to 10 times higher than what is considered dangerous. Since 1850, human activities have increased CO2 concentrations by 48%. Chemical substances commonly used in intensive agriculture, batteries or landfills are some of the causes of soil contamination. The groups most vulnerable to contamination are children, the elderly, pregnant women and people with pre-existing respiratory diseases.")
            elif clase [0] == "Naturales":
                await ctx.send(f"Below are some interesting facts about the environment: The Earth is an ellipse, not a perfect sphere, as it is flattened at the poles. The highest temperature recorded on Earth was 56.7°C in Death Valley, in the United States, and the lowest was -89.2°C in Antarctica. The Great Barrier Reef in Australia is the largest living structure on the planet and can be seen from space. Soil is the most biodiverse habitat on the planet, since almost 60% of all species live there. 90% of the waste in the oceans is plastic. Deforestation is one of the main environmental concerns. 70% of greenhouse gas emissions are the responsibility of cities, despite occupying only 2% of the planet's territory. Recycling one ton of paper saves 22 trees and reduces air pollution by 74%. 97% of the planet's water is salty, and only 3% is drinkable. Plastic pollution costs the global economy $8 billion. Since 1850, human activities have increased CO2 concentrations by 48%. And you can improve climate change by pressing: $help. And that will give you tips to help take care of climate change (;")

    else:
        await ctx.send("You forgot to upload the image :(")
@bot.command()
async def helpme(ctx):
    await ctx.send("To take care of climate change, you can do the following: Reduce consumption Buy less things, repair what you can, and recycle.  Reduce energy consumption: Turn off lights you are not using, unplug electronic devices, and use LED or low-energy light bulbs.  Reduce water consumption Avoid wasting water when brushing your teeth or hands, and use the washing machine and dishwasher when they are full. Reduce carbon emissions Use public transport or a bicycle instead of driving, and share a private vehicle with other people. Reduce food waste Don't waste food, as growing, producing, packaging and transporting it uses energy. Promote renewable energy Support the global transition towards the use of alternative energies such as solar energy or wind energy. Raise awareness Recommend all these tips to your family and friends to combat Climate Change.")
@bot.command()
async def convince(ctx):
    await ctx.send("To convince people to take care of climate change, you can: Focus on shared values, such as health, the economy or the desire for a better future. Speak from an ethical perspective about the impacts of climate change on health, the economy, access to water, food security and migratory flows. Inform and educate others. Some actions that can be done to combat climate change are: Use public transport or bicycle. Switch home energy to renewable sources, such as wind or solar. Replace traditional light bulbs with low consumption ones. Save water. Plant trees. Recycle. Join organizations that promote sustainable living. Adjust the diet. Buy locally and sustainably. Don't waste food.")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, I am a bot that fights for climate change.")

@bot.command()
async def bye(ctx):
    await ctx.send(f"Bye friend thanks for worrying about climate change")

@bot.command()
async def comands(ctx):
    await ctx.send(f"These are the commands: 1.- $helpme 2.- $convince 3.- $hello 4.- $bye 5.- $check : The check command is used when you send an image with a contaminated environment or one free of contamination.")


bot.run('')
