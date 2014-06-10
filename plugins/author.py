from whiffle import wikidotapi
from util import hook

@hook.command
def author(inp):
	".author <Author Name> -- Will return details regarding the author"
	api = wikidotapi.connection()
	pages = api.refresh_pages()
	authpages = []
	totalrating = 0
	pagetotal = 0
	pagerating = 0
	author = "None"
	for page in pages:
		for item in pagecache: #these two for loops iterate through every item within each page dictionary, the proper syntax for accessing a specific item is item[page][itemname],
			try: 
				if "entry" in item[page]["tags"]: #makes sure only articles are counted
					if author != "None":
						if author == item[page]["created_by"]:
							authpages.append(page)
							pagetitle = item[page]["title"]
							pagerating = item[page]["rating"]
							totalrating = totalrating + pagerating
							pagetotal = pagetotal + 1 
					else: #only if there is no author found yet, so in an ambigious input it only returns one author
						if inp.lower() in item[page]["created_by"].lower(): #this just matches the author with the first author match
							author = item[page]["created_by"]
							authpages.append(page)
							pagetitle = item[page]["title"]
							pagerating = item[page]["rating"]
							totalrating = totalrating + pagerating
							pagetotal = pagetotal + 1 #all lines above provide page data, math is pretty easy and self-explanatory
			except KeyError: #must do error handling for code to be valid, iterates through incorrect keys multiple times, do not print things in the except clause, slows down program immensely 
				pass
	avgrating = 0
	if pagetotal is not 0: #just so no division by zero
		avgrating = totalrating/pagetotal
	if not authpages: #if no author pages are added 
		return "Author not found."
	return "nonick::"+ author +" has written " + str(pagetotal) + " pages. They have " + str(totalrating)+ " net upvotes with an average rating of " + str(avgrating) + ". Their most recent article is " + pagetitle + "(Rating:" + str(pagerating) + ")- http://wanderers-library.wikidot.com/" + authpages[-1].lower()