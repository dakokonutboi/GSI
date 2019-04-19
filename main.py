print("GSI Started")

print("Loading components...")

import os, sys, time, requests, ppxlib, gsiconfig

pp = ppxlib

cmd = ""

username = ""

if gsiconfig.username == "":
	print("Please type the username you would like to use :")
	username = input("--->")
else:
	username = gsiconfig.username

status = "root"

trig = False

loop = True




while loop:
	try:
		print("---$["+username+"] @ ["+status+"]---}")
		cmd = input(">")
		trig = False
		exec("import gsicmd_" + cmd)
		exec("gsicmd_"+cmd+".act()")
	except ModuleNotFoundError:
		print("The command ["+cmd+"] is not recognized by GSI, check what you typed or try installing the command is it is not installed.")
	except NameError:
		print("The command ["+cmd+"] is not recognized by GSI, check what you typed or try installing the command is it is not installed.")
	except KeyboardInterrupt:
		print("Do you really want to exit GSI? If you do, type 'yes', if you do not, type any other thing.")
		ans = input("--->")
		if ans == "yes":
			exit()
		else:
			pass