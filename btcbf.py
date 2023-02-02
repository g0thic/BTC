import requests
from time import sleep
import os
import address_factory
from multiprocessing.pool import ThreadPool

class Run():
 
    def connect(self,address):
        try:
            return requests.get("https://blockchain.info/q/getreceivedbyaddress/"+address+"/").text
        except BaseException as e:
            raise Exception("con error")
        
    def fill_add_list(self):
        lt = list()
        s_ = address_factory.AddressFact()
        ss = ["Lib1","Lib2","Lib3","Lib4"]
        for sss in ss:
            x=s_.createAdress(sss).getAdrs()
            for item in x:
                lt.append(item)
        return lt

    def apped_to_file(self,ll,index):
        with open("foundkey.txt","a") as f:
            f.write(str(ll[index][0])+" "+str(ll[index][1])+" "+str(ll[index][2]))
            print(ll[index])
            f.write("\n")  
    def print_scr(self,ll:list,index:int):
        _ = os.system('cls')
        print("searching for : ", ll[index][0],end="\r")
    
    def rand_brute(self):
        ll = list()
        the_page = 0
        try:
            while True:
                ll.clear()
                ll = self.fill_add_list()
                for index in range(len(ll)):
                    the_page =0
                    self.print_scr(ll,index)
                    the_page = int(self.connect(ll[index][0]))
                    if the_page >0:
                        print("found address .. saving to file")
                        self.apped_to_file(ll,index)              
        except BaseException as ex:
            raise ex
    p:ThreadPool
    is_Active = False
    def init_worker(self, pn:int=2):
        self.p = ThreadPool(processes=pn)
        
    def start_worker(self):
        self.p.apply_async(self.rand_brute)
        
    def run(self):
        self.init_worker(100)
        is_Active = True
        self.start_worker()
        while is_Active:
            try:
                continue
            except KeyboardInterrupt:
                if self.p.is_Active:
                    self.p.close()
                is_Active = False
                sleep(1)
                print("Closing please wait.")
                return
            except BaseException:
                if self.p.is_Active:
                    self.p.close()
                is_Active = False
                sleep(1)
                return
        
        
    
if __name__ == "__main__":
    print("Welcome.")
    try:
        d:Run = Run()
        d.run()
    except BaseException as e:
        exit()
    


            
