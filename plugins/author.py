from whiffle import wikidotapi
from util import hook

@hook.command
def author(inp):
	".author <Author Name> -- Will return details regarding the author"
	if firstrefresh == 0:#make sure the cache actually exists
		return "Cache has not yet updated, please wait a minute and search again."
	api = wikidotapi.connection()
	api.Site = "wanderers-library"
	pages = api.refresh_pages()
	authpages = []
	totalrating = 0
	pagetotal = 0
	pagerating = 0
	author = "None"
	multimatch = []
	authorpage = ""
	for page in pages:
		for item in pagecache: #these two for loops iterate through every item within each page dictionary, the proper syntax for accessing a specific item is item[page][itemname],
			try: 
				if "entry" in item[page]["tags"]: #makes sure only articles are counted
					if author == item[page]["created_by"]:
						authpages.append(page)
						pagetitle = item[page]["title"]
						pagerating = item[page]["rating"]
						totalrating = totalrating + pagerating
						print page
						pagetotal = pagetotal + 1 
					if inp.lower() in item[page]["created_by"].lower() and author == "None": #this just matches the author with the first author match
						author = item[page]["created_by"]
						authpages.append(page)
						pagetitle = item[page]["title"]
						pagerating = item[page]["rating"]
						totalrating = totalrating + pagerating
						print page
						pagetotal = pagetotal + 1 #all lines above provide page data, math is pretty easy and self-explanatory
				else:
					if "author" in item[page]["tags"]:
						if author == item[page]["created_by"]:
							authorpage = "http://wanderers-library.wikidot.com/"+item[page]["fullname"] +" - "
			except KeyError: #must do error handling for code to be valid, iterates through incorrect keys multiple times, do not print things in the except clause, slows down program immensely 
				pass
	for page in pages: #this loop checks to see if multiple authors match input 
		for item in pagecache:
			try:
				if "entry" in item[page]["tags"]:
					if inp.lower() in item[page]["created_by"].lower():
						multimatch.append(item[page]["created_by"])
			except KeyError:
				pass
	for authors in multimatch: #checks to see if multiple authors found 
		if authors != author:
			return "There are "+ str(len(multimatch)) + " authors matching you query. Please be more specifc. " 
	avgrating = 0
	if pagetotal is not 0: #just so no division by zero
		avgrating = totalrating/pagetotal
	if not authpages: #if no author pages are added 
		return "Author not found."
	return "nonick::"+ authorpage+""+author +" has written " + str(pagetotal) + " pages. They have " + str(totalrating)+ " net upvotes with an average rating of " + str(avgrating) + ". Their most recent article is " + pagetitle + "(Rating:" + str(pagerating) + ")"#+"- http://wanderers-library.wikidot.com/" + authpages[-1].lower()