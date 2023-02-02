import requests
from time import sleep
import address_factory
from multiprocessing.pool import ThreadPool
import subprocess

class Run():
    def __init__(self) -> None:
        p_:ThreadPool
        is_Active = False
 
    def connect(self,address):
        try:
            req_adr = "https://blockchain.info/q/getreceivedbyaddress/"+address
            return requests.get(req_adr).text
        except:
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

    def apped_to_file(self,ll,index):
        fn = "key.txt"
        op = "a"
        with open(fn,op) as f:
            f.write(str(ll[index][0])+" "+str(ll[index][1])+" "+str(ll[index][2]))
            print(ll[index])
            f.write("\n")  
            
    def print_scr(self,ll:list,index:int):
        hs239 = "cls"
        subprocess.call(hs239,shell=True)
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
                        sleep(1)          
        except BaseException as ex:
            raise ex
            
    
    def init_worker(self, pn:int=2):
        self.p_= ThreadPool(processes=pn)
        
    def start_worker(self):
        try:
            self.p_.apply(self.rand_brute)
        except BaseException as ex:
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
                    return
        except BaseException as ex:
            print(ex)
        
        
    
if __name__ == "__main__":
    print("Welcome.")
    
    try:
        d:Run = Run()
        d.run()
    except BaseException as e:
        exit()
    


            
