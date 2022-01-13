import string
alphabet= list(string.ascii_lowercase)
quit=False
while quit== False:
    message=input("Enter the message\n").lower()
    direction= input("Choose an action \"encode\" or \"decode\" \n").lower()
    print(direction)
    shift= int(input("Enter shift number\n"))



    def encrypt(message, shift, alphabet,):
        mes=list(message)
        for i in range(len(mes)):
            letter = alphabet.index(mes[i])
            val=letter+shift
            if val>25:
                val-=25

            mes[i]= alphabet[val]

        print(f"{' '.join(mes)}")


    def decrypt(message, shift, alphabet, ):
        mes = list(message)
        for i in range(len(mes)):
            letter = alphabet.index(mes[i])
            val = letter - shift
            if val < 0:
                val += 26

            mes[i] = alphabet[val]

        print(f"{''.join(mes)}")


    if(direction=="encode"):
        encrypt(message, shift, alphabet)
    elif (direction == "decode"):
        decrypt(message, shift, alphabet)
    else:
        print("Invalid Input\n")

    response = input("Do you want to quit? \"YES\" or \"NO\" \n").lower()
    if response=="yes":
        quit=True
