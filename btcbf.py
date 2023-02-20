from typing import Any, Callable, Iterable, Mapping
import requests
from time import sleep
import address_factory
import multiprocessing as Multi_processing
import threading
import sys
import os
from fp.fp import FreeProxy
import random
import signal




class StaticMethods():
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_some_proxies():
        proxy: list = list()
        for i in range(2):
            try:
                proxy_server = FreeProxy(rand=True).get()
                proxy.append(str(proxy_server))
            except BaseException:
                continue
        return proxy

    @staticmethod
    def connect(address):
        try:
            url = "https://blockchain.info/q/getreceivedbyaddress/"+str(address)
            c = requests.get(url)
            return int(c.text)
        except BaseException as bx:
            return -1

    @staticmethod
    def connect_P(address, proxies: list):
        try:
            #p_=[]
            url = "https://blockchain.info/q/getreceivedbyaddress/"+str(address)
            result_ = requests.Response()
            if len(proxies) > 0:
                p_ = {1: proxies[random.randrange(len(proxies))]}
                result_ = requests.get(url, proxies=p_)
            return int(result_.text)
        except BaseException as ex:
            return -1

    @staticmethod
    def prnt_scr(txt):
        print(txt)


class Proxy_thread(threading.Thread):
    def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.data: list
        self.is_running : bool
    
    @property
    def PROXY_LIST(self):
        return self.data
    @property
    def IS_RUNNING(self):
        return self.is_running
    @IS_RUNNING.setter
    def IS_RUNNING(self,value:bool):
        self.is_running = value
    def update_proxies(self):
        
        while self.is_running:
            try:
                p_ = StaticMethods().get_some_proxies()
                if len(p_) >0:
                    for item in p_:
                        self.data.append(item)
                sleep(1)
            except BaseException as ex:
                sleep(10)
                continue

    def run(self):
        self.is_running = True
        self.data = list()
        self.update_proxies()


class Brute():
    LIB1 = "Lib1"
    LIB2 = "Lib2"
    LIB3 = "Lib3"
    LIB4 = "Lib4"
    LIB5 = "Lib5"
    LIB6 = "Lib6"
    def __init__(self) -> None:
        self.proxies = list()
        pass

    def connect(self, address):
        return StaticMethods().connect(address)

    def connect_P(self, address, proxies):
        return StaticMethods().connect_P(address, proxies)

    def get_adr_list(self):
        aa = list()
        bb = address_factory.AddressFact()
        cc = [self.LIB1, self.LIB2, self.LIB3,self.LIB4,self.LIB5]
        for dd in cc:
            try:
                ee = bb.createAdress(dd).getAdrs()
            except BaseException:
                continue
            for item in ee:
                aa.append(item)
        return aa

    def append_to_file(self, wallet: list):
        fn = "key.txt"
        op = "a"
        with open(fn, op) as f:
            f.write(str(wallet[0])+" "+str(wallet[1])+" "+str(wallet[2]))
            f.write("\n")

    def thread_func(self, wallet: list,):
        try:
            result = self.connect(wallet[0])
            if result > 0:
                str_ = "found: "+str(wallet[0])
                StaticMethods().prnt_scr(str_)
                self.append_to_file(wallet)
            elif result == 0:
                str_ = "address: "+str(wallet[0])+" result:"+str(result)
                StaticMethods().prnt_scr(str_)
            elif result == -1:
                str_ = "connection error"
                StaticMethods().prnt_scr(str_)
        except BaseException as ex:
            return

    def thread_func_P(self, wallet: list, proxies: list):
        try:
            result = self.connect_P(wallet[0], proxies)
            if result > 0:
                str_ = "found: "+str(wallet[0])
                StaticMethods().prnt_scr(str_)
                self.append_to_file(wallet)
            elif result == 0:
                str_ = "address: "+str(wallet[0])+" result: "+str(result)
                StaticMethods().prnt_scr(str_)
            elif result == -1:
                str_ = "connection error"
                StaticMethods().prnt_scr(str_)
            
        except BaseException as ex:
            return
    
    def rb_P(self):
        #proxies = StaticMethods().get_some_proxies()
        proxies = list()
        st = Proxy_thread()
        st.start()
        sleep(5)
        proxies = st.PROXY_LIST
        while(len(proxies)==0):
            try:
                proxies = st.PROXY_LIST
            except BaseException as ex:
                continue
        while True:
                try:
                    ll = self.get_adr_list()
                    t_list = list()
                    proxies = st.PROXY_LIST
                    for index in range(0, len(ll)):
                        t_ = threading.Thread(target=self.thread_func_P, args=(
                            ll[index], proxies,))
                        t_.start()
                        t_list.append(t_)
                    for item in t_list:
                        item.join()
                    sleep(len(ll)/int(random.uniform(1,len(ll))))
                    t_list.clear()
                except BaseException as ex:
                    st.IS_RUNNING = False
                    st.join()
                    raise ex
    def rb_(self):
        t_list = list()
        while True:
                try:
                    ll = self.get_adr_list()
                    
                    for index in range(0, len(ll)):
                        t_=threading.Thread(target=self.thread_func,
                                         args=(ll[index],))
                        t_.start()
                        t_list.append(t_)
                    for item in t_list:
                        item.join()
                    sleep(len(ll))
                    t_list.clear()
                except BaseException as ex:
                    raise ex
   
    def rand_brute(self, use_proxy=False):
        ll = list()
        BRUTE = True
        if use_proxy:
            try:
                self.rb_P()
                
            except BaseException as ex:
                    raise ex
        elif not use_proxy:
            try:
                self.rb_()
            except BaseException as ex:
                raise ex


class brute_manager():
    def __init__(self):
        self.ProcessList : list
        self.shared_ : Multi_processing.Manager().list

    def stop_worker(self):
        try:
            if len(self.ProcessList) > 0:
                for item in self.ProcessList:
                    try:
                        os.kill(item,signal.SIGINT)
                        #sleep(1)
                    except BaseException as eb:
                        continue
        except BaseException as ex:
            pass

    def worker_function(self,use_proxy,n,):
        try:
            Brute().rand_brute(use_proxy=use_proxy)
        except BaseException as ex:
            n[0]=False
            
    def start_worker(self,workers:int,use_proxy:bool):
        try:
            
            for index in range(workers):
                if self.shared_[0] == False:
                    break
                tt = Multi_processing.Process(target=self.worker_function,args=(use_proxy,self.shared_,))
                tt.start()
                self.ProcessList.append(tt.pid)
                sleep(workers/int(random.uniform(1,workers)))
            while (self.shared_[0]== True):
                try:
                    continue
                except BaseException as kex:
                    break
            self.shared_[0]=False
            self.stop_worker()
        except BaseException as ex:
            self.shared_[0]=False
            self.stop_worker()


    def manage(self, total_workers:int, enable_proxy:bool):
        try:
            self.ProcessList = list()
            self.shared_ =  Multi_processing.Manager().list()
            self.shared_.append(True)
            self.start_worker(workers=total_workers,use_proxy=enable_proxy)
        except BaseException as ex:
            self.stop_worker()

if __name__ == "__main__":

    StaticMethods.prnt_scr("Welcome")
    try:
        d: brute_manager = brute_manager()
        d.manage(total_workers=5,enable_proxy=True)
        StaticMethods.prnt_scr("see you")
    except BaseException as e:
        sys.exit()
