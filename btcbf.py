from typing import Any, Callable, Iterable, Mapping
import requests
from time import sleep
import address_factory
from multiprocessing.pool import ThreadPool
from multiprocessing import Process
import threading
import sys
import os
from fp.fp import FreeProxy
import random


class StaticMethods():
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_some_proxies():
        proxy: list = list()
        for i in range(0, 2):
            try:
                proxy_server = FreeProxy(rand=True).get()
                proxy.append(str(proxy_server))
            except BaseException:
                continue
        return proxy

    @staticmethod
    def connect(address):
        try:
            c = requests.get(
                "https://blockchain.info/q/getreceivedbyaddress/"+str(address))
            return int(c.text)
        except BaseException as bx:
            return -1

    @staticmethod
    def connect(address, proxies: list):
        try:
            p_ = {}
            if len(proxies) > 0:
                p_ = {1: proxies[random.randrange(len(proxies))]}
            result_ = requests.get(
                "https://blockchain.info/q/getreceivedbyaddress/"+str(address), proxies=p_)
            return int(result_.text)
        except BaseException:
            return -1

    @staticmethod
    def prnt_scr(txt):
        # os.system("cls")
        print(txt)


class Proxy_thread(threading.Thread):
    def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.data: list

    @property
    def PROXY_LIST(self):
        return self.data

    def update_proxies(self):
        p_ = StaticMethods().get_some_proxies()
        self.data = p_

    def run(self):
        self.update_proxies()


class Brute():
    def __init__(self) -> None:
        self.proxies = list()
        pass

    def connect(self, address):
        return StaticMethods().connect(address)

    def connect(self, address, proxies):
        return StaticMethods().connect(address, proxies)

    def get_adr_list(selsf):
        aa = list()
        bb = address_factory.AddressFact()
        cc = ["Lib1", "Lib2", "Lib3", "Lib4", "Lib5"]
        for dd in cc:
            ee = bb.createAdress(dd).getAdrs()
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
            str_ = "searching for: "+str(wallet[0])+" "+str(result)
            StaticMethods().prnt_scr(str_)
        except BaseException as ex:
            return

    def thread_func(self, wallet: list, proxies: list):
        try:

            result = self.connect(wallet[0], proxies)
            if result > 0:
                str_ = "found: "+str(wallet[0])
                StaticMethods().prnt_scr(str_)
                self.append_to_file(wallet)
            str_ = "Searching for: "+str(wallet[0])+" "+str(result)
            StaticMethods().prnt_scr(str_)
        except BaseException as ex:
            return

    def rand_brute(self, use_proxy=False):
        ll = list()
        BRUTE = True
        if use_proxy:
            proxies = StaticMethods().get_some_proxies()
            while BRUTE:
                try:
                    ll = self.get_adr_list()
                    st = Proxy_thread()
                    st.start()
                    for index in range(0, len(ll)):
                        threading.Thread(target=self.thread_func, args=(
                            ll[index], proxies,)).start()
                        sleep(index)
                    st.join()
                    for i in st.PROXY_LIST:
                        if i not in proxies:
                            proxies.append(i)

                except BaseException as ex:
                    raise ex
        elif not use_proxy:
            while BRUTE:
                try:
                    ll = self.get_adr_list()
                    for index in range(0, len(ll)):
                        threading.Thread(target=self.thread_func,
                                         args=(ll[index],)).start()
                        sleep(index)
                except BaseException as ex:
                    raise ex


class Run():
    def __init__(self):

        self.p_: ThreadPool

    def stop_worker(self):
        try:
            self.p_.close()
            self.p_.terminate()
            self.p_.join()
        except BaseException as ex:
            pass
        sleep(1)

    def worker_function(self):
        try:
            Brute().rand_brute(use_proxy=True)
        except BaseException as ex:
            self.stop_worker()

    def start_worker(self):
        try:
            self.p_.apply_async(func=self.worker_function)
            while (True):
                try:
                    continue
                except BaseException as kex:
                    break
            self.stop_worker()
        except BaseException as ex:
            self.stop_worker()
            return

    def run(self):
        self.p_ = ThreadPool(200)
        self.start_worker()


if __name__ == "__main__":
    print("Welcome.")
    try:

        d: Run = Run()
        d.run()
    except BaseException as e:
        sys.exit()
