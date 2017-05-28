import default_spy
import sys

#A function to welcome the spy
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
		

#Ask the user whether to add a new spy or continue with the default one
is_new_user = raw_input("Do you want to add a new spy or continue with the default spy. Enter y or n :")

#If the user wants to create a new spy
if is_new_user == 'y' or is_new_user == 'Y':
	print "Welcome to spy chat!"
	
	#Get the spy name
	spy_name = raw_input("Enter a new spy name: ")

	#If the name is entered
	if len(spy_name)>0:
		spy_salutation = raw_input("What should i call you? (Mr or Ms): ")

		if spy_salutation == "Mr":
			print "Welcome Mr."+spy_name
		elif spy_salutation == "Ms":
			print "Welcome Ms."+spy_name
		else:
			print "That's not a valid salutation"

		#Get the age of the spy as an integer value
		spy_age = int(raw_input("What is your age? "))

		#If the spy age is invalid, then exit the program
		if spy_age<12 or spy_age>50:
			print "Sorry! But we cant accept you to our spy organization :( Bbyee"
			sys.exit()

		#Get the rating of the spy as a float value
		spy_rating = float(raw_input("How would you rate yourself as a spy? "))

		#Check if the spy_rating is valid
		if spy_age<0 or spy_rating>5.0:
			print "Thats not a valid spy_rating!!!!"
		
		#Greet the spy
		welcome(spy_name,spy_age,spy_salutation,spy_rating);

#If the user is the default spy
elif is_new_user == 'n' or is_new_user == 'N':
	#Greet the spy
	welcome(default_spy.spy_name,default_spy.spy_age,default_spy.spy_salutation,default_spy.spy_rating);

#If the user presses anything other than y/n
else:
	print "Invalid Choice!"



