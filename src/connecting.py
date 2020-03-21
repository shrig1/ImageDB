import bcrypt as bc

username = b"theLordAndSavior"
password = b"MyNameJeff69420"
encrypted_message = bc.hashpw(message, bc.gensalt())
print(encrypted_message)
if(bc.checkpw(message, encrypted_message)):
    print("Yay")
else:
    print("Dang it")
