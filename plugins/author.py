from whiffle import wikidotapi
from util import hook

@hook.command
def author(inp):
	".author <Author Name> -- Will return details regarding the author"
	api = wikidotapi.connection()
	pages = api.refresh_pages()
	authpages = []
	total = 0
	pagetotal = 0
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
					else: #only if there is no author found yet, so in an ambigious input it only returns one author
						if inp.lower() in item[page]["created_by"].lower(): #this just matches the author with the first author match
							author = item[page]["created_by"]
							authpages.append(page)
							pagetitle = item[page]["title"]
							pagerating = item[page]["rating"]
			except KeyError:
				pass
	for page in authpages:
		rate = api.get_page_item(page,"rating")
		total += rate
		pagetotal = pagetotal+1
	avgrating = 0
	if pagetotal is not 0:
		avgrating = total/pagetotal
	if not authpages:
		return "Author not found."
	#if author == "Pixeltasim":
		#return "nonick::Fantastic Man"+" has written " + str(pagetotal) + " pages. With an average rating of " + str(avgrating) + ". Their most recent article is " + pagetitle + "(Rating:" + str(pagerating) + ") -http://wanderers-library.wikidot.com/" + authpages[-1].lower()
	return "nonick::"+ author +" has written " + str(pagetotal) + " pages. They have " + str(total)+ " net upvotes. With an average rating of " + str(avgrating) + ". Their most recent article is " + pagetitle + "(Rating:" + str(pagerating) + ")- http://wanderers-library.wikidot.com/" + authpages[-1].lower()