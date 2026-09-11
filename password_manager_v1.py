import time

Password = input("Please enter your password: ")
if Password == "Miraculous123":
    time.sleep(4)
    print("Access Granted!")
elif Password == "Lyoko123":
    time.sleep(4)
    print("Old Password Can't be used")
else:
    time.sleep(4)
    print("Access Denied!")
