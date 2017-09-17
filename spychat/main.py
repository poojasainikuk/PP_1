#import details
from spy_details import spy
from start_chat import start_chat

print "Let\'s get started...."
question = "Do you want to continue as " + spy['salutation']  + " " + spy['name'] + " (Y/N) : "
existing = raw_input(question)

 #validating users input

if(existing.upper() == "Y") :
     #user want to continue as default user

     #concatenation aof salutation and name of spy
    spy['name'] = spy['salutation']  + " " + spy['name']

     #starting chat application
    start_chat(spy['name'], spy['age'],  spy['rating'], spy['is_online'])
elif (existing.upper == "N") :
     #user want to continue as a new user
    spy['name'] = raw_input("Provide your name here :")
     #check whether spy has enterd some input or not
    if len(spy['name']) > 0 :
        #input more details about user

        spy['salutation'] = raw_input('what should we call you ? :')
        spy['age'] = int(raw_input("Enter your age?")) #typecasting

        while True:
            try:
                #typecasting
                spy['age'] = int(raw_input("enter your age? "))
                break
            except ValueError:
                print "Invalid age.try again"

        #concatenation of salutation and name
        spy['name'] = spy['salutation'] + " " + spy['name']

        spy['rating'] = float(raw_input(" What is your spy rating?" ))#typecasting

        while True:
            try:
                # typecasting
                spy['rating'] = float(raw_input("enter your rating? "))
                break
            except ValueError:
                print "Invalid rating.try again"

        spy['is_online'] = True

        #starting chat application
        start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])

    else:
        print 'Invalid input. please try again'
else:
    print " Wrong choice.Try again."





