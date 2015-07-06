"""
classes.py

This is a rough prototype of the discrete data entities in this project. It's intended more to be a reference than a functioning prototype, but it 
should run and you should be able to perform basic tests with it for your own understanding.


"""

class User:
	"""
	Users are people. People have money, content, and computers.

	This class is intended to accomodate four distinct sets of behavior:
		Makers
			Makers are the people who create content and put it up for sale. The "make" set of functionality includes:
				CRUD of content
				CRUD of media
		Buyers
			Buyers are customers. People who pay, through the network, for content hosted by it.
		Pirates
			Pirates are users who have content that we can't determine how they got or verify that They've paid for. As far as identical content goes, they can supply and earn from content pieces that are identical to the pieces sold by the network.
			Note that a pirate is only a pirate in relation to a specific piece of binary data. by default, the intention is to have any other data they own pay for the data they don't. 
		Inmates
			Inmates are abusive users who seek to undermine the network deliberately.  This can be anything from trying to steal other user's data or content to adding backdoors to content or what have you.  The intention is to not simply treat this as an error, but to make the network actively hostile to abuse and even revenge-seeking, to the scale of the damage done (corrupting inmate data, adding backdoors back into their systems with the very data they steal through their own backdoor, recuperating financial losses or inflicting expenses upon them to undo any benefit they gain, etc).
			Do unto others, after all.
	"""
	UID = "" 							#	Unique Identification. every user is unique.
	Username = ""						#	username
	email = ""							#	email address
	def __init__(self):
		pass

class Node:
	"""
	nodes are computers on the network.
	"""
	pass

class Content:
	"""
	Content is the stuff people make and put up for sale.
	"""	
	pass

class Media:
	"""
	Media is web stuff that presents the content for sale on the website.
	"""
	pass

class Authentication:
	"""
	Authentication is how the network tracks who's who, has what, and has sent which, when and to whom.
	"""
	pass

