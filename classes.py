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
		"""
		in production, this needs to handle user acount generation and adding users to the program logic from memory. For now, though, the idea is to start with a function that can be called to generate "test users".
		"""
		pass
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		pass

class Node:
	"""
	nodes are computers on the network.
	A node holds data (the content pieces, assembled into the content that the user bought or pirated, which are supplied to the network), processes input (user Authentication), and takes actions (sending and receiving content pieces, authenticating with the central server, etc). 
	"""
	mac_address = "" 			# all computers have one, although spoofing is a risk
	user_credentials = "" 		# a representation of the username/pass the node proves it has
	content = {}				# a dictionary of the content- ID and Path : key and value
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		pass
	pass

class Content:
	"""
	Content is the stuff people make and put up for sale. 

	The structure of content is this: 
		content is a "doubletree", where branches dictate version and platform.
			"version" branches dictate *specific attributes*.
				eg, Battlefield Vietnam Version 0:
					American "bombardier" class includes M-14 and m-79 grenade launcher <overpowered in online gameplay>
				Battlefield Vietnam Version 1:
					American "bombardier" has low powered 'standard' weapon (m1 carbine? not sure) and higher power "anti-armor" weapon to adjust multiplayer variables
			"platform" branches dictate *specific implementations*
				Macintosh
					direct3d v0
					direct3d v1
					etc
				Windows
					directx 9
					directx 10
					etc
				Linux
					openGL 5
					openGL 6
					etc
				etc

	"""	
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		pass
	pass

class ConPiece:
	"""
	a ConPiece, or Content Piece, is the individual packet of data transferred between nodes of the network.
	"""
	pass

class Media:
	"""
	Media is web stuff that presents the content for sale on the website. By default, it describes HTML and javascript, but this is a major security hole. Maybe some workaround with another markup will work better. But for now, the prototype should show vanilla HTML. I'll add more constraints as they are needed.

	**More Research Needed**
	"""
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		pass
	pass

class Authentication:
	"""
	Authentication is how the network tracks who's who, has what, and has sent which, when and to whom.  It consists of a set of keys that are recycled, and the combinations of which correlate to an interior database for record keeping. there are other parts to this, mostly based around making it difficult to predict, intercept, decipher, and use, even in long-term attacks, and so for the long term players the idea is to send them on a rat race of the same data over and over, and to change what it means every time. In old-school encryption terms, the idea is to keep anybody outside at a permanent depth of one (ref leo marks between silk and cyanide).
	"""
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		pass
	pass

