import classes
#import mktorrent


#Network initialization, putting together examples of all the pieces to make sure they all exist and can be used by the network.
def __init__():
	try:
		nodes = []
		users = []
		content = []
		
	except Exception, e:
		raise
	else:
		pass
	finally:
		pass



def __main__():
	print("derp")


__main__()

##below this is unimportant stuff, tests, or scratch. mostly ignore it.

#This is hows I mathing. Kawthort.
def mathmaker(nodes, pirates, songs, price, share, customers):		#nodes are the compters, songs are the things shared, price is cost, share is %awarded, customers is # sold
	print("pirate share is: %s spread per pirates") %(((((pirates/nodes) * share) * customers)/songs)-(songs*price)/pirates)
	
	print("non-pirate share is: %s")	%(((((nodes-pirates) * share) * customers)/songs)/(nodes-pirates))
	
	print("network share is: %s")%((price*share) * customers)
	
	print("songs paid for in full by pirates that otherwise wouldn't be: %s") %(((((pirates) * price )* share)*customers)/songs) 

	print("Total sales volume: %s") %(price * customers)

mathmaker(100.0, 90.0, 100.0, 1.0, 0.1, 10000.0)
			# 	100 nodes, 90 of them pirates, uploading 100 different songs at $1 each for a $0.10 share, at 10k uploads 
mathmaker(100.0, 99.0, 1.0, 1.0, 0.1, 10000.0)				
			#
mathmaker(100.0, 99.0, 10000.0, 1.0, 0.1, 10000.0)