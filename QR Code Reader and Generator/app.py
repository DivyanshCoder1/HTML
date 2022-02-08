import qrcode
import cv2

def wholefunc():

    print("Press 1 for generating a qr code and press 2 for reading qr code.Then press Enter")
    userInput = str(input("> "))

    reader = cv2.QRCodeDetector()

    if (userInput == "1"):
        print("Enter the link:-")
        userLink = input("> ")
        result = qrcode.make(userLink)
        result.save(userLink + ".jpg")
        wholefunc()

    elif (userInput == "2"):
        print("Enter the name of the image with extension")
        userImage = input("> ")
        val1, val2, val3 = reader.detectAndDecode(cv2.imread(userImage))
        print(val1)
        usermade = input("> Press any key to continue")
        wholefunc()

    else:
        wholefunc()

wholefunc()