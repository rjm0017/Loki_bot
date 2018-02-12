# Run this to run the bot; attach all packages to this!


def run_loop(irc, channel):
    while 1:
        text = irc.recv(2040)
        if text.find('PING') != -1:
            irc.send('PONG ' + text.split()[1] + 'rn')
        print text
