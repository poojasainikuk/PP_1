from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from globals import friends


def send_message():
    friend_choice = select_friend()

    original_image = raw_input("enter the name of image to hide the message : ")
    output_image = raw_input("enter name of output image: ")
    text = raw_input("enter your message :")

    #encrypt the message
    Steganography.encode(original_image, output_image, text)

    # save the send message
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_choice]['chats'].append(new_chat)
    print "your secret message  has been saved."