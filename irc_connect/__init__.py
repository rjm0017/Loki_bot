'''
 TODO - Make this package first!
 This package is required to connect to anything so making this work first is key

 There should be a way to make this package so that the user inputs their connection parameters on runtime, and
 maybe generate a token to reuse for faster activation?

 - Find the parameters you need to make a connection
    - bot_owner (your main twitch user/channel)
    - nick (name of bot)
    - channel ("#" + channel name you are hosting bot on)
    - server (??) <- I don't recall what this parameter was or was used for... I'll have to investigate
        ---- this is where to init the socket for the connection to twitch I think
        ((( TRY 'irc.chat.twitch.tv' )))
    - password (password to either the bot's twitch account or the user's twitch account)

 - Give the user a simple interface to connect with their bot/connect it to desired channel (CLI for now)

 - In the future, hosting this process on the web would make creating a GUI easy and make the data easier to secure

'''