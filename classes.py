"""
classes.py

This is a rough prototype of the discrete data entities in this project. It's intended more to be a reference than a functioning prototype, but it should run and you should be able to perform basic tests with it for your own understanding.

	I'm making it for mine too, to start.  It's to make the way ahead clear. Some people can't intuitively get the math, and I can't express math with mathematical language with any efficiency, but I can build this fucking thing.



And, Welcome. Lets kick some ass.

"""


def IDMAKER(Keyspace):
	"""
	This is a function to generate integer ID's that will probably be unique within a given keyspace. Basically just sequential keys.

	assumes a text-formatted ID.  Just for simplicity."""
	try:
		print(Keyspace)
		Keyspace = Keyspace + 1
		return(int(Keyspace))
	except:
		print("something's fucked! \n\n Value entered was: " + Keyspace + "\n\nHappy Debugging!")

	#	IDMAKER("10")


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
	
	UID 						= 	"" 				#	Unique Identification. every user is unique.
	Username 					= 	""				#	username
	Email 						= 	""				#	email address
	
	#	User Cultural and National Identity attributes
	Languages 					=	[]				#	list of languages user speaks
	Interface_Language 			=	""				#	Still, everybody has a preferred default.
	Time_Zone					=	""				#	The user's time zone <default London, UK>
	Country						=	""				#	

	#	Website attributes
	Owned_Content				=	[]				#	list of content this user owns
	Held_Content				=	[]				#	list of content this user doesn't own but has anyway


	#	Network attributes
	User_Nodes					=	[]				#	list of all nodes that this user has logged in on


	#	User Fiscal Attributes
	User_Local_Currency 		=	""				# 	what the default unit is for earned income
	Earned_Income 				= 	0.0				# 	How much money a user has earned
	Accumulated_Debt			=	0.0				#	How much the user has that they still need to pay for
	Connected_Accounts			=	[]				#	List of accounts that the user can make a withdrawal to

	#	User Functions
	def __init__(self, Keyspace, Username, email):
		"""
		in production, this needs to handle user acount generation and adding users to the program logic from memory. For now, though, the idea is to start with a function that can be called to generate "test users".
		"""
		self.UID = IDMAKER(Keyspace)
		self.Username = Username
		self.Email = email
#		self.Time_Zone = Time_Zone

	#	str function, so that 
	def __str__(self):
		print(self.UID)
		return (self.UID)

class Node:
	"""
	nodes are computers on the network.
	A node holds data (the content pieces, assembled into the content that the user bought or pirated, which are supplied to the network), processes input (user Authentication), and takes actions (sending and receiving content pieces, authenticating with the central server, etc). 
	"""
	mac_address 		=	"" 				# 	all computers have one, although spoofing is a risk
	user_credentials 	= 	"" 				# 	a representation of the username/pass the node proves it has
	content 			= 	[]				# 	a list of the content items a node has (human abstraction 'content')
	pieces				=	[]				#	a list of the content pieces node has (network 'content' data)

	#Node internal attributes
		#	File_Path is commented out because it's unneccessary for local testing
	#File_Path			=	""				#	default directory.  Should have a 'gitignore' knockoff for local files.

	Local_Files			=	[]				#	list of local files


	#server and network attributes
	Local_Keys			=	[]				#	list of keys node possesses

	#	Default Functions
	def __init__(self, mac, usercred):
		self.mac_address = mac
		self.user_credentials = usercred
	def __str__(self):
		return(self.mac_address, self.user_credentials)
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		pass
	
	#	Network behavior functions
	def upload(self, target, ContentPiece):
		pass
	def Bawkserver(self, recipientkey, ContentPiece): #Inform server of successful receipt of contentpiece with x key
		pass
	def getkeys (self, credentials):			#get a new set of authentication keys from the server for uploading
		pass


class Content:
	"""
	Content is the stuff people make and put up for sale. 

	The structure of content is this: 
		content is a "doubletree", where branches dictate version and platform.
			"version" branches dictate *specific attributes*- 
			"platform" branches dictate *specific implementations*- mac vs Windows vs Linux, etc
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

	def __init__(self, Owner, ):
		pass
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		pass
	pass


class ContentPiece:
	"""
	A ContentPiece is the individual packet of data transferred between nodes of the network.
	"""
	Piece_ID 			= 	"" 				#	UniqueID of this piece.
	Piece_FormatType 	= 	""				#	The filetype (size- determined compression block, discrete file, etc)
	Size 				= 	0 				#	integer, if you can type it. It needs to represent the size, in bytes
	Value 				= 	0.0				#	the value of one successful transfer. Used to calculate payment.
	
	#	data members where client and server use the same variables, but for local tasks
	Seeders 			= 	0				#	int or longint, depending on scale
	leechers 			= 	0				#	""
	Downloaders 		= 	0				#	""
	Pirates 			= 	0				#	integer number of pirates uploading this piece
	LastCheck			=	""				# 	datetime of the last time these variables were updated
	
	#	data members used only by the client
	successful_uploads 	= 	0 				#	tracking successful uploads for money.
	attempted_uploads 	= 	0				#	tracking unsuccessful upload attempts
	network_density 	= 	0 				#	tracking number of nodes attempting to upload this piece
	
	#	data members used only be the server
	

	#initialize
	def __init__(self, ID, Size, Value):
		self.Piece_ID= ID
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		self.dispose()
		

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

	#security stuff, so different people can have different media
	Media_Owner_Account	=	""				#	ID of the User who owns the content/media in question

	
	def __init__(self, owner):
		self.Media_Owner_Account = owner
		pass
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		pass
	

class Authentication:
	"""
	Authentication is how the network tracks who's who, has what, and has sent which, when and to whom.  It consists of a set of keys that are recycled, and the combinations of which correlate to an interior database for record keeping. there are other parts to this, mostly based around making it difficult to predict, intercept, decipher, and use, even in long-term attacks, and so for the long term players the idea is to send them on a rat race of the same data over and over, and to change what it means every time. In old-school encryption terms, the idea is to keep anybody outside at a permanent depth of one (ref leo marks between silk and cyanide).
	"""
	# Attributes
	UniqueID 		=		""		#	the ID of the Authentication object
	UserID 			=		""		#	the ID of the user who holds it (proxy ID)
	log 			=		{}		#	a log of instances where this key has been used to sign a transfer

	def __init__(self):
		pass
	def read(self):
		pass
	def update(self):
		pass
	def delete(self):
		pass
	
class Money:
	"""
		Money is the stuff everybody wants. 

		A "Money" is an object that describes the value for a ContentPiece. Value is determined by dividing the content by the number of bits- or failing that, bytes- arriving at a base value per bit- and then this is multiplied by the size of each ContentPiece to determine the size of each of their moneys.

		Linguistic note for humans: singular "Money", plural "Moneys".

		This class describes arbitrary amounts of value, in specific currencies, for specific ContentPiece instances. This is important, because a foundational premise of this network is the idea that transactions can be infinitely arbitrarily sized- to the extreme low end, and to the extreme high end.

		When Content iterates (new versions), Moneys need to be recalculated.

		Hmm. That smells like bullshit. Maybe there's a better way than that.

		Anyway, this is a server attribute.  Moneys are assigned centrally, upon verification.  A transfer that can't be verified can't be paid for, logically, because it opens the system up to paying out outputs that have no input.

		However, there is one thing the client side of the network can know about money: The amount.  This allows a client node to make decisions based on fiscal outcomes.  This is how money is used in the network as a dimension of data along which more efficient transfers can be optimized, rather than simply the scarcity model used in traditional peer networks.
	"""
	#	base attributes
	Currency_ID 			= 			""
	Currency_Name 			= 			""
	Content_ID 				= 			""

	#	Server-only Attributes
	Cash_Value 				=			0.0			#this is a float by default (provisional early research)


	#	Client side attribuets
	HashKey					=			""

"""
User_Keyspace = 0

TestUser1 = User(User_Keyspace, "derp", "derp")
TestUser2 = User(User_Keyspace, "derp", "derp")

TestUser1.__str__()
TestUser2.__str__()

TestUser3 = User(User_Keyspace, "derp", "derp")
TestUser3.__str__()
"""