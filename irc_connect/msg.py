def write(irc, channel, msg):
    irc.send(bytes("PRIVMSG " + channel + " :" + msg + "\n"))
