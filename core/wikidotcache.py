from time import sleep
import thread
import datetime
from whiffle import wikidotapi


def cache_refresh(): #calls itself automatically once called for the first time
	api = wikidotapi.connection()
	pages = api.refresh_pages()
	print "Refreshing cache"
	newpagecache = [] #the newpagecache is so that while it is updating you can still use the old one
	for page in pages:
		newpagecache.append(api.server.pages.get_meta({"site": api.Site, "pages": [page]}))
		time.sleep(0.4) #this keeps the api calls within an acceptable threshold
	print "Cache refreshed!"
	__builtin__.pagecache= newpagecache #__builtin__ means that pagecache is global and can be used by plugins
	ts = time.time()
	__builtin__.lastcacherefresh = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	time.sleep(3600) #one hour 
	cache_refresh() #calls itself again