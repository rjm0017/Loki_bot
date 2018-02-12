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

import socket


# loop to keep bot running
def get_text(irc):
    text = irc.recv(2040)
    if text.find('PING') != -1:
        irc.send('PONG ' + text.split()[1] + 'rn')

    return text


def connect(channelIn, passwordIn):

    bot_owner = 'loki_ssb'
    nick = 'iroh_bot'
    channel = '#' + channelIn
    server = 'irc.chat.twitch.tv'
    password = passwordIn

    irc = socket.socket()
    irc.connect((server, 6667))
    print irc.getsockname

    # send vars for connection to twitch chat
    irc.send('PASS ' + password + '\r\n')
    irc.send('USER ' + nick + '\r\n')
    irc.send('NICK ' + nick + '\r\n')
    irc.send('JOIN ' + channel + '\r\n')

    x = 1
    while 1:
        if x == 1:
            irc.send(bytes("PRIVMSG " + channel + " :" + "Hello There" + "\n"))
            x = 0
        text = get_text(irc)
        print text


connect('mikamora', 'oauth:p80gefayqxc6hijs0nhp5ph5sbdqdd')


# things are going to have to move around but it functions
