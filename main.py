import discord
import speech_recognition as sr
import os
import soundfile as sf

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(message)

        for attachment in message.attachments:
            if attachment.filename.endswith(".ogg"):
                print("Voice message detected!")

                await attachment.save(f"./voices_ogg/{attachment.filename}")

                data, samplerate = sf.read("./voices_ogg/"+attachment.filename)
                sf.write("./voices_wav/"+(attachment.filename.replace(".ogg", ".wav")), data, samplerate)

                with sr.AudioFile("./voices_wav/"+(attachment.filename.replace(".ogg", ".wav"))) as source:
                    audio_data = r.record(source)
                    text = r.recognize_google(audio_data)
                    embedVar = discord.Embed(description=text, color=0x010101)
                    await message.reply(embed=embedVar)

with open("token.txt") as f:
    TOKEN = f.readline()

r= sr.Recognizer()

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
