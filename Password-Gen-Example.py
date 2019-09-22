loginNo = input("Login To Enter Login Password: ").replace(" ","")
if len(loginNo) != 10:
	print("Invalid Login Password")
	exit()



def CheckBit(code,verify=True,bit=9):
	checkBit = []
	checkBit += code
	codeArr = []
	for i in range(0,len(code)):
		if i == bit:
			continue
		codeArr.append(int(checkBit[i]))
	checksum = sum(codeArr) % 10
	if verify == False:
		return checksum
	if code[bit] == str(checksum):
		return 10
	else:
		return checksum


		
def FindType(code):
	if (code[3] == "8" or code[3] == "9") and CheckBit(code,True,4) == 10:
		return 4
	elif (code[3] == "2" or code[3] == "3") and CheckBit(code,True,5) == 10:
		return 2
	elif (code[3] == "4" or code[3] == "5") and CheckBit(code,True,7) == 10:
		return 3
	elif (code[3] == "7" or code[3] == "6") and CheckBit(code,True,8) == 10:
		return 1
	elif (code[3] == "0" or code[3] == "1") and CheckBit(code,True,9) == 10:
		return 0
	else:
		return 5

def FindCheckLoc(code):
	i = 0
	while i < len(code):
		print("CHECK "+str(i)+","+str(CheckBit(code,True,i)))
		i = i +1

def GetTamaIndex(code, type):
	tamaIndex = []
	if type == 0: 
		tamaIndex.append(code[5])
		tamaIndex.append(code[8])
	elif type == 1: 
		tamaIndex.append(code[5])
		tamaIndex.append(code[7])
	elif type == 2: 
		tamaIndex.append(code[2])
		tamaIndex.append(code[4])
	elif type == 3: 
		tamaIndex.append(code[8])
		tamaIndex.append(code[4])
	elif type == 4:  
		tamaIndex.append(code[9])
		tamaIndex.append(code[7])
	return tamaIndex

def GetTamaRegion(code, type):
	if type == 0: 
		return code[1]
	elif type == 1: 
		return code[0]
	elif type == 2: 
		return code[1]
	elif type == 3: 
		return code[2]
	elif type == 4: 
		return code[5]


type = FindType(loginNo)
if type != 5:
	tIndex = GetTamaIndex(loginNo,type)
	tRegion = GetTamaRegion(loginNo,type)
	
	print("Recognized Type! " + str(type))
	print("Tama Index: "+str(tIndex))
	print("Tama Region: "+str(tRegion))
	
	win = input("Are you a WINNER? [y/n] ").lower()
	if win == "y":
		what = input("What did you win? [item/money] ").lower()
		if what == "item":
			which = input("What item did you win? (enter id) [000:999] ").lower()
			while len(which) < 3:
				which = "0"+which
			logout = "3"+str(tRegion)+str(which)+"\n"+str(tIndex[0])+"01"+str(tIndex[1])
			logout += str(CheckBit(logout.replace("\n",""),False))
			print("OK Good day sir! \n"+logout)
		if what == "money":
			howmuch = input("How much did you win? (01=100GP, 02=200GP, 03=500GP, 04=700GP, 05=1000GP)").lower()
			if len(howmuch) == 1:
				howmuch = "0"+howmuch
			logout = "2"+str(tRegion)+"000\n"+str(tIndex[0])+str(howmuch)+str(tIndex[1])
			logout += str(CheckBit(logout.replace("\n",""),False))
			print("OK Good day sir! \n"+logout)
	else:
		logout = "1"+str(tRegion)+"000\n"+str(tIndex[0])+"01"+str(tIndex[1])
		logout += str(CheckBit(logout.replace("\n",""),False))
		print("OK Good day sir! \n"+logout)
	
else:
	print("Invalid Login Password!")
	
	
