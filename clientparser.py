import argparse

def parseircdata(data):
	"""
	The parser for arguments to setup IRC channels.
	Returns an argparse-namespace containing hostname,
	port, nickname, realname, ident, and channel.
	"""
        parser = argparse.ArgumentParser(description='An IRC client')

        parser.add_argument('--hs',
                    dest='host',
                    metavar='HOST',
                    default='irc.freenode.net',
                    help='the name of the host')

        parser.add_argument('--p',
                    dest='port',
                    metavar='PORT',
                    type=int,
                    default=6667,
                    help='the port')

        parser.add_argument('--n',
                    dest='nick',
                    metavar='NICK',
                    default='my_nickname',
                    help='the nickname of user')

        parser.add_argument('--i',
                    dest='ident',
                    metavar='IDENT',
                    default='an_ident',
                    help='the ident of user')
                                    
        parser.add_argument('--r',
                    dest='realname',
                    metavar='REALNAME',
                    default='a_realname',
                    help='the realname of user')
                    
        parser.add_argument('--c',
                    dest='channel',
                    metavar='CHANNEL',
                    default='#r',
                    help='the channel to join')
                    
        ircdata = parser.parse_args(data.split())
        ircdata.channel = ircdata.channel if ircdata.channel[0] == '#' else '#' + ircdata.channel
        return ircdata