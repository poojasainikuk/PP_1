#import statements

from globals import STATUS_MESSAGES

updated_status_message = None
def add_status(current_status_message):
    if current_status_message != None:
        print 'your current status message os %s \n' % (current_status_message)
    else:
        print 'you don\'t have any status message currently \n'

    #ask user for choosing from older message.
    default = raw_input("do you want to selectfrom older status (Y/N)? ")


    if default.upper() == "N" :
        new_status_message = raw_input("what status messagew do you want to set?: \n ")


        #validating use input.
        if len(new_status_message) > 0:
            #adding new status messageto the list.
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
            print 'your updated status message is: %s' % (updated_status_message)
        else:
            print "you did not provide any status message.Try again." \


    elif default.upper() == 'Y' :
        #counter for serial number of message.
        item_position = 1

        #for printing all older message.
        for message in STATUS_MESSAGES:
            print '%d. %s' %(item_position, message)
            item_position = item_position + 1

        #asking user choice.
        message_selection = int(raw_input("\nChoose from the above message \n"))

        #validating user input.
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
            print 'your updated status message is: %s' % (updated_status_message)
        else:
            print "invalid choicde. try agin."
    else:
        print 'the option you choose is not valid! press either y or n'

    return updated_status_message
