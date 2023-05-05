import discord
import re
from discord.ext import commands

token = "MTEwMzMxOTk2NTAzMDk1MzA2MA.GBbiqh.1QXO7BCU1Ntn8vBNmOXOd8d2iY09hiNqPJ3HE4"

intents = discord.Intents.default()
intents.message_content = True

# Crea una instancia de bot
bot = commands.Bot(command_prefix='ai ', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


# Evento que responde con rimas
@bot.event
async def on_message(message):
    # Obtener la última palabra del mensaje
    last_word = message.content.split()[-1].lower()
    # Le quita todas los símbolos de exclamación y de interrogación
    caracteres_a_eliminar = "!?."
    last_word = last_word.rstrip(caracteres_a_eliminar)

    # Comprueba que no sea un mensaje del propio bot
    if message.author == bot.user:
        return

    # Comprobar si el final del mensaje es una operación matemática
    if re.match(r".*[0-9]+([\+\-\*/][0-9]+)+$", last_word):
        # Calcular el resultado de la operación
        result = eval(last_word)
        # Comprobar si el resultado es 5
        if result % 10 == 5 and result % 100 != 15:
            # Mencionar al autor del mensaje en la respuesta
            response = "Por el culo te la hinco"
            # Enviar la respuesta citando al mensaje original
            await message.channel.send(response, reference=message, mention_author=True)

    # Comprueba si acaba en inco y la palabra no es hinco
    if ((last_word.endswith("inco") or last_word.endswith("5")) != last_word.endswith(
            "15")) and last_word != "hinco":
        # Responder al mensaje
        response = "Por el culo te la hinco"
        await message.channel.send(response, reference=message, mention_author=True)

    # Comprueba si acaba en ado y la palabra no es colgado
    if (last_word.endswith("ado") and last_word != "colgado"):
        # Responder al mensaje
        response = "El que tengo aquí colgado"
        await message.channel.send(response, reference=message, mention_author=True)

    # Comprueba si acaba en ada y la palabra no es colgada
    if (last_word.endswith("ada")) and last_word != "colgada":
        # Responder al mensaje
        response = "La que tengo aquí colgada"
        await message.channel.send(response, reference=message, mention_author=True)

    # Comprueba si acaba en ano y la palabra no es mano
    if (last_word.endswith("ano")) and last_word != "mano":
        # Responder al mensaje
        response = "Me la agarras con la mano"
        await message.channel.send(response, reference=message, mention_author=True)

    # Comprueba si acaba en ao y la palabra no es colgao
    if (last_word.endswith("ao")) and last_word != "colgao":
        # Responder al mensaje
        response = "El que tengo aquí colgao"
        await message.channel.send(response, reference=message, mention_author=True)


bot.run(token)
