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


class Address(object):
    address: list = list()

    def get_addr(self):
        return self.address


class Lib1(Address):

    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.get_addr()

    def get_addr(self):
        key = Key()
        self.address.append([key.address, key.to_wif(), key.to_hex()])
        self.address.append([key.segwit_address, key.to_wif(), key.to_hex()])


class Lib2(Address):
    MAX = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    MAINNET = 'mainnet'

    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        setup(self.MAINNET)
        self.get_addr1()
        self.get_addr2()

    def get_addr2(self):

        priv = PrivateKey()

        pub = priv.get_public_key()

        address_c = pub.get_address(True)
        address = pub.get_address(False)
        address_seg = pub.get_segwit_address()

        self.address.append(
            [address.to_string(), priv.to_wif(), priv.key.to_string().hex()])
        self.address.append(
            [address_c.to_string(), priv.to_wif(), priv.key.to_string().hex()])
        self.address.append(
            [address_seg.to_string(), priv.to_wif(), priv.key.to_string().hex()])

    def get_addr1(self):
        x = random.randrange(
            1, self.MAX)
        priv = PrivateKey(secret_exponent=x)
        pub = priv.get_public_key()
        address_c = pub.get_address(True)
        address = pub.get_address(False)
        address_seg = pub.get_segwit_address()

        self.address.append(
            [address.to_string(), priv.to_wif(), priv.key.to_string().hex()])
        self.address.append(
            [address_c.to_string(), priv.to_wif(), priv.key.to_string().hex()])
        self.address.append(
            [address_seg.to_string(), priv.to_wif(), priv.key.to_string().hex()])


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
        self.get_addr12()
        self.get_addr10()
        self.get_addr11()
        
    def get_addr11(self):

        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.KOREAN).generate()
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
        self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
        self.address.append(
            [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])

    def get_addr10(self):
        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.KOREAN).generate(strength=128)
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
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

    def get_addr12(self):
        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.KOREAN).generate(strength=256)
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
        self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
        self.address.append(
            [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
        
    def get_addr9(self):

        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.JAPANESE).generate()
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
        self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
        self.address.append(
            [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])

    def get_addr8(self):
        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.JAPANESE).generate(strength=128)
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
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

    def get_addr7(self):
        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.JAPANESE).generate(strength=256)
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
        self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
        self.address.append(
            [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])
    def get_addr4(self):

        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.CHINESE_TRAD).generate()
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
        self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
        self.address.append(
            [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])

    def get_addr5(self):
        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.CHINESE_TRAD).generate(strength=128)
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
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

    def get_addr6(self):
        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.CHINESE_TRAD).generate(strength=256)
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
        self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
        self.address.append(
            [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])


    def get_addr1(self):

        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.ENGLISH).generate()
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
        self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
        self.address.append(
            [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])

    def get_addr2(self):
        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.ENGLISH).generate(strength=128)
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
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

    def get_addr3(self):
        i: BIP32HDWallet = BIP32HDWallet()
        wo = Mnemonic(self.ENGLISH).generate(strength=256)
        i.from_mnemonic(wo)
        self.address.append([i.address(), i.wif(), i.private_key()])
        self.address.append([i.p2sh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2pkh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wsh_address(), i.wif(), i.private_key()])
        self.address.append([i.p2wpkh_address(), i.wif(), i.private_key()])
        self.address.append(
            [i.p2wpkh_in_p2sh_address(), i.wif(), i.private_key()])


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

    def gen_hex(self):
        str_ = ""
        for i in range(256):
            str_ += bin(random.getrandbits(1)).replace(self.B0, "")
        bb = int(str_, 2)
        bb = hex(bb).replace(self.X0, "")
        return str(bb)

    def get_adr4(self):
        hex_ = os.urandom(32).hex()
        key_ = Key().from_hex(hex_)
        self.address.append([key_.address, key_.to_wif(), hex_])
        self.address.append([key_.segwit_address, key_.to_wif(), hex_])

    def get_adr3(self):
        try:
            hex_ = secrets.token_hex(32)
            key_ = Key().from_hex(hex_)
            self.address.append([key_.address, key_.to_wif(), hex_])
            self.address.append([key_.segwit_address, key_.to_wif(), hex_])
        except BaseException as ex:
            return

    def get_adr2(self):
        try:
            hex_String = "0123456789abcdef"
            hex_ = ''.join([secrets.choice(hex_String) for x in range(64)])
            key_ = Key().from_hex(hex_)
            self.address.append([key_.address, key_.to_wif(), hex_])
            self.address.append([key_.segwit_address, key_.to_wif(), hex_])

        except BaseException as ex:
            return

    def get_adr1(self):
        try:

            hex_ = self.gen_hex()
            key_ = Key().from_hex(hex_)
            self.address.append([key_.address, key_.to_wif(), hex_])
            self.address.append([key_.segwit_address, key_.to_wif(), hex_])
        except Exception as ex:
            return


class AddressFact():
    def createAdress(self, typ):
        targetclass = typ
        return globals()[targetclass]()
