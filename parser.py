import argparse

def parsedatargs(data):
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
				    help='the nickname')

	parser.add_argument('--i',
                    dest='ident',
                    metavar='IDENT',
				    default='an_ident',
				    help='the ident')

	parser.add_argument('--r',
                    dest='realname',
                    metavar='REALNAME',
				    default='a_realname',
				    help='the realname')

	return parser.parse_args()