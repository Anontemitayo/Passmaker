#Check my code but do not steal it!
import time as t
import os
import sys


os.system('clear')
print(''' \033[1;33;40m
 ____                               _             
|  _ \ __ _ ___ ___ _ __ ___   __ _| | _____ _ __ 
| |_) / _` / __/ __| '_ ` _ \ / _` | |/ / _ \ '__|
|  __/ (_| \__ \__ \ | | | | | (_| |   <  __/ |   
|_|   \__,_|___/___/_| |_| |_|\__,_|_|\_\___|_|   

[+] Coded by Anontemitayo
[✓]  A tool to generate a victim based password list
\033[0m
  ''')
choice = '''\033[1;31;40m
 [1] 1 victim password list
 [2] 2 victims password list
 [3] Usage and About the tool
 [4] Exit the tool  \033[0m
 
 '''
print(choice)
cho = int(input('\033[1;31;40m Enter a number : '))
if cho == 1:
	os.system('clear')
	print(''' \033[1;33;40m
 ____                               _             
|  _ \ __ _ ___ ___ _ __ ___   __ _| | _____ _ __ 
| |_) / _` / __/ __| '_ ` _ \ / _` | |/ / _ \ '__|
|  __/ (_| \__ \__ \ | | | | | (_| |   <  __/ |   
|_|   \__,_|___/___/_| |_| |_|\__,_|_|\_\___|_|   

[✓]  A tool to generate a victim based password list
 ''')
	Vic = str(input(" Enter your victim's name : "))
	with open('/storage/emulated/0/password.txt','w') as f:
	 	hi = Vic.upper()
	 	low = Vic.lower()
	 	cap = Vic.capitalize()
	 	f.write(hi)
	 	f.write("\n")
	 	f.write(cap)
	 	f.write("\n")
	 	f.write(low)
	 	f.write("\n")
	 	for i in range(0,1001):
	 		wor = Vic+str(i)
	 		f.write(wor)
	 		f.write("\n")
	f.close()
	t.sleep(1)
	print('''
\033[1;32;40m Your  file has been created ✓
File path : /storage/emulated/0/password.txt
''' )
	
elif cho == 2 :
 os.system('clear')
 print(''' \033[1;33;40m
 ____                               _             
|  _ \ __ _ ___ ___ _ __ ___   __ _| | _____ _ __ 
| |_) / _` / __/ __| '_ ` _ \ / _` | |/ / _ \ '__|
|  __/ (_| \__ \__ \ | | | | | (_| |   <  __/ |   
|_|   \__,_|___/___/_| |_| |_|\__,_|_|\_\___|_|   

[✓]  A tool to generate a victim based password list 

''')
 Name = str(input("\033[1;32;40mEnter the name of your victim : "))
 Aname = input('Enter a password you think he/she can use: ')

 digit = int(input('Enter the numbers you think he/she can use [Numbers only e.g12345] :  '))
 num = str(digit)

 with open('/storage/emulated/0/passwordlist.txt','w') as file:
 	low = Name.upper()
 	hi = Name.lower()
 	cap = Name.capitalize()
 	alow = Aname.upper()
 	ahi = Aname.lower()
 	aca = Aname.capitalize()
 	file.write(low)
 	file.write("\n")
 	file.write(hi)
 	file.write("\n")
 	file.write(cap)
 	file.write("\n")
 	file.write(ahi)
 	file.write("\n")
 	file.write(alow)
 	file.write("\n")
 	file.write(aca)
 	file.write("\n")
 	file.write(num)
 	file.write("\n")
 	for i in range(0,1000):
	    passt = Name+str(i)
	    file.write(passt)
	    file.write("\n")
	    passk = Aname+str(i)
	    file.write(passk)
	    file.write("\n") 
 file.close()
 t.sleep(1)
 print('''\033[1;32;40m
Your  file has been created ✓
File path : /storage/emulated/0/passwordlist.txt
''' )
elif cho == 3:
	os.system('clear')
	print(''' \033[1;33;40m
 ____                               _             
|  _ \ __ _ ___ ___ _ __ ___   __ _| | _____ _ __ 
| |_) / _` / __/ __| '_ ` _ \ / _` | |/ / _ \ '__|
|  __/ (_| \__ \__ \ | | | | | (_| |   <  __/ |   
|_|   \__,_|___/___/_| |_| |_|\__,_|_|\_\___|_|   

[✓]  A tool to generate a victim based password list

  ''')
	print('''\033[1;33;40m
	[+] About the tool : 
The tool is created by Anontemitayo to generate a victim based password list
	[+] Usage:
Choose 1 to create a victim based password list with only one name(Victim's)
Choosing 2 gives you the opportunity to create a victim based password list with the victim's name , Any password you think the victim might use and digit you think the victim can use
		''')
elif cho == 4:
	os.system('clear')
	sys.exit()