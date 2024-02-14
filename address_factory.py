from bit import Key
from bitcoinutils.setup import setup
from bitcoinutils.keys import PrivateKey
import random
from bitcoinaddress import Wallet
from mnemonic import Mnemonic
from hdwallet.utils import is_mnemonic
from hdwallet import *
import hashlib
import base58
import binascii
import secrets
import os
import time
import codecs
import string
import sys
from art import *

class Address(object):
    address: list = list()
    def getAdrs(self):
        return self.address


class Lib1(Address):

    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.get_addr()
        self.get_addr1()
        
    def get_addr1(self):
        listLength = len(self.address)
        for t in range(listLength):
            text = self.address[t][0]
            hex_ =hashlib.sha256(codecs.encode(text)).hexdigest()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                    [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])

    def get_addr(self):
        key = Key()
        i = HDWallet().from_private_key(key.to_hex())
        self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
        self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])


class Lib2(Address):
    MAX = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    MAINNET = 'mainnet'

    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        setup(self.MAINNET)
        self.get_addr1()
        self.get_addr2()
        self.get_addr3()
        self.get_addr4()
        self.get_addr5()
        
        
    def get_addr3(self):
        try:
            priv = binascii.b2a_hex(os.urandom(32))
            i = HDWallet().from_private_key(priv)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                    [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()]) 
        except:
            return
        
         
    def get_addr4(self):
        try:
            priv = ''.join(random.choices(string.hexdigits, k=64)) 
            i = HDWallet().from_private_key(priv)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                    [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()]) 
        except:
            return
        
    def get_addr5(self):
        try:
            listLength = len(self.address)
            for t in range(listLength):
                text = self.address[t][0]
                hex_ =hashlib.sha256(codecs.encode(text)).hexdigest()
                i = HDWallet().from_private_key(hex_)
                self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
                self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
                self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
                self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
                self.address.append(
                        [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return

    def get_addr2(self):
        
        try:
        

            priv = PrivateKey()
            i = HDWallet().from_private_key(priv.key.to_string().hex())
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                    [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return

    def get_addr1(self):
        try:
            x = random.randrange(
                1, self.MAX)
            priv = PrivateKey(secret_exponent=x)
            i = HDWallet().from_private_key(priv.key.to_string().hex())
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                    [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except:
            return


class Lib3(Address):
    MAINNET = "mainnet"
    PUBADDR1 = "pubaddr1"
    PUBADDR1C = "pubaddr1c"
    PUBADDR3 = "pubaddr3"
    PUBADDRBC1_P2WPKH = "pubaddrbc1_P2WPKH"
    PUBADDRBC1_P2WSH = "pubaddrbc1_P2WSH"
    WIF = "wif"
    HEX = "hex"

    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.get_addr()
        self.get_addr1()
        
    def get_addr1(self):
        listLength = len(self.address)
        for t in range(listLength):
            text = self.address[t][0]
            hex_ =hashlib.sha256(codecs.encode(text)).hexdigest()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                    [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])

    def get_addr(self):
        wallet = Wallet()
        wif = wallet.key.__dict__[self.MAINNET].__dict__[self.WIF]
        hex_ = wallet.key.__dict__[self.HEX]
        adr1 = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR1]
        self.address.append([adr1, wif, hex_])
        adr2 = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR1C]
        self.address.append([adr2, wif, hex_])
        adr3 = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR3]
        self.address.append([adr3, wif, hex_])
        adr4 = wallet.address.__dict__[
            self.MAINNET].__dict__[self.PUBADDRBC1_P2WSH]
        self.address.append([adr4, wif, hex_])
        adr5 = wallet.address.__dict__[
            self.MAINNET].__dict__[self.PUBADDRBC1_P2WPKH]
        self.address.append([adr5, wif, hex_])


class Lib4(Address):
    CHINESE_TRAD = "chinese_traditional"
    ENGLISH = 'english'
    JAPANESE = 'japanese'
    KOREAN = 'korean'

    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.get_addr1()
        self.get_addr2()
        self.get_addr3()
        self.get_addr4()
        self.get_addr5()
        self.get_addr6()
        self.get_addr7()
        self.get_addr8()
        self.get_addr9()
        self.get_addr10()
        self.get_addr11()
        self.get_addr12()
        self.get_addr13()
        
    def get_addr13(self):
        listLength = len(self.address)
        for t in range(listLength):
            text = self.address[t][0]
            hex_ =hashlib.sha256(codecs.encode(text)).hexdigest()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                    [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        
    def get_addr11(self):
        try:
            i: HDWallet = HDWallet()
            wo = Mnemonic(self.KOREAN).generate()
            i.from_mnemonic(wo)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return

    def get_addr10(self):
        try:
            i: HDWallet = HDWallet()
            wo = Mnemonic(self.KOREAN).generate(strength=128)
            i.from_mnemonic(wo)
            self.address.append(
                [i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return

    def get_addr12(self):
        try:
            i: HDWallet = HDWallet()
            wo = Mnemonic(self.KOREAN).generate(strength=256)
            i.from_mnemonic(wo)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return
        
    def get_addr9(self):
        try:
            i: HDWallet = HDWallet()
            wo = Mnemonic(self.JAPANESE).generate()
            i.from_mnemonic(wo)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return

    def get_addr8(self):
        try:
            i: HDWallet = HDWallet()
            wo = Mnemonic(self.JAPANESE).generate(strength=128)
            i.from_mnemonic(wo)
            self.address.append(
                [i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return

    def get_addr7(self):
        try:
            i: HDWallet = HDWallet()
            wo = Mnemonic(self.JAPANESE).generate(strength=256)
            i.from_mnemonic(wo)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return
    def get_addr4(self):
        try:
            i: HDWallet = HDWallet()
            wo = Mnemonic(self.CHINESE_TRAD).generate()
            i.from_mnemonic(wo)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return

    def get_addr5(self):
        try:
            i: HDWallet = HDWallet()
            
            wo = Mnemonic(self.CHINESE_TRAD).generate(strength=128)
            i.from_mnemonic(wo)
            self.address.append(
                [i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return

    def get_addr6(self):
        try:
            i: HDWallet = HDWallet()
            wo = Mnemonic(self.CHINESE_TRAD).generate(strength=256)
            i.from_mnemonic(wo)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return


    def get_addr1(self):
        try:
            i: HDWallet = HDWallet()
            wo = Mnemonic(self.ENGLISH).generate()
            i.from_mnemonic(wo)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return

    def get_addr2(self):
        try:
            i: HDWallet = HDWallet()
            wo = Mnemonic(self.ENGLISH).generate(strength=128)
            i.from_mnemonic(wo)
            self.address.append(
                [i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return

    def get_addr3(self):
        try:
            i: HDWallet = HDWallet()
            wo = Mnemonic(self.ENGLISH).generate(strength=256)
            i.from_mnemonic(wo)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return


class Lib5(Address):
    HEX = 'hex'
    X0 = '0x'
    B0 = '0b'
    MAINNET = 'mainnet'

    def __init__(self) -> None:
        super().__init__()

        self.address.clear()
        setup(self.MAINNET)
        
        self.get_adr1()
        self.get_adr2()
        self.get_adr3()
        self.get_adr4()
        self.get_adr5()
        self.get_adr6()
        
        self.get_adr7()
        self.get_adr8()
        self.get_adr9()

    def get_adr9(self):
        try:
        
            listLength = len(self.address)
            for t in range(listLength):
                text = self.address[t][0]
                hex_ =hashlib.sha256(codecs.encode(text)).hexdigest()
                i = HDWallet().from_private_key(hex_)
                self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
                self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
                self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
                self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
                self.address.append(
                        [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except Exception as ex:
            return
    
    def get_adr8(self):
        try:
            hex_ = self.gen_hash8()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return
        
    def gen_hash8(self):
        try:
            
            xi = ''.join(random.choices(string.ascii_uppercase + string.ascii_letters + string.ascii_lowercase+
                             string.digits + string.whitespace + string.punctuation + string.hexdigits + string.octdigits, k=random.randint(1,999999)))
            text = xi 
            bb =hashlib.sha256(codecs.encode(text)).hexdigest()
            return bb
        except BaseException as ex:
            return        
    def get_adr7(self):
        try:
            hex_ = self.gen_hash7()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return
        
    def gen_hash7(self):
        try:
            
            xi = ''.join(random.choices(string.ascii_uppercase + string.ascii_letters + string.ascii_lowercase+
                             string.digits + string.whitespace + string.punctuation + string.hexdigits + string.octdigits, k=random.randint(1,999999)))
            yj = ''.join(random.choices(string.ascii_lowercase + string.ascii_letters + string.ascii_uppercase+
                             string.digits + string.whitespace + string.punctuation+ string.hexdigits + string.octdigits, k=random.randint(1,999999)))
            text = xi + yj
            bb =hashlib.sha256(codecs.encode(text)).hexdigest()
            return bb
        except BaseException as ex:
            return    
        
    def get_adr6(self):
        try:
            hex_ = self.gen_hash6()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return
        
    def gen_hash6(self):
        try:
            
            xi = ''.join(random.choices(string.ascii_uppercase + string.ascii_letters + string.ascii_lowercase+
                             string.digits + string.whitespace + string.punctuation + string.hexdigits + string.octdigits, k=random.randint(1,999999)))
            yj = ''.join(random.choices(string.ascii_lowercase + string.ascii_letters + string.ascii_uppercase+
                             string.digits + string.whitespace + string.punctuation+ string.hexdigits + string.octdigits, k=random.randint(1,999999)))
            yz = ''.join(random.choices(string.ascii_lowercase + string.ascii_letters + string.ascii_uppercase+
                             string.digits + string.whitespace + string.punctuation+ string.hexdigits + string.octdigits, k=random.randint(1,999999)))
            text = xi + yj + yz
            bb =hashlib.sha256(codecs.encode(text)).hexdigest()
            return bb
        except BaseException as ex:
            return
        


        
        
    def get_adr5(self):
        try:
            str_ = random.getrandbits(256)
            hex_ = hex(str_).replace(self.X0, "")
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return
        
        
    def gen_hex(self):
        str_ = ""
        for i in range(256):
            str_ += str(random.getrandbits(1))
        bb = int(str_, 2)
        bb = hex(bb).replace(self.X0, "")
        return bb

    def get_adr4(self):
        try:
            hex_ = os.urandom(32).hex()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return


    def get_adr3(self):
        try:
            hex_ = secrets.token_hex(32)
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return

    def get_adr2(self):
        try:
            hex_ = ''.join([secrets.choice(string.hexdigits) for x in range(64)])
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
            

        except BaseException as ex:
            return

    def get_adr1(self):
        try:

            hex_ = self.gen_hex()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except Exception as ex:
            return




#https://github.com/Destiner/blocksmith
class Lib6(Address):
    def __init__(self):
        super().__init__()
        self.address.clear()
        self.POOL_SIZE = 256
        self.KEY_BYTES = 32
        self.CURVE_ORDER = int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141', 16)
        self.pool = [0] * self.POOL_SIZE
        self.pool_pointer = 0
        self.prng_state = None
        self.__init_pool()
        self.get_adr()
        self.get_adr1()

    def get_adr1(self):
        listLength = len(self.address)
        for t in range(listLength):
            text = self.address[t][0]
            hex_ =hashlib.sha256(codecs.encode(text)).hexdigest()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                    [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        
    def get_adr(self):
       key = self.generate_key()
       i = HDWallet().from_private_key(key)
       self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
       self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
       self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
       self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
       self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        
    def seed_input(self, str_input):
        time_int = int(time.time())
        self.__seed_int(time_int)
        for char in str_input:
            char_code = ord(char)
            self.__seed_byte(char_code)
            
    def generate_key(self):
        big_int = self.__generate_big_int()
        big_int = big_int % (self.CURVE_ORDER - 1) # key < curve order
        big_int = big_int + 1 # key > 0
        key = hex(big_int)[2:]
        # Add leading zeros if the hex key is smaller than 64 chars
        key = key.zfill(self.KEY_BYTES * 2)
        return key

    def __init_pool(self):
        for i in range(self.POOL_SIZE):
            random_byte = secrets.randbits(8)
            self.__seed_byte(random_byte)
        time_int = int(time.time())
        self.__seed_int(time_int)

    def __seed_int(self, n):
        self.__seed_byte(n)
        self.__seed_byte(n >> 8)
        self.__seed_byte(n >> 16)
        self.__seed_byte(n >> 24)

    def __seed_byte(self, n):
        self.pool[self.pool_pointer] ^= n & 255
        self.pool_pointer += 1
        if self.pool_pointer >= self.POOL_SIZE:
            self.pool_pointer = 0
    
    def __generate_big_int(self):
        if self.prng_state is None:
            seed = int.from_bytes(self.pool, byteorder='big', signed=False)
            random.seed(seed)
            self.prng_state = random.getstate()
        random.setstate(self.prng_state)
        big_int = random.getrandbits(self.KEY_BYTES * 8)
        self.prng_state = random.getstate()
        return big_int
 
class Lib7(Address):
    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.get_adr1()
        self.get_adr2()
        self.get_adr3()
    
    def get_adr1(self):
        try:
            hex_ = self.gen_hash1()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return
           
    def gen_hash1(self):
        try:
            t = art("rand",number=random.randint(1,999999))
            bb =hashlib.sha256(codecs.encode(t)).hexdigest()
            return bb
        except BaseException as ex:
            return  
        
    def get_adr2(self):
        try:
            hex_ = self.gen_hash2()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return
           
    def gen_hash2(self):
        try:
            t = art("random",number=random.randint(1,99999))
            bb =hashlib.sha256(codecs.encode(t)).hexdigest()
            return bb
        except BaseException as ex:
            return
        
    def get_adr3(self):
        try:
            hex_ = self.gen_hash2()
            i = HDWallet().from_private_key(hex_)
            self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
            self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
            self.address.append(
                [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        except BaseException as ex:
            return
           
    def gen_hash3(self):
        try:
            t = randart()
            bb =hashlib.sha256(codecs.encode(t)).hexdigest()
            return bb
        except BaseException as ex:
            return
      
      
class AddressFact():
    def instance(self, typ):
        targetclass = typ
        return globals()[targetclass]()
