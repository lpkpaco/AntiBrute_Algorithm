import time
import random
global pw
pw =  random.randint(1000,9999)
global count
count = 0
count2 = 0
global resold
resold = 0
global resnew
resnew= 0
def algorithm():
    global count
    global count2
    if count2 == 1:
        global diff2
        global diff1
        diff2 = diff1
        diff1 = resnew - resold
        if diff1 == diff2:
            print("Our algorithm detected that you are bruting our system. Starting lockdown protection...")
            time.sleep(0.5)
            print("Password panel disabled.")
            exit()
        else:
            pass
    if count == 1:
        diff1 = resnew - resold
        if count2 == 0:
            count2 += 1
    else:
        count += 1
while True:
    if count == 1:
        resold = resnew
    resnew =  input("Password: ")
    try:
        resnew = int(resnew)
    except:
        print("Error")
        exit()
    algorithm()
    if resnew == pw:
        print("ok")
        exit()