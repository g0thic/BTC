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
        # self.GetAddress3()

    def GetAddress3(self):

        for x in range(5):
            setup('mainnet')
            xx = random.randint(1,self.MAX)
            priv = PrivateKey(secret_exponent=xx)
            pub = priv.get_public_key()
            address = pub.get_address()
            self.address.append(
                [address.to_string(), priv.to_wif(), priv.to_bytes()])

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
        self.get_Add3()
        self.get_Add4()
        self.get_Add5()
        #self.get_Add1()
        self.get_Add2()
        self.get_Add6()

    def get_Add1(self):
        wallet = Wallet()
        key = wallet.key.__dict__[self.MAINNET].__dict__[self.WIF]
        hex_ = wallet.key.__dict__[self.HEX]
        adr1 = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR1]
        self.address.append([adr1, key, hex_])
        adr2 = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR1C]
        self.address.append([adr2, key, hex_])
        adr3 = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR3]
        self.address.append([adr3, key, hex_])
        adr4 = wallet.address.__dict__[
            self.MAINNET].__dict__[self.PUBADDRBC1_P2WSH]
        self.address.append([adr4, key, hex_])
        adr5 = wallet.address.__dict__[
            self.MAINNET].__dict__[self.PUBADDRBC1_P2WPKH]
        self.address.append([adr5, key, hex_])

    def get_Add6(self):
        wallet = Wallet()
        adr = wallet.address.__dict__[
            self.MAINNET].__dict__[self.PUBADDRBC1_P2WPKH]
        key = wallet.key.__dict__[self.MAINNET].__dict__[self.WIF]
        hex_ = wallet.key.__dict__[self.HEX]
        self.address.append([adr, key, hex_])

    def get_Add2(self):
        wallet = Wallet()
        adr = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR1C]
        key = wallet.key.__dict__[self.MAINNET].__dict__[self.WIF]
        hex_ = wallet.key.__dict__[self.HEX]
        self.address.append([adr, key, hex_])

    def get_Add3(self):
        wallet = Wallet()
        adr = wallet.address.__dict__[
            self.MAINNET].__dict__[self.PUBADDRBC1_P2WSH]
        key = (wallet.key.__dict__[self.MAINNET].__dict__[self.WIF])
        hex_ = wallet.key.__dict__[self.HEX]
        self.address.append([adr, key, hex_])

    def get_Add4(self):
        wallet = Wallet()
        adr = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR3]
        key = (wallet.key.__dict__[self.MAINNET].__dict__[self.WIF])
        hex_ = wallet.key.__dict__[self.HEX]
        self.address.append([adr, key, hex_])

    def get_Add5(self):
        wallet = Wallet()
        adr = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR1]
        key = (wallet.key.__dict__[self.MAINNET].__dict__[self.WIF])
        hex_ = wallet.key.__dict__[self.HEX]
        self.address.append([adr, key, hex_])

class Lib4(Address):

    def __init__(self) -> None:
        super().__init__()
        self.language = "english"
        self.address.clear()
        self.get_addr1()
        self.get_addr2()
        self.get_addr3()

    def get_addr1(self):

        i: BIP49HDWallet = BIP49HDWallet()
        wo = Mnemonic(self.language).generate()
        h = is_mnemonic(wo)
        if h:
            i.from_mnemonic(wo)
            self.address.append([i.address(), i.wif(), wo])
            self.address.append([i.p2sh_address(),i.wif(),wo])
            self.address.append([i.p2pkh_address(),i.wif(),wo])
            self.address.append([i.p2wsh_address(),i.wif(),wo])
            self.address.append([i.p2wpkh_address(),i.wif(),wo])
            self.address.append([i.p2wpkh_in_p2sh_address(),i.wif(),wo])
            print("hello")
            
    def get_addr2(self):
        try:
            i: BIP49HDWallet = BIP49HDWallet()
            m = Mnemonic(self.language)
            wo = m.generate(strength=128)
            h = is_mnemonic(wo)
            if h:
                i.from_mnemonic(wo)
                self.address.append([i.address(), i.wif(), wo])
            self.address.append([i.p2sh_address(),i.wif(),wo])
            self.address.append([i.p2pkh_address(),i.wif(),wo])
            self.address.append([i.p2wsh_address(),i.wif(),wo])
            self.address.append([i.p2wpkh_address(),i.wif(),wo])
            self.address.append([i.p2wpkh_in_p2sh_address(),i.wif(),wo])
            x=1/0
        except BaseException as e:
            pass



    def get_addr3(self):
        i: BIP44HDWallet = BIP44HDWallet()

        m = Mnemonic(self.language)
        wo = m.generate(strength=256)
        h = is_mnemonic(mnemonic=wo)
        if h:
            i.from_mnemonic(wo)
            self.address.append([i.address(), i.wif(), wo])
            self.address.append([i.p2sh_address(),i.wif(),wo])
            self.address.append([i.p2pkh_address(),i.wif(),wo])
            self.address.append([i.p2wsh_address(),i.wif(),wo])
            self.address.append([i.p2wpkh_address(),i.wif(),wo])
            self.address.append([i.p2wpkh_in_p2sh_address(),i.wif(),wo])

class Lib5(Address):
    LANGUAGE = 'english'
    SEGWIT = 'segwit'
    P2SH_SEGWIT = 'p2sh-segwit'
    BITCOIN = 'bitcoin'

    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.get_adr1()
        self.get_adr2()
        self.get_adr3()
        #self.get_adr4()
        self.get_adr5()
        self.get_adr6()

    def get_adr1(self):
        name = random.choice(string.ascii_letters)
        bitcoinlib.wallets.wallet_delete_if_exists(name)
        p = Mnemonic(language=self.LANGUAGE).generate()
        
        w = bitcoinlib.wallets.wallet_create_or_open(name, keys=p, network=self.BITCOIN)
        key_ = w.get_key()
        self.address.append([key_.address, key_.wif, p])

    def get_adr2(self):
        name = random.choice(string.ascii_letters)
        bitcoinlib.wallets.wallet_delete_if_exists(name)
        p = Mnemonic(language=self.LANGUAGE).generate()
        w = bitcoinlib.wallets.wallet_create_or_open(
            name, keys=p, network=self.BITCOIN, witness_type=self.SEGWIT)
        key_ = w.get_key()
        
        self.address.append([key_.address, key_.wif, p])

    def get_adr3(self):
        name = random.choice(string.ascii_letters)
        bitcoinlib.wallets.wallet_delete_if_exists(name)
        p = Mnemonic(language=self.LANGUAGE).generate()
        
        w = bitcoinlib.wallets.wallet_create_or_open(
            name, keys=p, network=self.BITCOIN, witness_type=self.P2SH_SEGWIT)
        
        key_ = w.get_key()
        self.address.append([key_.address, key_.wif, p])

    def get_adr4(self):
        name = random.choice(string.ascii_letters)
        bitcoinlib.wallets.wallet_delete_if_exists(name)
        w = bitcoinlib.wallets.wallet_create_or_open(
            name, keys=[Keys.HDKey(), Keys.HDKey().public()], network=self.BITCOIN)
        key_ = w.get_key()
        self.address.append([key_.address, key_.wif, "Lib5"])

    def get_adr5(self):
        name = random.choice(string.ascii_letters)
        bitcoinlib.wallets.wallet_delete_if_exists(name)
        w = bitcoinlib.wallets.wallet_create_or_open(name, network=self.BITCOIN)
        key_ = w.get_key()
        self.address.append([key_.address, key_.wif, "Lib5"])

    def get_adr6(self):
        k = Keys.HDKey(multisig=True)
        self.address.append([k.address(),k.private_byte,k.private_hex])
  

class Lib6(Address):
    HEX = 'hex'
    X0 = '0x'
    B0 = '0b'
    MAINNET = 'mainnet'
    RIPEMD160   ='ripemd160'
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


    
