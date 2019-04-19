import requests

def act():
	print("\n GSI Command installer \n")

	print("Please type the name of the command you would like to install.")
	com = input("--->")

	print("Connecting to the GSI command repository...")

	rqc = requests.get("http://localhost/gsicentral/cmdindex.txt")
	