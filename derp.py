"""
This is a simulation case of the expletive project, just done as a thought experiment/test case.

I'm doing this because I'm scared shitless that the fucking thing won't work, and that I've gone insane, and
I need to reason my way back to sanity.  My apologies if this reads unusually, I'm just trying to make this
run.

Because if it fucking runs, I'm going to do cool stuff with it.
"""

#imports must be justified
#import decimal
#sqlite3 to store data by default
import sqlite3

import Classes

#random, for testing
import random

try: 
	#set up database
	"""
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	# Create table
	c.execute('''CREATE TABLE stocks
	             (date text, trans text, symbol text, qty real, price real)''')
	# Insert a row of data
	c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
	# Save (commit) the changes
	conn.commit()
	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	conn.close()
	"""
	print ("example DB ran")
except:
	print("example DB didn't run")

#srs DB attempt
try :
	Proto_DB = sqlite3.connect('prototype.db')
	P= Proto_DB.cursor()

	#creating tables
	#P.execute('''CREATE TABLE content
					#(date text, title text, owner text, unique_ID text, price real)''')
	#P.commit()
	P.list('''tables'''	)

	P.close()


	print("Prototype DB ran")
except: 
	print("try didn't run")
	pass

#determine the price for a piece of content
def dataprice (dataoalsize, dataoalprice):
	#price per byte
	byteprice =  (dataoalprice / dataoalsize)
	#show data
	print("price per byte: ", byteprice)

#Simulation content for demonstration purposes
class Content:
	Content_ID = ""
	Content_Name = ""
	Content_Data = 0
	Content_Price = 0.0
	Content_Byteprice = 0.0
	def __Init__(self, __ID__, name, data, price):
		self.Content_ID = __ID__
		self.Content_Name = name
		self.Content_Data = data
		self.Content_Price = price
		self.Content_Byteprice = self.Content_Price / self.Content_Data
	def __str__(self):
		#this is a function to return the values of each of the default data members as CSV
		return  self.Content_ID, self.Content_Name, self.Content_Data, self.Content_Price, self.Content_Byteprice
	def __serialize__(self):
		pass

Derp = (Content)
Derp.__Init__(Derp, 1, "Herp", 1024, 1.00)

#a simulation peernode
class PeerNode:
	#attributes:
	unique_ID = ""
	name = ""

	#Address for FTP'ing files
	Node_Address = ""
	#the content a node has on it
	pass


#This exists as an intermediary for other classes to describes the relationships to content
# Eg, users have "owned content" and "held content" (stuff they own, vs stuff they have)
#Content creators have a list of "original content" etc. That's what this is for.
class Content_List():
	pass

#a simulation of the server
class server:
	"""
	What goes here?
		a list of data that the server has to server
		the content hosted on the network
			every location of every piece
	"""

	Master_Content_List = {}		#This is the list of actively directoried content that the server makes available to the network.
	Content_Piece_List = {}
	Peer_List = {}
	User_List = {}
	User_Transfer_Keyspace = {}

	pass

class User():
	Username = ""
	Password = ""
	Owned_Content = (Content_List)




"""
#testing
dataprice (1024, 1.00)
print(Derp.__str__(Derp))
"""

def __main__():
	print("derpmain")
	print("Press any key to exit...")
	pass

__main__()