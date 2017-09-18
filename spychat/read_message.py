from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends


def send_message():
    sender = select_friend()

    secret_image = raw_input("enter encrypted image: ")
    secret_text = Steganography.decode(secret_image)

    #save the data
    new_chat = {
        "message" : secret_text
        "time" : datetime.now()
        "sent_by_me" : False
    }

    friends[sender]['chats'].append(new_chat)
    print "your secret message  has been saved."