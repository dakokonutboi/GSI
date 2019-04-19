import requests

def act():
	print("Please type the location to the file that you want to get. (Do not forget the 'http://' in the beginning of the location)")
	loc  = input("--->")
	print(requests.get(loc).text)