import time
Age = int(input("Enter your age:"))
if Age >= 18:
    print("Checking if you meet the requirements...")
    time.sleep(5)
    print("You meet the requirements to drive a car!")
else:
    print("Checking if you meet the requirements")
    time.sleep(5)
    print("Im sorry, you are not allowed to drive a car!")
