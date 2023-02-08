import requests
from time import sleep
import address_factory
from multiprocessing.pool import ThreadPool
import threading
import sys
import os

@staticmethod
def connect(address):
    try:
        c = requests.get("https://blockchain.info/q/getreceivedbyaddress/"+str(address))
        return int(c.text)
    except BaseException as bx:
        return -1
    
@staticmethod
def prnt_scr(txt):
    os.system("cls")
    print(txt)
    

    
class Brute():
    def __init__(self) -> None:
        self.the_page : int=0  
        self.ERROR : bool = False 
        self.exec : Exception
        
    def connect(self,address):
            return connect(address)
        
    def fill_add_list(selsf):
        aa = list()
        bb = address_factory.AddressFact()
        cc = ["Lib1","Lib2","Lib3","Lib4"]
        for dd in cc:
            ee=bb.createAdress(dd).getAdrs()
            for item in ee:
                aa.append(item)
        return aa
    
    def append_to_file(self,wallet:list):
        fn = "key.txt"
        op = "a"
        with open(fn,op) as f:
            f.write(str(wallet[0])+" "+str(wallet[1])+" "+str(wallet[2]))
            f.write("\n")  
            
            
    def thread_func(self,wallet:list,):
        try:
            str_ = "searching for: "+str(wallet[0])
            t1 = threading.Thread(target=prnt_scr,args=(str_,))
            t1.start()
            result = self.connect(wallet[0])
            if result > 0:
                self.append_to_file(wallet)
        except BaseException as ex:
            self.exec = ex
            self.ERROR = True
            
               
    
    
    def rand_brute(self):
        ll = list()
        self.the_page = 0
        BRUTE = True
        try:
            while BRUTE and (not self.ERROR):
                if self.ERROR:
                    break
                ll = self.fill_add_list()
                for index in range(0,len(ll)):
                    sleep(0.1)
                    t_ = threading.Thread(target=self.thread_func,args=(ll[index],))
                    t_.start()
                    if self.ERROR: 
                        t_.join()
                        sleep(20)
                        break
        except BaseException as ex:
            self.ERROR =True
            self.exec = ex
            
        
class Run():
    def __init__(self) -> None:
        self.p_:ThreadPool
    
    def init_worker(self, pn:int=2):
        self.p_= ThreadPool(processes=pn)
    def stop_worker(self):
        self.p_.close()
        
    def worker_function(self):
        Brute().rand_brute()
        
    def start_worker(self):
            self.p_.apply(self.worker_function)
            
    def run(self):
            self.init_worker()
            self.start_worker()

if __name__ == "__main__":
    print("Welcome.")
    try:
        d:Run = Run()
        d.run()
    except BaseException as e:
        print(e)
        sys.exit()
    


            
