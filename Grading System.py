import time

Grade = 100
Grade = int(input("Please enter your current grade: "))
if Grade == 100:
    print("calculating..Please wait...")
    time.sleep(5)
    print("Your current grade is A+")
elif Grade >= 80:
    print("calculating..Please wait...")
    time.sleep(5)
    print("Your current grade is A")
elif Grade >= 65:
    print("calculating..Please wait...")
    time.sleep(5)
    print("Your current grade is C+")
else:
    print("calculating..Please wait...")
    time.sleep(5)
    print("Your current grade is F")
