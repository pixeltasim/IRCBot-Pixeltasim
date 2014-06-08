from util import hook

@hook.command
def thorn(inp):
	return "Thorn is a version 1.0 SkyBot maintained with added functionality by Pixeltasim. Thorn has updated its cache last at " + lastcacherefresh 
@hook.regex("hugs thorn")
def hug(match):
	return "nonick::I'm just going to stand here stoically"
@hook.regex("thorn sucks")
def insultpart(match):
	return "nonick::That really hurts"
