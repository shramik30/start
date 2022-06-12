import sys
with open("new.data","a") as fp:
	print("Enter the data from key board and press @ to stop")
	while(True):
		kbddata=input()
		if(kbddata=="@"):
			sys.exit()
		else:
			fp.write(kbddata+"\n")
