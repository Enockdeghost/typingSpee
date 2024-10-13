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
                "im studying IT","Tanzania is known for the archeological dig site of Olduvai Gorge, home to some of the oldest evidence of human ancestry in the world.",
                "Tanzania is famous for its ugali. Commonly known as the national dish, ugali is one of the most widely consumed dishes throughout the country and is either served as the main component or a complement to many meals",
                "Tanzania is estimated to be home to more than 100 different tribes, giving it incredible ethnic diversity. Yet, one tribe, in particular, is most well-known inside and outside of Tanzania. That would be the Maasai."]
        
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