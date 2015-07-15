"""
classes.py

This is a rough prototype of the discrete data entities in this project. It's intended more to be a reference than a functioning prototype, but it 
should run and you should be able to perform basic tests with it for your own understanding.

And, Welcome. Lets kick some ass.

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
	
	UID 				= 	"" 				#	Unique Identification. every user is unique.
	Username 			= 	""				#	username
	email 				= 	""				#	email address
	
	#User Cultural and National Identity attributes
	Languages 			=	{}				#	never assume somebody only speaks as few languages as you do.
	Interface_Language 	=	""				#	Still, everybody has a preferred default.
	Time_Zone			=	"London, UK"	#	The default time zone the user sees all things in relation to <default London, UK, because it's +0 GMT>
	Country				=	""				#

	#Network attributes
	User_Nodes			=	{}				#	set of all nodes that have historically used this user's credentials


	#User Fiscal Attributes
	User_Local_Currency =	""				# 	what the default unit is for earned income
	Earned_Income 		= 	0.0				# 	How much money a user has earned
	Accumulated_Debt	=	0.0				#	How much the user has that they still need to pay for
	Connected_Accounts	=	{}				#	Which financial institution accounts are connected to this one

	#User Functions
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
	mac_address 		=	"" 				# 	all computers have one, although spoofing is a risk
	user_credentials 	= 	"" 				# 	a representation of the username/pass the node proves it has
	content 			= 	{}				# 	a dictionary of the content- ID and Path : key and value

	#Node internal attributes
	File_Path			=	""				#	The default directory where files are searched for from.  Should include a 'gitignore' knockoff to not include local files.
	Local_Files			=	{}				#	A dictionary of the local files- {Content_ID: directory location} pairing

	#server specific attributes

	#Functions
	def __init__(self):
		pass
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
				Mac, PC, Linux, PS4, iPad, etc


		This stricture sounds complicated, but the idea is to implement versions on platform, and so there are two tools to update 

	"""	
	
	#Base Attributes
	Content_Name 			=		""			#	Content Name, for humans to refer to it by.
	Content_ID				=		""			#	Content unique identifier, for machines to use.
	Content_Description		= 		""			#	a brief (tweet length) description of what it is, for humans to use
	Content_PieceTree		=		""			#	A tree that describes the structure of the content.  This is what becomes a tracker on the server

	#Fiscal attributes
	Content_Price			=		0.0			#	Monetary price to buy a single instance of the content.
	Content_version			=		{}			#	


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
	Piece_ID 			= 	"" 				#	UniqueID of this piece.
	Piece_FormatType 	= 	""				#	The filetype (size- determined compression block, discrete file, etc)
	Size 				= 	0 				#	integer, if you can type it. It needs to represent the size, in bytes
	Value 				= 	0.0				#	the value of one complete/successful/verified/permitted transfer of one piece. Used to calculate payment. **More Research Needed**
	
	#data members where client and server use the same variables, but for local tasks
	Seeders 			= 	0				#	int or longint, depending on scale
	leechers 			= 	0				#	""
	Downloaders 		= 	0				#	""
	Pirates 			= 	0				#	 OK, some explanation: because pirates save the network money, they preferentially are at the front of the line, all attributes being equal.
	
	#data members used only by the client
	successful_uploads 	= 	0 				#	tracking how many times a given piece has been successfully uploaded, for money.
	attempted_uploads 	= 	0				#	tracking how many times a given piece has been unsuccessfully uploaded, for no money.
	network_density 	= 	0 				#	tracking how many nodes on the network are also attempting to upload said file
	
	#data members used only be the server
	
	#initialize
	def __init__(self):
		pass
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		pass
	pass	



class Media:
	"""
	Media is web stuff that presents the content for sale on the website. By default, it describes HTML and javascript, but this is a major security hole. Maybe some workaround with another markup will work better. But for now, the prototype should show vanilla HTML. I'll add more constraints as they are needed.

	**More Research Needed**
	"""
	Media_ID 			= 	""				#	tracking ID. 
	Media_Name 			= 	""				#	a name for humans to track.
	Media_Val 			= 	""				#	the actual stuff that the media represents. 
	Media_Type 			= 	""				#	the actual type of the media in question
	Content_ID			=	""				#	ID of the content the media is in relation to
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

