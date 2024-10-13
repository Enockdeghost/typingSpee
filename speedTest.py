#import from python library
from time import *
import random as e

#fuction for detect error/istales
def mistake(partest,usertest):
    error = 0
    #some motivation
    if error >= 20:
        print('====you can do this====')
    elif error <20:
        print('===here we go===')
    else:
        print('====continue practise====')
    
    #loop for len partest(paragraph)
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1    
        except :
            error = error + 1
    return error   

#fuction for speed time..s==startTime, e==endTime
def speed_time(time_s,time_e,user_input):
    time_delay = time_e - time_s
    time_r = round(time_delay,1) 
    speed = len(user_input) / time_r
    return round(speed)

# loop for ask user want to play or not
while True:
    again = input("ready to test (yes/no): ")
    if again == 'yes':
        # list contain our words
        test = ["my name is enock but every body call me ino",
                "i study at jriit at sakina",
                "im studying IT"]
        
        test1 = e.choice(test)
         # typing heading
        print('----typing speed----\n')
        print(f'{test1}\n')

        time1 = time()
        # receive from user
        testinput = input("enter: ")
        time2 = time()
        print("speed:  ", speed_time(time1,time2,testinput,),'second')
        print('error! ',mistake(test1,testinput  ))
    elif again == 'no':
        print('its okay')
        break
    else:
        print('wrong input')