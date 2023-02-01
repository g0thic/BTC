import requests
from time import sleep
import os
import address_factory
from multiprocessing.pool import ThreadPool

 
def connect(address):
    try:
        return requests.get("https://blockchain.info/q/getreceivedbyaddress/"+address+"/").text
    except:
        raise Exception("con error")
    
def fillAddList():
    l = list()
    s = address_factory.AddressFact()
    ss = ["Lib1","Lib2","Lib3","Lib4"]
    for sss in ss:
        x=s.createAdress(sss).getAdrs()
        for item in x:
            l.append(item)
    
    return l

def apped_to_file(ll,index):
    with open("foundkey.txt","a") as f:
        f.write(str(ll[index][0])+" "+str(ll[index][1])+" "+str(ll[index][2]))
        print(ll[index])
        f.write("\n")  

def rand_brute():
    ll = list()
    the_page = 0
    try:
        while True:
            ll.clear()
            ll = fillAddList()
            for index in range(len(ll)):
                the_page =0
                _ = os.system('cls')
                print("searching for : ", ll[index][0],end="\r")
                the_page = int(connect(ll[index][0]))
                if the_page >0:
                    print("found address .. saving to file")
                    apped_to_file(ll,index)              
    except BaseException as e:
        raise e

def run():
    print()
    p: ThreadPool = ThreadPool(processes=100)
    is_Active = True
    p.apply_async(rand_brute)
    while is_Active:
        try:
            continue
        except KeyboardInterrupt:
            p.close()
            is_Active = False
            sleep(1)
            print("Closing please wait.")
    
if __name__ == "__main__":
    try:
        print("Welcome.")
        run()
    except BaseException as e:
        exit()


            