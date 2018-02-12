import socket
import runner


def connect(channelIn, passwordIn):
    bot_owner = 'loki_ssb'
    nick = 'iroh_bot'
    channel = '#' + channelIn
    server = 'irc.chat.twitch.tv'
    password = passwordIn

    irc = socket.socket()
    irc.connect((server, 6667))

    # send vars for connection to twitch chat
    irc.send('PASS ' + password + '\r\n')
    irc.send('USER ' + nick + '\r\n')
    irc.send('NICK ' + nick + '\r\n')
    irc.send('JOIN ' + channel + '\r\n')

    runner.run_loop(irc, channel)
