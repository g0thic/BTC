import requests
from time import sleep
import address_factory
from multiprocessing.pool import ThreadPool
from multiprocessing import Process
import threading
import sys
import os
from fp.fp import FreeProxy



class StaticMethods():
    def __init__(self) -> None:
        pass
    @staticmethod
    def get_some_proxies():
        proxy_dict :dict = dict()
        for i in range(0,10):
            proxy_server = FreeProxy(rand=True).get()
            proxy_dict.__setitem__(str(i),str(proxy_server))
        return proxy_dict
        
        
    @staticmethod
    def connect(address):
        try:
            #proxy_dic = StaticClass().fill_proxy_dic()
            #StaticClass().fill_proxy_dic()
            c = requests.get("https://blockchain.info/q/getreceivedbyaddress/"+str(address))
            return int(c.text)
        except BaseException as bx:
            
            return -1
    @staticmethod
    def connect_proxy(address,proxies):
        try:
            #proxy_dic = StaticClass().fill_proxy_dic()
            #StaticClass().fill_proxy_dic()
            c = requests.get("https://blockchain.info/q/getreceivedbyaddress/"+str(address),proxies=proxies)
            return int(c.text)
        except BaseException as bx:
            
            return -1
          
    @staticmethod
    def prnt_scr(txt):
        #os.system("cls")
        print(txt)
    

    
class Brute():
    def __init__(self) -> None:
        pass 
    
    
    def connect(self,address):
            return StaticMethods().connect(address)
        
    def connect_proxy(self,address,proxies):
        return StaticMethods().connect_proxy(address,proxies) 
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
            sleep(1)
            result = self.connect(wallet[0])
            if result > 0:
                str_ = "found: "+str(wallet[0])
                StaticMethods().prnt_scr(str_)
                self.append_to_file(wallet)
            str_ = "searching for: "+str(wallet[0])+" "+str(result)
            StaticMethods().prnt_scr(str_)
        except BaseException as ex:
            self.exec = True
    
    def thread_func_proxy(self,wallet:list,proxies:dict):
        try:
            sleep(1)
            result = self.connect_proxy(wallet[0],proxies)
            if result > 0:
                str_ = "found: "+str(wallet[0])
                StaticMethods().prnt_scr(str_)
                self.append_to_file(wallet)
            str_ = "searching for: "+str(wallet[0])+" "+str(result)
            StaticMethods().prnt_scr(str_)
        except BaseException as ex:
            self.exec = True
        
            
               
    
    exec = False
              
    def rand_brute(self,use_proxy=False):
        ll = list()
        BRUTE = True
        if use_proxy: 
            proxies = StaticMethods().get_some_proxies()
            while BRUTE:
                try:
                    ll = self.fill_add_list()
                    for index in range(0,len(ll)):
                        threading.Thread(target=self.thread_func_proxy,args=(ll[index],proxies,)).start()
                        sleep(1)
                except BaseException as ex:
                    raise ex
        elif not use_proxy:
            while BRUTE:
                try:
                    ll = self.fill_add_list()
                    for index in range(0,len(ll)):
                        threading.Thread(target=self.thread_func,args=(ll[index],)).start()
                        sleep(1)
                except BaseException as ex:
                    raise ex
                   
        
class Run():
    def __init__(self):
        
        self.p_:ThreadPool
        self.t1:ThreadPool
        
    
    def init_worker(self, pn:int=1):
        self.p_= ThreadPool(processes=pn)
        self.t1 = ThreadPool()
        
    def stop_worker(self):
        try:
            self.t1.terminate()
        except BaseException as ex:
            pass
        try:
            self.p_.close()
        except BaseException as ex:
            pass
        sleep(1)
        print("Closing")
    
    def worker_function(self):
        try:
            Brute().rand_brute(True)
        except BaseException as ex:
            self.stop_worker()
            
            
    def KeyBoardThread(self):
        while True:
            try:
                continue
            except KeyboardInterrupt as kex:
                break
            except BaseException as kex:
                break
            
    def start_worker(self):
        try:
            
            self.p_.apply_async(func=self.worker_function)
            self.t1.apply(self.KeyBoardThread)
            self.stop_worker()
        except BaseException as ex:
            self.stop_worker()
            
    def run(self):
        self.init_worker(100)
        sleep(1)
        self.start_worker()

if __name__ == "__main__":
    print("Welcome.")
    try:
        
        d:Run = Run()
        d.run()
    except BaseException as e:
        sys.exit()
    


            
