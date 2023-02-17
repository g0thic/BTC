from bit import Key
from bitcoinutils.setup import setup
from bitcoinutils.keys import PrivateKey
import random
import string
from bitcoinaddress import Wallet
from mnemonic import Mnemonic
from hdwallet.utils import is_mnemonic
from hdwallet import *
import bitcoinlib.wallets
import bitcoinlib.keys as Keys
import hashlib
import base58
import binascii



class Address(object):
    address: list = list()

    def getAdrs(self):
        return self.address


class Lib1(Address):

    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.GetAddress()

    def GetAddress(self):
        key = Key()
        self.address.append([key.address, key.to_wif(), key.to_hex()])

class Lib2(Address):
    MAX = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.GetAddress1()
        self.GetAddress2()
        
    def GetAddress2(self):
        setup('mainnet')
        priv = PrivateKey()

        pub = priv.get_public_key()

        address = pub.get_address()

        self.address.append(
            [address.to_string(), priv.to_wif(), priv.to_bytes()])

    def GetAddress1(self):
        setup('mainnet')
        x = random.randrange(
            1, self.MAX)
        priv = PrivateKey(secret_exponent=x)
        pub = priv.get_public_key()
        address = pub.get_address()
        self.address.append(
            [address.to_string(), priv.to_wif(), priv.to_bytes()])

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
        self.get_Add1()
        
    def get_Add1(self):
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

    def __init__(self) -> None:
        super().__init__()
        self.language = "english"
        self.address.clear()
        self.get_addr1()
        self.get_addr2()
        self.get_addr3()

    def get_addr1(self):

        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.language).generate()
        if is_mnemonic(wo):
            i.from_mnemonic(wo)
            self.address.append([i.address(), i.wif(), wo])
            self.address.append([i.p2sh_address(),i.wif(),wo])
            self.address.append([i.p2pkh_address(),i.wif(),wo])
            self.address.append([i.p2wsh_address(),i.wif(),wo])
            self.address.append([i.p2wpkh_address(),i.wif(),wo])
            self.address.append([i.p2wpkh_in_p2sh_address(),i.wif(),wo])
            
    def get_addr2(self):
        try:
            
            i: BIP32HDWallet = BIP32HDWallet()
            wo = Mnemonic(self.language).generate(strength=128)
            if is_mnemonic(wo):
                i.from_mnemonic(wo)
                self.address.append([i.address(), i.wif(), wo])
                self.address.append([i.p2sh_address(),i.wif(),wo])
                self.address.append([i.p2pkh_address(),i.wif(),wo])
                self.address.append([i.p2wsh_address(),i.wif(),wo])
                self.address.append([i.p2wpkh_address(),i.wif(),wo])
                self.address.append([i.p2wpkh_in_p2sh_address(),i.wif(),wo])
        except BaseException as e:
            pass



    def get_addr3(self):
        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.language).generate(strength=256)
        if is_mnemonic(wo):
            i.from_mnemonic(wo)
            self.address.append([i.address(), i.wif(), wo])
            self.address.append([i.p2sh_address(),i.wif(),wo])
            self.address.append([i.p2pkh_address(),i.wif(),wo])
            self.address.append([i.p2wsh_address(),i.wif(),wo])
            self.address.append([i.p2wpkh_address(),i.wif(),wo])
            self.address.append([i.p2wpkh_in_p2sh_address(),i.wif(),wo])


class Lib5(Address):
    HEX = 'hex'
    X0 = '0x'
    B0 = '0b'
    MAINNET = 'mainnet'
    RIPEMD160 ='ripemd160'
    EXT_PREFIX = "80"

    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        for counter in range(0,5):
            self.Get_Address()

    def gen_hex(self):
        str_ = ""
        for i in range(256):
            str_ += bin(random.getrandbits(1)).replace(self.B0, "")
        bb = int(str_, 2)
        bb = hex(bb).replace(self.X0, "")
        return str(bb)

    def calc_wif(self,hex_):
        private_key_static = hex_
        extended_key = self.EXT_PREFIX+private_key_static
        first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
        second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
        final_key = extended_key+second_sha256[:8]
        WIF = base58.b58encode(binascii.unhexlify(final_key))
        return WIF.__str__().replace("b'","").replace("'","")
    
    def Get_Address(self):
        try:
            setup('mainnet')
            hex_ = self.gen_hex()
            wif = self.calc_wif(hex_)
            priv = PrivateKey.from_wif(wif)
            pub = priv.get_public_key()
            address = pub.get_address(False).to_string()
            c_address = pub.get_address(True).to_string()
            seg_adr = pub.get_segwit_address().to_string()
            
            self.address.append([address, hex_,wif])
            self.address.append([seg_adr,hex_,wif])
            self.address.append([c_address,hex_,wif])
        except Exception as ex:
            self.Get_Address()

        
class AddressFact():
    def createAdress(self, typ):
        targetclass = typ
        return globals()[targetclass]()

