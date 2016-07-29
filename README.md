# TheExpletiveProject 

Purpose:

This project is intended to be a startup (to make money) by implementing a solution to the problems of piracy and digital content delivery.

Description of Function:

This- the public facing portion of this endeavor- is a peer network that can only upload content to known customers (this allows income from those customers), but which can be uploaded to by anybody on the condition that the content uploaded is identical. This provides the customers with a service- content delivery, on demand. For providing this service, part of the sale goes to the people running the computer that successfully uploaded the content they bought. This means that for uploading content, normal users on the network can earn money passively- just by leaving their computers on.

Since the premise of this project is to earn money AND solve piracy, the way piracy is dealt with is this: if a pirate uploads enough content to customers to pay for a copy of their pirated content, they don't get the money from the thing they don't own, we buy it for them- because they've earned it- and then they can start earning money afterwards like everyone else.  Hopefully, the opportunity to immediately and easily spend money on other pieces of the same kind of content these users like will entice further sales, but if not, they have earned what they keep and so we can profitably afford to give it to them.

Now, on the back end of this there is some spooky black magic that I've been working on for a while, because this isn't a new idea. Part of the requirements mean knowing where the money is coming in AND where the money is going out, and part of the risk with having money involved is abusive behavior- so I've got some kooky vindictive devious backstabbing-- technicaly legal-- little ideas I've been implementing. If you know about this stuff and have input, I'd love to hear it.

#Todo for this project:

-get website up and running that tests can be run on 
	--Domain registerd (www.TheExpletiveProject.com)
	--Hosting- Heroku (free) and AWS learning (expires march 2016...? double check)
	-- Dango 4, python 3.5

-get authentication server up and runnig 
	--Prototyping/testing
		---google appengine/Golang
		---Python 2.7/Django3.5 [RIP]

-get client software up and running
	--QBittorrent fork : platform independent (mac, linux, win)
		---Extend authentication services-
			----[blackbox]

#Business 

I haven't registered this as a business, and won't until there's more than me working on it, or until I have income to report from it. 

So far, there are people who have committed to being users (some customers, some sellers, some evangelists), but there is nothing for them to use.

If you do something that makes the company, the split is 50% gets held by the company, and the rest of the profit is divided among each employee. The 50% taken by the company is the operating capital.

Update: 7/15/15

This project needs to have a EULA.  Since it is open-source, at least to the extent that you're reading this right now, I figure I can put some ideas up and if any of them piss people off too much, I can change them later.

basics:

By signing up, you agree to participate on the terms that this network specifies. These specifications all have a purpose; their aim is to protect the network first, and the individual users (including affiliates, members of Expletive Interactive, ad nauseum) second. There are no exceptions to these rules.

By downloading content, you undestand and agree to the following:
	to allow your computer to report to the network what the source of that content was; this is to let that source get paid.

By uploading content, you understand and agree to the following:
	that the content you have arranged, to the best of your ability, to upload exactly the content that is being requested, and have not added or removed any part of it, for any reason
		that further, if you upload abusive content- including but not limited to content which deliberately manipulates the network for your own financial gain, for the targeted financial loss of another, or which attacks members of the network in any other way- for any reason- then the budget that will be allocated to interdicting you will be twice the opportunity cost your behavior on the network has inflicted, and any means that are legally available in any location you may be will be utilized, within the scope of that budget, to prevent you from continuing such actions.


#Philosophies


As a general principle, I think you should get what you earn. So I have ideas for calculating how much everything in this project might conceivably be worth. Example: if you make the only client program for this network on your platform, you get some commission on every new unique customer from that platform, or something cool like that. Let's make this fair, but let's give people a reason to participate.

So, there are perhaps 5-6 billion people online, but only 2 billion participating in the online economy. Part of the problem seems to be that there is no way, by default, to participate; but since the delivery of content is such a standard transaction, and since it can be monetized this way, it gives the content delivery networks the advantage of human ingenuity over its predecessor networks; this is a network type that can literally accomodate a sneakernet as a delivery mechanism for its content.

There is also an infinite wellspring of potential that comes from having this sort of availability of data, whether it's kids in asia learning English from playing CounterStrike or StarCraft or the mom and pop shops who can operate a photo studio thanks to a pirated copy of photoshop on their workhorse Pentium 3. By not facilitating this, the traditional distribution economy incurs unnecessary opportunity cost; but by the piracy that solves it by inflicting the opportunity costson the content creators. A good solution is to use piracy as the means of distribution to customers- so this project is the implementation of that solution.

This project is simply the first of many that will implement experimental methods of monetizing this wellspring of opportunity. I think this can be used to cure AIDS and cancer and end world hunger, not by itself, but as a first step in the process of getting ourselves to the point where we can do it independently everywhere. Having a first step- like a high performance authenticated distributed network- is the kind of thing you can build on, to do distributed computing for things like HIV and Cancer research. so to that extent, this is a humanitarian project as well.

#Contributors

Kendall Meade

	The originator of this project.  I'm a former missionary, amateur linguist and historian, a student of every discipline I can discover information on, and an omnivore of the human experience. I'm also a single dad living in a basement with his kids, so my time to contribute code and make revisions is limited.
