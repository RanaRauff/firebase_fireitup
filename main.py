import os
from firebase import firebase
from scrap import ScrapComp
import schedule
import time

fb = firebase.FirebaseApplication('https://fireitup-1c90a.firebaseio.com/',None)


# ===================================================================================
DataBase_R = os.getenv("DataBase_R")
DataBase_B = os.getenv("DataBase_B")
# ===================================================================================


def task():
    
    realtime_data = ScrapComp().get_data()
    # print(realtime_data)
    # fb.delete('/mytestdata/','1')
    res = fb.patch('/rr', realtime_data)
    print("database updated", res)


while True:
    print("started running .....")
    # schedule.run_pending()
    # task()
    print(DataBase_B, DataBase_R)
    print("waiting for 60 second(s) .....")
    time.sleep(60)
    # task()
    # break
