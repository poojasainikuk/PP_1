#import details
from spy_details import spy_name, spy_salutation , spy_age, spy_is_online, spy_rating
from start_chat import start_chat

print "Let\'s get started...."
question = "Do you want to continue as " + spy_salutation  + " " + spy_name + " (Y/N) : "
existing = raw_input(question)

 #validating users input

if(existing.upper() == "Y") :
     #user want to continue as default user

     #concatenation aof salutation and name of spy
    spy_name = spy_salutation  + " " + spy_name

     #starting chat application
    start_chat(spy_name, spy_age,  spy_rating, spy_is_online)
elif (existing.upper == "N") :
     #user want to continue as a new user
    spy_name = raw_input("Provide your name here :")
     #check whether spy has enterd some input or not
    if len(spy_name) > 0 :
        #input more details about user
        spy_age = 0
        spy_rating = 0.0
        spy_is_online = False
        spy_salutation = raw_input('what should we call you ? :')
        spy_age = int(raw_input("Enter your age?")) #typecasting

        #concatenation of salutation and name
        spy_name = spy_salutation + " " + spy_name

        spy_rating = float(raw_input(" What is your spy rating?" ))#typecasting
        spy_is_online = True

        #starting chat application
        start_chat(spy_name, spy_age, spy_rating, spy_is_online)

    else:
        print 'Invalid input. please try again'
else:
    print " Wrong choice.Try again."





