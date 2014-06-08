from whiffle import wikidotapi
from util import hook
import re
import time,threading

@hook.command
def tale(inp):
	".tale <Article Name> -- Will return first page containing exact match to Article Name"
	api = wikidotapi.connection()
	pages = api.refresh_pages()
	line = re.sub("[ ,']",'-',inp)
	for page in pages:
		for item in pagecache:
			if line.lower() in page:
				if api.page_exists(page.lower()):
					try:
						rating = item[page]["rating"]
						if rating < 0:
							ratesign = "-"
						if rating >= 0:
							ratesign = "+"
						ratestring = "Rating["+ratesign+str(rating)+"]"
						author = item[page]["created_by"]
						authorstring = "Written by "+author
						title = item[page]["title"]
						sepstring = ", "
						return "nonick::"+title+" ("+ratestring+sepstring+authorstring+") - http://wanderers-library.wikidot.com/"+page.lower()
					except KeyError:
						pass 
				else:
					return "nonick::Match found but page does not exist, please consult pixeltasim for error."
	return "nonick::Page not found"
		


	