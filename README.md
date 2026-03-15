# discord-transcriber
## this is a transcriber for your own server.

### To create this bot for your server
You need python3 (3.8<=).
Then you need to create a folder for the bot. 
Inside it run cmd and type:
> python3 -m venv ven

After that activate venv by running
## Linux/macOS:
> source venv/bin/activate
## Windows:
> venv/bin/activate

Now we have to install dependencies
> pip install discord.py SpeechRecognition pydub pysoundfile numpy

For now we are done here, we will come back here later, so leave cmd open.
Now we have to go (Discord Developers)[https://discord.com/developers/applications] page 
and click create and select "Create bot..." and complete the form given there.
Now we have a bot, but we have to connect it to our python script, so we click on bot that's on the left.
Under Token click "Reset Token", and copy it. 
Now we need to go back to our python script.
Create a file named "token.txt". 
Inside it paste the token, and run this command in cmd:
> python3 main.py
