import default_spy
import sys

#A function to welcome the spy with a cool message
def welcome(name,age,salutation,rating):
	print "********************************"
	print "Logging you in...\n"
	print "Welcome "+salutation+". "+name
	print "Your details are as under: "
	print "============================"
	print "Age = "+str(age)
	print "Rating = "+str(rating)
	
	#Print appropriate message according to the spy rating
	if rating >= 4.5:
		verdict = "Wow! You are such an awesome spy xO "
	elif rating<4.5 and rating >= 3.5:
		verdict = "You are cool. :)"
	elif rating<3.5 and rating>=2.5:
		verdict = "Mehh! Keep working hard spy. You still have a long way to go!"
	else:
		verdict = "Beta. Tumse naa ho paaega!"

	print "Verdict = "+verdict
	print "============================" 
		
#Define the variables required as global
spy_name = ""
spy_salutation = ""
spy_rating = 0
spy_age = 0



#Ask the user whether to add a new spy or continue with the default one
is_new_user = raw_input("Do you want to add a new spy? Enter y or n :")

#If the user wants to create a new spy
if is_new_user.lower() == 'y':
	print "Welcome to spy chat!"
	
	#Get the spy name
	spy_name = raw_input("Enter a new spy name: ")

	#If the name is entered
	if len(spy_name)>0:
		
		#Accept input until a valid spy salutation is specified
		is_invalid_sal = True
		while is_invalid_sal:
			spy_salutation = raw_input("What should i call you? (Mr or Ms): ")
			if spy_salutation.lower() == "mr":
				print "Welcome Mr."+spy_name
				is_invalid_sal=False
			elif spy_salutation.lower() == "ms":
				print "Welcome Ms."+spy_name
				is_invalid_sal=False
			else:
				print "That's not a valid salutation. Try Again!"

		#Get the age of the spy as an integer value
		spy_age = int(raw_input("What is your age? "))

		#If the spy age is invalid, then exit the program
		if spy_age<12 or spy_age>50:
			print "============================================================="
			print "Sorry! But we cant accept you to our spy organization :( Bbyee"
			sys.exit()

		is_invalid_rating = True

		#Accept input until a valid spy rating is specified
		while is_invalid_rating:
			#Get the rating of the spy as a float value
			spy_rating = float(raw_input("How would you rate yourself as a spy? "))

			#Check if the spy_rating is valid
			if spy_age<0 or spy_rating>5.0:
				print "A true spy rates himself between 0 and 5. Try again!!"
			else:				
				is_invalid_rating = False

#If the user is the default spy
elif is_new_user.lower() == 'n':
	#Assign the default values to the variables
	spy_name = default_spy.spy_name
	spy_age = default_spy.spy_age
	spy_rating = default_spy.spy_rating
	spy_salutation = default_spy.spy_salutation

#If the user presses anything other than y/n
else:
	print "A spy chooses his letters wisely. You shall not pass!! "
	print "Terminating program..."
	sys.exit()

#Greet the spy
welcome(spy_name,spy_age,spy_salutation,spy_rating)

#Menu for the spy
while True:
	print "+=+=+=+=+=+= SPY MENU =+=+=+=+=+=+=+=+"
	print "1) Add a status update"
	print "2) Add a friend"
	print "3) Send a secret message" 
	print "4) Read a secret message"
	print "5) Read chats from a user"
	print "6) Close application"

	choice = int(raw_input("Enter your choice: "))
	print "You chose "+str(choice)

	if choice == 1:
		pass
	elif choice == 2:
		pass
	elif choice == 3:
		pass
	elif choice == 4:
		pass
	elif choice == 5:
		pass
	elif choice == 6:
		print "============================"
		print "The program will now terminate."
		print "Adios Spy!"
		break
	else:
		print "The choice is invalid. Try again!"
