import requests
from time import sleep
import address_factory
from multiprocessing.pool import ThreadPool
import threading
import os



class Run():
    def __init__(self) -> None:
        self.p_:ThreadPool
        self.is_Active = False
        self.b_ :Brute = Brute()
 
    
    def init_worker(self, pn:int=2):
        
        self.p_= ThreadPool(processes=pn)
    def stop_worker(self):
        self.p_.close()
    def start_worker(self):
        try:
            self.is_Active = True
            self.p_.apply(self.b_.rand_brute)
        except BaseException as ex:
            self.stop_worker()
            raise(ex)
        
    def run(self):
        try:
            self.init_worker(1000)
            self.start_worker()
            is_Active = True
            while is_Active:
                try:
                    continue
                except KeyboardInterrupt:
                    if self.p_.is_Active:
                        self.p_.close()
                    is_Active = False
                    sleep(1)
                    print("Closing please wait.")
                    return
                except BaseException:
                    if self.p.is_Active:
                        self.p.close()
                    is_Active = False
                    sleep(1)
        except BaseException as ex:
            self.stop_worker()
            raise(ex)  


class Brute():
    def __init__(self) -> None:
        self.the_page : int=0   
    def connect(self,address):
        try:
            #req_adr = "https://blockchain.info/q/getreceivedbyaddress/"+str(address)
            p = int(requests.get("https://blockchain.info/q/getreceivedbyaddress/"+str(address)).text)
            return p
        except BaseException as ex:
            raise Exception("con error")
        
    def fill_add_list(self):
        l_ = list()
        s_ = address_factory.AddressFact()
        l1 = "Lib1"
        l2 = "Lib2"
        l3 = "Lib3"
        l4 = "Lib3"
        ss = [l1,l2,l3,l4]
        for sss in ss:
            x=s_.createAdress(sss).getAdrs()
            for item in x:
                l_.append(item)
        return l_

    def apped_to_file(self,wallet):
        fn = "key.txt"
        op = "a"
        with open(fn,op) as f:
            f.write(str(wallet[0])+" "+str(wallet[1])+" "+str(wallet[2]))
            print(wallet)
            f.write("\n")  
            
    def print_scr(self,address,):
            os.system("cls")
            print("searching for : ", address,end="\r")
            sleep(0.001)
    
    
    def thread_func(self,wallet:list,):
        try:
            threading.Thread(target=self.print_scr,args=(wallet[0],)).start()
            if self.connect(wallet[0]) > 1:
                self.apped_to_file(wallet)
        except BaseException as ex:
            raise ex
            
            
        
    def rand_brute(self):
        ll = list()
        self.the_page = 0
        BRUTE = True
        try:
            while BRUTE:
                    ll = self.fill_add_list()
                    for index in range(0,len(ll)):
                        threading.Thread(target=self.thread_func,args=(ll[index],)).start()
                        
                   
        except BaseException as ex:
            raise ex
            
       
        
    
if __name__ == "__main__":
    print("Welcome.")
    try:
        d:Run = Run()
        d.run()
    except BaseException as e:
        d.stop_worker()
        exit()
    


            
