# Hack
Este es mi proyecto final de python pro
## Esta es la idea de mi proyecto
> Hacer un bot de DC que envie informacion ayudando al usuario a ayudar a nuestro planeta para evitar el calentamiento global y que cuando mandes fotos sobre cosas con o sin calentamiento global diga cual es cual
> Mi proyecto es un BOT de DC que se beneficia con comandos y con vision por ordenador
> 
## Este es el tipo de mi proyecto:
> Bot de discord
## Las bibliotecas que voy a utilizar:
- Biblioteca discord
- Biblioteca commands
- Biblioteca os, random
- Biblioteca get_class
- Biblioteca Image, ImageOps
- Biblioteca numpy as np
## Referencias útiles:
- Referencia import discord
from discord.ext import commands
import os, random
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
            if clase [0] == "Perros":
                await ctx.send(f"Aquí hay algunos datos interesantes sobre los perros: Sentidos: Los perros tienen un olfato 15 veces más sensible que el de los humanos y un oído 4 veces más agudo. Algunos estudios sugieren que pueden detectar enfermedades como el cáncer, la diabetes o el COVID con su olfato; Percepción del tiempo: Los perros pueden percibir lapsos de tiempo de hasta 4 horas;  Contacto visual: Los perros son los únicos animales no primates que miran a los humanos a los ojos;  Sudoración: Los perros sudan a través de sus almohadillas, por lo que a veces se puede ver un rastro húmedo en sus patas;Aprendizaje: Los perros aprenden las rutinas y hábitos de sus dueños, por lo que pueden saber cuándo es hora de pasear o cenar; Patadas hacia atrás: Después de orinar, los perros dan patadas hacia atrás para dejar su olor, un comportamiento conocido como comportamiento de raspado; Beneficios para las personas: Tener un perro puede proporcionar una sensación de bienestar emocional y ayudar a las personas a recuperarse de traumas personales.")
            elif clase [0] == "Gatos":
                await ctx.send(f"Aquí hay algunos datos interesantes sobre los gatos: Dormir: Los gatos pasan la mayor parte del día durmiendo, alrededor de dos tercios. Audición: La audición de los gatos es mejor que la de los perros. Velocidad: Los gatos pueden correr hasta 49 km/h en cortas distancias. Saltos: Los gatos pueden saltar hasta cinco veces su altura en un solo salto. Sobrevivencia: Algunos gatos han sobrevivido a caídas de 20 metros gracias a su reflejo de enderezamiento. Sonidos: Los gatos pueden hacer alrededor de 100 sonidos diferentes. Cerebro: El cerebro de un gato es más similar al de un humano que al de un perro. Raza: Existen aproximadamente 40 razas de gatos reconocidas. Flexibilidad: Los gatos pueden rotar sus orejas 180 grados. Visión: Los gatos perciben los colores de forma menos intensa que los humanos, y ven principalmente tonalidades frías como el azul y el verde. Expectativa de vida: En promedio, un gato vive hasta 12 años, pero puede llegar a vivir hasta 20 años si se le da una buena alimentación y se tiene un buen cuidado. Parpadear: Parpadear lentamente es una forma de construir una relación con los gatos, ya que imita su sonrisa.")
    else:
        await ctx.send("Olvidaste subir la imagen :(")
bot.run()
## Los artículos de la guía que me ayudarán durante el desarrollo
El mejor profe de Python pro (;
## Saludos profe
