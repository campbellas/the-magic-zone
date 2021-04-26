import sys
#This is a playful program that will print a list of fibonacci sequence numbers.
fiboNumList = [0, 1]
firstNum = 0
secondNum = 1


print("\n" * 75 + "Please indicate how many items you want: ")

###Get number of fibonacci sequence. If 0, 1, 2: print.  Else: calculate###
#ValueError and KeyboardInterrupt exceptions handled
while True:
	try:
		numWanted = input(">>  ")
		
		#0, 1, 2: Print and exit
		if int(numWanted) == 0:
			print("Cheeky bugger, why did you even call this program?")
			sys.exit()
			
		elif int(numWanted) == 1:
			print("[0]")
			sys.exit()
			
		elif int(numWanted) == 2:
			print("[0, 1]")
			sys.exit()
		
		#3 and above: calculate now, print later
		else:
			#Without the -2, a list 3 or higher will include 2 additional values
			for num in range(int(numWanted)-2):
				holdIt = fiboNumList[firstNum] + fiboNumList[secondNum]
				firstNum += 1
				secondNum += 1
				fiboNumList.append(holdIt)
			
			break
	
	
	except ValueError:
		print("That number is not a valid number.")
		
	except KeyboardInterrupt:
		print("\n" * 75 + "Thank you for coming")
		sys.exit()

 #print the result
print(fiboNumList)
