from whiffle import wikidotapi
from util import hook
import re
import time,threading

@hook.command
def scp(inp): #this is for WL use, easily adaptable to SCP
	".tale <Article Name> -- Will return first page containing exact match to Article Name"
	api = wikidotapi.connection() #creates API connection
	api.Site = "scp-wiki"
	pages = api.refresh_pages() #refresh page list provided by the API, is only a list of strings
	line = re.sub("[ ,']",'-',inp) #removes spaces and apostrophes and replaces them with dashes, per wikidot's standards
	for page in pages: 
		if "scp-"+line.lower() == page: #check for first match to input
			if api.page_exists(page.lower()): #only api call in .tale, verification of page existence
				try: #must do error handling as the key will be wrong for most of the items
					if "scp" in api.get_page_item(page,"tags"): #check for tag
						rating = api.get_page_item(page,"rating")
						if rating < 0:
							ratesign = "-"
						if rating >= 0:
							ratesign = "+" #adds + or minus sign in front of rating
						ratestring = "Rating["+ratesign+str(rating)+"]" 
						author = api.get_page_item(page,"created_by")
						authorstring = "Written by "+author
						title = api.get_page_item(page,"title")
						sepstring = ", "
						return "nonick::"+title+" ("+ratestring+sepstring+authorstring+") - http://scp-wiki.net/"+page.lower() #returns the string, nonick:: means that the caller's nick isn't prefixed
				except KeyError:
					pass 
				else:
					return "nonick::Match found but page does not exist, please consult pixeltasim for error."
	return "nonick::Page not found"
		